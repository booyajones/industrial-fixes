#!/usr/bin/env pwsh
# assign_authors.ps1 - Bulk assign author names based on article tags

$blogDir = "src\data\blog"
$stats = @{ "Marcus Webb" = 0; "Dana Kowalski" = 0; "James Rutherford" = 0; "unchanged" = 0 }

$files = Get-ChildItem $blogDir -Filter "*.md"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # Only update articles with generic authors
    if (-not ($content -match 'author:\s*"?(ErrorCodeFixes|errorcodefixes\.com)"?')) {
        $stats["unchanged"]++
        continue
    }
    
    # Extract tags block
    $tags = ""
    if ($content -match '(?ms)tags:\s*\n((?:\s+- .+\n)+)') {
        $tags = $Matches[1]
    }
    
    # Determine author based on tags
    $newAuthor = $null
    
    if ($tags -match '\b(vfd|cnc|industrial-maintenance|plc|drives|motor-overload|dc-bus|heatsink|overcurrent|allen-bradley|siemens|yaskawa|danfoss|abb|fanuc|haas|mazak|okuma)\b') {
        $newAuthor = "Dana Kowalski"
    } elseif ($tags -match '\b(water-heater|tankless|plumbing|ice-machine|commercial-kitchen|commercial-refrigeration|refrigeration|hoshizaki|scotsman|manitowoc|ice-o-matic|follett|beverage-air|true-refrigerator|arctic-air|master-bilt|perlick|turbo-air)\b') {
        $newAuthor = "James Rutherford"
    } elseif ($tags -match '\b(hvac|furnace|heat-pump|mini-split|boiler|air-conditioner|ac|thermostat|compressor|heating|cooling|carrier|trane|lennox|goodman|rheem|york|american-standard|amana|heil|tempstar|mitsubishi|daikin|fujitsu|friedrich|ecobee|honeywell)\b') {
        $newAuthor = "Marcus Webb"
    } else {
        # Default to Marcus Webb for anything else HVAC-adjacent
        $newAuthor = "Marcus Webb"
    }
    
    # Replace author line
    $newContent = $content -replace 'author:\s*"?(ErrorCodeFixes|errorcodefixes\.com)"?', "author: `"$newAuthor`""
    
    if ($newContent -ne $content) {
        Set-Content -Path $file.FullName -Value $newContent -NoNewline
        $stats[$newAuthor]++
    }
}

Write-Host "Author assignment complete:"
$stats.GetEnumerator() | Sort-Object Key | ForEach-Object { Write-Host "  $($_.Key): $($_.Value)" }
