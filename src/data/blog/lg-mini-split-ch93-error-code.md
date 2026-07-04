---
title: "LG Mini Split CH93 Error Code - Causes & Fix"
description: "CH93 means indoor/outdoor communication failure. Most common fix: power-cycle the system for 5 minutes and check outdoor unit power."
pubDatetime: 2026-05-31T00:58:14Z
modDatetime: 2026-05-31T00:58:14Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - lg
money_part: "Indoor/outdoor interconnect cable"
most_likely_cause: "Outdoor unit without power"
---

## LG Mini Split CH93 Error Code — What It Means

The CH93 error code on an LG mini split indicates a communication problem between the indoor and outdoor units. LG defines this fault as an inability for the two units to exchange control data properly. On models released after 2021, CH93 can also appear when the outdoor unit is not receiving electrical power at all, so the fault is not always a pure data-line issue.

This error often appears during test run or startup when the system attempts to establish communication and finds the link unstable. LG's support documentation points to unstable power supply, loose cable connections, or other electrical factors as the root cause. A successful repair depends on methodically checking power and wiring before assuming a board has failed.

[Jump to Fix](#fix)

## Common Causes

- **Outdoor unit without power** On newer models (2021+), CH93 will display if the outdoor unit has no electrical supply, even when wiring is intact.
- **Loose or damaged interconnect wiring** The communication cable between indoor and outdoor units may have a loose terminal, broken conductor, or damaged insulation.
- **Unstable power supply** LG notes that voltage fluctuations or intermittent breaker contact can prevent stable communication during startup.
- **Corroded or dirty terminal connections** Moisture or oxidation at the interconnect terminals interrupts the low-voltage data signal between units.
- **Failed communication circuit board** If power and wiring are confirmed good, a PCB in either the indoor or outdoor unit may have a fault in its communication circuitry.

## Step-by-Step Fix {#fix}

1. **Turn off all power** to the mini split system at the breaker or disconnect switch and wait a full 5 minutes before restoring power, then observe whether CH93 clears after the system restarts.
2. **Verify outdoor unit power** by confirming line voltage is present at the outdoor disconnect and that the outdoor unit's status LED (if equipped) is lit or that the compressor and fan attempt to run.
3. **Inspect the interconnect cable** between indoor and outdoor units for visible damage, pinched insulation, or poor routing that may have exposed conductors to moisture.
4. **Check all terminal connections** at both the indoor and outdoor unit PCBs, tightening each screw and cleaning any corrosion or debris from the terminal blocks.
5. **Measure line voltage** at the indoor unit to confirm it matches the nameplate rating and is stable without sag or spiking that could disrupt communication.
6. **Swap or isolate the cable** if a spare low-voltage interconnect is available, to rule out a conductor break that is not visible externally.
7. **Request factory service or replace the PCB** if power, wiring, and terminals are all confirmed correct but CH93 persists, since board-level diagnostics require live signal tracing that LG does not publish for field techs.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor/outdoor interconnect cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch93-error-code&k=Indoor%2Foutdoor+interconnect+cable&tag=errorcodefixes-20) \| Multi-conductor low-voltage control wire. Verify gauge and conductor count against your model's installation manual before ordering. |
| Indoor unit PCB (communication board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch93-error-code&k=Indoor+unit+PCB+%28communication+board%29&tag=errorcodefixes-20) \| Order by complete model and serial number. Replace only after confirming power and wiring are correct. |
| Outdoor unit PCB (main control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch93-error-code&k=Outdoor+unit+PCB+%28main+control+board%29&tag=errorcodefixes-20) \| Model-specific. Substitute only if indoor board and all wiring have been ruled out through live testing. |

## When to Call a Pro

Call a qualified HVAC technician if the CH93 code returns after a full power reset and you have confirmed that the outdoor unit breaker is on. Communication faults require systematic testing of low-voltage signals, terminal integrity, and board function that go beyond simple visual inspection. If you are not comfortable working inside energized electrical panels or tracing multi-conductor control wiring, professional service is the safer choice. LG recommends requesting service whenever the error persists after checking power and cable connections, because misdiagnosing a wiring issue as a board failure leads to unnecessary parts cost and downtime.

## See Also

- [LG Range F6 Error Code - Causes & Fix](/posts/lg-range-f6-error-code/)
- [LG Dryer Shuts Off Early - Causes & Fix](/posts/lg-dryer-shuts-off-early/)
- [LG Refrigerator rS Error Code - Causes & Fix](/posts/lg-refrigerator-rs-error-code/)
- [LG Dishwasher AE Error Code - Causes & Fix](/posts/lg-dishwasher-ae-error-code/)
