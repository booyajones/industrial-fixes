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

  // Basic validation. Never trust client input.
  if (!email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || email.length > 254) {
    return new Response(JSON.stringify({ error: "invalid email" }), {
      status: 400, headers: { "content-type": "application/json" },
    });
  }
  if (!env.RESEND_API_KEY || !env.RESEND_AUDIENCE_ID) {
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
      body: JSON.stringify({ email, unsubscribed: false }),
    },
  );

  // Resend returns 201 on create and 200/422 if the contact already exists.
  // Either way the user's intent is satisfied, so we send them to /thanks/.
  const ok = r.ok || r.status === 422;
  const wantsJson = (request.headers.get("accept") || "").includes("application/json")
    || ct.includes("application/json");

  if (wantsJson) {
    return new Response(JSON.stringify({ ok }), {
      status: ok ? 200 : 502, headers: { "content-type": "application/json" },
    });
  }
  // No-JS form fallback: redirect to the thank-you page regardless.
  return redirect(cat);
};
