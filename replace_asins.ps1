param(
    [string]$BlogDir = "C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog",
    [string]$MapFile = "C:\Users\Administrator\.openclaw\workspace\industrial-fixes\asin_map.json",
    [string]$Tag = "errorcodefixes-20"
)

Write-Host "=== Amazon Search URL to ASIN Replacement ===" -ForegroundColor Cyan
Write-Host "Blog dir: $BlogDir"
Write-Host "Map file: $MapFile"
Write-Host ""

# Read ASIN mapping
if (-not (Test-Path $MapFile)) {
    Write-Error "ASIN map file not found: $MapFile"
    exit 1
}
$asinMap = Get-Content $MapFile | ConvertFrom-Json
Write-Host "Loaded $($asinMap.PSObject.Properties.Count) ASIN mappings" -ForegroundColor Green
Write-Host ""

# Build regex: match any Amazon search URL with our tag
# Pattern: https://www.amazon.com/s?k=SEARCHTERM&tag=errorcodefixes-20
$searchUrlPattern = 'https://www\.amazon\.com/s\?k=([^&"]+)(?:&amp;|&)tag=errorcodefixes-20'

# Track stats
$totalArticlesProcessed = 0
$totalLinksReplaced = 0
$totalArticlesUpdated = 0
$articlesUpdated = @()
$termMatchCount = @{}

# For each mapping term, build a version that can be found inside larger search queries
# E.g. "gas valve" should match "honeywell+gas+valve+replacement"
$termPatterns = @{}
foreach ($term in $asinMap.PSObject.Properties) {
    $searchKey = $term.Name.ToLower()
    # Convert "gas valve" to regex "gas[\s\+]+valve" to match inside "honeywell+gas+valve+replacement"
    $words = $searchKey -split '\s+' | ForEach-Object { [regex]::Escape($_) }
    $pattern = $words -join '[\s\+]+'
    $termPatterns[$pattern] = @{
        SearchKey = $term.Name
        ASIN = $term.Value
    }
}

# For each article
Get-ChildItem $BlogDir -Filter "*.md" | ForEach-Object {
    $file = $_
    $content = Get-Content $file.FullName -Raw
    $originalContent = $content
    $changesInFile = 0
    $fileUpdates = @()

    # Find all Amazon search URLs in this article
    $matches = [regex]::Matches($content, $searchUrlPattern)
    
    foreach ($match in $matches) {
        $fullUrl = $match.Value
        $searchQuery = $match.Groups[1].Value  # URL-decoded search key (uses + for spaces)
        $searchQueryLower = $searchQuery.ToLower()
        
        # Check which mapping term matches - prefer more specific (longer) patterns
        $matchedTerm = $null
        $matchedASIN = $null
        $bestMatchLen = 0
        
        foreach ($pattern in $termPatterns.Keys) {
            if ($searchQueryLower -match $pattern) {
                $info = $termPatterns[$pattern]
                $termLen = $info.SearchKey.Length
                # Prefer longer/more specific match
                if ($termLen -gt $bestMatchLen) {
                    $bestMatchLen = $termLen
                    $matchedTerm = $info.SearchKey
                    $matchedASIN = $info.ASIN
                }
            }
        }
        
        if ($matchedASIN) {
            # Build replacement URL
            $replacementUrl = "https://www.amazon.com/dp/$matchedASIN`?tag=$Tag"
            
            # Replace in content (escape regex special chars in URL)
            $escapedUrl = [regex]::Escape($fullUrl)
            $content = $content -replace $escapedUrl, $replacementUrl
            $changesInFile++
            $totalLinksReplaced++
            
            # Track which terms were matched
            if (-not $termMatchCount.ContainsKey($matchedTerm)) {
                $termMatchCount[$matchedTerm] = 0
            }
            $termMatchCount[$matchedTerm]++
            $fileUpdates += "$matchedTerm->$matchedASIN"
        }
    }

    if ($changesInFile -gt 0) {
        # Write updated content
        Set-Content $file.FullName $content -NoNewline
        $totalArticlesUpdated++
        $articlesUpdated += "  + $($file.Name) ($changesInFile replacements)"
        Write-Host "  UPDATED $($file.Name): $changesInFile link(s)" -ForegroundColor Yellow
    }
    $totalArticlesProcessed++
}

Write-Host ""
Write-Host "=== REPLACEMENT SUMMARY ===" -ForegroundColor Cyan
Write-Host "Articles scanned: $totalArticlesProcessed"
Write-Host "Articles updated: $totalArticlesUpdated"
Write-Host "Total links replaced: $totalLinksReplaced"
Write-Host ""

if ($totalLinksReplaced -gt 0) {
    Write-Host "=== Term Match Breakdown ===" -ForegroundColor Green
    $termMatchCount.GetEnumerator() | Sort-Object Value -Descending | ForEach-Object {
        Write-Host "  $($_.Key): $($_.Value) replacements"
    }
}

if ($articlesUpdated.Count -gt 0 -and $articlesUpdated.Count -le 50) {
    Write-Host ""
    Write-Host "=== Updated Articles ===" -ForegroundColor Green
    $articlesUpdated | ForEach-Object { Write-Host $_ }
} elseif ($articlesUpdated.Count -gt 50) {
    Write-Host ""
    Write-Host "=== Updated Articles (first 50 shown) ===" -ForegroundColor Green
    $articlesUpdated | Select-Object -First 50 | ForEach-Object { Write-Host $_ }
    Write-Host "  ... and $($articlesUpdated.Count - 50) more"
}

Write-Host ""
Write-Host "=== ASIN Map Used ===" -ForegroundColor Cyan
$asinMap.PSObject.Properties | Sort-Object Name | ForEach-Object {
    Write-Host "  '$($_.Name)' -> $($_.Value)"
}

Write-Host ""
Write-Host "Done!" -ForegroundColor Green
