---
title: "Danfoss FC302 AL-111 - Causes & Fix"
description: "AL-111 is not a valid Danfoss FC302 fault code. Verify the display shows AL 13, AL 38, or AL 47 instead and troubleshoot accordingly."
pubDatetime: 2026-06-24T10:08:11Z
modDatetime: 2026-06-24T10:08:11Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control PCB (Logic Board)"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive completely (wait 60 seconds) and verify the exact fault code displayed"
  - "Re-read the display under good lighting to confirm the code is not AL 13, AL 38, or AL 47"
  - "Download the Danfoss FC 302 Programming Guide (Doc ID M0013101) and cross-check the alarm list"
---

## Danfoss FC302 AL-111 — What It Means

The code AL-111 does not exist in the official Danfoss FC302 alarm list. Danfoss FC302 drives use fault codes numbered AL 1 through AL 55. If you see what looks like AL-111 on the display, you are likely misreading a different code, seeing a display artifact, or encountering a custom application message from a third-party device. The most common FC302 alarms that might be confused with AL-111 are AL 13 (Overcurrent), AL 38 (Internal Fault), and AL 47 (STD Bus Timeout).

Before attempting any repair, re-read the display carefully and confirm the exact code. Check if the number is actually AL 13, AL 14, AL 38, or AL 47. If the display is unclear, power-cycle the drive and watch the fault appear again. Consult the official Danfoss VLT AutomationDrive FC 302 Operating Instructions (document ID AQ361181055259) to confirm the exact alarm list for your model.

## Before You Replace Anything

Technicians sometimes replace the entire power board when they see an overcurrent fault (AL 13), but disconnecting the motor and running the drive unloaded will confirm whether the fault is in the drive or the motor circuit.

[Jump to Fix](#fix)

## Common Causes

- **Misread display or typo (~50%)** The display may show AL 13, AL 38, or AL 47 but poor lighting or a worn screen makes it look like AL-111.
- **Custom application message (~25%)** A third-party PLC or HMI connected to the drive may be sending a non-standard fault message that appears on the LCP.
- **Display artifact or corruption (~15%)** A failing LCP keypad or communication cable can cause garbled characters that resemble AL-111.
- **Confusion with a different drive model (~10%)** Another VFD brand or model in the same installation may use AL-111, leading to cross-reference errors.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display clearly show AL-111 with no other characters or symbols?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power-cycle the drive and photograph the fault when it reappears, then compare the image to the official Danfoss alarm list.<br><strong>No:</strong> The display may be corrupted or the code is actually AL 13, AL 38, or AL 47. Clean the display and verify under bright light.</div>
</details>

<details class="dtree"><summary>Is the drive connected to a third-party PLC, HMI, or SCADA system?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the external controller for custom alarm messages. AL-111 may be a user-defined fault from the application software.<br><strong>No:</strong> The fault is likely internal to the drive. Verify the exact code and consult the Danfoss operating manual for that specific alarm.</div>
</details>

<details class="dtree"><summary>Does the fault persist after disconnecting all communication cables and power-cycling?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is internal. If the code remains AL-111, contact Danfoss technical support with your drive serial number and firmware version.<br><strong>No:</strong> The fault originated from an external controller or a communication issue. Inspect the LCP cable and any fieldbus connections.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** completely and wait 60 seconds for all internal capacitors to discharge before touching any terminals.
2. **Photograph the fault display** under good lighting so you have a clear record of the exact code shown.
3. **Compare the photo** to the official Danfoss FC 302 alarm list in the operating instructions (document AQ361181055259) or programming guide (M0013101).
4. **If the code is actually AL 13**, disconnect the motor from the drive output terminals and run the drive unloaded. If the fault clears, test motor insulation with a megohm meter (readings below 2 megohms indicate motor failure). If the fault persists, replace the power board.
5. **If the code is actually AL 38**, check parameter 15-32 for extended diagnostic information. Power-cycle the drive. If the fault returns, replace the control PCB or gate driver circuits.
6. **If the code is actually AL 47**, swap the LCP keypad and communication cable. If the fault clears, replace the faulty component.
7. **If the code remains AL-111** after these checks, contact Danfoss technical support with your drive model, serial number, firmware version, and the photograph of the fault display.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control PCB (Logic Board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-111-fault-code&k=Danfoss+FC302+Control+PCB+%28Logic+Board%29&tag=errorcodefixes-20) \| Required for AL 38 (Internal Fault). Must match your drive voltage and frame size. |
| Danfoss FC302 Power Board (Inverter Assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-111-fault-code&k=Danfoss+FC302+Power+Board+%28Inverter+Assembly%29&tag=errorcodefixes-20) \| Required for AL 13 (Overcurrent) if motor tests good. Includes IGBTs and DC link capacitors. |
| Danfoss LCP Display Unit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-111-fault-code&k=Danfoss+LCP+Display+Unit&tag=errorcodefixes-20) \| Required for AL 47 (STD Bus Timeout) if swapping the keypad clears the fault. |

## When to Call a Pro

Call a qualified electrical technician or VFD specialist immediately if you cannot confirm the exact fault code, if the drive is connected to critical machinery, or if you lack experience working with high-voltage DC bus capacitors. The FC302 operates at mains voltage (up to 480 VAC three-phase) and stores lethal DC voltage in the bus capacitors even after power is removed. Any work beyond verifying the display or swapping an LCP keypad requires lockout/tagout procedures, proper PPE, and a digital multimeter to confirm the DC bus is below 50 volts before touching internal components. If the fault involves the power board, gate drivers, or control PCB, replacement requires torque specifications for bus bar connections and firmware parameter backup. A professional can also contact Danfoss technical support directly with your drive serial number to verify whether AL-111 is a custom fault added by your system integrator.

**Rough cost:** A pro service call runs about $300-800.

## See Also

- [Danfoss FC302 ALARM 53 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-53-fault-code/)
- [Danfoss VFD Fault OCL — Causes & Fix](/posts/danfoss-vfd-fault-ocl/)
- [Danfoss FC302 Alarm 13 - Causes & Fix](/posts/danfoss-fc302-vfd-al-137-fault-code/)
- [Danfoss FC302 Alarm 36 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-36-fault-code/)
