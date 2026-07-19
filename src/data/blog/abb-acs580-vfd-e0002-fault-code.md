---
title: "ABB ACS580 VFD E0002 Fault Code - Causes & Fix"
description: "E0002 on an ABB ACS580 VFD signals an overcurrent fault. Most often caused by a short in the motor or cable; inspect wiring first."
pubDatetime: 2026-07-17T07:41:04Z
modDatetime: 2026-07-17T07:41:04Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "Motor cable (shielded VFD-rated)"
most_likely_cause: "Short circuit or ground fault in motor winding or output cable"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Disconnect the motor cable from the drive output terminals and clear the fault to see if the drive will run unloaded"
  - "Inspect motor cable for visible damage, pinch points, or moisture intrusion"
  - "Check that motor nameplate current rating matches the drive output current rating and parameter settings"
---

## ABB ACS580 VFD E0002 Fault Code — What It Means

The E0002 fault code on an ABB ACS580 variable frequency drive indicates an overcurrent condition has been detected. This means the drive has measured current flow exceeding its safe operating threshold, either in the output circuit to the motor or internally. The drive trips to protect itself and the connected motor from damage.

Overcurrent faults can occur during acceleration, steady-state operation, or deceleration. The exact threshold and behavior depend on your drive model and parameter settings. Consult your model's manual for the specific current limits and fault-response settings. The fault usually points to an issue in the motor, motor cable, or drive output stage rather than the control circuitry.

## Before You Replace Anything

Technicians sometimes replace the drive itself without first isolating the motor and testing the cable. A simple insulation-resistance (megger) test on the motor windings and cable can reveal a short or ground fault and save the cost of a new drive.

[Jump to Fix](#fix)

## Common Causes

- **Shorted or grounded motor winding (~35%)** Insulation breakdown in the motor stator creates a direct path to ground or between phases, drawing excessive current.
- **Damaged motor cable (~25%)** Cable insulation failure from abrasion, moisture, or rodent damage causes phase-to-phase or phase-to-ground shorts.
- **Mechanical overload or locked rotor (~20%)** A jammed load or seized bearing forces the motor to draw high current trying to turn the shaft.
- **Incorrect drive parameter settings (~10%)** Acceleration time set too short, current limit set too low, or motor parameters mismatched to the actual motor can trigger nuisance trips.
- **Failed output stage (IGBT module) in the drive (~7%)** A shorted transistor in the drive's inverter section causes uncontrolled current flow and immediate fault.
- **Loose or corroded output connections (~3%)** High resistance at terminals creates arcing and current spikes that the drive interprets as overcurrent.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear and stay clear when the motor cable is disconnected from the drive output terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is in the motor or motor cable. Perform an insulation-resistance test on both the motor windings and the cable to locate the short or ground fault.<br><strong>No:</strong> The drive output stage may be damaged. Call a qualified VFD technician to test the IGBT module and internal components.</div>
</details>

<details class="dtree"><summary>Can you rotate the motor shaft freely by hand with power off and the load disconnected?</summary>
<div class="dtree-body"><strong>Yes:</strong> Mechanical jam is not the issue. Focus on electrical insulation tests of the motor and cable.<br><strong>No:</strong> A seized bearing or jammed load is forcing the motor to draw high current. Repair or replace the motor bearings and clear any obstruction in the driven equipment.</div>
</details>

<details class="dtree"><summary>Have the drive parameters (acceleration time, motor nameplate data, current limit) been verified against the actual motor and load?</summary>
<div class="dtree-body"><strong>Yes:</strong> Parameter mismatch is unlikely. Proceed with insulation and component testing.<br><strong>No:</strong> Re-enter the correct motor nameplate values and increase acceleration time. Reset the fault and test at no load before reconnecting the full load.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Lock out and tag out** all power sources to the drive and motor following your facility's electrical safety procedures.
2. **Record the fault history** from the drive display or keypad to note when and how often the E0002 fault occurs.
3. **Disconnect the motor cable** from the drive output terminals (U, V, W) and remove any load from the motor shaft if accessible.
4. **Measure insulation resistance** on the motor windings using a 500 V or 1000 V megohmmeter; reading below 1 megohm to ground or between phases indicates insulation failure.
5. **Test the motor cable** separately with the megohmmeter; check each conductor to ground and phase-to-phase for shorts or low resistance.
6. **Inspect all output connections** at the drive and motor terminal box for loose hardware, corrosion, or burn marks; clean and retorque terminals to the manufacturer's specification.
7. **Review and correct drive parameters** including motor nominal current, voltage, frequency, acceleration time, and deceleration time to match the motor nameplate and application requirements; consult your model's parameter manual.
8. **Restore power and test** the drive at no load (motor disconnected) to confirm the fault does not recur; if clear, reconnect the motor and cable and run at reduced speed before full-load testing.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Motor cable (shielded VFD-rated) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0002-fault-code&k=Motor+cable+%28shielded+VFD-rated%29&tag=errorcodefixes-20) \| Use cable rated for VFD duty with proper shielding and sized per NEC and drive manual |
| Three-phase AC motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0002-fault-code&k=Three-phase+AC+motor&tag=errorcodefixes-20) \| Must match drive output voltage, current, and frequency ratings; verify nameplate before ordering |

## When to Call a Pro

Call a qualified electrician or VFD technician if you lack the tools or training to perform live voltage measurements, insulation-resistance testing, or drive parameter programming. High-voltage DC bus capacitors inside the drive remain charged even after input power is removed and pose a lethal shock hazard. If the fault persists after verifying motor and cable integrity, the drive's internal IGBT output stage may have failed and requires component-level diagnosis and repair or drive replacement. Professional service is also warranted if the application involves process-critical equipment, explosive atmospheres, or machinery that requires a risk assessment before troubleshooting.

**Rough cost:** A pro service call runs about $200-800.

## See Also

- [ABB ACS880 Fault 2310 - Overcurrent Diagnosis and Fix](/posts/abb-acs880-fault-2310/)
- [ABB ACS580 Fault 2330 Earth Leakage, Causes & Fix](/posts/abb-acs580-fault-2330/)
- [ABB VFD Fault 4110 — Causes & Fix](/posts/abb-vfd-fault-4110/)
- [ABB VFD Fault 2310 — Causes & Fix](/posts/abb-vfd-fault-2310/)
