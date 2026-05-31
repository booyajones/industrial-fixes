---
title: "Mitsubishi U7 Error Code — Refrigerant System Fault"
description: "Mitsubishi mini-split Error Code U7 means an outdoor unit fan motor or inverter fault. Learn the causes, how to diagnose, and how to fix Mitsubishi U7."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - mitsubishi
  - mini-split
  - inverter
---

# Mitsubishi Error Code U7 — Refrigerant System / Outdoor Fan Fault

**Error Code U7** on Mitsubishi inverter mini-split systems indicates an abnormality in the outdoor unit — most commonly an outdoor fan motor fault or an inverter drive fault detected by the outdoor PCB. The meaning can vary slightly by model series.

## Jump to Fix

- [Most Likely Cause](#most-likely-cause)
- [Diagnosis Steps](#diagnosis)
- [Parts](#parts)

## U7 vs E7 — What's the Difference?

On Mitsubishi mini-splits:
- **E7** = Outdoor fan motor fault (typically on standard inverter models)
- **U7** = Similar fault on newer or Mr. Slim series — outdoor unit PCB or fan motor issue

Check the exact definition in your model's service manual. Both codes indicate an outdoor-unit fault that requires inspection of the fan motor, capacitor, and PCB.

## Common Causes {#most-likely-cause}

| Cause | Likelihood |
|---|---|
| Failed outdoor fan motor | Very High |
| Failed or weak run capacitor | High |
| Debris blocking outdoor fan | Medium |
| Outdoor inverter PCB fault | Medium |
| Low supply voltage during hot weather | Medium |
| Hall-effect sensor fault in brushless fan | Low |

## Step-by-Step Diagnosis {#diagnosis}

**Step 1 — Check outdoor fan operation**
- Power the unit and call for cooling
- Outdoor fan should start within 30 seconds of compressor start
- If fan doesn't spin: check for debris, then test capacitor and motor

**Step 2 — Test the run capacitor**
- Outdoor fan capacitors: typically 2–5 µF, 370V or 440V
- Weak capacitor causes the motor to hum, run hot, and eventually fail
- Replace capacitor if µF is more than ±6% out of rating

**Step 3 — Check motor winding resistance**
- With power off and capacitor discharged, disconnect motor wiring at the PCB
- Measure across each winding pair
- Open or very high resistance = failed motor

**Step 4 — Check supply voltage**
- Mitsubishi units require supply voltage within ±10% of nameplate
- Low voltage during peak summer demand causes motor and inverter faults
- Measure L-N voltage at the outdoor disconnect under load

**Step 5 — Inspect brushless fan motor (DC fan models)**
- Newer Mitsubishi models use brushless DC fans controlled by the inverter
- These fans have a Hall-effect sensor feedback
- If the motor spins but generates U7: Hall-effect sensor may be failed
- Replace the motor assembly (sensor is not serviceable separately on most models)

**Step 6 — Check the outdoor PCB**
- If motor and capacitor check out, check the PCB fan output signal
- On DC fan models, check PWM signal at the fan connector
- PCB failed if voltage is missing with correct input conditions

## Replacement Parts {#parts}

| Part | Notes |
|---|---|
| Outdoor fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-mitsubishi-u7-error-code&tag=errorcodefixes-20) \| Match HP, RPM, blade pitch, and rotation |
| Run capacitor | [Amazon](https://www.amazon.com/dp/B01M05L7B3?ascsubtag=ecf-mitsubishi-u7-error-code&tag=errorcodefixes-20) \| Match µF and voltage rating exactly |
| Outdoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-mitsubishi-u7-error-code&tag=errorcodefixes-20) \| Model-specific — match firmware revision if applicable |
## Reset Procedure

1. Correct the identified fault
2. Power cycle at the outdoor disconnect (off for 5 minutes)
3. Restore power and initiate cooling call
4. Monitor for 10 minutes — U7 should not return if repair is complete

> **Pro tip:** Mitsubishi mini-splits with DC inverter fans (common on newer models) don't use a traditional capacitor — the PCB controls fan speed via PWM signal. If replacing the motor on a DC-fan unit, confirm the replacement is rated for DC inverter drive.

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)

## See Also

- [Mitsubishi P5 Error Code — Drain Pump Fault: Causes & Fix](/posts/mitsubishi-p5-error-code/)
- [Mitsubishi MSY-GL Mini-Split Error Codes - Full Fault Guide](/posts/mitsubishi-msy-gl-error-codes/)
- [Mitsubishi FR-E800 Fault E6 — Causes & Fix](/posts/mitsubishi-fr-e800-fault-e6/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
