# inject-affiliate-links.ps1
# Run this AFTER Impact.com approves Repair Clinic / SupplyHouse / Grainger campaigns.
# Replaces plain-text part source mentions with tracked affiliate links.
#
# SETUP: Fill in your Impact.com tracking URLs below before running.
# Get them from app.impact.com → Campaigns → [merchant] → Links → Get Link
#
# Usage: powershell -ExecutionPolicy Bypass -File inject-affiliate-links.ps1

$REPAIRCLINIC_BASE = "https://www.repairClinic.com/?utm_source=errorcodefixes&utm_medium=affiliate"   # Replace with Impact tracking URL
$SUPPLYHOUSE_BASE  = "https://www.supplyhouse.com/?utm_source=errorcodefixes&utm_medium=affiliate"    # Replace with Impact tracking URL
$GRAINGER_BASE     = "https://www.grainger.com/?utm_source=errorcodefixes&utm_medium=affiliate"       # Replace with Impact tracking URL
$AMAZON_BASE       = "https://www.amazon.com/?tag=errorcodefixes-20"                                   # Replace with your Amazon Associates tag

# Mapping: plain text mention → replacement markdown link
$replacements = @{
    # RepairClinic
    "| RepairClinic |"       = "| [RepairClinic]($REPAIRCLINIC_BASE) |"
    "RepairClinic |"         = "[RepairClinic]($REPAIRCLINIC_BASE) |"
    ", RepairClinic"         = ", [RepairClinic]($REPAIRCLINIC_BASE)"
    "RepairClinic,"          = "[RepairClinic]($REPAIRCLINIC_BASE),"

    # SupplyHouse
    "| SupplyHouse |"        = "| [SupplyHouse]($SUPPLYHOUSE_BASE) |"
    "SupplyHouse |"          = "[SupplyHouse]($SUPPLYHOUSE_BASE) |"
    ", SupplyHouse"          = ", [SupplyHouse]($SUPPLYHOUSE_BASE)"
    "SupplyHouse,"           = "[SupplyHouse]($SUPPLYHOUSE_BASE),"
    "/ SupplyHouse"          = "/ [SupplyHouse]($SUPPLYHOUSE_BASE)"

    # Grainger
    "| Grainger |"           = "| [Grainger]($GRAINGER_BASE) |"
    "Grainger |"             = "[Grainger]($GRAINGER_BASE) |"
    ", Grainger"             = ", [Grainger]($GRAINGER_BASE)"
    "Grainger,"              = "[Grainger]($GRAINGER_BASE),"

    # Amazon
    "| Amazon |"             = "| [Amazon]($AMAZON_BASE) |"
    "Amazon |"               = "[Amazon]($AMAZON_BASE) |"
    ", Amazon"               = ", [Amazon]($AMAZON_BASE)"
    "Amazon,"                = "[Amazon]($AMAZON_BASE),"
    "HVAC Supply, Amazon"    = "HVAC Supply, [Amazon]($AMAZON_BASE)"
}

Push-Location $PSScriptRoot

$files = Get-ChildItem src\data\blog -Filter "*.md"
$totalFixed = 0
$filesFixed = 0

foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw
    $originalContent = $content
    $fileChanged = $false

    foreach ($pattern in $replacements.Keys) {
        # Only replace if it's not already a markdown link (avoid double-linking)
        if ($content -match [regex]::Escape($pattern) -and $content -notmatch "\[$pattern\]") {
            $content = $content.Replace($pattern, $replacements[$pattern])
            $fileChanged = $true
            $totalFixed++
        }
    }

    if ($fileChanged) {
        Set-Content $f.FullName $content -NoNewline
        Write-Host "Injected links: $($f.Name)"
        $filesFixed++
    }
}

Write-Host ""
Write-Host "Done. Files updated: $filesFixed, link replacements: $totalFixed"
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Replace placeholder URLs above with real Impact.com tracking links"
Write-Host "  2. Run: git add -A && git commit -m 'Add affiliate tracking links' && git push"
Write-Host "  3. Verify live at https://errorcodefixes.com"

Pop-Location
