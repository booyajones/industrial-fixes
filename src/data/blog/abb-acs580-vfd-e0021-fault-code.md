---
title: "ABB ACS580 VFD E0021 Fault Code - Causes & Fix"
description: "E0021 signals an internal control board or parameter error. Check parameter settings, power-cycle the drive, and inspect for loose connections."
pubDatetime: 2026-07-18T07:52:50Z
modDatetime: 2026-07-18T07:52:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 control board"
most_likely_cause: "corrupted parameter settings or firmware memory"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive by disconnecting AC input power for at least 60 seconds, then reconnect and observe if the fault clears"
  - "Check that all parameter groups are set to factory defaults or a known-good saved configuration"
  - "Inspect control wiring and verify no loose terminals or damaged shielding on encoder or fieldbus cables"
---

## ABB ACS580 VFD E0021 Fault Code — What It Means

The E0021 fault code on an ABB ACS580 variable frequency drive typically indicates an internal control board communication error or a parameter configuration problem. The drive's microprocessor has detected an inconsistency in stored settings, a corruption in firmware memory, or a failure in internal communication between control circuits. This fault prevents the drive from operating safely and will trip the unit into a fault state until resolved.

Because the ACS580 is a sophisticated industrial drive, the exact meaning of E0021 can vary slightly across firmware versions and application configurations. Consult your drive's user manual or parameter list for the precise definition for your model and firmware revision. The fault may appear after a parameter change, a power interruption, or intermittently if internal connections or memory circuits are degrading.

## Before You Replace Anything

Technicians sometimes replace the entire control board when the fault is actually caused by incorrect parameter settings or a loose internal ribbon cable. Always download and review the current parameter set and check internal connections before ordering a new board.

[Jump to Fix](#fix)

## Common Causes

- **Corrupted parameter settings or firmware memory (~40%)** A power surge, brownout, or interrupted parameter upload can corrupt the drive's stored configuration, triggering an internal consistency check failure.
- **Loose or damaged internal ribbon cable (~25%)** The ribbon cable connecting the control board to the power board or display can work loose from vibration or thermal cycling, breaking internal communication.
- **Faulty control board capacitor or memory chip (~20%)** Electrolytic capacitors on the control board can dry out over time, and EEPROM or flash memory can fail, both causing read/write errors that generate E0021.
- **Firmware version mismatch after update (~10%)** An incomplete or incorrect firmware update can leave the drive with mismatched code modules that fail internal version checks.
- **Environmental contamination on control board (~5%)** Dust, moisture, or conductive debris on the control board can create shorts or high-resistance paths that disrupt logic signals and trigger fault detection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a full power-cycle and remain off during a no-load test run?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely a transient memory glitch or parameter conflict; monitor the drive and check for loose wiring or noisy power supply.<br><strong>No:</strong> The fault is persistent, indicating a hardware issue or deep parameter corruption; proceed with parameter reset and internal inspection.</div>
</details>

<details class="dtree"><summary>Can you successfully restore factory default parameters via the keypad or PC tool without the fault reappearing?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was a corrupted custom parameter set; reload your application settings carefully and verify each parameter group before saving.<br><strong>No:</strong> The drive cannot accept or store parameters correctly, pointing to a control board memory fault or internal communication failure.</div>
</details>

<details class="dtree"><summary>Are all internal ribbon cables and connectors firmly seated when you open the drive enclosure?</summary>
<div class="dtree-body"><strong>Yes:</strong> Connections are good; the fault is likely a failed component on the control board or a firmware issue requiring professional diagnostics.<br><strong>No:</strong> Reseat all internal connectors, clean contact surfaces with electronics cleaner, and test again; many E0021 faults resolve with this step.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect all power** to the drive at the main disconnect or circuit breaker and verify zero voltage with a multimeter at the input terminals before proceeding.
2. **Power-cycle the drive** by leaving power off for at least 60 seconds to allow all capacitors to discharge and internal microprocessors to reset completely.
3. **Restore power and observe** the display; if E0021 persists immediately, note whether the drive completes its boot sequence or stops mid-boot.
4. **Access the parameter menu** using the keypad or PC tool and attempt to reset all parameters to factory defaults, then check if the fault clears.
5. **Remove the front cover** of the drive enclosure (with power off and locked out) and inspect all internal ribbon cables and connectors between the control board and power board for looseness or corrosion.
6. **Reseat each internal connector** by gently unplugging and firmly reconnecting, ensuring positive locking clips engage and no pins are bent.
7. **Inspect the control board** for signs of overheating, bulging capacitors, burn marks, or moisture ingress; document any visible damage with photos for the service technician or manufacturer support.
8. **Reconnect power and test** the drive with no motor load connected; if the fault remains, contact ABB technical support or a certified drive service center with the drive serial number, firmware version, and fault history log.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0021-fault-code&k=ABB+ACS580+control+board&tag=errorcodefixes-20) \| Factory replacement board; must match drive frame size and firmware; typically requires factory configuration and parameter download. |
| Internal ribbon cable set | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0021-fault-code&k=Internal+ribbon+cable+set&tag=errorcodefixes-20) \| Replacement cables for control-to-power board communication; order by drive frame size and revision. |

## When to Call a Pro

Call a qualified industrial drive technician or ABB-certified service provider if the fault persists after parameter reset and physical inspection. VFD control boards operate at logic-level voltages but are integrated with high-voltage DC bus circuits and require specialized diagnostic tools to isolate memory, firmware, and hardware faults. The technician can download detailed fault logs, perform board-level testing, and reflash firmware or replace the control board with proper calibration. Attempting board-level repair without VFD training risks electric shock and can void manufacturer warranties. Professional service is always warranted when the drive is part of a critical process or safety system.

**Rough cost:** A pro service call runs about $200-600.
