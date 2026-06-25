---
title: "Danfoss FC302 AL-99 Fault - Causes & Fix"
description: "AL-99 is not a valid Danfoss FC302 code. Most likely a misread display (Alarm 38 internal fault). Power cycle the drive first."
pubDatetime: 2026-06-23T10:16:46Z
modDatetime: 2026-06-23T10:16:46Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 control/logic card"
most_likely_cause: "misread display or Alarm 38 internal control-card fault"
likelihood: "the most common cause if the display shows anything close to 99"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive (turn off, wait 5 minutes, restart) to clear transient errors"
  - "Check parameter 15-32 on the LCP for additional fault codes that explain the internal issue"
  - "Verify the exact alarm number on the display (look closely for Alarm 38, Alarm 13, or Alarm 16 instead of AL-99)"
---

## Danfoss FC302 AL-99 Fault — What It Means

The code AL-99 does not appear in any official Danfoss FC302 documentation. Danfoss FC302 drives use numeric alarm IDs like Alarm 13, Alarm 38, or Alarm 16. No published manual lists AL-99 or AL-99 fault. This likely results from a misread display (for example, confusing AL-38 with AL-99), a typo, or a third-party display error. If you see something that looks like AL-99, the most common internal fault on the FC302 is Alarm 38, which indicates an internal fault in the drive's logic or control board, memory corruption, or firmware errors. Alarm 38 is often triggered by transient software glitches, control card component failure, or electrical noise damaging the control card. Check your drive's LCP display carefully and consult the Danfoss FC302 manual Table 6.1 for the exact alarm number and its definition.

## Before You Replace Anything

Technicians sometimes replace the entire power stack or IGBT module when Alarm 38 appears, but the fault is usually in the control/logic card. Check parameter 15-32 for extended diagnostics and power cycle the drive three times before ordering hardware.

[Jump to Fix](#fix)

## Common Causes

- **Misread or typoed alarm number (~40%)** The display shows Alarm 38 or another numeric code but was recorded as AL-99 in error.
- **Firmware corruption or memory error in the control card (Alarm 38) (~30%)** Transient software errors or corrupted firmware in the drive's logic board trigger an internal fault.
- **Control board component failure (Alarm 38) (~20%)** Damaged ICs, failed capacitors, or solder joints on the control/logic card cause persistent internal faults.
- **Electrical noise or voltage spikes (Alarm 38) (~10%)** Noise coupled into control wiring or transient voltage spikes damage the control card logic.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive display show a two-digit numeric alarm (e.g. 38, 13, 16) instead of AL-99?</summary>
<div class="dtree-body"><strong>Yes:</strong> Look up that alarm number in the Danfoss FC302 manual Table 6.1 and follow the repair steps for that specific code.<br><strong>No:</strong> The code AL-99 is not valid. Contact Danfoss technical support or check if the drive is a non-Danfoss model.</div>
</details>

<details class="dtree"><summary>Does the alarm clear after a single power cycle and not return?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was a transient software glitch. Monitor the drive for recurring alarms over the next few days.<br><strong>No:</strong> The fault is persistent. Check parameter 15-32 for extended diagnostics and plan to replace the control card.</div>
</details>

<details class="dtree"><summary>Does parameter 15-32 show additional fault codes or extended diagnostics?</summary>
<div class="dtree-body"><strong>Yes:</strong> Use those codes to narrow the failure (e.g. memory checksum error, watchdog timeout). Replace the control card or update firmware via Danfoss MCT 10 software.<br><strong>No:</strong> The control card itself is likely failed. Replace the control/logic card for your exact FC302 model.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm number** by looking directly at the LCP display. Write down the full code including any prefix or suffix. If it truly says AL-99, note the drive model and serial number.
2. **Power cycle the drive** by turning off mains power, waiting at least 5 minutes for capacitors to discharge, then restarting. Observe whether the alarm reappears immediately or after a few seconds.
3. **Check parameter 15-32** for extended diagnostics. Press the menu button on the LCP, navigate to parameter group 15, and scroll to 15-32. Record any additional fault codes or numbers displayed.
4. **Test control-card supply voltage** by measuring 24 VDC at terminals 12 and 13 with a multimeter. If voltage is unstable or missing, check external 24 VDC supply or internal power-supply board.
5. **Inspect control wiring for noise** by verifying that all digital input cables are shielded and grounded at one end. Reroute control wiring away from power cables if they run parallel.
6. **Replace the control/logic card** if the alarm persists after three power cycles and parameter 15-32 confirms a memory or watchdog fault. Order the correct FC302 control card from Danfoss or an authorized distributor and swap the board.
7. **Contact Danfoss technical support** if the code AL-99 remains on the display after all steps, as this may indicate a rare hardware fault or a non-standard drive version not covered in published manuals.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 control/logic card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-99-fault-code&k=Danfoss+FC302+control%2Flogic+card&tag=errorcodefixes-20) \| Must match your exact FC302 power rating and firmware version; check the drive nameplate and order from Danfoss or Wake Industrial. |
| Danfoss FC302 power stack assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-99-fault-code&k=Danfoss+FC302+power+stack+assembly&tag=errorcodefixes-20) \| Includes IGBTs and capacitors; only needed if Alarm 38 parameter 15-32 indicates IGBT or gate-driver fault rather than pure logic fault. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss-certified service partner if you cannot confirm the exact alarm number, if parameter 15-32 shows codes you do not understand, or if the drive continues to fault after a control-card replacement. Professional diagnostics include oscilloscope tests of gate-driver signals, firmware reflashing via MCT 10 software, and full power-stack load testing. If the drive is under warranty, contact Danfoss immediately rather than opening the enclosure. High-voltage DC bus capacitors remain charged for several minutes after power-off and pose a serious shock hazard.

**Rough cost:** A pro service call runs about $300-800 depending on whether a control card or full power stack is needed.
