---
title: "MRCOOL E1 Error Code - Causes & Fix"
description: "E1 means the indoor and outdoor units can't communicate. Check wiring connections first, then power cycle the system to reset."
pubDatetime: 2026-05-31T07:55:30Z
modDatetime: 2026-05-31T07:55:30Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - mrcool
---

## MRCOOL E1 Error Code — What It Means

The E1 (or EL01) error code on a MRCOOL mini split indicates a communication failure between the indoor and outdoor units. The two units exchange control signals over a dedicated pair of wires, and this code appears when that signal is interrupted, distorted, or not being received correctly. MRCOOL identifies this as a communication circuit fault rather than a refrigerant or compressor problem.

In the field, the timing of the code offers a clue: if the error comes and goes or returns after a delay, it often points to loose wiring or a damaged cable. If the code reappears immediately after a reset or power cycle, a control board is more likely at fault. Multi-zone systems can also throw E1 when an indoor unit is connected to the wrong outdoor terminal.

[Jump to Fix](#fix)

## Common Causes

- **Loose or mislanded communication wiring** Terminals at the indoor or outdoor unit may have backed out, corroded, or never been fully seated during installation.
- **Damaged communication cable** Cuts, abrasions, pinch points, or an open circuit along the run interrupt the signal between units.
- **Incorrect indoor/outdoor terminal pairing** On multi-zone systems, an indoor unit connected to the wrong outdoor port will fail to communicate.
- **Splices or added devices in the communication path** MRCOOL specifically requires no splices in the communication wire, and any added equipment can introduce resistance or signal loss.
- **Faulty control board** If wiring checks pass and the code returns immediately after reset, the indoor or outdoor control board may have failed.
- **Power surge, storm damage, or pest intrusion** Physical damage to boards or wiring from lightning, rodents, or corrosion can disrupt the control circuit.

## Step-by-Step Fix {#fix}

1. **Turn off power at the breaker** for at least 15 minutes before inspecting any wiring or touching control boards.
2. **Inspect the communication wiring** from the indoor unit to the outdoor unit, checking for loose terminals, cuts, abrasions, or burn marks along the entire run.
3. **Confirm correct terminal pairing** by verifying that each indoor unit is landed on the matching outdoor port (especially on multi-zone systems) and that there are no splices or added devices in the communication path.
4. **Restore power and reset the system** by turning the breaker back on and cycling the unit off and on at the remote to see if the code clears.
5. **Measure supply voltage** at the unit before chasing control faults: for 115 V systems expect about 115 V from L to N, 115 V from L to ground, and 0 V from N to ground; for 220 V systems expect about 220 V from L1 to L2 and about 110 V from each line to ground.
6. **Test communication voltage between terminals 2 and 3** using a DC meter; the reading should fluctuate between positive and negative, a fixed reading suggests an indoor board problem, and a consistently positive reading suggests an outdoor board issue.
7. **Swap the communication cable** with a known-good run (if you have multiple zones) to see if the fault moves with the cable or stays with the indoor unit, then replace the failed board or cable accordingly.

## Parts Often Needed

| Part | Notes |
|------|-------|
| MRCOOL indoor control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-e1-error-code&k=MRCOOL+indoor+control+board&tag=errorcodefixes-20) \| Match the part number printed on your existing board or consult your model number. |
| MRCOOL outdoor control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-e1-error-code&k=MRCOOL+outdoor+control+board&tag=errorcodefixes-20) \| Verify model compatibility and voltage rating before ordering. |
| Communication cable (18/2 or per spec sheet) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-e1-error-code&k=Communication+cable+%2818%2F2+or+per+spec+sheet%29&tag=errorcodefixes-20) \| verify fitment for your model |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with line voltage, if the wiring inspection does not reveal an obvious loose connection or cut, or if the code returns immediately after a power cycle despite correct wiring. Control board diagnosis requires a multimeter and familiarity with DC signal measurement. A technician will also verify that your system has not sustained surge damage and that all terminals meet manufacturer torque and pairing specs. If you have a multi-zone system and are unsure which indoor unit corresponds to which outdoor port, a pro can map the zones and prevent further communication faults.
