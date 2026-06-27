---
title: "Danfoss FC302 AL-115 Fault - Causes & Fix"
description: "AL-115 is not a standard Danfoss FC302 code. It likely means Alarm 15 (hardware mismatch) or Alarm 13 (DC bus low voltage). Check cards."
pubDatetime: 2026-06-25T09:15:25Z
modDatetime: 2026-06-25T09:15:25Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 compatible option card"
most_likely_cause: "Incompatible or unseated option card (if Alarm 15), or low input voltage or failed rectifier (if Alarm 13)"
likelihood: "the most common cause for Alarm 15 is an option card issue, and for Alarm 13 is input voltage or rectifier failure"
diy_or_pro: "pro"
free_checks:
  - "Reseat or remove any option cards in the drive slots and power-cycle the drive"
  - "Measure all three input phase voltages at the drive terminals with a multimeter"
  - "Check for blown input fuses or loose input wire connections at the drive terminals"
part_price: "$150-500 for an option card or rectifier/power board assembly"
---

## Danfoss FC302 AL-115 Fault — What It Means

There is no documented AL-115 fault code in the Danfoss FC302 series official alarm list. The code likely refers to Alarm 15, which indicates a hardware mismatch between the drive and an installed option card (brake controller, communication module, or positioning card). Alternatively, it may be a misread of Alarm 13, which means DC bus voltage has dropped below the minimum threshold and the drive has tripped to protect itself.

If the fault is Alarm 15, the drive has detected an incompatible, improperly seated, or unrecognized option card in one of its expansion slots. If it is Alarm 13, the input power supply is either too low, unbalanced, or the internal rectifier and DC link components have failed. Verify the exact alarm number on the drive display before proceeding.

## Before You Replace Anything

Technicians sometimes replace the entire power board when Alarm 13 appears, but the fault is often a blown input fuse or loose input wire. Measure all three input phases with a voltmeter and check fuses before ordering internal boards.

[Jump to Fix](#fix)

## Common Causes

- **Incompatible or unseated option card (Alarm 15) (~30%)** The drive detects an option card that is not recognized, is incompatible with the FC302 model, or is not seated properly in the slot.
- **Low input voltage or phase loss (Alarm 13) (~25%)** One or more input phases are below nominal voltage, imbalanced beyond 3 percent, or missing entirely.
- **Failed rectifier diodes or DC link capacitors (Alarm 13) (~20%)** Internal rectifier diodes have failed open or DC bus capacitors have aged and lost capacitance, preventing the bus from reaching rated voltage.
- **Blown input fuse (Alarm 13) (~15%)** An input fuse has blown due to a previous overcurrent event or component failure, cutting power to one phase of the rectifier.
- **Firmware mismatch between drive and option card (Alarm 15) (~10%)** The option card firmware is older or newer than the drive firmware and the two cannot communicate properly.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is an option card installed in any of the drive expansion slots?</summary>
<div class="dtree-body"><strong>Yes:</strong> Remove or reseat the card and power-cycle the drive. If the alarm clears, the card was incompatible or poorly seated. Replace with a compatible card or update firmware via MCT 10 software.<br><strong>No:</strong> The fault is likely Alarm 13 (DC bus voltage). Measure input voltages at the drive terminals. If all three phases are present and balanced, the rectifier or power board is likely failed.</div>
</details>

<details class="dtree"><summary>Are all three input phase voltages within 3 percent of nominal and balanced?</summary>
<div class="dtree-body"><strong>Yes:</strong> The input power is good. Disconnect the motor and run the drive unloaded. If Alarm 13 persists, the rectifier, inverter, or DC link capacitors inside the drive have failed.<br><strong>No:</strong> The input power is bad. Check for blown fuses, loose wires, or an upstream supply issue. Tighten connections and replace any blown fuses before restarting.</div>
</details>

<details class="dtree"><summary>Does the alarm clear when the drive runs with no motor load?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or driven load is drawing excessive current or causing a voltage sag. Reduce load, check motor winding resistance, or increase drive ramp times.<br><strong>No:</strong> The fault is internal to the drive. Replace the rectifier board or entire power board assembly.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the exact alarm number** on the drive display or via the control panel. Confirm whether it reads Alarm 15, Alarm 13, or another code.
2. **If Alarm 15, remove or reseat any option cards** installed in the drive expansion slots. Power-cycle the drive and check if the alarm clears.
3. **Check option card compatibility** by consulting the Danfoss FC302 option card list in the manual or on the Danfoss website. Replace the card with a compatible model if needed.
4. **If Alarm 13, measure all three input phase voltages** at the drive input terminals using a voltmeter. Verify that all phases are present and within 3 percent of nominal.
5. **Inspect input fuses and wire connections** at the drive terminals. Replace any blown fuses and tighten all input wire connections.
6. **Disconnect the motor and run the drive unloaded** by removing the motor leads from U, V, and W terminals. If Alarm 13 persists, the fault is internal.
7. **Replace the rectifier or power board** if the DC bus voltage remains low with no load and input power is confirmed good. If option card firmware is outdated, update via MCT 10 software and retry.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 compatible option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-115-fault-code&k=Danfoss+FC302+compatible+option+card&tag=errorcodefixes-20) \| Match the card type (brake, communication, or positioning) and verify compatibility with your FC302 model and firmware version. |
| Danfoss FC302 rectifier or power board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-115-fault-code&k=Danfoss+FC302+rectifier+or+power+board+assembly&tag=errorcodefixes-20) \| Required if internal rectifier diodes or DC link capacitors have failed. Consult Danfoss part number lookup by drive model and frame size. |
| Input fuse cartridge | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-115-fault-code&k=Input+fuse+cartridge&tag=errorcodefixes-20) \| Match the fuse amperage and voltage rating stamped on the drive nameplate or shown in the FC302 manual for your frame size. |
| Danfoss FC302 logic or control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-115-fault-code&k=Danfoss+FC302+logic+or+control+PCB&tag=errorcodefixes-20) \| Needed only if the drive mis-flags the option card or if firmware cannot be updated. Rare replacement for Alarm 15. |

## When to Call a Pro

Call a qualified technician or industrial electrician if you are not comfortable working inside the drive enclosure or measuring high-voltage DC bus components. Rectifier and power board replacement requires de-energizing the drive, discharging DC link capacitors, and handling circuit boards with proper ESD precautions. If you do not have MCT 10 software or experience with Danfoss firmware updates, a technician can verify option card compatibility, update firmware, and replace internal boards safely. Also call a pro if input power issues trace back to the facility distribution panel or transformer, as those repairs require a licensed electrician.

**Rough cost:** A pro service call runs about $200-800 depending on whether it is a card replacement, fuse, or power board.

## See Also

- [Danfoss FC302 WARNING 73 - Causes & Fix](/posts/danfoss-fc302-vfd-al-73-fault-code/)
- [Danfoss FC302 VFD AL-153 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-153-fault-code/)
- [Danfoss FC302 VFD Alarm 14 - Causes & Fix](/posts/danfoss-fc302-vfd-al-140-fault-code/)
- [Danfoss FC302 Alarm 32 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-32-fault-code/)
