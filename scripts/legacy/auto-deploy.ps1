#!/usr/bin/env pwsh
# auto-deploy.ps1 - Nightly auto-deploy for errorcodefixes.com
# Runs: build -> deploy to Cloudflare Pages
# Scheduled via Windows Task Scheduler

$ErrorActionPreference = "Stop"
$repo = "C:\Users\Administrator\.openclaw\workspace\industrial-fixes"
$logFile = "$repo\auto-deploy.log"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

function Log($msg) {
    "$timestamp $msg" | Tee-Object -FilePath $logFile -Append
}

Log "=== Auto-deploy started ==="

Set-Location $repo

# Pull latest from GitHub
Log "Pulling latest from GitHub..."
$pull = git pull origin main 2>&1
Log $pull

# Check if anything changed
$status = git status --short
if (-not $status) {
    Log "No changes detected. Skipping build."
    exit 0
}

Log "Changes detected. Building..."

# Build
$env:NODE_OPTIONS = "--max-old-space-size=4096"
$env:CLOUDFLARE_API_TOKEN = "$env:CLOUDFLARE_API_TOKEN"

npx astro build 2>&1 | Tee-Object -FilePath "$repo\build-auto.log"
if ($LASTEXITCODE -ne 0) {
    Log "Build failed! Exit code $LASTEXITCODE"
    exit 1
}

Log "Build succeeded. Running pagefind..."
npx pagefind --site dist --output-path dist/pagefind 2>&1 | Out-Null

# Copy public assets
Copy-Item "public/_headers" "dist/_headers" -Force -ErrorAction SilentlyContinue
Copy-Item "public/robots.txt" "dist/robots.txt" -Force -ErrorAction SilentlyContinue
Copy-Item "public/llms.txt" "dist/llms.txt" -Force -ErrorAction SilentlyContinue

Log "Deploying to Cloudflare Pages..."
npx wrangler pages deploy dist/ --project-name=industrial-fixes --commit-dirty=true 2>&1 | Tee-Object -FilePath "$repo\deploy-auto.log"
if ($LASTEXITCODE -ne 0) {
    Log "Deploy failed! Exit code $LASTEXITCODE"
    exit 1
}

Log "=== Auto-deploy complete ==="
