---
title: "LG Mini-Split CH21 Error Code — Outdoor Unit High Pressure"
description: "LG mini-split CH21 error code means high pressure protection on the outdoor unit. Learn the causes, how to diagnose, and how to fix LG CH21."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - lg
  - mini-split
  - refrigerant
---

# LG Mini-Split CH21 Error Code — Outdoor Unit High Pressure

**Error Code CH21** on LG mini-split systems means the high-pressure protection device has tripped on the outdoor unit. The system has detected refrigerant pressure above the safe operating limit and shut down the compressor to prevent damage.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## What Triggers CH21

The CH21 code is triggered by one of two conditions:
1. The high-pressure switch (electromechanical) opens due to excessive discharge pressure
2. The high-pressure sensor (transducer) reads a pressure above the board's software limit

For R-410A systems, the high-pressure switch typically trips at 590–620 psig.

## Common Causes {#most-likely-cause}

| Cause | Likelihood |
|---|---|
| Dirty or blocked condenser coil | Very High |
| Outdoor fan motor or capacitor failed | Very High |
| Refrigerant overcharge | Medium |
| Non-condensables in refrigerant system | Medium |
| Restricted liquid line (TXV issue) | Medium |
| Failed high-pressure switch | Low |
| High ambient temperature with undersized system | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Inspect the condenser coil**
- Look for dirt, cottonwood, leaves, or grease on the condenser coil fins
- Clean with alkaline coil cleaner from inside out (fins will bend easily — use low pressure)
- Even 30% coil blockage can cause CH21 in summer

**Step 2 — Check the outdoor fan**
- Fan not running = blown capacitor or failed motor
- Fan running slowly = weak capacitor (check µF)
- Typical LG outdoor fan capacitor: 3–5 µF, 370–440V AC

**Step 3 — Connect refrigerant gauges**
- High-side pressure (R-410A) at 95°F ambient: 280–320 psig is normal
- High-side above 400 psig with fans running and coil clean = refrigerant or non-condensable issue
- Calculate subcooling: temperature difference between liquid line temp and saturation temp
  - Subcooling above 20°F suggests overcharge

**Step 4 — Check for non-condensables**
- Non-condensables (air, nitrogen) cause high head pressure without high subcooling
- Recover refrigerant, evacuate to 500 microns, recharge to nameplate specification

**Step 5 — Test the high-pressure switch**
- Check switch continuity at ambient temperature — should be closed
- If switch is open at ambient pressure, replace

## CH21 Reset Procedure

LG mini-splits allow 3 high-pressure trips before hard lockout:
1. Correct the root cause
2. Turn off the unit from the remote
3. Wait 3 minutes for the minimum off-timer
4. Restart — CH21 should clear
5. For hard lockout: cycle the breaker (off for 30 seconds)

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| Outdoor fan run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-lg-mini-split-ch21-error-code&tag=errorcodefixes-20) \| LG-specific — match µF and voltage |
| Outdoor fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-lg-mini-split-ch21-error-code&tag=errorcodefixes-20) \| Match HP, RPM, and shaft diameter |
| High-pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-lg-mini-split-ch21-error-code&tag=errorcodefixes-20) \| LG part — match trip pressure (590 psig for R-410A) |
| Condenser coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch21-error-code&k=Condenser+coil&tag=errorcodefixes-20) \| Extensive fin damage — clean before condemning |
> **Pro tip:** In areas with heavy cottonwood or pollen, schedule annual coil cleaning in spring before cooling season. A clean coil prevents most CH21 faults without any refrigerant work.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
