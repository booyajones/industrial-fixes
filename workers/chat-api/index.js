export default {
  async fetch(request, env) {
    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type',
        }
      });
    }

    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }

    let body;
    try {
      body = await request.json();
    } catch (e) {
      return new Response('Invalid JSON', { status: 400 });
    }

    const { question } = body;
    if (!question || typeof question !== 'string') {
      return new Response('Missing question', { status: 400 });
    }

    const siteBase = 'https://errorcodefixes.com';
    let context = '';
    let sourceArticle = null;

    try {
      // Fetch the static search index (cached at CDN edge)
      const indexResp = await fetch(`${siteBase}/search-index.json`, {
        headers: { 'User-Agent': 'errorcodefixes-chatbot/1.0' }
      });

      if (indexResp.ok) {
        const articles = await indexResp.json();

        // Tokenize the question: lowercase, split on spaces/punctuation, keep 2+ chars
        const tokens = question
          .toLowerCase()
          .split(/[\s\.,!?;:()\[\]{}"'\/\\-]+/)
          .map(t => t.replace(/[^a-z0-9]/g, ''))
          .filter(t => t.length >= 2);

        // Score each article
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
          if (score > bestScore) {
            bestScore = score;
            bestArticle = article;
          }
        }

        // Minimum score threshold: 3
        if (bestArticle && bestScore >= 3) {
          const articleUrl = `${siteBase}${bestArticle.url}`;
          const pageResp = await fetch(articleUrl, {
            headers: { 'User-Agent': 'errorcodefixes-chatbot/1.0' }
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

    // Build prompt
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
          { role: 'user', content: userMessage }
        ],
        max_tokens: 500,
        temperature: 0.3,
      })
    });

    if (!openAIResponse.ok) {
      await openAIResponse.text(); // consume body
      return new Response(JSON.stringify({
        answer: 'Sorry, the AI service is temporarily unavailable. Please check the full article on our site.',
        source: sourceArticle
      }), {
        status: 200,
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        }
      });
    }

    const openAIData = await openAIResponse.json();
    const answer = openAIData.choices?.[0]?.message?.content
      || 'Sorry, I could not generate an answer.';

    return new Response(JSON.stringify({
      answer,
      source: sourceArticle
    }), {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      }
    });
  }
};
