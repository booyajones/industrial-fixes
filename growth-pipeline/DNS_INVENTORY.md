# DNS Inventory — errorcodefixes.com

Final state as of 2026-05-24, after Email Routing + Resend setup.

## Hosting / app
| Type | Name | Value | Notes |
|---|---|---|---|
| CNAME | `errorcodefixes.com` | `industrial-fixes.pages.dev` | Cloudflare Pages |
| CNAME | `gateway.errorcodefixes.com` | `5119f864-...cfargotunnel.com` | CF Argo Tunnel (chat worker) |

## Email — receive (Cloudflare Email Routing)
| Type | Name | Value | Notes |
|---|---|---|---|
| MX | `errorcodefixes.com` | `route1.mx.cloudflare.net` | Pri 10 |
| MX | `errorcodefixes.com` | `route2.mx.cloudflare.net` | Pri 20 |
| MX | `errorcodefixes.com` | `route3.mx.cloudflare.net` | Pri 30 |
| TXT | `errorcodefixes.com` | `v=spf1 include:_spf.mx.cloudflare.net ~all` | Apex SPF (CF receive) |
| TXT | `cf2024-1._domainkey` | `v=DKIM1; h=sha256; ... p=MIIBIjAN...` | CF DKIM (auto-managed) |

## Email — send (Resend, subdomain scope)
| Type | Name | Value | Notes |
|---|---|---|---|
| MX | `send.errorcodefixes.com` | `feedback-smtp.us-east-1.amazonses.com` | Pri 10 — Resend bounce handling |
| TXT | `send.errorcodefixes.com` | `v=spf1 include:amazonses.com ~all` | Resend SPF |
| TXT | `resend._domainkey` | `p=MIGfMA0G...` | Resend DKIM public key |

## Email — security
| Type | Name | Value | Notes |
|---|---|---|---|
| TXT | `_dmarc.errorcodefixes.com` | `v=DMARC1; p=none; rua=mailto:chris.a.wyatt@gmail.com; pct=100; adkim=r; aspf=r` | Monitor mode initially. Reports go to chris.a.wyatt@. Ramp to `p=quarantine` after 30 days of clean reports. |

## Operational notes

- Apex SPF only authorizes CF for sending — Resend's subdomain SPF is scoped
  to `send.errorcodefixes.com` so the two don't conflict.
- DMARC `aspf=r` (relaxed) means subdomain SPF satisfies alignment for
  any `*@errorcodefixes.com` sender, which is how Resend's `frank@` will
  pass DMARC.
- DKIM keys: CF rotates theirs automatically. Resend's key is fixed for
  the domain's lifetime in their system.
- CF DNS Edit perm lives on `CLOUDFLARE_DNS_TOKEN` env var (sourced from
  `~/.openclaw/keys/openclaw.env` — separate from the 3 Pages-scoped
  tokens that don't have DNS Edit).
