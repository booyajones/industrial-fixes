// Cloudflare Pages Function: POST /api/quote
// Industrial lead capture: takes the QuoteRequest form (equipment, fault code,
// description, contact) and forwards it as ONE transactional email to the
// dispatch inbox via the Resend API. Runs server-side so the Resend API key is
// never exposed to the browser. Accepts both form-encoded (no-JS fallback) and
// JSON, mirroring functions/api/subscribe.ts.
//
// Pages env vars required (set as secrets on the CF Pages project):
//   RESEND_API_KEY        re_...  (already configured for /api/subscribe)

interface Env {
  RESEND_API_KEY: string;
}

// Minimal local type so `astro check` (tsc) can type this without pulling in
// @cloudflare/workers-types. At runtime Cloudflare Pages recognises the named
// `onRequestPost` export and injects the real context.
type PagesContext<E> = { request: Request; env: E };

// Same Resend-verified sender the site's newsletter uses (domain-verified
// errorcodefixes.com). Leads land in the dispatch inbox; reply_to is the lead.
const FROM_ADDR = "Industrial Error Code Fixes <newsletter@errorcodefixes.com>";
const TO_ADDR = "info@errorcodefixes.com";

function redirect(): Response {
  return new Response(null, { status: 303, headers: { Location: "/quote-received/" } });
}

// No-JS validation failure: a raw JSON dump in the browser is a dead end for
// the reader. Serve a minimal, self-contained HTML page instead (Back button
// preserves the filled-in form).
function htmlError(msg: string, status = 400): Response {
  const body = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Couldn't send your request</title></head>
<body style="font-family: system-ui, sans-serif; max-width: 32rem; margin: 4rem auto; padding: 0 1rem; line-height: 1.55;">
<h1 style="font-size: 1.25rem;">Couldn't send your request</h1>
<p>${msg}</p>
<p>Use your browser's Back button to fix it and try again, or email
<a href="mailto:info@errorcodefixes.com">info@errorcodefixes.com</a> directly.</p>
<p><a href="/">Back to errorcodefixes.com</a></p>
</body></html>`;
  return new Response(body, { status, headers: { "content-type": "text/html;charset=utf-8" } });
}

// Clamp + strip newlines so no field can smuggle extra structure into the
// subject line or bloat the email body.
function clean(v: unknown, max: number): string {
  return String(v ?? "").replace(/[\r\n]+/g, " ").trim().slice(0, max);
}

export const onRequestPost = async (ctx: PagesContext<Env>): Promise<Response> => {
  const { request, env } = ctx;

  let equipment = "";
  let faultCode = "";
  let details = "";
  let email = "";
  let phone = "";
  let zip = "";
  let honeypot = "";

  const ct = request.headers.get("content-type") || "";
  try {
    if (ct.includes("application/json")) {
      const b = (await request.json()) as Record<string, unknown>;
      equipment = clean(b.equipment, 120);
      faultCode = clean(b.fault_code, 40);
      details = String(b.details ?? "").trim().slice(0, 2000);
      email = clean(b.email, 254);
      phone = clean(b.phone, 30);
      zip = clean(b.zip, 10);
      honeypot = clean(b.company, 100);
    } else {
      const form = await request.formData();
      equipment = clean(form.get("equipment"), 120);
      faultCode = clean(form.get("fault_code"), 40);
      details = String(form.get("details") ?? "").trim().slice(0, 2000);
      email = clean(form.get("email"), 254);
      phone = clean(form.get("phone"), 30);
      zip = clean(form.get("zip"), 10);
      honeypot = clean(form.get("company"), 100);
    }
  } catch {
    // fall through to validation
  }

  const wantsJson =
    (request.headers.get("accept") || "").includes("application/json") ||
    ct.includes("application/json");

  // Honeypot filled -> bot. Pretend success (no email sent) so the bot learns
  // nothing; a human never sees this field.
  if (honeypot) {
    if (wantsJson) {
      return new Response(JSON.stringify({ ok: true }), {
        status: 200, headers: { "content-type": "application/json" },
      });
    }
    return redirect();
  }

  // Basic validation. Never trust client input.
  if (!email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
    if (!wantsJson) return htmlError("The email address doesn't look valid, and we need it to reply.");
    return new Response(JSON.stringify({ error: "invalid email" }), {
      status: 400, headers: { "content-type": "application/json" },
    });
  }
  if (!equipment) {
    if (!wantsJson) return htmlError("Please tell us the equipment brand and model.");
    return new Response(JSON.stringify({ error: "missing equipment" }), {
      status: 400, headers: { "content-type": "application/json" },
    });
  }
  if (!env.RESEND_API_KEY) {
    if (!wantsJson) return htmlError("The request service is temporarily unavailable.", 500);
    return new Response(JSON.stringify({ error: "not configured" }), {
      status: 500, headers: { "content-type": "application/json" },
    });
  }

  const referer = request.headers.get("referer") || "";
  const subject = `Quote request: ${equipment}${faultCode ? ` — ${faultCode}` : ""}`;
  const text = [
    "New quote request from errorcodefixes.com",
    "",
    `Equipment:  ${equipment}`,
    `Fault code: ${faultCode || "(not given)"}`,
    `Email:      ${email}`,
    `Phone:      ${phone || "(not given)"}`,
    `ZIP:        ${zip || "(not given)"}`,
    `Page:       ${referer || "(unknown)"}`,
    "",
    "What's happening:",
    details || "(not given)",
  ].join("\n");

  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: FROM_ADDR,
      to: [TO_ADDR],
      reply_to: email,
      subject,
      text,
    }),
  });

  const ok = r.ok;

  if (wantsJson) {
    return new Response(JSON.stringify({ ok }), {
      status: ok ? 200 : 502, headers: { "content-type": "application/json" },
    });
  }
  // No-JS form fallback: only claim success when the email actually went out —
  // a thank-you page over a dropped lead would be a silent lie.
  if (!ok) return htmlError("We couldn't send your request just now.", 502);
  return redirect();
};
