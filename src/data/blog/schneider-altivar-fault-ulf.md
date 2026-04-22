---
title: "Schneider Altivar Fault ULF — Causes & Fix"
description: "What Schneider Altivar VFD fault code ULF means, why motor underload trips, and how to diagnose and configure it."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - schneider
---

## Schneider Altivar Fault ULF — What It Means

ULF on a Schneider Electric Altivar drive indicates a motor underload fault. The drive detected that the motor is drawing significantly less current than expected for its speed and load — typically below 20–30% of the rated current threshold set in the underload parameters. An underload condition usually means the driven load has been lost or disconnected: a broken belt, a cavitating pump, or a coupling failure. The drive trips to alert the operator that the process is no longer functioning correctly.

[Jump to Fix](#fix)

## Common Causes

- **Broken belt or coupling** — The mechanical link between the motor and the driven load has failed. The motor spins freely with no load, drawing very little current.
- **Cavitating or air-locked pump** — A pump running without sufficient fluid (dry run, low tank level, or vapor lock) draws significantly less current than normal operating load.
- **Conveyor or process jam resolved but load disconnected** — After a jam clears, if a conveyor section disconnects or a chain breaks, the motor loses its load.
- **ULF threshold set too high** — The underload detection threshold in the Altivar parameters is configured so sensitively that normal light-load conditions trigger a false ULF fault.

## Step-by-Step Fix {#fix}

1. **Inspect the driven equipment for mechanical failure** — Check belts, couplings, chains, and shafts between the motor and the load. A visually broken or slipping belt is the most common cause of ULF.
2. **Check pump suction conditions** — If the driven load is a pump, verify that suction piping is not air-locked, that the inlet valve is open, and that the tank or source has adequate fluid level.
3. **Review the underload parameters** — Access the underload detection parameters on the Altivar (typically LUL — Underload current threshold, and tUL — Underload time delay). Verify the threshold is set appropriately for your application. Increase the time delay to prevent nuisance trips during brief low-load transients.
4. **Confirm motor current under normal conditions** — If the load is intact and the process is operating normally but ULF still trips, measure actual motor current with a clamp meter and compare to the ULF threshold setting. Adjust the threshold downward to accommodate normal operating current range.
5. **Repair or replace the mechanical failure** — Replace a broken belt, coupling, or chain. Prime the pump if air-locked.
6. **Disable ULF if not required** — For applications where underload protection is not needed, ULF detection can be disabled in the Altivar parameters. Consult your application requirements before doing this.
7. **Reset the fault** — After resolving the load issue or adjusting parameters, reset the ULF fault via keypad and confirm the drive runs without re-tripping.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Drive belt (V-belt or synchronous)](https://www.amazon.com/s?k=Drive%20belt%20(V-belt%20or%20synchronous)&tag=errorcodefixe-20) | Replace if worn, cracked, or broken |
| [Flexible coupling insert](https://www.amazon.com/s?k=Flexible%20coupling%20insert&tag=errorcodefixe-20) | Replace if rubber insert or spider has failed |
| [Pump foot valve / check valve](https://www.amazon.com/s?k=Pump%20foot%20valve%20%2F%20check%20valve&tag=errorcodefixe-20) | Replace if pump is losing prime repeatedly |

## When to Call a Pro

If the driven load appears mechanically intact but ULF continues to trip, a drive technician should review the full parameter set and perform a load current analysis to correctly configure the underload detection thresholds for the specific application.
