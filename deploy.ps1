#!/usr/bin/env pwsh
# deploy.ps1 - Build and deploy errorcodefixes.com to Cloudflare Pages
# Usage: pwsh deploy.ps1
# Requires: CLOUDFLARE_API_TOKEN and CF_ZONE_ID environment variables

if (-not $env:CLOUDFLARE_API_TOKEN) {
    Write-Host "ERROR: CLOUDFLARE_API_TOKEN env var not set. Aborting." -ForegroundColor Red
    exit 1
}

$CF_TOKEN = $env:CLOUDFLARE_API_TOKEN
$ZONE_ID = if ($env:CF_ZONE_ID) { $env:CF_ZONE_ID } else { "813cc094fec38ff0e2e666e534334944" }

Write-Host "Building site..." -ForegroundColor Cyan
$env:NODE_OPTIONS = "--max-old-space-size=4096"
npx astro build
if ($LASTEXITCODE -ne 0) {
    Write-Host "Build failed. Aborting deploy." -ForegroundColor Red
    exit 1
}

Write-Host "Running pagefind index..." -ForegroundColor Cyan
npx pagefind --site dist
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pagefind failed. Aborting deploy." -ForegroundColor Red
    exit 1
}

# Copy _headers and robots.txt to dist
Copy-Item "public/_headers" "dist/_headers" -Force -ErrorAction SilentlyContinue
Copy-Item "public/robots.txt" "dist/robots.txt" -Force -ErrorAction SilentlyContinue

Write-Host "Deploying to Cloudflare Pages..." -ForegroundColor Cyan
npx wrangler pages deploy dist/ --project-name=industrial-fixes --commit-dirty=true
if ($LASTEXITCODE -ne 0) {
    Write-Host "Deploy failed." -ForegroundColor Red
    exit 1
}

Write-Host "Purging Cloudflare cache..." -ForegroundColor Cyan
$headers = @{ "Authorization" = "Bearer $CF_TOKEN"; "Content-Type" = "application/json" }
$purge = Invoke-RestMethod -Uri "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" -Headers $headers -Method Post -Body '{"purge_everything":true}'
if ($purge.success) {
    Write-Host "Cache purged." -ForegroundColor Green
} else {
    Write-Host "Cache purge failed: $($purge.errors | ConvertTo-Json)" -ForegroundColor Yellow
}

Write-Host "Done. Live at https://errorcodefixes.com" -ForegroundColor Green
