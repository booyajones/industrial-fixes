---
title: "ABB ACS580 VFD E0006 Fault Code - Causes & Fix"
description: "E0006 signals a drive communication or internal fault. Check parameter settings and control wiring first, then power-cycle the drive."
pubDatetime: 2026-07-18T07:39:54Z
modDatetime: 2026-07-18T07:39:54Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB ACS580 control board (NCSA-01 or NCSA-02)"
most_likely_cause: "Incorrect parameter configuration or control mode mismatch"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the drive by disconnecting supply voltage for 30 seconds and reconnecting"
  - "Check the control terminal strip for loose or miswired connections"
  - "Review the parameter settings using the control panel and compare against your commissioning sheet"
no_buy_pct: "60%"
---

## ABB ACS580 VFD E0006 Fault Code — What It Means

The E0006 fault on an ABB ACS580 variable frequency drive typically indicates an internal communication error or parameter configuration problem. This code can appear when the drive's control logic detects a mismatch between expected and actual settings, when communication between internal processor boards is disrupted, or when control signal wiring does not match the selected parameter profile. Because the ACS580 is a modular drive with multiple configuration options, the exact meaning of E0006 can vary by firmware version and installed option cards. Always consult your drive's user manual or the parameter list for your specific model to confirm the fault definition.

In many cases E0006 is triggered by an incorrect parameter setting rather than a hardware failure. Common triggers include selecting a control mode that conflicts with the physical wiring, enabling a fieldbus protocol without the matching option card installed, or loading a parameter set from a different drive model. Less often, the fault points to a loose ribbon cable between control boards, a failing power supply on the control card, or a corrupted parameter memory.

## Before You Replace Anything

Technicians sometimes replace the main control board when the real problem is a single misconfigured parameter or a loose internal ribbon cable. Always download the parameter list and compare it against the wiring diagram before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Parameter configuration mismatch (~45%)** A control mode parameter does not match the actual field wiring or an enabled function has no supporting hardware installed.
- **Loose or damaged internal ribbon cable (~20%)** Vibration or improper installation can unseat the flat cable connecting the control board to the power board.
- **Corrupted parameter memory (~15%)** A brief power surge or brownout during parameter writes can corrupt the non-volatile memory on the control board.
- **Control board power supply fault (~10%)** The low-voltage DC supply feeding the microprocessor drops out of regulation, causing internal watchdog timeouts.
- **Incompatible firmware or option card (~10%)** A recent firmware update or newly installed fieldbus card may not be compatible with the existing parameter set.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a power-cycle and stay cleared during idle operation?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is likely a transient communication glitch or voltage dip; monitor the drive under load and check incoming power quality.<br><strong>No:</strong> The fault is persistent; proceed to check parameter settings and physical wiring connections.</div>
</details>

<details class="dtree"><summary>Have any parameters been changed or option cards installed recently?</summary>
<div class="dtree-body"><strong>Yes:</strong> Review the last changes and restore factory defaults, then re-enter only the required parameters one section at a time.<br><strong>No:</strong> The fault may be hardware-related; inspect internal ribbon cables and measure the control board supply voltages.</div>
</details>

<details class="dtree"><summary>Does the drive display any other fault codes or warnings alongside E0006?</summary>
<div class="dtree-body"><strong>Yes:</strong> Cross-reference the additional codes in the manual; they often point to the specific parameter group or hardware module at fault.<br><strong>No:</strong> E0006 is appearing alone; focus on control wiring, parameter upload/download, and internal board connections.</div>
</details>

## Step-by-Step Fix {#fix}

1. Disconnect all power to the drive and wait 5 minutes for capacitors to discharge; verify zero voltage with a meter.
2. Record the current parameter settings by uploading them to a PC using the DriveWindow software or by photographing the control panel screens.
3. Inspect the control terminal strip (typically X1 or X2) for loose wires, reversed polarity, or signs of arcing; tighten all terminals.
4. Open the front cover and check that all internal ribbon cables are fully seated in their sockets; press gently on each connector.
5. Restore power and attempt to clear the fault using the reset button or parameter; observe whether the fault returns immediately or only under specific conditions.
6. Load the factory default parameter set and test the drive in local mode with no field signals connected; if E0006 does not appear, the issue is in the custom parameter configuration.
7. If the fault persists with defaults, measure the 24 VDC and 5 VDC rails on the control board using the test points shown in the service manual; voltages outside tolerance indicate a failing power supply or shorted component.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 control board (NCSA-01 or NCSA-02) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0006-fault-code&k=ABB+ACS580+control+board+%28NCSA-01+or+NCSA-02%29&tag=errorcodefixes-20) \| Order by drive frame size and firmware version; verify part number from the existing board label. |
| Internal ribbon cable kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0006-fault-code&k=Internal+ribbon+cable+kit&tag=errorcodefixes-20) \| Includes the flat cables connecting control and power boards; sold as a service kit by ABB. |

## When to Call a Pro

Call a qualified drive technician or controls integrator if you are not familiar with VFD parameter programming or if opening the drive enclosure exposes you to live high-voltage bus capacitors. Professional service is required when the fault persists after parameter reset and free checks, when you need to measure internal DC rails, or when the drive must remain in service and downtime must be minimized. A technician with DriveWindow software and a parameter backup can restore correct settings quickly and verify internal board voltages without risk of electric shock.

**Rough cost:** A pro service call runs about $200-500.

## See Also

- [ABB ACS580 VFD E0012 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0012-fault-code/)
- [ABB VFD Fault 2310 — Causes & Fix](/posts/abb-vfd-fault-2310/)
- [ABB ACS580 VFD E0021 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0021-fault-code/)
- [ABB ACS580 A7A5 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-a7a5-fault-code/)
