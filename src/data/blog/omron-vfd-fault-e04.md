---
title: "Omron 3G3MX2 E04 Fault — Ground Fault"
description: "Omron MX2 / 3G3MX2 E04 fault means the drive detected a ground fault on the output. Learn causes, diagnostics, and the fix for E04."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - omron
  - mx2
  - ground-fault
---

## Omron 3G3MX2 E04 Fault — What It Means

**E04** on an Omron MX2 (3G3MX2) drive means the inverter detected a **ground fault** on the motor output. Current is leaking from one or more output phases to ground, and the drive trips instantly to protect itself.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding insulation failure**. Older motors frequently ground under VFD duty.
- **Damaged output cable**. Pinched or wet cable can leak current to ground.
- **Moisture in the motor terminal box**. Condensation is a common cause after washdown or seasonal shutdown.
- **Long cable run creating leakage current**. High capacitive leakage can trip sensitive drives.
- **Drive output failure**. If E04 appears with the motor disconnected, the drive may be damaged.

## Step-by-Step Fix {#fix}

1. **Disconnect the motor leads from the drive**. Power the drive back up. If E04 disappears, the problem is in the motor or cable.
2. **Megger the motor**. Measure each phase to ground. Below 1 MΩ is a failure.
3. **Megger the cable separately** with both ends disconnected.
4. **Inspect for moisture** in the terminal box and conduit. Dry and clean before retrying.
5. **Check cable length and shielding**. Long runs may require proper VFD cable and grounding practices.
6. **Test the drive with no motor connected**. If E04 still appears, replace the drive.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [VFD-rated motor cable](https://www.amazon.com/s?k=VFD-rated%20motor%20cable&tag=errorcodefixe-20) | Replace if insulation is damaged |
| [Motor](https://www.amazon.com/s?k=Motor&tag=errorcodefixe-20) | Replace or rewind if grounded |
| [Omron MX2 drive](https://www.amazon.com/s?k=Omron%20MX2%20drive&tag=errorcodefixe-20) | Replace if output stage is failed |

## When to Call a Pro

If ground resistance looks borderline or the application has a very long motor run, a technician with a megger and leakage-current experience can separate true ground faults from nuisance trips.
