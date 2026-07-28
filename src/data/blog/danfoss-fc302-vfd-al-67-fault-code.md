---
title: "Danfoss FC302 AL-67 Fault - Causes & Fix"
description: "AL-67 means option module configuration mismatch on your Danfoss VFD. Most common fix: reseat the option card and power-cycle the drive."
pubDatetime: 2026-06-22T10:20:33Z
modDatetime: 2026-06-22T10:20:33Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 option module (FCN, FCM, ENC, or communication module)"
most_likely_cause: "Loose or improperly seated option card"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive completely (disconnect AC mains, wait 10 seconds, reconnect and restart)"
  - "Open the enclosure and visually inspect that the option module is fully seated in its slot with no debris"
  - "Verify terminal 37 is not incorrectly connected to terminal 12 and that terminal 27 is not in use unless required"
no_buy_pct: "60%"
---

## What this code means
Alarm 67 on the Danfoss FC302 VFD indicates that the drive has detected a different option card (communication, I/O, or encoder module) than the one previously configured or recognized during startup. This is a configuration validation error, not a power or motor fault. The drive performs a self-check at startup and compares the expected option module ID with the actual hardware present. When these do not match, AL-67 is triggered.

The fault typically appears after an option module has been physically inserted, removed, replaced, or when the stored configuration has been corrupted by a power loss or firmware glitch. The drive will not operate normally until the hardware and software configuration are brought back into alignment.

## Before You Replace Anything

Technicians sometimes replace the control card when the real issue is simply a loose or incompatible option module. Always verify the physical module is seated correctly and matches the drive's parameter configuration before ordering control boards.

## Common Causes

- **Loose or improperly seated option card (~40%)** Physical vibration or incomplete installation causes intermittent detection or failure to initialize during the drive's startup self-check.
- **Option module swapped without parameter update (~25%)** A fieldbus or I/O module was replaced with a different type but the drive's internal parameters still reference the old module ID.
- **Power loss or firmware glitch (~15%)** A sudden shutdown or brownout corrupted the stored option module configuration in the drive's memory.
- **Incorrect terminal wiring conflict (~10%)** Terminal 37 or terminal 27 is active and conflicts with the option module's expected functionality, causing detection failure.
- **Non-genuine or incompatible option module (~7%)** A third-party or wrong-series module lacks the correct identification firmware and the drive cannot recognize it.
- **Faulty control PCB (~3%)** In rare cases the drive's control board itself fails to properly read a correctly installed and compatible option module.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm clear after a full power-cycle (AC mains disconnected for 10 seconds)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The configuration was temporarily corrupted. Document the issue and monitor for recurrence, which may indicate a loose card or wiring vibration.<br><strong>No:</strong> Proceed to physically inspect the option module slot and verify the module is fully seated and matches the drive parameters.</div>
</details>

<details class="dtree"><summary>Is the installed option module the same model number as the one listed in the drive's parameter configuration?</summary>
<div class="dtree-body"><strong>Yes:</strong> The module may be loose or damaged. Reseat it firmly, clean any debris from the connector, and restart the drive.<br><strong>No:</strong> The drive expects a different module. Either replace the physical module with the correct type or use Danfoss MCT 10 software to reconfigure the drive for the installed module.</div>
</details>

<details class="dtree"><summary>Are terminals 37 or 27 wired for functions not required by your application?</summary>
<div class="dtree-body"><strong>Yes:</strong> Disconnect terminal 37 from terminal 12 if not needed and set parameter 5-12 (Terminal 27 Digital Input) to [0] No function, then restart.<br><strong>No:</strong> The option module or control card is likely faulty and requires professional diagnosis with MCT 10 software or replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect all power** by turning off the AC mains supply and any DC-link power sources including UPS or batteries, and wait at least 10 seconds for capacitors to discharge.
2. **Open the drive enclosure** and locate the option module slot on the control card, typically on the side or front of the FC302 unit.
3. **Inspect the option module physically** for proper seating, bent pins, or debris in the connector, and press firmly to reseat if necessary.
4. **Verify the module model number** matches the configuration expected by the drive, either by checking the label or using Danfoss MCT 10 software to read the current module ID.
5. **Power-cycle the drive** by reconnecting AC mains and allowing it to complete its startup self-check, then observe whether AL-67 clears.
6. **Check terminal wiring** to confirm terminal 37 is not connected to terminal 12 unless your application requires it, and set parameter 5-12 to [0] No function if terminal 27 is unused.
7. **Reconfigure or replace the module** using MCT 10 software to update the drive parameters if the physical module has changed, or install the correct Danfoss-certified option module if the current one is incompatible or damaged.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 option module (FCN, FCM, ENC, or communication module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-67-fault-code&k=Danfoss+FC302+option+module+%28FCN%2C+FCM%2C+ENC%2C+or+communication+module%29&tag=errorcodefixes-20) \| Must match your application and be Danfoss-certified for the FC302 series; consult your drive's manual for the correct model number. |
| Danfoss FC302 control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-67-fault-code&k=Danfoss+FC302+control+PCB&tag=errorcodefixes-20) \| Only needed if the option module is confirmed good but the drive still fails to detect it after reseating and power-cycling. |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained to work inside variable frequency drives or if you lack access to Danfoss MCT 10 configuration software. High-voltage AC mains and DC-link capacitors present shock and arc-flash hazards. A professional can safely diagnose whether the issue is a loose module, incorrect parameter settings, or a failed control board, and can reconfigure the drive or replace components as needed. If your facility does not have a maintenance contract, expect a service call fee plus parts and labor.

**Rough cost:** A pro service call runs about $150-400 for service call and configuration reset, more if module replacement needed.
