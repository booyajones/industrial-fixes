---
title: "Mitsubishi U7 Error Code — Refrigerant System Fault"
description: "Mitsubishi mini-split Error Code U7 means an outdoor unit fan motor or inverter fault. Learn the causes, how to diagnose, and how to fix Mitsubishi U7."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
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

| [Cause](https://www.amazon.com/s?k=Cause&tag=errorcodefixe-20) | Likelihood |
|---|---|
| [Failed outdoor fan motor](https://www.amazon.com/s?k=Failed%20outdoor%20fan%20motor&tag=errorcodefixe-20) | Very High |
| [Failed or weak run capacitor](https://www.amazon.com/s?k=Failed%20or%20weak%20run%20capacitor&tag=errorcodefixe-20) | High |
| [Debris blocking outdoor fan](https://www.amazon.com/s?k=Debris%20blocking%20outdoor%20fan&tag=errorcodefixe-20) | Medium |
| [Outdoor inverter PCB fault](https://www.amazon.com/s?k=Outdoor%20inverter%20PCB%20fault&tag=errorcodefixe-20) | Medium |
| [Low supply voltage during hot weather](https://www.amazon.com/s?k=Low%20supply%20voltage%20during%20hot%20weather&tag=errorcodefixe-20) | Medium |
| [Hall-effect sensor fault in brushless fan](https://www.amazon.com/s?k=Hall-effect%20sensor%20fault%20in%20brushless%20fan&tag=errorcodefixe-20) | Low |

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
| [Outdoor fan motor](https://www.amazon.com/s?k=Outdoor%20fan%20motor&tag=errorcodefixe-20) | Match HP, RPM, blade pitch, and rotation |
| [Run capacitor](https://www.amazon.com/s?k=Run%20capacitor&tag=errorcodefixe-20) | Match µF and voltage rating exactly |
| [Outdoor PCB](https://www.amazon.com/s?k=Outdoor%20PCB&tag=errorcodefixe-20) | Model-specific — match firmware revision if applicable |

## Reset Procedure

1. Correct the identified fault
2. Power cycle at the outdoor disconnect (off for 5 minutes)
3. Restore power and initiate cooling call
4. Monitor for 10 minutes — U7 should not return if repair is complete

> **Pro tip:** Mitsubishi mini-splits with DC inverter fans (common on newer models) don't use a traditional capacitor — the PCB controls fan speed via PWM signal. If replacing the motor on a DC-fan unit, confirm the replacement is rated for DC inverter drive.
