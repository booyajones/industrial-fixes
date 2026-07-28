// Cloudflare Pages Function: POST /api/subscribe
// Adds an email to the Resend "General" audience. Runs server-side so the
// Resend API key is never exposed to the browser. Replaces the old direct
// POST-to-Beehiiv signup. Accepts both form-encoded (no-JS fallback) and JSON.
//
// Pages env vars required (set as secrets on the CF Pages project):
//   RESEND_API_KEY        re_...
//   RESEND_AUDIENCE_ID    the "General" audience id

interface Env {
  RESEND_API_KEY: string;
  RESEND_AUDIENCE_ID: string;
}

// Minimal local type so `astro check` (tsc) can type this without pulling in
// @cloudflare/workers-types. At runtime Cloudflare Pages recognises the named
// `onRequestPost` export and injects the real context.
type PagesContext<E> = { request: Request; env: E };

function redirect(cat: string): Response {
  const loc = "/thanks/" + (cat && cat !== "industrial" ? "?cat=" + encodeURIComponent(cat) : "");
  return new Response(null, { status: 303, headers: { Location: loc } });
}

// No-JS validation failure: serve a minimal HTML page instead of dumping raw
// JSON in the browser (Back button preserves the filled-in form).
function htmlError(msg: string, status = 400): Response {
  const body = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Couldn't sign you up</title></head>
<body style="font-family: system-ui, sans-serif; max-width: 32rem; margin: 4rem auto; padding: 0 1rem; line-height: 1.55;">
<h1 style="font-size: 1.25rem;">Couldn't sign you up</h1>
<p>${msg}</p>
<p>Use your browser's Back button to fix it and try again, or email
<a href="mailto:info@errorcodefixes.com">info@errorcodefixes.com</a> directly.</p>
<p><a href="/">Back to errorcodefixes.com</a></p>
</body></html>`;
  return new Response(body, { status, headers: { "content-type": "text/html;charset=utf-8" } });
}

export const onRequestPost = async (ctx: PagesContext<Env>): Promise<Response> => {
  const { request, env } = ctx;
  let email = "";
  let cat = "industrial";

  const ct = request.headers.get("content-type") || "";
  try {
    if (ct.includes("application/json")) {
      const b = (await request.json()) as { email?: string; ecf_cat?: string };
      email = (b.email || "").trim();
      cat = (b.ecf_cat || "industrial").trim();
    } else {
      const form = await request.formData();
      email = String(form.get("email") || "").trim();
      cat = String(form.get("ecf_cat") || "industrial").trim();
    }
  } catch {
    // fall through to validation
  }

  // Normalise the category to a safe slug (it is stored on the Resend contact
  // below and echoed into the redirect URL). Client input, never trusted.
  cat = cat.toLowerCase().replace(/[^a-z0-9-]/g, "").slice(0, 40) || "industrial";

  const wantsJson = (request.headers.get("accept") || "").includes("application/json")
    || ct.includes("application/json");

  // Basic validation. Never trust client input.
  if (!email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || email.length > 254) {
    if (!wantsJson) return htmlError("The email address doesn't look valid.");
    return new Response(JSON.stringify({ error: "invalid email" }), {
      status: 400, headers: { "content-type": "application/json" },
    });
  }
  if (!env.RESEND_API_KEY || !env.RESEND_AUDIENCE_ID) {
    if (!wantsJson) return htmlError("The signup service is temporarily unavailable.", 500);
    return new Response(JSON.stringify({ error: "not configured" }), {
      status: 500, headers: { "content-type": "application/json" },
    });
  }

  const r = await fetch(
    `https://api.resend.com/audiences/${env.RESEND_AUDIENCE_ID}/contacts`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      // Segmentation: Resend contacts have no custom fields, so the equipment
      // category the reader signed up from (ecf_cat: "hvac" | "cnc" | ...) is
      // stored in last_name. This is what makes the audience segmentable —
      // e.g. send the CNC cheat-sheet update only to last_name=cnc — instead
      // of discarding the category at the door.
      body: JSON.stringify({ email, unsubscribed: false, last_name: cat }),
    },
  );

  // Resend returns 201 on create and 200/422 if the contact already exists.
  // Either way the user's intent is satisfied, so we send them to /thanks/.
  const ok = r.ok || r.status === 422;

  if (wantsJson) {
    return new Response(JSON.stringify({ ok }), {
      status: ok ? 200 : 502, headers: { "content-type": "application/json" },
    });
  }
  // No-JS form fallback: redirect to the thank-you page regardless.
  return redirect(cat);
};
