Push-Location C:\Users\Administrator\.openclaw\workspace\industrial-fixes

$files = Get-ChildItem src\data\blog -Filter "*.md"
$fixedStep = 0
$fixedParts = 0

foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw
    $changed = $false

    # Fix Step-by-Step Fix heading missing anchor
    if ($content -match "## Step-by-Step Fix\r?\n" -and $content -notmatch "## Step-by-Step Fix \{#step-by-step-fix\}") {
        $content = $content -replace "## Step-by-Step Fix(\r?\n)", "## Step-by-Step Fix {#step-by-step-fix}`$1"
        $changed = $true
        $fixedStep++
    }

    # Fix Parts heading missing anchor (various phrasings)
    if ($content -match "## Parts That May Need Replacement\r?\n" -and $content -notmatch "## Parts That May Need Replacement \{#parts-that-may-need-replacement\}") {
        $content = $content -replace "## Parts That May Need Replacement(\r?\n)", "## Parts That May Need Replacement {#parts-that-may-need-replacement}`$1"
        $changed = $true
        $fixedParts++
    }

    if ($changed) {
        Set-Content $f.FullName $content -NoNewline
        Write-Host "Fixed: $($f.Name)"
    }
}

Write-Host "Done. Step anchors fixed: $fixedStep, Parts anchors fixed: $fixedParts"
Pop-Location
