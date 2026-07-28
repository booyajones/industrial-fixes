---
title: "Yaskawa A1000 AL-22 - Causes & Fix"
description: "AL-22 does not exist on the A1000. You likely saw u22 (fault history menu) or LT-2 (capacitor maintenance alarm). Check the display again."
pubDatetime: 2026-06-29T10:37:23Z
modDatetime: 2026-06-29T10:37:23Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa A1000 replacement drive (same HP and voltage rating)"
most_likely_cause: "misreading the display (u22 fault history menu or LT-2 capacitor alarm)"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Write down the exact characters on the display and compare to the A1000 fault list in your manual"
  - "If the display shows u22, press Enter to view the actual stored fault code"
  - "Check ambient temperature around the drive cabinet (should be below 40°C for full capacity)"
---

## What this code means
The Yaskawa A1000 does not have a fault code named AL-22. If you see u22 on the display, that is the fault history monitor menu, not a fault itself. Press Enter on u22 to view the actual stored fault code (like oC for overcurrent or oH for overheat), then diagnose that specific code. If you saw LT-2 (which looks similar to AL-2), that is a capacitor maintenance alarm indicating the main circuit and control circuit capacitors have reached 90% of their expected life (typically around 10 years). LT-2 is an alarm, not a fault, so the drive continues operating, but Yaskawa recommends replacing the entire drive when this alarm appears.

If the display shows something else that you interpreted as AL-22, write down the exact characters and compare them to the full fault list in your A1000 manual. Common codes that operators misread include LT-2, u22, oL (overload), and oC (overcurrent). Always verify the exact code before ordering parts or starting repairs.

## Before You Replace Anything

Users often order replacement boards or capacitors without confirming the actual code. Write down the exact code on the display and compare it to the A1000 fault list in the manual before buying anything.

## Common Causes

- **Misread display showing u22 fault history menu (~40%)** The operator saw u22 and thought it was a fault code, but u22 is only a menu to view past faults stored in memory.
- **Misread LT-2 capacitor maintenance alarm as AL-2 (~30%)** The display shows LT-2 (capacitor life at 90%), which looks similar to AL-2 under poor lighting or viewing angle.
- **Aged capacitors triggering LT-2 (~15%)** Main circuit and control capacitors have degraded after 10+ years of operation or prolonged high ambient temperature exposure.
- **Poor ventilation accelerating capacitor aging (~10%)** Blocked airflow or failed cooling fan causes internal temperature to rise above 40°C, shortening capacitor life and triggering LT-2 earlier.
- **Incorrect code transcription from panel (~5%)** The operator wrote down the wrong characters or confused similar-looking codes like oL, LC, or LT with AL.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show exactly u22 with a lowercase u?</summary>
<div class="dtree-body"><strong>Yes:</strong> Press Enter to view the actual stored fault code, then diagnose that fault using the A1000 manual.<br><strong>No:</strong> Write down the exact characters (including case and hyphens) and compare to the A1000 fault list.</div>
</details>

<details class="dtree"><summary>Does the display show LT-2 (with a hyphen)?</summary>
<div class="dtree-body"><strong>Yes:</strong> This is a capacitor maintenance alarm. The drive still runs, but plan to replace the entire drive soon (Yaskawa does not support field capacitor replacement).<br><strong>No:</strong> The code you saw is not AL-22. Check the manual for the exact code or call a VFD technician to read the panel.</div>
</details>

<details class="dtree"><summary>Is the ambient temperature around the drive above 40°C (104°F)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Improve ventilation, check the cooling fan, and clean any dust from the heat sink. High temperature accelerates capacitor aging and can cause multiple alarms.<br><strong>No:</strong> The issue is likely misread code or a different fault. Confirm the exact code before proceeding.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Write down the exact code** displayed on the digital operator, including uppercase, lowercase, hyphens, and numbers.
2. **Compare the code** to the fault and alarm list in your A1000 manual (consult the appendix or troubleshooting chapter).
3. **If the display shows u22**, press the Enter key to navigate into the fault history and read the actual stored fault code (like oC, oH, or LT-2).
4. **If the display shows LT-2**, check the ambient temperature around the drive and confirm cooling fan operation. Plan to replace the drive, as Yaskawa recommends full replacement when capacitors reach 90% life.
5. **If you see a different code**, look up that specific code in the manual and follow the diagnostic steps for that fault (for example, oC requires checking motor and cable insulation, oH requires checking heat sink and fan).
6. **Take a photo** of the display if you are unsure of the exact characters, and send it to a qualified VFD technician or Yaskawa distributor for confirmation.
7. **Do not order parts** based on AL-22, as that code does not exist in the A1000 fault list and ordering the wrong component wastes time and money.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa A1000 replacement drive (same HP and voltage rating) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-a1000-vfd-al-22-fault-code&k=Yaskawa+A1000+replacement+drive+%28same+HP+and+voltage+rating%29&tag=errorcodefixes-20) \| Required for LT-2 alarm; Yaskawa does not support field capacitor replacement on the A1000 series. |

## When to Call a Pro

Call a qualified VFD technician or Yaskawa-authorized service provider if you cannot identify the exact code on the display, if the drive shows multiple faults at once, or if you confirm an LT-2 alarm and need help selecting and installing a replacement drive. VFD work involves high DC bus voltages (600V or more) that remain present even after input power is disconnected, so only trained personnel should open the drive cabinet or measure internal voltages. If you see u22 and cannot navigate the menu to view the stored fault, a technician can retrieve the fault history using parameter programming software and diagnose the root cause. For LT-2, a pro can also evaluate whether your application and environment contributed to early capacitor aging and recommend ventilation or cooling improvements for the replacement drive.

**Rough cost:** A pro service call runs about $1,500-4,000 for drive replacement (LT-2) or $150-500 for fault diagnosis and repair (other codes).
