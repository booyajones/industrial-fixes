---
title: "Yaskawa GA800 E66 Fault - Causes & Fix"
description: "E66 is not a standard GA800 fault code in Yaskawa documentation. Verify the exact display, check wiring and the elementary diagram, then contact Yaskawa support."
pubDatetime: 2026-06-06T11:50:22Z
modDatetime: 2026-06-06T11:50:22Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
diy_or_pro: "pro"
money_part: "GA800 control board"
most_likely_cause: "Misread or misidentified display"
---

## What this code means
E66 does not appear as a standard fault code in the available Yaskawa GA800 manufacturer documentation. The GA800 uses a defined set of fault, alarm, and error codes, but E66 is not confirmed among them. This means the display may be showing a communication message, an option-card code, or a misread character. Yaskawa expects technicians to identify the exact fault or alarm code, the drive model and spec number, the serial number, and the application context before troubleshooting or calling support.

Because the code is not documented in the standard fault tables, the correct approach is to verify what the keypad or display is actually showing, record the full drive nameplate information, and refer to the elementary diagram and wiring to understand what circuit or option might be involved. The GA800 maintenance and troubleshooting manual supports only fan and control board replacement as field-serviceable components, so further diagnosis and repair for unconfirmed codes require manufacturer support.

## Before You Replace Anything

Do not replace the control board or power module without first confirming the exact code definition and checking for loose connections or wiring faults. Many drive faults are caused by external wiring issues that appear as internal errors.

## Common Causes

- **Misread or misidentified display** The operator keypad may be showing a communication message, option alarm, or a character similar to E66 that is actually a different code.
- **Communication or option card fault** If an optional communication or expansion card is installed, the code may originate from that module rather than the main drive.
- **Loose or damaged control wiring** Control terminals, parameter connections, or wiring to external devices can trigger unrecognized or intermittent fault displays.
- **Control board fault** The control board is one of the two field-replaceable components mentioned in the GA800 maintenance guide and may generate non-standard displays if failing.
- **Cooling fan failure** The cooling fan is the other field-replaceable component and its failure can lead to secondary faults or unusual error messages.
- **Corrupted parameter memory** Drive parameters stored in memory may be corrupted, causing the display to show non-standard codes or behave unpredictably.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the keypad show the same code every time the drive powers up?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is persistent. Record the exact characters, model, and serial number, then consult the elementary diagram and contact Yaskawa support.<br><strong>No:</strong> The fault is intermittent. Check all control wiring connections and inspect for loose terminals or damaged cables before the next power cycle.</div>
</details>

<details class="dtree"><summary>Is an optional communication or expansion card installed in the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Remove or reseat the option card and power cycle the drive. The code may be option-specific and not documented in the main fault table.<br><strong>No:</strong> The fault originates in the main drive. Verify the cooling fan is running and check for obvious control board damage or burnt components.</div>
</details>

<details class="dtree"><summary>Can you clearly read all characters on the keypad display without obstruction or flickering?</summary>
<div class="dtree-body"><strong>Yes:</strong> The display is clear. Write down the exact code including any leading or trailing characters, then cross-reference it with the GA800 manual fault list.<br><strong>No:</strong> The display may be faulty or the keypad may need reseating. Clean the display and reseat the keypad connector before assuming the code is E66.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive following all plant safety procedures and wait for the DC bus to discharge completely before opening the enclosure or touching any terminals.
2. **Photograph or write down** the exact characters shown on the keypad or display, including any leading letters, trailing digits, or symbols that appear alongside E66.
3. **Record the drive nameplate** information including the full model number, spec code, serial number, voltage rating, and current rating so you have complete identification for support.
4. **Inspect the control board and fan** for visible damage, burnt components, loose connectors, or debris, since these are the only two field-replaceable items explicitly supported in the GA800 maintenance guide.
5. **Check all control terminal wiring** against the elementary diagram, looking for loose screws, damaged insulation, miswired terminals, or incorrect parameter wiring that could generate a non-standard fault.
6. **Reseat any optional communication or expansion cards** if installed, power cycle the drive, and observe whether the code clears or changes to a recognized alarm or fault.
7. **Contact Yaskawa technical support** with the recorded drive information, exact code display, application details, and time in service to obtain the correct fault definition and repair guidance for your specific drive configuration.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e66-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Order by drive model and spec code. Only replace after confirming the fault definition with Yaskawa support. |
| GA800 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e66-fault-code&k=GA800+cooling+fan+assembly&tag=errorcodefixes-20) \| Match the fan voltage and frame size to your drive nameplate. Check fan operation before ordering. |

## When to Call a Pro

Call a qualified Yaskawa service technician or distributor immediately if the drive displays E66 or any other unrecognized code. The GA800 maintenance guide explicitly limits field-serviceable repairs to fan and control board replacement, and all other diagnosis and component-level repair require factory training and support. A technician will verify the exact code definition, check the elementary diagram and parameter settings, inspect the power module and internal connections, and coordinate with Yaskawa if the fault is not documented in standard literature. Do not attempt to clear or reset unconfirmed faults without understanding their cause, as this can lead to equipment damage or unsafe operation.

**Rough cost:** A pro service call runs about $200-500.
