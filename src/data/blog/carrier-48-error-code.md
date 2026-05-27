---
title: "Carrier 48 Error Code — Induced Draft Motor Lockout"
description: "Carrier flash code 48 means the induced draft motor has failed to start or is running out of spec. Learn causes, diagnostic steps, and replacement parts."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
  - furnace
  - inducer
---

# Carrier Error Code 48 — Induced Draft Motor Lockout

Flash code **48** on a Carrier furnace or rooftop unit means the induced draft (ID) motor has failed to prove operation within the startup sequence. The control board detected that the inducer did not reach the required speed before the ignition sequence began.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Step-by-Step Diagnosis](#diagnosis)
- [Replacement Parts](#parts)

## What Is the Induced Draft Motor?

The induced draft motor (inducer) pulls combustion gases through the heat exchanger and out the flue. On modern Carrier furnaces and RTUs, the control board verifies inducer operation via the pressure switch circuit before allowing the gas valve to open. If the inducer fails to run or fails to generate sufficient negative pressure, Code 48 trips.

## Common Causes {#most-likely-cause}

| Cause | Likelihood |
|---|---|
| Failed inducer motor (seized or winding failure) | High |
| Failed run capacitor on inducer motor | High |
| Blocked or restricted flue | Medium |
| Defective pressure switch | Medium |
| Broken or kinked pressure switch hose | Medium |
| Control board relay failure | Low |
| Wiring issue to inducer motor | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Check for physical operation**
- With power on, initiate a heat call and listen/look for the inducer to spin
- If no movement: check 24V or 115V power at the motor terminals
- If power present but no movement: test capacitor µF (replace if out of spec)

**Step 2 — Test the run capacitor**
- Typical inducer capacitors: 3–5 µF, 370V
- Read µF with a capacitor tester — replace if more than 6% out of rating

**Step 3 — Check the pressure switch**
- With inducer running, measure the pressure switch hose with a manometer
- Pressure should exceed the switch trip point (typically -0.3 to -0.5 in. w.c.)
- Blow through the hose — any restriction means blocked condensate or debris

**Step 4 — Inspect the flue**
- Look for bird nests, ice, or physical obstruction in the flue pipe
- Check the draft hood or vent cap at the roof termination

**Step 5 — Check inducer motor resistance**
- With power off, disconnect motor and measure winding resistance
- Open winding (infinite ohms) = failed motor — replace

**Step 6 — Inspect wiring**
- Check for loose connections at the motor plug
- Verify control board relay is energizing (listen for click)

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| Inducer motor | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-48-error-code&tag=errorcodefixes-20) \| Match HP, RPM, and frame — Carrier HC21ZE117 is common |
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-carrier-48-error-code&tag=errorcodefixes-20) \| Match µF and voltage — 370V minimum |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-48-error-code&tag=errorcodefixes-20) \| Match the negative pressure trip point |
| Pressure switch hose | [Amazon](https://www.amazon.com/dp/B0CPTHML1N?ascsubtag=ecf-carrier-48-error-code&tag=errorcodefixes-20) \| Check for cracks at both ends |
## Reset Procedure

After repairing the fault, press the reset button on the control board or cycle power to clear Code 48. If the code returns within the first 5 minutes, the repair is incomplete.

> **Safety:** Always shut off the disconnect and verify no voltage before working inside the unit. Induced draft motor failures can allow combustion gases to enter the building if the heat exchanger is also cracked — inspect the heat exchanger visually while you have the unit open.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier 24 Error Code — Causes & Fix](/posts/carrier-24-error-code/)
- [Carrier 34 Error Code — Ignition Proving Failure Fix](/posts/carrier-34-error-code/)
- [Carrier Error Code 56 — IFC Fault (Induced Draft Motor)](/posts/carrier-56-error-code/)
- [Carrier Comfort 24ACC4 AC Error Codes - Full Flash Code Guide](/posts/carrier-comfort-24acc4-error-codes/)
