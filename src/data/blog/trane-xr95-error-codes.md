---
title: "Trane XR95 Furnace Error Codes — Complete Guide"
description: "Trane XR95 furnace error codes: all LED flash codes for the 95% AFUE single-stage XR95, causes, and fixes."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane XR95 Error Codes — What It Means

The Trane XR95 (model S9X1) is a single-stage, 95% AFUE condensing gas furnace. It uses a standard Trane/American Standard IFC control board with a diagnostic LED that flashes fault codes through the lower access panel. The XR95's high efficiency means it uses a secondary heat exchanger to extract more heat from combustion gases — and that secondary exchanger is a common source of codes not seen on older 80% furnaces.

## Flash Code Quick Reference

| Flash Code | Meaning | Priority |
|-----------|---------|---------|
| 1 flash | System lockout (retries exceeded) | High |
| 2 flashes | Pressure switch stuck open | High |
| 3 flashes | High-limit or roll-out switch open | High |
| 4 flashes | Ignition failure | High |
| 5 flashes | Flame sensed without call for heat | Critical |
| 6 flashes | 115V line voltage fault / bad polarity | Medium |
| 7 flashes | Gas valve fault | Critical |
| 8 flashes | Low flame sense signal | Medium |
| 9 flashes | Igniter circuit fault | Medium |
| Slow blink | Normal standby | None |
| Rapid blink | Normal operation | None |

## Most Common XR95-Specific Issues

### 2 Flashes: Pressure Switch — XR95 Specifics
The XR95 uses a two-stage condensate drain system with a secondary heat exchanger coil. The most common cause of 2-flash codes on XR95 units is a plugged secondary heat exchanger. This shows up as water backing up in the flue trap. The secondary heat exchanger on the XR95 is a coil inside the furnace cabinet — it can plug with mineral scale over 10–15 years of service.

**Check first:** The PVC condensate trap at the bottom of the furnace. If water sits in the trap during operation, the secondary coil drain is restricted. Cleaning the trap and drain tubing resolves most 2-flash faults.

### 3 Flashes: High Limit — XR95 Specifics
The XR95 uses an ECM variable-speed blower motor on some configurations and a standard PSC motor on others. If the blower motor is failing and running at reduced speed, the heat exchanger overheats. On XR95 with ECM motors, a motor that's running but not reaching commanded speed triggers limit faults. Check for a fault code from the ECM motor itself (some have a separate LED or use the board's diagnostic port).

### 4 Flashes: Ignition Failure
The XR95 uses a silicon nitride hot-surface igniter. Typical life is 5–10 years. The igniter glows visible red-orange through the sight glass. If the igniter glows but no flame appears, verify gas pressure and check for a stuck gas valve. If the igniter doesn't glow at all, it's open — measure resistance (should be 40–90 ohms cold).

## Step-by-Step Fix for Code 2 (Most Common)

1. Turn off the furnace at the thermostat and disconnect switch.
2. Locate the condensate trap — white PVC U-trap near the base of the furnace.
3. Disconnect the drain hose from the trap outlet and pour water through. Water should drain freely.
4. If blocked, disassemble the trap by removing the two screws or clips and clean with warm water.
5. Reconnect and restore power. Run a heat cycle and verify the code clears.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hot-surface igniter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-xr95-error-codes&k=Hot-surface+igniter&tag=errorcodefixes-20) \| Trane CNT05473 or OEM equivalent |
| Condensate trap | [Amazon](https://www.amazon.com/dp/B077J4Y763?ascsubtag=ecf-trane-xr95-error-codes&tag=errorcodefixes-20) \| Trane CPT0048 or compatible |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-trane-xr95-error-codes&tag=errorcodefixes-20) \| 0.60"–0.80" WC, Trane model-specific |
| IFC control board | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-trane-xr95-error-codes&tag=errorcodefixes-20) \| CNT05369 or match board label |
## When to Call a Pro
If 3-flash (high limit) or 2-flash codes repeat after cleaning the condensate trap and replacing the filter, a technician should inspect the secondary heat exchanger for scale buildup or damage. Chemical descaling of a plugged secondary coil is a service-level repair.

## Related Articles

- [Trane 1 Flash Error Code — Causes & Fix](/posts/trane-1-flash-error-code/)
- [Trane Error Code 126 — Ignition Lockout Fix](/posts/trane-126-error-code/)
- [Trane 2 Flashes Error Code — Causes & Fix](/posts/trane-2-flashes-error-code/)
- [Trane 3 Flashes Error Code — Pressure Switch Fault Fix](/posts/trane-3-flashes-error-code/)
- [Trane 3 Flash Pressure Switch Fault — Detailed Diagnosis Guide](/posts/trane-3-flashes-pressure-switch/)
