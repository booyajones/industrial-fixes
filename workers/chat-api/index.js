// errorcodefixes.com chat API Worker — hardened against cost-abuse (2026-06-16).
// This is a PUBLIC endpoint that calls OpenAI on every request, so without
// guards anyone (or a bot flood) can run up the OpenAI bill. Guards added:
//   1. Origin/Referer allowlist — only errorcodefixes.com may call it; CORS
//      reflects the validated origin instead of '*' (kills cross-origin abuse).
//   2. Per-IP rate limit via Cloudflare's native rate-limiting binding (no KV
//      needed). Falls open only if the binding isn't deployed yet.
//   3. Input cap — reject oversized questions (expensive prompts).
// The OpenAI key remains a Worker secret (never in code).

const ALLOWED_ORIGINS = [
  'https://errorcodefixes.com',
  'https://www.errorcodefixes.com',
];
const MAX_QUESTION_CHARS = 600;

function pickOrigin(request) {
  // Allow if the Origin OR Referer is one of ours. Browsers always send at
  // least Referer for a real page request; a bare scripted hit sends neither.
  const origin = request.headers.get('Origin') || '';
  if (ALLOWED_ORIGINS.includes(origin)) return origin;
  const referer = request.headers.get('Referer') || '';
  if (ALLOWED_ORIGINS.some(o => referer.startsWith(o))) {
    // Reflect the canonical origin for CORS when only Referer matched.
    return origin && ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  }
  return null; // not allowed
}

function corsHeaders(allowedOrigin) {
  return {
    'Access-Control-Allow-Origin': allowedOrigin || ALLOWED_ORIGINS[0],
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Vary': 'Origin',
  };
}

export default {
  async fetch(request, env) {
    const allowedOrigin = pickOrigin(request);

    // CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders(allowedOrigin) });
    }
    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }

    // 1. Origin lock — reject calls that are not from errorcodefixes.com.
    if (!allowedOrigin) {
      return new Response(JSON.stringify({ error: 'forbidden origin' }), {
        status: 403, headers: { 'Content-Type': 'application/json' },
      });
    }

    // 2. Per-IP rate limit (native CF binding; falls open if not configured).
    if (env.RATE_LIMITER && typeof env.RATE_LIMITER.limit === 'function') {
      const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
      try {
        const { success } = await env.RATE_LIMITER.limit({ key: ip });
        if (!success) {
          return new Response(JSON.stringify({ error: 'rate limited' }), {
            status: 429,
            headers: { 'Content-Type': 'application/json', 'Retry-After': '30', ...corsHeaders(allowedOrigin) },
          });
        }
      } catch (e) { /* rate limiter unavailable — fail open, other guards remain */ }
    }

    let body;
    try {
      body = await request.json();
    } catch (e) {
      return new Response('Invalid JSON', { status: 400, headers: corsHeaders(allowedOrigin) });
    }

    const { question } = body;
    if (!question || typeof question !== 'string') {
      return new Response('Missing question', { status: 400, headers: corsHeaders(allowedOrigin) });
    }
    // 3. Input cap — block expensive oversized prompts.
    if (question.length > MAX_QUESTION_CHARS) {
      return new Response(JSON.stringify({ error: 'question too long' }), {
        status: 413, headers: { 'Content-Type': 'application/json', ...corsHeaders(allowedOrigin) },
      });
    }

    const siteBase = 'https://errorcodefixes.com';
    let context = '';
    let sourceArticle = null;

    try {
      const indexResp = await fetch(`${siteBase}/search-index.json`, {
        headers: { 'User-Agent': 'errorcodefixes-chatbot/1.0' },
      });
      if (indexResp.ok) {
        const articles = await indexResp.json();
        const tokens = question
          .toLowerCase()
          .split(/[\s\.,!?;:()\[\]{}"'\/\\-]+/)
          .map(t => t.replace(/[^a-z0-9]/g, ''))
          .filter(t => t.length >= 2);

        let bestScore = 0;
        let bestArticle = null;
        for (const article of articles) {
          const titleLower = article.title.toLowerCase();
          let score = 0;
          for (const token of tokens) {
            if (article.keywords && article.keywords.includes(token)) score += 2;
            if (titleLower.includes(token)) score += 3;
            if (article.slug && article.slug.includes(token)) score += 2;
          }
          if (score > bestScore) { bestScore = score; bestArticle = article; }
        }

        if (bestArticle && bestScore >= 3) {
          const articleUrl = `${siteBase}${bestArticle.url}`;
          const pageResp = await fetch(articleUrl, {
            headers: { 'User-Agent': 'errorcodefixes-chatbot/1.0' },
          });
          if (pageResp.ok) {
            const html = await pageResp.text();
            const text = html
              .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
              .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
              .replace(/<[^>]+>/g, ' ')
              .replace(/\s+/g, ' ')
              .trim()
              .substring(0, 4000);
            context = text;
            sourceArticle = articleUrl;
          }
        }
      }
    } catch (e) {
      // Context fetch failed — still answer with general knowledge
    }

    const systemPrompt = `You are an expert industrial equipment technician for errorcodefixes.com.
You help diagnose and fix error codes for HVAC systems, CNC machines, VFDs, commercial refrigeration, boilers, and more.
Be concise, practical, and direct. Use plain text — no markdown.
If article context is provided, answer primarily from that content and cite the article link.
If not, draw on your technical knowledge.
Always lead with the most likely cause, then provide clear fix steps.`;

    const userMessage = context
      ? `Question: ${question}\n\nRelevant article content:\n${context}`
      : `Question: ${question}`;

    const openAIResponse = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.OPENAI_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'gpt-4o-mini',
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: userMessage },
        ],
        max_tokens: 500,
        temperature: 0.3,
      }),
    });

    if (!openAIResponse.ok) {
      await openAIResponse.text();
      return new Response(JSON.stringify({
        answer: 'Sorry, the AI service is temporarily unavailable. Please check the full article on our site.',
        source: sourceArticle,
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json', ...corsHeaders(allowedOrigin) },
      });
    }

    const openAIData = await openAIResponse.json();
    const answer = openAIData.choices?.[0]?.message?.content
      || 'Sorry, I could not generate an answer.';

    return new Response(JSON.stringify({ answer, source: sourceArticle }), {
      headers: { 'Content-Type': 'application/json', ...corsHeaders(allowedOrigin) },
    });
  },
};
