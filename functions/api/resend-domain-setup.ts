// TEMPORARY maintenance endpoint (2026-07-28) — will be removed once
// errorcodefixes.com is verified as a Resend sending domain.
//
// Purpose: /api/quote sends leads via Resend, but Resend rejects sends with
// 403 "domain is not verified". The RESEND_API_KEY lives only in the CF Pages
// env (sealed secret), so domain setup must run FROM the function runtime.
// This endpoint drives exactly three fixed Resend domain actions and returns
// only non-secret data (DNS records that are destined for public DNS anyway).
//
// Gate: requires header x-ecf-admin matching env.ECF_ADMIN_TOKEN (a sealed
// CF Pages secret set out-of-band — never present in this public repo).

interface Env {
  RESEND_API_KEY: string;
  ECF_ADMIN_TOKEN: string;
}

type PagesContext<E> = { request: Request; env: E };

const API = "https://api.resend.com";

export const onRequestPost = async (ctx: PagesContext<Env>): Promise<Response> => {
  const { request, env } = ctx;

  const gate = request.headers.get("x-ecf-admin") || "";
  if (!env.ECF_ADMIN_TOKEN || gate !== env.ECF_ADMIN_TOKEN) {
    return new Response("Not found", { status: 404 });
  }

  let action = "";
  try {
    action = String(((await request.json()) as Record<string, unknown>).action ?? "");
  } catch {
    /* fall through */
  }

  const headers = {
    Authorization: `Bearer ${env.RESEND_API_KEY}`,
    "Content-Type": "application/json",
  };

  let r: Response;
  if (action === "create") {
    r = await fetch(`${API}/domains`, {
      method: "POST",
      headers,
      body: JSON.stringify({ name: "errorcodefixes.com", region: "us-east-1" }),
    });
  } else if (action === "list") {
    r = await fetch(`${API}/domains`, { method: "GET", headers });
  } else if (action.startsWith("verify:")) {
    const id = action.slice("verify:".length).replace(/[^a-zA-Z0-9-]/g, "");
    r = await fetch(`${API}/domains/${id}/verify`, { method: "POST", headers });
  } else if (action.startsWith("get:")) {
    const id = action.slice("get:".length).replace(/[^a-zA-Z0-9-]/g, "");
    r = await fetch(`${API}/domains/${id}`, { method: "GET", headers });
  } else {
    return new Response(JSON.stringify({ error: "unknown action" }), {
      status: 400,
      headers: { "content-type": "application/json" },
    });
  }

  const body = await r.text();
  return new Response(JSON.stringify({ upstream: r.status, body: body.slice(0, 8000) }), {
    status: 200,
    headers: { "content-type": "application/json" },
  });
};
