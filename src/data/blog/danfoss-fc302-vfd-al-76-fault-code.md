---
title: "Danfoss FC302 AL-76 Fault - Causes & Fix"
description: "AL-76 (Alarm 38 sub-code 76) means start current detected during start delay. Most often a motor short, ground fault, or cable breakdown."
pubDatetime: 2026-06-22T10:28:01Z
modDatetime: 2026-06-22T10:28:01Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 rectifier board"
most_likely_cause: "Motor short or ground fault"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive and clear the fault; if it recurs immediately the issue is hardware-related"
  - "Disconnect the motor from the drive output; power on the drive; if the fault clears the motor or cable is faulty"
---

## Danfoss FC302 AL-76 Fault — What It Means

Alarm 38 with sub-code 76 on the Danfoss FC302 VFD means "start current in the start delay time." The drive monitors output current during the programmed start delay (parameter group 3-**) and triggers this fault if current flows before the motor is allowed to accelerate. This indicates the motor is drawing current prematurely, which can damage the drive or signal a wiring or control problem.

The fault appears on the display as Alarm 38 with a secondary numeric code (76), not as a standalone "AL 76." It is an internal fault that prevents the drive from starting and points to either a motor or power-section defect that creates unexpected current at zero speed.

## Before You Replace Anything

Technicians sometimes replace the entire VFD before checking the motor and cable. Disconnect the motor and measure insulation resistance with a megohmmeter; if resistance to ground is below 1 MΩ, the motor or cable is faulty, not the drive.

[Jump to Fix](#fix)

## Common Causes

- **Motor short or ground fault (~40%)** A shorted winding or ground fault causes current to flow immediately when power is applied, even during the start delay.
- **Damaged motor cable (~25%)** Cable insulation breakdown or phase-to-phase short creates instantaneous current before the drive begins acceleration.
- **Faulty rectifier or IGBT module (~20%)** Internal power board short (such as a failed IGBT) creates current on the output even at zero speed.
- **Incorrect motor data (~10%)** Wrong nominal current or mismatched motor parameters cause the drive to falsely detect excess start current.
- **Option card mismatch or control wiring error (~5%)** Incompatible brake or serial card can trigger internal logic faults, and digital input configured as external interlock can cause unusual start behavior.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear when you disconnect the motor from the drive output and power on the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or motor cable is faulty; measure insulation resistance to ground and phase-to-phase resistance with a megohmmeter.<br><strong>No:</strong> The drive's internal power section (rectifier or inverter module) is likely shorted; check for blown input fuses or replace the power board.</div>
</details>

<details class="dtree"><summary>With a megohmmeter, is motor insulation resistance to ground above 1 MΩ and phase-to-phase resistance balanced (typically 0.1 to 5 Ω)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor is healthy; check the motor cable for shorts or ground faults, and verify motor parameters in the drive match the nameplate.<br><strong>No:</strong> The motor has a winding short or ground fault; replace the motor or have it rewound by a qualified shop.</div>
</details>

<details class="dtree"><summary>Is the motor nominal current (parameter 1-20) set to match the motor nameplate exactly?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor data is correct; inspect option cards and control wiring for incompatibility or missing 24 VDC supply.<br><strong>No:</strong> Enter the correct nominal current from the motor nameplate; also confirm motor connection type (Y or Δ) in parameter 1-25 matches actual wiring.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power cycle and reset.** Turn off the main power to the drive. Wait 30 seconds, then restore power. Clear the fault from the display. If Alarm 38 sub-code 76 recurs immediately, the problem is hardware-related and you must proceed with isolation and testing.
2. **Disconnect the motor.** Remove the U, V, and W leads from the drive output terminals. Power on the drive. If the fault no longer appears, the motor or motor cable is the culprit. If the fault persists, the drive's internal power board is shorted.
3. **Measure motor insulation.** Use a megohmmeter (500 VDC test voltage) to measure resistance from each phase to ground. You should see greater than 1 MΩ. Any reading below 1 MΩ indicates insulation failure. Also measure phase-to-phase resistance (expect 0.1 to 5 Ω, depending on motor size) and confirm the readings are balanced within a few percent.
4. **Inspect the motor cable.** Check the cable jacket for cuts, abrasion, or moisture entry. Use the megohmmeter to test the cable end-to-end with the motor disconnected. Replace the cable if you find a phase-to-phase short or ground fault.
5. **Verify motor parameters.** Navigate to parameter 1-20 (motor nominal current) and confirm it matches the motor nameplate current exactly. Check parameter 1-25 (motor connection) to make sure the drive is configured for the actual Y or Δ wiring. Incorrect values can cause false current detection.
6. **Check the drive power section.** If the motor and cable test good but the fault remains, inspect the drive for a blown input fuse or failed rectifier. Remove any option cards (brake, serial) and reseat them. If the fault still occurs with the motor disconnected, replace the rectifier board or the entire power/inverter module.
7. **Confirm control wiring.** Verify that 24 VDC is present at terminal 12 and that any digital input configured as "External Interlock" is closed. Open interlock circuits can cause unusual start behavior and trigger internal faults. Consult the FC302 manual for your specific control-wiring diagram.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 rectifier board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-76-fault-code&k=Danfoss+FC302+rectifier+board&tag=errorcodefixes-20) \| Match the frame size and voltage rating to your drive model; consult the drive's type code label. |
| Danfoss FC302 IGBT inverter module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-76-fault-code&k=Danfoss+FC302+IGBT+inverter+module&tag=errorcodefixes-20) \| Required if the power section is shorted; specify the correct power rating and frame size. |
| Three-phase motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-76-fault-code&k=Three-phase+motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Use cable rated for variable-frequency drive duty; length and gauge must match your installation. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if you are not comfortable working with three-phase power or performing high-voltage insulation tests. Replacing the drive's internal rectifier or IGBT module requires knowledge of DC bus discharge procedures and proper torque specs for power terminals. If the motor tests show a winding fault, a motor shop can rewind or replace the motor. Any work on the VFD power section should be done by someone trained in variable-frequency drive service to avoid electric shock or further damage to the drive.

**Rough cost:** A pro service call runs about $300-800 for motor cable replacement or power board repair; motor replacement $500-3,000 depending on size.

## See Also

- [Danfoss FC302 Alarm 26 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-26-fault-code/)
- [Danfoss FC302 AL-158 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-158-fault-code/)
- [Danfoss FC302 AL-65 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-65-fault-code/)
- [Danfoss FC302 AL-62 - Causes & Fix](/posts/danfoss-fc302-vfd-al-62-fault-code/)
