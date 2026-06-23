---
title: "Yaskawa GA800 A.122 Alarm - Causes & Fix"
description: "A.122 is an input/reference configuration alarm on the GA800 VFD. Most common fix: verify speed-reference wiring and analog input settings."
pubDatetime: 2026-06-08T11:20:48Z
modDatetime: 2026-06-08T11:20:48Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
most_likely_cause: "Incorrect wiring or missing connection of the speed-reference signal to the analog input terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Yaskawa GA800 control board"
---

## Yaskawa GA800 A.122 Alarm — What It Means

A.122 is an alarm code, not a power-stage fault, indicating the GA800 drive is not receiving or recognizing the expected speed-reference signal. The drive expects a valid analog input (voltage or current) at the configured terminals, and when wiring is incorrect, terminals are miswired, or DIP switch settings do not match the input type, the alarm appears. Yaskawa's troubleshooting workflow requires you to remove the root cause before resetting the alarm.

This alarm does not point to a failed power component. Instead it signals a mismatch between what the drive is configured to read (via its internal DIP switches and terminal assignments) and what is actually wired to the analog input terminals A1, A2, A3, and AC common. Fixing A.122 usually means correcting wiring, confirming the reference signal type (voltage or current), and matching the DIP switch settings to that type.

## Before You Replace Anything

Technicians sometimes replace the control board before checking wiring and DIP switch settings. Always verify reference signal wiring against the connection diagram and check the analog input selector switches before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect or missing reference wiring (~50%)** The speed-reference signal is not connected to the correct terminal (A1 for voltage, A2 for current) or the AC common is loose or missing.
- **DIP switch input-type mismatch (~30%)** The analog input selector DIP switches (S12 for A2, S13 for A3) are set for voltage when the wiring provides current, or vice versa.
- **No commanded speed reference (~10%)** The drive is in run mode but no external signal is present because the controller or PLC output is disabled or failed.
- **Open circuit in reference wiring harness (~5%)** A broken wire or loose terminal screw interrupts the signal path between the controller and the drive's analog input.
- **Control board analog input circuit fault (~5%)** The board's input circuit has failed and cannot read a valid signal even when wiring and settings are correct.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the drive displaying A.122 while a run command is active and the controller is outputting a reference signal?</summary>
<div class="dtree-body"><strong>Yes:</strong> The reference signal is being sent but the drive is not recognizing it. Check wiring to A1/A2/A3 and AC common, then verify DIP switch settings match your input type.<br><strong>No:</strong> Confirm the controller or PLC is actually sending a speed reference and that the run command is active. If no reference is present, troubleshoot the upstream control system first.</div>
</details>

<details class="dtree"><summary>Does the wiring diagram show voltage reference connected to A1 and common to AC?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify DIP switch S13 is set for voltage input on A1. If the switch is correct, measure the signal voltage at the terminals to confirm it is present.<br><strong>No:</strong> Check whether the reference is current (A2) or voltage (A3) and confirm the corresponding DIP switch (S12 for A2, S13 for A3) matches that type.</div>
</details>

<details class="dtree"><summary>After correcting wiring and DIP switches, does the alarm clear when you press RESET on the keypad?</summary>
<div class="dtree-body"><strong>Yes:</strong> The configuration mismatch is resolved. Monitor the drive during normal operation to confirm stable reference signal.<br><strong>No:</strong> The control board analog input circuit may be damaged. Contact Yaskawa technical support with the drive model and spec number for further diagnostics.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lock out** the drive per NFPA 70E and your facility's safety procedures before inspecting wiring.
2. **Locate the connection diagram** in the GA800 manual or on the inside of the drive cover, and identify which terminal (A1, A2, or A3) is used for the speed reference and whether it is voltage or current.
3. **Inspect the analog input wiring** at terminals A1, A2, A3, and AC common. Confirm the signal wire and common are tight and that the signal type (voltage or current) matches the terminal assignment in the diagram.
4. **Check the DIP switch settings** for the analog input. Switch S12 defines the input type for A2 (current or voltage), and S13 defines the type for A3. Set each switch to match the wiring.
5. **Verify the reference signal** is present by measuring voltage (0–10 V typical) at A1 and AC, or current (4–20 mA typical) at A2 and AC, using a multimeter while the controller is commanding a reference.
6. **Correct any miswiring or open connections**, then restore power and press RESET on the keypad while the A.122 alarm is displayed to clear it.
7. **Test the drive** by commanding a low-speed reference and confirming the motor runs without the alarm returning. If A.122 reappears, document the wiring configuration and contact Yaskawa technical support for control board diagnostics.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-122-fault-code&k=Yaskawa+GA800+control+board&tag=errorcodefixes-20) \| Required only if the analog input circuit is confirmed failed after wiring and settings are verified correct. Contact Yaskawa with your drive's model and spec number to order the correct replacement board. |
| Shielded analog signal cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-122-fault-code&k=Shielded+analog+signal+cable&tag=errorcodefixes-20) \| Use if the existing reference wiring is damaged or does not meet the drive's noise-immunity requirements. Consult the GA800 manual for recommended cable type and grounding practice. |

## When to Call a Pro

Call a qualified electrician or VFD technician if you are not trained in industrial control wiring or if your facility requires certified personnel for work on drives above 600 V or inside locked electrical rooms. A.122 involves verifying wiring against the connection diagram, measuring low-voltage analog signals, and adjusting DIP switches, all of which require familiarity with control schematics and safe work on energized equipment. If wiring and settings are correct but the alarm persists, the control board's analog input circuit may have failed, and Yaskawa technical support should be contacted before ordering parts. Do not replace the control board without first documenting the wiring, DIP switch positions, and measured signal levels, because the same alarm will return if the root cause is a configuration mismatch rather than a hardware fault.

**Rough cost:** A pro service call runs about $150–400 for service call and wiring correction, depending on labor and whether rewiring is required.

## See Also

- [Yaskawa A1000 PF Fault - Causes & Fix](/posts/yaskawa-a1000-vfd-pf-fault-code/)
- [Yaskawa A1000 CPF00 - Causes & Fix](/posts/yaskawa-a1000-vfd-cpf00-fault-code/)
- [Yaskawa GA800 E73 Fault - Causes & Fix](/posts/yaskawa-ga800-vfd-e73-fault-code/)
- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
