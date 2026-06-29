---
title: "Danfoss FC302 AL-124 - Causes & Fix"
description: "AL-124 is not a valid Danfoss FC302 code. Check your display again or consult the manual for the correct alarm number (1–100+)."
pubDatetime: 2026-06-24T10:20:20Z
modDatetime: 2026-06-24T10:20:20Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Brake resistor"
diy_or_pro: "pro"
free_checks:
  - "Verify the exact alarm number on the display and write it down"
  - "Check all input power connections for loose wires or blown fuses"
  - "Disconnect the motor and reset the drive to see if the alarm clears"
---

## Danfoss FC302 AL-124 — What It Means

AL-124 does not exist in the Danfoss FC302 fault code library. Danfoss FC302 drives use alarm numbers 1 through 100+ (for example, Alarm 4 is Mains Phase Loss, Alarm 8 is DC Under Voltage, Alarm 12 is DC Bus Overvoltage). The string "AL-124" may be a misread display, a code from a different Danfoss series (such as FC301), or a custom accessory alarm. Double-check the display and record the exact alarm number shown.

If you are seeing Alarm 12 (DC Bus Overvoltage), the drive's internal DC link voltage has exceeded safe limits (around 410V for 230V models, around 720V for 480V models). Common causes include a jammed motor, incorrect motor current parameter, brake resistor failure, or input voltage problems. If you are seeing Alarm 17 (STD Bus Timeout), communication with the keypad or accessory has been lost, usually due to a faulty cable or dead LCP display.

## Before You Replace Anything

Technicians sometimes replace the entire logic board or inverter module when the real issue is a shorted brake resistor or loose input connection. Measure the brake resistor resistance (typically 10–100Ω) and check all three input phase voltages before ordering expensive boards.

[Jump to Fix](#fix)

## Common Causes

- **Misread or invalid alarm number (~50%)** The display may show a corrupted number, or the code belongs to a different drive series.
- **Motor mechanical overload (if Alarm 12) (~20%)** A jammed shaft, stuck pump, or seized bearing forces the DC bus voltage above safe limits.
- **Brake resistor failure (if Alarm 12) (~15%)** A shorted or open brake resistor cannot dissipate regenerative energy, causing overvoltage.
- **Incorrect motor current parameter (if Alarm 12) (~10%)** Parameter 1-24 set higher than the motor's actual rating forces excess current and voltage spikes.
- **Faulty LCP keypad or cable (if Alarm 17) (~5%)** A dead display or broken serial cable causes the drive to lose communication with the front panel.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show a clear, stable alarm number between 1 and 100?</summary>
<div class="dtree-body"><strong>Yes:</strong> Write down the exact number and look it up in the FC302 manual (the code is valid).<br><strong>No:</strong> The display may be corrupted or the drive is a different model; power-cycle and check the model plate.</div>
</details>

<details class="dtree"><summary>Can you disconnect the motor and run the drive at low speed without the alarm?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or its load is likely jammed or overloaded; inspect the mechanical system.<br><strong>No:</strong> The fault is inside the drive (brake resistor, input power, or board failure).</div>
</details>

<details class="dtree"><summary>Are all three input phase voltages present and within 3% of each other?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input power is good; focus on the motor, brake resistor, and internal parameters.<br><strong>No:</strong> Tighten connections, replace blown fuses, or check upstream switchgear.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive** and lock out the input disconnect to make sure safe troubleshooting.
2. **Record the exact alarm number** from the LCP display and compare it to the fault code table in the FC302 manual.
3. **Check all input power connections** and measure voltage on all three phases; they must be within 3% of nominal.
4. **Disconnect the motor** from the drive and attempt a low-speed test run to isolate mechanical overload.
5. **Measure the brake resistor** (if equipped) with a multimeter; resistance should be 10–100Ω per drive rating.
6. **Verify Parameter 1-24** (Motor Nominal Current) matches the motor nameplate; adjust if set too high.
7. **Call a qualified VFD technician** if the alarm persists after these checks or if internal boards require replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Brake resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-124-fault-code&k=Brake+resistor&tag=errorcodefixes-20) \| Match resistance and wattage rating to your FC302 frame size. |
| LCP keypad display | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-124-fault-code&k=LCP+keypad+display&tag=errorcodefixes-20) \| For Alarm 17 or if the display is corrupted or unresponsive. |

## When to Call a Pro

Call a qualified VFD technician if the alarm number does not appear in the FC302 manual, if you lack a multimeter or safe lockout procedure, or if internal boards or the power module need replacement. High-voltage DC bus capacitors remain charged even after input power is removed, and a shock can be fatal. A technician can also download parameter backups, test the inverter module with specialized equipment, and verify motor winding integrity with a megger.

**Rough cost:** A pro service call runs about $150–400 depending on which alarm is actually present and whether a resistor, board, or motor needs replacement.

## See Also

- [Danfoss FC302 Alarm 51 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-51-fault-code/)
- [Danfoss FC302 Alarm AL 29 — Causes & Fix](/posts/danfoss-fc302-fault-al-29/)
- [Danfoss FC302 ALARM 26 - Causes & Fix](/posts/danfoss-fc302-alarm-26-fault-code/)
- [Danfoss FC302 VFD Alarm 28 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-28-fault-code/)
