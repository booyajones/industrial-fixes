---
title: "Rinnai RUR Series Error Codes — Tankless Water Heater Fault Guide"
description: "Complete guide to Rinnai RUR series condensing tankless water heater error codes, fault causes, and step-by-step troubleshooting for the most common failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - plumbing
  - rinnai
  - tankless-water-heater
---

## Rinnai RUR Series Error Codes — What They Mean

The Rinnai RUR series (RUR160iN, RUR199iN, RUR160eN, RUR199eN) are condensing tankless water heaters with efficiency ratings up to 0.96 UEF. They display fault codes on the controller (MC-91-2 or equivalent). The RUR series uses PVC venting and produces condensate, distinguishing it from the non-condensing RL and RV series. Errors appear on the remote controller display.

[Jump to Fix](#fix)

## Rinnai RUR Series Error Code Reference

| Code | Meaning |
|------|---------|
| 02 | Bypass flow control fault |
| 10 | Exhaust air temperature sensor fault |
| 11 | Ignition failure |
| 12 | Flame failure during operation |
| 14 | Thermal fuse (overtemp) tripped |
| 16 | Overtemp — maximum outlet temperature exceeded |
| 25 | Condensate neutralizer/drain fault |
| 31 | Combustion air inlet sensor fault |
| 32 | Outlet water temperature sensor fault |
| 33 | Heat exchanger outlet sensor fault |
| 52 | Modulating gas valve error |
| 61 | Fan/combustion air fault |
| 65 | Water flow adjustment fault |
| 71 | Gas valve solenoid fault |
| 72 | Flame sensor fault |
| 79 | Water temperature mismatch |

## Common Causes by Code

- **Code 11 — Ignition failure** — On the RUR, ignition failure is commonly caused by low incoming gas pressure, a fouled igniter, or a blocked venting system. The RUR uses direct ignition — the spark igniter and flame sensor are in the burner assembly.
- **Code 12 — Flame failure** — Flame established but lost. In condensing units like the RUR, condensate water running across the burner can cause flame loss in poorly sloped or blocked condensate drain conditions.
- **Code 14 — Thermal fuse** — The thermal fuse is a one-time device that trips if the exhaust temperature exceeds the limit. A thermal fuse trip indicates a serious overtemp event — investigate the root cause (flue blockage, scale in heat exchanger, abnormally high firing rate) before replacing the fuse.
- **Code 25 — Condensate drain** — The RUR produces condensate continuously during operation. Code 25 indicates the condensate drain is backed up or the neutralizer (if installed) is bypassed. Check the condensate drain line for blockage.
- **Code 61 — Fan fault** — The combustion fan motor has failed to reach speed or has stalled. Inspect the fan wheel for debris. A failed bearing in the combustion fan causes noise, then Code 61 as speed drops below the minimum.
- **Code 65 — Flow adjustment** — The water flow adjustment servo in the RUR has a fault. This valve modulates water flow to maintain the set outlet temperature. A failed servo or control board output causes Code 65.
- **Code 71 — Gas valve solenoid** — The gas valve solenoid has not received or responded to the opening signal. Check 24V output from the control board to the gas valve. If 24V is present but valve doesn't open, replace the valve.
- **Code 72 — Flame sensor** — Flame rod is not detecting the flame after ignition. Clean the flame rod and inspect the ceramic insulator for cracks.

## Step-by-Step Fix {#fix}

1. **Read the code from the remote controller** — The MC-91-2 remote shows the error code on the display. Note the code before resetting.
2. **For Code 11** — Check gas supply pressure at the RUR inlet (should be 3.5–7" W.C. for NG, 8–14" W.C. for LP). Inspect the PVC air intake termination outdoors — the combustion air inlet must be clear of snow, ice, and debris.
3. **For Code 12** — Inspect the condensate drain slope and confirm the drain line exits freely. If condensate is backing up inside the unit, it can quench the flame.
4. **For Code 14** — Locate the thermal fuse (single-use; flat rectangular component in the exhaust path). Test for continuity — no continuity means it has blown. Replace only after identifying and correcting the root cause.
5. **For Code 25** — Find the condensate drain outlet (PVC pipe from the bottom or side of the unit). Confirm it drains to an appropriate floor drain or condensate pump. Clear any blockage with warm water.
6. **For Code 61** — Listen to the fan during startup. The RUR fan should spin up and reach operating speed within 15 seconds. A high-pitched bearing noise followed by Code 61 indicates a worn bearing.
7. **Reset** — Press the ON/OFF button on the remote controller to reset after correcting the fault. For Code 14, the thermal fuse must be replaced — the unit will not operate until continuity is restored.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Thermal fuse | [Amazon](https://www.amazon.com/s?k=Thermal+fuse&tag=errorcodefixes-20) \| One-time device; investigate cause before replacing |
| Combustion fan assembly | [Amazon](https://www.amazon.com/s?k=Combustion+fan+assembly&tag=errorcodefixes-20) \| For Code 61; includes wheel |
| Gas valve | [Amazon](https://www.amazon.com/s?k=Gas+valve&tag=errorcodefixes-20) \| For Code 71 with confirmed 24V signal |
| Flame sensor rod | [Amazon](https://www.amazon.com/s?k=Flame+sensor+rod&tag=errorcodefixes-20) \| For Code 72; clean first |
| Condensate drain trap | [Amazon](https://www.amazon.com/s?k=Condensate+drain+trap&tag=errorcodefixes-20) \| Check for blockage or replace if cracked |
| Remote controller (MC-91-2) | [Amazon](https://www.amazon.com/s?k=Remote+controller+%28MC-91-2%29&tag=errorcodefixes-20) \| If display is faulty or communication fails |
## When to Call a Pro

Thermal fuse replacement and gas valve diagnosis require licensed plumbing and/or gas technicians in most jurisdictions. If Code 14 has tripped, do not simply replace the fuse and restart — the underlying cause (heat exchanger scale, blocked flue) must be corrected. Contact Rinnai technical support (1-800-621-9419) for warranty assistance.
