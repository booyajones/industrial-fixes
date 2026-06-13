---
title: "ABB ACS880 Fault Codes - Causes & Fix"
description: "ABB ACS880 fault codes indicate drive problems like overcurrent, overvoltage, or overtemp. Most common: check motor cables and cooling."
pubDatetime: 2026-06-11T09:44:17Z
modDatetime: 2026-06-11T09:44:17Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS880 Control Board"
most_likely_cause: "Motor cable damage or mechanical binding"
likelihood: "the most common cause for overcurrent faults"
diy_or_pro: "pro"
---

## ABB ACS880 Fault Codes — What It Means

The ABB ACS880 drive uses alphanumeric fault codes to diagnose problems. The first digit tells you the category: 2xxx codes are overcurrent or short circuit faults, 3xxx are overvoltage faults, 7xxx are temperature warnings, and F0xxx are internal drive failures. Common examples include 2310 (sustained overcurrent during operation), 2340 (short circuit detected in motor cable or windings), 2330 (ground fault or leakage current), 3210 (DC link overvoltage from fast deceleration or high line voltage), 7120 or 7121 (drive or IGBT overtemperature), F0001 (internal control board or firmware fault), and F0120 (encoder feedback failure).

Each code points to a specific hardware or configuration problem. Overcurrent faults usually mean mechanical binding, wrong acceleration settings, or cable damage. Overvoltage faults happen when a high-inertia load decelerates too quickly and pumps energy back into the drive. Temperature faults point to cooling system failure or a hot environment. Internal faults often require factory service or board replacement. Always record the exact code and consult your drive's firmware manual for the precise definition, since code meanings can vary slightly between ACS880 models and firmware versions.

## Before You Replace Anything

Technicians often replace the drive itself when the real problem is a shorted motor cable or jammed load. Before replacing the drive, disconnect the motor cable and measure insulation resistance to ground and between phases with a megohmmeter.

[Jump to Fix](#fix)

## Common Causes

- **Damaged motor cable (~30%)** Physical damage to the output cable insulation causes phase-to-phase or phase-to-ground shorts that trigger 2330 or 2340 faults.
- **Mechanical binding or jam (~25%)** A seized bearing, misaligned coupling, or jammed load forces the motor to draw excessive current and trip 2310 overcurrent faults.
- **Cooling system failure (~20%)** Clogged air filters, bent fan blades, or a failed drive cooling fan cause the heatsink or IGBT temperature to exceed limits and trigger 7120 or 7121 faults.
- **Deceleration time too short (~15%)** When a high-inertia load decelerates faster than the drive can dissipate energy, the DC link voltage spikes and triggers 3210 overvoltage faults.
- **Motor startup data mismatch (~10%)** If parameter 99 motor data does not match the actual motor nameplate, the drive calculates wrong current limits and trips on 2310.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drive trip immediately on power-up before the motor runs?</summary>
<div class="dtree-body"><strong>Yes:</strong> Likely a shorted motor cable, motor winding failure, or internal IGBT damage. Disconnect the motor cable and run a megohmmeter test on the cable and motor.<br><strong>No:</strong> The fault occurs during operation, so check for mechanical binding, wrong acceleration settings, or cooling blockage.</div>
</details>

<details class="dtree"><summary>Can you spin the motor shaft freely by hand with power off?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical binding is not the issue. Check motor cable insulation, parameter settings (acceleration time and motor data), and drive cooling airflow.<br><strong>No:</strong> The load is jammed or a bearing has seized. Fix the mechanical problem before restarting the drive.</div>
</details>

<details class="dtree"><summary>Are the drive's cooling fans running and filters clean?</summary>
<div class="dtree-body"><strong>Yes:</strong> Cooling is working. Focus on electrical causes like cable faults, parameter mismatches, or overvoltage from fast deceleration.<br><strong>No:</strong> Clean or replace air filters and verify fan operation. Overtemperature faults will persist until cooling is restored.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the exact fault code** from the drive display or keypad and write down the code number (e.g., 2310, 3210, 7120) before resetting the fault.
2. **Consult the drive firmware manual** to confirm the exact meaning of the code for your ACS880 model, since definitions can vary by firmware version.
3. **Power down and lockout** the drive, then disconnect the motor cable from the drive output terminals U, V, and W.
4. **Megohmmeter test the motor cable and motor** by measuring insulation resistance from each phase to ground and between phases (should be greater than 1 megohm for a healthy cable).
5. **Inspect motor and load mechanically** by rotating the motor shaft by hand to check for binding, seized bearings, or misaligned couplings.
6. **Check drive cooling system** by verifying that all cooling fans are spinning freely, air filters are clean, and there is no dust buildup on heatsinks.
7. **Review drive parameters** in group 46 (acceleration and deceleration times) and group 99 (motor startup data) to confirm they match your motor nameplate and load inertia, then consult your model's parameter table for recommended settings.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS880 Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-880-fault-codes&k=ABB+ACS880+Control+Board&tag=errorcodefixes-20) \| For F0001 internal faults; confirm part number from your drive nameplate before ordering. |
| Drive Cooling Fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-880-fault-codes&k=Drive+Cooling+Fan&tag=errorcodefixes-20) \| Match voltage and CFM rating to your ACS880 frame size. |
| Motor Output Cable (Shielded VFD-Rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-880-fault-codes&k=Motor+Output+Cable+%28Shielded+VFD-Rated%29&tag=errorcodefixes-20) \| Use cable rated for variable frequency drive service with proper gauge for motor current. |

## When to Call a Pro

Call a qualified drive technician or ABB-certified service provider for any fault that persists after you have verified cable integrity, mechanical freedom, and cooling airflow. Internal faults (F0xxx codes) almost always require board-level diagnostics or factory repair. Overvoltage faults that recur after adjusting deceleration time may need a braking resistor installation, which must be sized and wired by a professional. If you are not trained to work with high-voltage DC link circuits (up to 800 VDC on larger models) or lack a megohmmeter and insulation testing experience, do not attempt repairs beyond inspecting filters and fans. Drive repairs involve lethal voltages and require specific safety procedures and test equipment.

**Rough cost:** A pro service call runs about $300-1200 depending on fault and parts.

## See Also

- [ABB Inverter Fault Code F0001 - Causes & Fix](/posts/abb-inverter-fault-code-f0001/)
- [ABB VFD Fault 9300 — Causes & Fix](/posts/abb-vfd-fault-9300/)
- [ABB ACS580 FF63 - STO Diagnostics Failure Fix](/posts/abb-acs580-ff63-fault-code/)
- [ABB ACS580 A7CE Fault Code - Causes & Fix](/posts/abb-acs580-a7ce-fault-code/)
