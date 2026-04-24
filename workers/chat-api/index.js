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
      // Strategy 1: brand + number match → try exact slug
      const brandMatch = question.toLowerCase().match(
        /(carrier|goodman|lennox|trane|rheem|york|daikin|mitsubishi|haas|fanuc|yaskawa|abb|siemens|hoshizaki|manitowoc|amana|bryant|comfortmaker|keeprite|ruud|heil|tempstar|arcoaire|icp|day[\s-]?night|payne|totaline|janitrol|american[\s-]?standard|coleman|york|nordyne|frigidaire|gibson|westinghouse|electrolux|white[\s-]?rodgers|honeywell|echelon|bosch|weil[\s-]?mclain|burnham|peerless|utica|crown|slant[\s-]?fin|hydrotherm|lochinvar|triangle[\s-]?tube|buderus|viessmann|baxi|biasi|vaillant|rinnai|navien|noritz|takagi|paloma|bosch|stiebel[\s-]?eltron|grundfos|bell[\s-]?gossett|taco|armstrong|aurora|roper|speed[\s-]?queen|maytag|whirlpool|kenmore|ge|lg|samsung|panasonic|sharp|sanyo|fujitsu|hitachi|toshiba|gree|midea|aux|haier|chigo|pioneer|senville|mr[\s-]?cool|mini[\s-]?split|ptac|ptacunit|issi|allen[\s-]?bradley|rockwell|ab|omron|schneider|modicon|delta|automation[\s-]?direct|click|koyo|idec|keyence|mitsubishi[\s-]?electric|melsec|nais|panasonic[\s-]?plc|vfd|drive|inverter|servo|motor|pump|compressor|chiller|ahu|rtu|rooftop)/
      );
      const codeMatch = question.match(/\b([A-Z]{0,4}[\d]{1,4}[A-Z]{0,4})\b/);

      if (brandMatch && codeMatch) {
        // Build a clean slug: brand-CODE-error-code
        const brand = brandMatch[1].replace(/[\s-]+/g, '-').toLowerCase();
        const code = codeMatch[1].toLowerCase();
        const slug = `${brand}-${code}-error-code`;
        const articleUrl = `${siteBase}/posts/${slug}/`;

        const articleResp = await fetch(articleUrl, {
          headers: { 'User-Agent': 'errorcodefixes-chatbot/1.0' }
        });

        if (articleResp.ok) {
          const html = await articleResp.text();
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

      // Strategy 2: if still no context, try the Pagefind search index
      // Pagefind exposes a /pagefind/pagefind-index.json; we can search it
      // by fetching the top-level index and scanning for matching entries.
      if (!context) {
        const indexUrl = `${siteBase}/pagefind/pagefind-index.json`;
        const indexResp = await fetch(indexUrl, {
          headers: { 'User-Agent': 'errorcodefixes-chatbot/1.0' }
        });

        if (indexResp.ok) {
          const indexData = await indexResp.json();
          // pagefind-index.json has { pages: [...] } or { segments: [...] }
          // The pages array contains { url, content, ... }
          const pages = indexData.pages || indexData.results || [];

          // Simple keyword match: build query tokens from the question
          const tokens = question.toLowerCase()
            .replace(/[^a-z0-9\s]/g, ' ')
            .split(/\s+/)
            .filter(t => t.length > 2);

          let bestScore = 0;
          let bestPage = null;

          for (const page of pages.slice(0, 2000)) {
            const url = (page.url || '').toLowerCase();
            const content = (page.content || page.text || '').toLowerCase();
            let score = 0;
            for (const token of tokens) {
              if (url.includes(token)) score += 3;
              if (content.includes(token)) score += 1;
            }
            if (score > bestScore) {
              bestScore = score;
              bestPage = page;
            }
          }

          if (bestPage && bestScore > 0) {
            const pageUrl = bestPage.url.startsWith('http')
              ? bestPage.url
              : `${siteBase}${bestPage.url}`;
            const pageResp = await fetch(pageUrl, {
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
              sourceArticle = pageUrl;
            }
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
If article context is provided below, use it as the primary source.
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
