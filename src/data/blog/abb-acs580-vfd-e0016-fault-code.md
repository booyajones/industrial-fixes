---
title: "ABB ACS580 VFD E0016 Fault - Causes & Fix"
description: "E0016 signals an internal drive fault on the ABB ACS580. Most often a control board issue or firmware corruption. Reset the drive first."
pubDatetime: 2026-07-18T07:49:28Z
modDatetime: 2026-07-18T07:49:28Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 control board (NINT-6x or equivalent)"
most_likely_cause: "Control board fault or firmware corruption"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive completely and check if the fault clears on restart"
  - "Perform a fault reset using the control panel or parameter 0004"
  - "Check the display for additional sub-codes or warnings that accompany E0016"
---

## ABB ACS580 VFD E0016 Fault — What It Means

The E0016 fault on an ABB ACS580 variable frequency drive indicates an internal system error detected by the drive's control logic. This code typically points to a problem within the drive's control circuitry, firmware, or communications between internal boards. It is less common than motor-related faults and usually requires attention to the drive itself rather than the connected motor or wiring.

Because E0016 is an internal fault, the drive has detected something inconsistent in its own operation, such as a watchdog timer failure, memory error, or communication breakdown between the control board and power board. The fault may appear on startup, during operation, or after a power cycle. Always consult your drive's user manual or parameter list for the exact definition, as internal fault codes can vary between firmware versions and drive models.

## Before You Replace Anything

Technicians sometimes replace the entire drive when the fault is actually a corrupted parameter set or loose internal ribbon cable. Always back up parameters, perform a factory reset, and check internal connections before ordering a new control board or drive.

[Jump to Fix](#fix)

## Common Causes

- **Control board failure or firmware corruption (~40%)** The drive's main control board may have experienced a fault, memory error, or firmware corruption that prevents normal operation.
- **Internal communication error between boards (~25%)** A loose or corroded ribbon cable or connector between the control board and power board can interrupt internal data exchange.
- **Parameter corruption or incompatible parameter set (~20%)** Stored parameters may have become corrupted due to power loss, electrical noise, or an incomplete firmware update.
- **Electromagnetic interference or noise (~10%)** High electrical noise from nearby equipment or poor grounding can cause the drive to register false internal faults.
- **Power supply fluctuation or brownout (~5%)** Unstable incoming line voltage or a momentary dip can cause the control processor to fault and log E0016.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a full power cycle and fault reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may have been transient due to noise or a momentary power issue. Monitor the drive during operation and check grounding and line voltage stability.<br><strong>No:</strong> The fault is persistent, indicating a hardware or firmware problem. Proceed to parameter backup and factory reset.</div>
</details>

<details class="dtree"><summary>Does the drive display any additional fault codes or warnings along with E0016?</summary>
<div class="dtree-body"><strong>Yes:</strong> Note all codes and cross-reference them in the manual. Multiple codes can help pinpoint whether the issue is power-related, communication-related, or board-level.<br><strong>No:</strong> E0016 alone suggests an internal control board or firmware issue. Attempt a factory parameter reset and firmware reload if available.</div>
</details>

<details class="dtree"><summary>Does the fault appear immediately on power-up, or only during motor operation?</summary>
<div class="dtree-body"><strong>Yes:</strong> If it appears immediately, the control board or internal communication is likely at fault. If during operation, check for electrical noise, grounding, or load-related disturbances.<br><strong>No:</strong> Intermittent faults suggest noise, loose connections, or thermal issues. Inspect internal connectors and cooling fans.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** completely by opening the upstream disconnect and waiting at least five minutes for capacitors to discharge.
2. **Record all current parameters** by uploading them to a PC using the drive's software tool or writing down critical settings from the keypad.
3. **Perform a fault reset** by navigating to parameter 0004 (Fault Reset) and executing the reset, or by cycling power and pressing the reset button on the keypad.
4. **Inspect internal connections** by removing the front cover and checking that all ribbon cables and connectors between the control board and power board are seated firmly and free of corrosion.
5. **Restore factory defaults** through the parameter menu (consult your model's manual for the exact reset parameter), then reload your saved parameters one group at a time to isolate any corrupted settings.
6. **Update or reload firmware** if your drive supports field updates, using ABB's DriveStudio or DriveWindow software and the latest firmware file from ABB's support site.
7. **Test under no load** by disconnecting the motor and powering up the drive to see if E0016 recurs, helping isolate drive-internal faults from external noise or load issues.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 control board (NINT-6x or equivalent) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0016-fault-code&k=ABB+ACS580+control+board+%28NINT-6x+or+equivalent%29&tag=errorcodefixes-20) \| Match the exact board revision and firmware version to your drive model and serial number |
| Internal ribbon cable kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0016-fault-code&k=Internal+ribbon+cable+kit&tag=errorcodefixes-20) \| Replacement flat-flex cables if inspection reveals damage or intermittent contact |

## When to Call a Pro

Call a qualified electrical technician or ABB-certified service partner if the fault persists after a factory reset and firmware reload, or if you are uncomfortable working inside the drive enclosure. Variable frequency drives contain high-voltage DC bus capacitors that remain charged even after input power is disconnected. Internal board replacement and advanced diagnostics require specialized tools, knowledge of drive architecture, and proper ESD precautions. A professional can also liaise with ABB technical support to obtain board-level diagnostics, log files, and warranty service if the drive is still under coverage.

**Rough cost:** A pro service call runs about $300-800.

## See Also

- [ABB ACS580 VFD E0022 Fault - Causes & Fix](/posts/abb-acs580-vfd-e0022-fault-code/)
- [ABB ACS580 VFD E0031 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0031-fault-code/)
- [ABB ACS550 EFB2 Fault Code - Causes & Fix](/posts/abb-acs550-efb2-fault-code/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
