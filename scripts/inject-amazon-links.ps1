# Amazon Associates Affiliate Link Injection Script
# Associate Tag: errorcodefixe-20
# Injects Amazon search links into "Parts Often Needed" tables across all posts

$ASSOCIATE_TAG = "errorcodefixe-20"
$BLOG_DIR = "C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog"
$files = Get-ChildItem $BLOG_DIR -Filter "*.md"
$modified = 0
$skipped = 0

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # Check if file has a Parts Often Needed table
    if ($content -notmatch '\|\s*Part\s*\|') {
        $skipped++
        continue
    }
    
    # Check if already has Amazon links
    if ($content -match 'amazon\.com') {
        $skipped++
        continue
    }
    
    $newContent = $content
    
    # Match table rows in Parts Often Needed section
    # Pattern: | Part Name | Notes |
    # We want to turn "Part Name" into an Amazon search link
    $newContent = [regex]::Replace($newContent, 
        '\|\s*([^\|]+?)\s*\|\s*([^\|]+?)\s*\|',
        {
            param($match)
            $col1 = $match.Groups[1].Value.Trim()
            $col2 = $match.Groups[2].Value.Trim()
            
            # Skip header rows
            if ($col1 -eq 'Part' -or $col1 -eq '---' -or $col1 -eq '------' -or $col1 -match '^-+$') {
                return $match.Value
            }
            
            # Skip if already a link
            if ($col1 -match '\[.*\]\(.*\)') {
                return $match.Value
            }
            
            # Build Amazon search URL
            $searchQuery = [Uri]::EscapeDataString($col1)
            $amazonUrl = "https://www.amazon.com/s?k=$searchQuery&tag=$ASSOCIATE_TAG"
            
            return "| [$col1]($amazonUrl) | $col2 |"
        }
    )
    
    if ($newContent -ne $content) {
        Set-Content $file.FullName $newContent -Encoding UTF8 -NoNewline
        $modified++
    }
}

Write-Host "Done. Modified: $modified files. Skipped: $skipped files."
