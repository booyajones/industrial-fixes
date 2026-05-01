---
title: "Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix"
description: "What Mitsubishi City Multi P8 and E6 commercial VRF error codes mean, why they trip, and how to diagnose and fix them."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - hvac
  - mitsubishi
---

## Mitsubishi City Multi P8 and E6 Error Codes — What They Mean

**P8** and **E6** are two of the most common fault codes on Mitsubishi City Multi commercial VRF systems (PUHY, PURY, and PUMY outdoor units paired with City Multi indoor units):

- **P8** — Refrigerant system fault / abnormal discharge pipe temperature. The outdoor unit detected a problem in the refrigerant circuit — typically high discharge temperature from low charge, expansion device malfunction, or non-condensable gas.
- **E6** — Communication error between the outdoor unit and one or more indoor units. The system can't maintain valid communication on the refrigerant circuit control bus.

Both codes cause the affected zone to stop cooling or heating. E6 often affects multiple indoor units simultaneously if the communication wiring backbone is broken.

[Jump to Fix](#fix)

## Common Causes

- **P8 — Low refrigerant charge** — A leak has reduced the system charge, causing discharge temperatures to spike as the compressor works harder with less refrigerant to cool it.
- **P8 — Expansion valve fault** — A failed electronic expansion valve (EEV) doesn't regulate refrigerant flow properly, causing abnormal discharge temperatures.
- **E6 — Communication wire fault** — The transmission wire (typically TB3 or the system bus) has a loose connection, broken wire, or incorrect termination resistance between any two components.
- **E6 — Address conflict** — Two indoor units with the same unit address on the same refrigerant line set cause communication collisions and E6.

## Step-by-Step Fix {#fix}

1. **For E6 — Check communication wiring** — Power down the affected units. Inspect all communication wire terminal blocks at the outdoor unit and every indoor unit on the affected line. Tighten all screws and look for corroded or broken conductors.
2. **For E6 — Check unit addresses** — Verify no two indoor units on the same line set share the same unit address. Access each indoor unit's service mode and confirm addresses are sequential and unique (per Mitsubishi installation manual).
3. **For P8 — Check refrigerant temperatures** — Connect Mitsubishi's TG-2000 or MelCloud service tool to read live refrigerant temperatures. Discharge temperatures above 230°F (110°C) confirm high discharge temperature protection has tripped.
4. **For P8 — Inspect for refrigerant leak signs** — Check outdoor unit connections, the lineset, and indoor unit coil connections for oil staining. Any oil track = refrigerant leak site.
5. **Reset and monitor** — After addressing the root cause, cycle all breakers for 5 minutes, restore power, and allow the system to self-initialize (this takes 3–5 minutes on City Multi). Both P8 and E6 should clear automatically if the root cause is fixed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Electronic expansion valve (EEV) | [Amazon](https://www.amazon.com/s?k=Electronic+expansion+valve+%28EEV%29&tag=errorcodefixes-20) \| Replace if P8 persists with adequate refrigerant charge |
| Communication cable (VCTF 0.75mm²) | [Amazon](https://www.amazon.com/s?k=Communication+cable+%28VCTF+0.75mm%C2%B2%29&tag=errorcodefixes-20) \| Replace if continuity test shows broken communication conductor |
| Refrigerant charge (R-410A) | [Amazon](https://www.amazon.com/s?k=Refrigerant+charge+%28R-410A%29&tag=errorcodefixes-20) \| Add only after locating and repairing leak; EPA 608 certification required |
## When to Call a Pro

Mitsubishi City Multi VRF systems require specialized diagnostic tools (TG-2000, MelCloud) and Mitsubishi Diamond Contractor training to diagnose correctly. Refrigerant work on VRF systems requires EPA 608 certification and VRF-specific recovery equipment.

## Related Articles

- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
- [Mitsubishi E3 Error Code — Indoor Fan Motor Fault Fix](/posts/mitsubishi-e3-error-code/)
