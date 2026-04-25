from pathlib import Path
import re

p = Path(r"C:\Users\Administrator\.openclaw\workspace\industrial-fixes\src\data\blog")
meta = {
    'ruud-upnl-heat-pump-error-codes.md': (
        'Ruud UPNL Heat Pump Error Codes - What It Means and How to Fix It',
        'Ruud UPNL Prestige variable-speed heat pumps use communicating diagnostics to report pressure, sensor, fan, reversing valve, and control board faults. This guide explains the most common UPNL error codes and the repair steps that usually solve them.',
        '## What Does Ruud UPNL Heat Pump Error Codes Mean?'
    ),
    'ruud-ugph-error-codes.md': (
        'Ruud UGPH Error Codes - What It Means and How to Fix It',
        'Ruud UGPH gas furnaces use LED blink codes to report ignition, pressure switch, inducer, limit, and rollout faults. This guide explains every 1 through 9 flash code and the fixes that usually get the furnace running again.',
        '## What Does Ruud UGPH Error Codes Mean?'
    ),
    'ecosmart-eco27-error-codes.md': (
        'EcoSmart ECO 27 Error Codes - What It Means and How to Fix It',
        'EcoSmart ECO 27 electric tankless water heaters use E1, E2, E3, E4, and Err codes to report flow, sensor, heating element, and thermal cutoff faults. This guide shows what each code means and the parts most likely to fix it.',
        '## What Does EcoSmart ECO 27 Error Codes Mean?'
    ),
    'ecosmart-eco36-error-codes.md': (
        'EcoSmart ECO 36 Error Codes - What It Means and How to Fix It',
        'EcoSmart ECO 36 electric tankless water heaters use the same core fault architecture as the ECO 27, but the higher-capacity unit has different flow, amperage, and heating element considerations. This guide explains each code and the repair steps that make sense on the 36kW platform.',
        '## What Does EcoSmart ECO 36 Error Codes Mean?'
    ),
    'eccotemp-i12-error-codes.md': (
        'Eccotemp i12 Error Codes - What It Means and How to Fix It',
        'Eccotemp i12 indoor tankless water heaters use E1 through E9 codes to report ignition, flame, temperature, flow, and fan faults. This guide explains what each code usually means and how to diagnose the likely failed part.',
        '## What Does Eccotemp i12 Error Codes Mean?'
    ),
    'eccotemp-fvi12-error-codes.md': (
        'Eccotemp FVI12 Error Codes - What It Means and How to Fix It',
        'Eccotemp FVI12 flush-mount indoor tankless water heaters share the i12 error architecture but add installation-specific airflow and access issues. This guide explains the common E1 through E9 codes and the fastest path to diagnosing them.',
        '## What Does Eccotemp FVI12 Error Codes Mean?'
    ),
    'takagi-tkjr2-error-codes.md': (
        'Takagi TK-Jr2 Error Codes - What It Means and How to Fix It',
        'Takagi TK-Jr2 tankless water heaters use numeric codes like 11, 12, 14, 16, 31, 52, 61, and 91 to report ignition, sensor, gas valve, fan, and exhaust faults. This guide explains every major TK-Jr2 code and the repair steps that usually fix it.',
        '## What Does Takagi TK-Jr2 Error Codes Mean?'
    ),
    'friedrich-mini-split-error-codes.md': (
        'Friedrich Mini-Split Error Codes - What It Means and How to Fix It',
        'Friedrich mini-split systems use E-codes and F-codes to report sensor faults, fan failures, pressure protection events, and communication problems. This guide covers the most important Friedrich Uni-Fit, Kühl, and ductless error codes in one place.',
        '## What Does Friedrich Mini-Split Error Codes Mean?'
    ),
    'american-standard-platinum-18-heat-pump-codes.md': (
        'American Standard Platinum 18 Heat Pump Codes - What It Means and How to Fix It',
        'American Standard Platinum 18 heat pumps use the AccuLink communicating platform to report numeric faults from the outdoor unit, air handler, and thermostat. This guide explains the most important system, sensor, compressor, and communication codes, plus the repair steps that usually solve them.',
        '## What Does American Standard Platinum 18 Heat Pump Codes Mean?'
    ),
    'bosch-ids-2-heat-pump-error-codes.md': (
        'Bosch IDS 2 Heat Pump Error Codes - What It Means and How to Fix It',
        'Bosch IDS 2.0 heat pumps use inverter-driven controls, thermistors, and board-level protection logic to report faults before major damage happens. This guide explains the most common E-codes and F-codes, what they indicate, and the repair steps worth trying before replacing expensive parts.',
        '## What Does Bosch IDS 2 Heat Pump Error Codes Mean?'
    ),
}

for fname, (title, desc, h1) in meta.items():
    path = p / fname
    txt = path.read_text(encoding='utf-8')
    txt = txt.replace('\u2013', '-').replace('\u2014', '-').replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    frontmatter = (
        f'---\n'
        f'title: "{title}"\n'
        f'description: "{desc}"\n'
        f'pubDatetime: 2026-04-25T00:00:00Z\n'
        f'author: errorcodefixes.com\n'
        f'tags:\n'
        f'  - hvac\n'
        f'  - error-codes\n'
        f'---\n'
    )
    txt = re.sub(r'^---\n.*?\n---\n', frontmatter, txt, count=1, flags=re.S)
    txt = re.sub(r'^## .*?Mean\?$', h1, txt, count=1, flags=re.M)

    headings = [m.group(0) for m in re.finditer(r'^## .+$', txt, flags=re.M)]
    if len(headings) >= 2:
        txt = txt.replace(headings[1], '## How to Fix It', 1)

    lines = txt.splitlines()
    out = []
    in_parts = False
    for line in lines:
        if line.strip() == '## Parts You May Need':
            in_parts = True
            out.append(line)
            continue
        if in_parts and line.startswith('| Part |'):
            out.append('| Part | Why You Need It | Approx. Cost |')
            continue
        if in_parts and line.startswith('|------'):
            out.append('|------|----------------|-------------|')
            continue
        if in_parts and line.startswith('| ') and '[Search on Amazon](' in line:
            cols = [x.strip() for x in line.split('|')[1:-1]]
            if len(cols) >= 4:
                part, why, cost, link = cols[:4]
                m = re.search(r'\((https://[^)]+)\)', link)
                if m:
                    part = f'[{part}]({m.group(1)})'
                out.append(f'| {part} | {why} | {cost} |')
                continue
        if in_parts and line.startswith('## ') and line.strip() != '## Parts You May Need':
            in_parts = False
        out.append(line)

    path.write_text('\n'.join(out) + '\n', encoding='utf-8')

print(f'normalized {len(meta)} files')
