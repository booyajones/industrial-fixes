---
title: "Mitsubishi Mini Split U4 Error Code — Causes & Fix"
description: "What Mitsubishi U4 means on mini split systems, why the outdoor thermistor faults, and how to diagnose and fix it."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - mitsubishi
---

## Mitsubishi Mini Split U4 Error Code — What It Means

The Mitsubishi U4 error code indicates a **communication fault between the indoor and outdoor units**. On many Mitsubishi MSZ/MXZ series systems, U4 specifically points to a problem with the outdoor unit thermistor circuit or a signal interruption on the communication wire between units. The system locks out to protect the compressor when it can't receive valid temperature and status data from the outdoor unit. U4 appears on the indoor unit display and often blinks on the outdoor unit's diagnostic LED.

[Jump to Fix](#fix)

## Common Causes

- **Damaged or loose communication wiring** — The S (signal) wire between indoor and outdoor units is the most common culprit; rodent damage, loose terminals, or a nick in the wire breaks communication.
- **Failed outdoor unit thermistor** — The outdoor air or discharge pipe thermistor sends temperature data back to the indoor PCB; a short or open thermistor generates U4.
- **Outdoor PCB failure** — The outdoor control board may have failed due to power surge, moisture, or component aging.
- **Power supply issue to outdoor unit** — If the outdoor unit isn't fully powered, communication fails and U4 trips on the indoor unit.

## Step-by-Step Fix {#fix}

1. **Inspect the inter-unit wiring** — Shut off the breaker, remove the outdoor unit service panel, and check terminals S1, S2, and S3 (or per your model's wiring diagram). Look for corrosion, loose screws, or broken insulation.
2. **Check communication wire continuity** — With power off, use a multimeter to verify continuity on each wire from indoor to outdoor terminal block. Any open reading indicates a break that must be spliced or rewired.
3. **Test the outdoor thermistors** — Disconnect the outdoor thermistor connector from the PCB and measure resistance with a multimeter. At 25°C (77°F), most Mitsubishi thermistors read approximately 10–15 kΩ. An open or shorted reading means thermistor replacement.
4. **Verify outdoor unit power** — Confirm line voltage (typically 208–240V) at the outdoor unit disconnect. Low voltage or single-phasing causes communication dropout.
5. **Reset the system** — Restore power, clear the fault by holding the RESET button on the indoor unit or cycling the breaker for 5 minutes. If U4 returns within one operating cycle, replace the flagged thermistor or outdoor PCB.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor thermistor (discharge or ambient) | [Amazon](https://www.amazon.com/s?k=Outdoor+thermistor+%28discharge+or+ambient%29&tag=errorcodefixes-20) \| Confirm which thermistor is flagged; Mitsubishi part numbers vary by model series |
| Inter-unit communication cable (3-conductor) | [Amazon](https://www.amazon.com/s?k=Inter-unit+communication+cable+%283-conductor%29&tag=errorcodefixes-20) \| Replace damaged run; use same gauge as OEM wiring |
| Outdoor control PCB | [Amazon](https://www.amazon.com/s?k=Outdoor+control+PCB&tag=errorcodefixes-20) \| Replace if thermistors test good but fault persists |
## When to Call a Pro

If all wiring tests good and both thermistors measure within spec, the outdoor PCB has likely failed. PCB replacement on Mitsubishi mini splits involves refrigerant-side interlock checks — a certified HVAC technician should perform the swap and verify system operation.

## Related Articles

- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi PEX City Multi Error Codes (Indoor Unit): Complete Guide](/posts/mitsubishi-city-multi-pex-error/)
- [Mitsubishi CNC Alarm 500 — Causes & Fix](/posts/mitsubishi-cnc-alarm-500/)
- [Mitsubishi CNC Alarm Y96 — Causes & Fix](/posts/mitsubishi-cnc-alarm-y96/)
- [Mitsubishi E1 Error Code — Indoor/Outdoor Communication Fault Fix](/posts/mitsubishi-e1-error-code/)
