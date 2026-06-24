---
title: "ABB ACS580 A4A3 Fault Code - Causes & Fix"
description: "A4A3 does not exist in ABB docs; you likely see A4A0 (control board overheating) or 5681 (power unit communication loss). Check fan/airflow."
pubDatetime: 2026-06-21T10:38:30Z
modDatetime: 2026-06-21T10:38:30Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS580 Cooling Fan Assembly"
most_likely_cause: "Cooling fan failure or blocked airflow"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact fault code and auxiliary code on the keypad (A4A0, 5681, etc.) to confirm which fault is active"
  - "Check that the front cover is installed and tightened (the ACS580 airflow path requires the cover to be in place)"
  - "Inspect the cooling fan and vents for dust or debris and clean with compressed air"
part_price: "$80-150"
no_buy_pct: "60%"
---

## ABB ACS580 A4A3 Fault Code — What It Means

The fault code A4A3 does not appear in official ABB ACS580 documentation. The code you are seeing is most likely A4A0 (Control Board Temperature) or a PU communication error such as 5681. A4A0 means the internal temperature of the control board has exceeded the safe operating limit, triggering a thermal shutdown to prevent permanent damage to the electronics. If your display strictly reads A4A3 and not A4A0, it is possible the drive is reporting a Power Unit communication failure (often code 5681), which shares similar symptoms of the control unit being unable to function due to power or signal issues.

For A4A0, the drive is protecting itself from heat damage caused by inadequate cooling. For PU communication faults, the 24V supply to the control board or the connection between the control unit and power unit has failed. Either fault will prevent normal operation until the underlying issue is resolved.

## Before You Replace Anything

Technicians often replace the entire control board when the real problem is a failed cooling fan or a clogged vent. Check the fan operation and clean all vents before ordering a new board.

[Jump to Fix](#fix)

## Common Causes

- **Cooling fan failure (~40%)** The control board cooling fan is not spinning, has a broken connection, or is clogged with dust, preventing heat removal from the electronics.
- **Blocked airflow (~30%)** The drive is installed in a confined space, the front cover is missing or loose, or ventilation vents are obstructed, restricting the designed airflow path.
- **24V supply failure (~15%)** The internal 24V supply of the power unit is not functioning, or the external 24V supply (if parameter 95.04 is set to 1) is dead, causing a PU communication fault.
- **High ambient temperature (~10%)** The surrounding environment is too hot (consult your model's temperature table) without external cooling, causing the control board to overheat.
- **Connection fault between CU and PU (~5%)** The cable connecting the Control Unit to the Power Unit is loose or damaged, preventing communication and triggering a fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the cooling fan spin when the drive is powered on?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan is working. Check for blocked vents or high ambient temperature and clean all airflow paths.<br><strong>No:</strong> The fan is failed or disconnected. Inspect the fan connection at the control board and replace the fan if needed.</div>
</details>

<details class="dtree"><summary>Is the front cover installed and tightened?</summary>
<div class="dtree-body"><strong>Yes:</strong> The airflow path is correct. Check the fan and internal 24V supply if the fault persists.<br><strong>No:</strong> Install and tighten the front cover. The ACS580 requires the cover for proper airflow and will overheat without it.</div>
</details>

<details class="dtree"><summary>Does the fault code read exactly A4A0 or something else like 5681?</summary>
<div class="dtree-body"><strong>Yes:</strong> A4A0 is a temperature fault. Focus on cooling (fan, vents, ambient temperature).<br><strong>No:</strong> If the code is 5681 or another communication fault, check parameter 95.04 and the 24V supply to the control board.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the fault code** on the keypad and note any auxiliary code (e.g., A4A0-1 or A4A0-2) which specifies which fan or sensor triggered the fault.
2. **Power down the drive** and wait for all capacitors to discharge (consult the drive manual for safe lock-out procedures) before opening the enclosure.
3. **Inspect the cooling fan** by removing the front cover and checking that the fan spins freely by hand and is free of dust or debris.
4. **Clean all vents and the fan** using compressed air, blowing away any accumulated dust or obstructions in the airflow path.
5. **Check the fan connection** at the control board terminal and measure voltage at the fan terminals if the fan is not running when the drive is powered on.
6. **Verify parameter 95.04** (Control Board Supply) matches the physical setup (0 for internal 24V, 1 for external 24V) and measure 24V DC at the CU-PU connection points if a communication fault is present.
7. **Replace the fan assembly** if the fan is faulty or does not spin, and reboot the control unit using the drive parameters after repairs are complete.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 Cooling Fan Assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a4a3-fault-code&k=ABB+ACS580+Cooling+Fan+Assembly&tag=errorcodefixes-20) \| Match the fan part number to your specific drive frame size and voltage rating |
| ABB ACS580 Control Board (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a4a3-fault-code&k=ABB+ACS580+Control+Board+%28CU%29&tag=errorcodefixes-20) \| Only needed if the board itself is damaged or the 24V supply has failed internally |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in safe lock-out/tag-out procedures for high-voltage equipment. Even after power-down, the ACS580 retains dangerous DC bus voltages in its capacitors. A professional can safely diagnose whether the fault is a simple fan replacement, a control board failure, or a power unit issue requiring replacement of major components. If the fault persists after cleaning and fan replacement, or if you measure no 24V supply at the control board, the drive may need factory-level service or board replacement that requires programming and commissioning.

**Rough cost:** A pro service call runs about $150-400.

## See Also

- [ABB ACH580 HVAC VFD Fault Codes — Full Diagnostic Guide - What It Means and How to Fix It](/posts/abb-ach580-fault-codes/)
- [ABB VFD Fault 3210 — Causes & Fix](/posts/abb-vfd-fault-3210/)
- [ABB ACS580 A7A3 Fault - Causes & Fix](/posts/abb-acs580-vfd-a7a3-fault-code/)
- [ABB ACS580 A2B4 Fault Code - Causes & Fix](/posts/abb-acs580-a2b4-fault-code/)
