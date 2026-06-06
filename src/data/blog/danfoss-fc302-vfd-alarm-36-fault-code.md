---
title: "Danfoss FC302 Alarm 36 - Causes & Fix"
description: "Alarm 36 on a Danfoss FC302 VFD means mains failure or loss of supply voltage. Check input fuses and incoming power connections first."
pubDatetime: 2026-06-04T09:12:26Z
modDatetime: 2026-06-04T09:12:26Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 36 — What It Means

Alarm 36 on the Danfoss FC302 variable frequency drive displays as "WARNING/ALARM 36, Mains failure." This alarm tells you the drive has lost its incoming supply voltage or the power has dropped out of the range it needs to operate. The alarm is only active when parameter 14-10 Mains Failure is not set to "No Function," so if that parameter is disabled the drive will not report this condition.

In plain terms, the FC302 is saying it cannot see stable mains power on its line-side terminals. Something upstream has interrupted the feed, whether a tripped breaker, a blown fuse, a loose wire, or an actual utility outage. The drive cannot run without proper incoming voltage, so it shuts down and throws Alarm 36 until you restore the supply and reset the fault.

[Jump to Fix](#fix)

## Common Causes

- **Blown input fuses** The fuses protecting the frequency converter's input terminals have opened due to overcurrent or age, cutting off mains supply to the drive.
- **Upstream power loss** A tripped breaker, open disconnect, or utility outage has removed voltage from the circuit feeding the VFD.
- **Loose or broken line-side wiring** A terminal screw has backed off, a wire has fractured, or a splice has failed on the mains supply path to the drive's input.
- **Failed contactor or relay** An upstream magnetic contactor that feeds the drive has stuck open or burned contacts, preventing voltage from reaching the FC302.
- **Parameter 14-10 configuration** Parameter 14-10 is set to detect mains failure and the incoming voltage briefly dipped below threshold, triggering the alarm even if power is now stable.

## Step-by-Step Fix {#fix}

1. **Verify incoming mains power** by using a multimeter to measure line voltage at the upstream disconnect or panel feeding the drive, confirming all three phases (or both legs) are present and match nameplate requirements.
2. **Inspect and test the input fuses** on the line side of the FC302, removing each fuse and checking continuity with a meter or replacing all fuses if any are open.
3. **Check all line-side terminals and wiring** at the drive's L1, L2, L3 input points, tightening any loose screws and inspecting for broken strands, corrosion, or burn marks.
4. **Examine upstream contactors and disconnects** for proper closure and clean contacts, cycling the contactor manually if possible and replacing it if the contacts are pitted or the coil does not pull in.
5. **Review parameter 14-10 Mains Failure** in the drive's control panel or software, verifying it is set appropriately for your application or setting it to "No Function" if nuisance alarms occur and your system does not require this protection.
6. **Restore mains power** to the drive by closing any open disconnect or resetting any tripped breaker, then reset Alarm 36 from the keypad and monitor for return of the fault.
7. **Run a test cycle** under load to confirm the drive operates normally without recurrence of the mains failure alarm, watching for voltage sags or phase imbalance that could retrigger the fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input line fuses for Danfoss FC302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-36-fault-code&k=Input+line+fuses+for+Danfoss+FC302&tag=errorcodefixes-20) \| Match the ampere and voltage rating shown on your drive's nameplate and wiring diagram. |
| Three-phase magnetic contactor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-36-fault-code&k=Three-phase+magnetic+contactor&tag=errorcodefixes-20) \| Select a contactor rated for the full-load current of the VFD if the existing unit has failed or shows contact damage. |

## When to Call a Pro

Call a qualified electrician or automation technician if you are not comfortable working with three-phase mains voltage, if the alarm persists after replacing fuses and verifying all connections, or if you measure unstable or missing phases at the upstream panel. A licensed professional can safely trace the supply circuit, measure phase balance under load, and verify grounding and bonding meet code. If the drive continues to report Alarm 36 with confirmed good incoming power and correct parameter settings, the internal power-supply stage may have failed and the unit will need factory repair or replacement by someone trained on Danfoss VFDs.
