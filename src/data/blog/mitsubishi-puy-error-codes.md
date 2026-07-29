---
title: "Mitsubishi PUY Air Handler Error Codes — Fault Code Diagnostic Guide"
description: "Complete guide to Mitsubishi PUY series air handler error codes, what each fault means, and step-by-step troubleshooting for the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - mitsubishi
  - mini-split
money_part: "EEV coil"
---

## Mitsubishi PUY Air Handler Error Codes — What They Mean

The Mitsubishi PUY (Power Unit, Y-series) is a ducted air handler designed to work with Mitsubishi's City Multi VRF system. It is a commercial-grade indoor unit that connects to the outdoor VRF or heat pump system via refrigerant piping. Error codes appear on the wired remote controller, the main unit LED, or the ME remote maintenance controller.

## Mitsubishi PUY Common Error Codes

| Code | Meaning |
|------|---------|
| E0 | Remote controller communication error |
| E1 | Indoor PCB fault |
| E3 | Fan motor error |
| E4 | Drain sensor error or drain overflow |
| E6 | Transmission error (indoor-outdoor) |
| E9 | EEV (electronic expansion valve) error |
| P1 | Intake air temperature sensor fault |
| P2 | Pipe temperature sensor fault |
| P4 | Drain full or sensor fault |
| P6 | Freeze protection or overload protection |
| P8 | High-temperature protection |
| P9 | High-temperature pipe protection |
| U6 | Compressor overcurrent or system protection |

## Common Causes by Code

- **E0 — Remote controller communication** — The wired remote has lost communication with the indoor unit PCB. Check the signal wire connection between the remote and the unit. A failed remote controller or indoor PCB can also cause E0.
- **E3 — Fan motor** — The PUY uses a DC fan motor. E3 appears when the motor fails to reach the commanded speed. Check for mechanical obstruction (debris in the fan), motor winding failure, or PCB output fault.
- **E4 / P4 — Drain** — The PUY has a drain pan with a float switch. E4/P4 indicates the drain is full or the float switch has failed. Clear the condensate drain, confirm the pump is operating (if equipped with a condensate pump), and check float switch continuity.
- **E6 — Transmission error** — Communication failure between the indoor PUY unit and the outdoor VRF unit. Check the transmission wiring (two-wire bus) between units. Also check that the dip switch addressing matches the outdoor unit's configuration.
- **E9 — EEV error** — The electronic expansion valve coil is not responding. Measure EEV coil resistance at the indoor unit — should be consistent across the winding pairs. A failed coil can be replaced without opening the refrigerant circuit.
- **P6 — Freeze/overload protection** — Freeze protection activates when the indoor coil temperature drops to near 32°F. Common causes: low airflow (dirty filter, blocked grilles, failed fan), low refrigerant charge, or very low return air temperature.
- **U6 — Compressor protection** — This code from the indoor unit indicates a system-level protection response initiated by the outdoor VRF unit. Check the outdoor unit for its own error codes — U6 from the indoor is typically a secondary symptom.

## Step-by-Step Fix {#fix}

1. **Read the code** — Display is on the wired remote controller. In some configurations, the ME remote maintenance controller provides more detail including timestamps and fault count.
2. **For E0** — Check the remote controller signal wires at the indoor unit terminal block. Power cycle the indoor unit. If fault persists after power cycle, test with a different remote controller.
3. **For E3** — Inspect the fan inlet and outlet for obstructions. With power off, spin the fan by hand — should rotate freely. Power on and listen: no sound = power issue; hum without motion = mechanical fault.
4. **For E4 / P4** — Locate the drain pan under the PUY coil. If full of water, the drain is blocked. Clear the drain pipe. If drain is empty, the float switch is stuck or failed — test switch continuity.
5. **For E6** — Trace the two-wire transmission cable from the PUY terminal block to the outdoor unit. Check for pinched cables at any panel penetration. Confirm the unit address dip switches match the system configuration.
6. **For P6** — Check the filter on the PUY return air inlet. Confirm all return and supply grilles are open and unobstructed. Measure the suction pressure at the indoor unit service port.
7. **For E9** — Access the EEV coil (clip-on to the valve body). Disconnect the coil connector and measure winding resistance. Compare to service data (typically 33–56 ohms across winding pairs).

## Parts Often Needed

| Part | Notes |
|------|-------|
| EEV coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-puy-error-codes&k=EEV+coil&tag=errorcodefixes-20) \| Removable; replace before refrigerant work |
| Wired remote controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-puy-error-codes&k=Wired+remote+controller&tag=errorcodefixes-20) \| Test swap to isolate E0 |
| Drain float switch | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-puy-error-codes&k=Mitsubishi+Drain+float+switch&tag=errorcodefixes-20) \| Check continuity; replace if stuck |
| Indoor PCB | [Amazon](https://www.amazon.com/s?k=Indoor+PCB&tag=errorcodefixes-20) \| For E1 or persistent unexplained faults |
| DC fan motor | [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-puy-error-codes&k=Mitsubishi+DC+fan+motor&tag=errorcodefixes-20) \| For E3 with confirmed mechanical fault |
| Transmission cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-puy-error-codes&k=Transmission+cable&tag=errorcodefixes-20) \| Two-wire; replace entire run if damaged |
## When to Call a Pro

Mitsubishi VRF systems require City Multi-certified technicians for refrigerant work, system commissioning, and address configuration. Any U6 fault should be investigated at the outdoor VRF unit as well — the indoor PUY is reporting a system-level issue, not just an indoor unit issue.
