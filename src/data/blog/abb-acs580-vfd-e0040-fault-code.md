---
title: "ABB ACS580 VFD E0040 Fault - Causes & Fix"
description: "E0040 signals an undervoltage fault on the ACS580 drive. Most often caused by supply voltage dip or loose input connections."
pubDatetime: 2026-07-19T07:28:29Z
modDatetime: 2026-07-19T07:28:29Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 DC bus capacitor module"
most_likely_cause: "Low incoming supply voltage or momentary voltage dip"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify that all input power terminal connections are tight and free of corrosion"
  - "Check for tripped breakers or blown fuses upstream in the supply circuit"
  - "Reset the fault from the keypad and observe whether it recurs immediately or only under load"
---

## ABB ACS580 VFD E0040 Fault — What It Means

The E0040 fault code on an ABB ACS580 variable frequency drive indicates an undervoltage condition on the DC bus. The drive has detected that incoming supply voltage has dropped below the minimum threshold required for safe operation, so it trips to protect both the drive and the connected motor.

This fault can be triggered by problems in the utility supply, wiring issues between the supply and the drive, or internal drive components that monitor or convert the incoming AC voltage. The drive will not restart until the fault is cleared and the underlying cause is corrected.

## Before You Replace Anything

Technicians sometimes replace the main control board or DC bus capacitors without first measuring actual line voltage at the input terminals and checking all input connections for tightness and corrosion.

[Jump to Fix](#fix)

## Common Causes

- **Low or unstable supply voltage (~40%)** Utility voltage sags, brownouts, or an undersized transformer can cause the DC bus voltage to fall below the trip threshold.
- **Loose or corroded input power connections (~25%)** Poor contact at the L1, L2, L3 terminals or upstream connections creates voltage drop under load.
- **Faulty DC bus voltage sensing circuit (~15%)** A failing voltage monitor on the control board may falsely report undervoltage even when supply is correct.
- **Aging DC bus capacitors (~10%)** Capacitors with reduced capacitance may not hold the DC bus voltage steady during load transients.
- **Incorrect drive parameter settings (~7%)** Undervoltage trip level set too high or motor acceleration too aggressive can trigger the fault during startup.
- **Blown input line fuse or defective input reactor (~3%)** A fuse with high resistance or a damaged input choke can limit current and cause voltage sag.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault occur immediately at power-up, before the motor even starts?</summary>
<div class="dtree-body"><strong>Yes:</strong> The supply voltage or input wiring is likely at fault. Measure line voltage at the drive input terminals with a multimeter.<br><strong>No:</strong> The fault may be load-related. Check for mechanical binding on the motor or incorrect acceleration ramp settings in the drive parameters.</div>
</details>

<details class="dtree"><summary>Is the measured line voltage at the drive input terminals within the nameplate range for your model?</summary>
<div class="dtree-body"><strong>Yes:</strong> The supply is good. Inspect input terminal tightness, then test DC bus voltage sensing or consider internal drive components.<br><strong>No:</strong> Correct the supply voltage issue first. Check for voltage drop in upstream wiring, undersized breakers, or utility service problems.</div>
</details>

<details class="dtree"><summary>Does the fault clear and not return after a simple reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The trip was likely a momentary voltage dip. Monitor the supply for recurring sags and consider adding a line reactor or adjusting trip thresholds if allowed.<br><strong>No:</strong> The fault is persistent. Perform a thorough inspection of all power connections and measure DC bus voltage if accessible to isolate the fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect and lock out power** to the drive at the supply breaker before performing any inspection or testing.
2. **Measure the incoming line voltage** at the L1, L2, and L3 input terminals using a true-RMS multimeter and compare to the drive nameplate voltage range.
3. **Inspect all input power connections** for tightness, corrosion, or signs of overheating, and re-torque terminals to the value specified in the installation manual.
4. **Check upstream circuit protection** including breakers, fuses, and any input line reactors or EMC filters for damage or high resistance.
5. **Review the drive parameter settings** using the keypad or PC tool, focusing on the undervoltage trip level and motor acceleration ramp times, and adjust if they are outside recommended values for your application.
6. **Clear the fault** from the keypad and restart the drive under no-load or light-load conditions to see if the fault recurs.
7. **Call a qualified electrician or drive technician** if supply voltage is correct and connections are sound, as internal DC bus capacitors or the control board voltage-sensing circuit may need replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 DC bus capacitor module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0040-fault-code&k=ABB+ACS580+DC+bus+capacitor+module&tag=errorcodefixes-20) \| Consult your exact frame size and model number for the correct capacitor kit. |
| ABB ACS580 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0040-fault-code&k=ABB+ACS580+control+board&tag=errorcodefixes-20) \| Required if voltage sensing circuit is defective; match board part number to your drive. |

## When to Call a Pro

Call a qualified electrician or drive technician if you measure correct supply voltage and all input connections are tight but the fault persists. Diagnosing internal DC bus components, voltage sensing circuits, or rectifier sections requires high-voltage test equipment and knowledge of drive internals. Also call a professional if you are not comfortable working with three-phase power systems or performing live voltage measurements, as line-voltage work presents serious shock and arc-flash hazards.

**Rough cost:** A pro service call runs about $150-400.
