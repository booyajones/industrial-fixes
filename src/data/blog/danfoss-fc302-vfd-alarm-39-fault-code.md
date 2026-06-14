---
title: "Danfoss FC302 VFD ALARM 39 - Causes & Fix"
description: "ALARM 39 on Danfoss FC302 means no feedback from heat sink sensor. Check ribbon cable between power card and gate-drive card first."
pubDatetime: 2026-06-03T10:48:05Z
modDatetime: 2026-06-03T10:48:05Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 ribbon cable (power card to gate-drive card)"
most_likely_cause: "Bad or loose ribbon cable between power card and gate-drive card"
---

## Danfoss FC302 VFD ALARM 39 — What It Means

ALARM 39 on a Danfoss VLT AutomationDrive FC 302 means "Heat sink sensor" and reports "No feedback from the heat sink temperature sensor." Specifically, the IGBT thermal sensor signal is not available on the power card. This is a hardware feedback fault, not a programming issue. Danfoss identifies the problem as originating in the power card, the gate-drive card, or the ribbon cable connecting the two. The drive cannot safely operate without valid IGBT temperature data, so it shuts down to protect the power semiconductors from thermal damage.

[Jump to Fix](#fix)

## Common Causes

- **Bad or loose ribbon cable between power card and gate-drive card** The interconnect cable can work loose, suffer bent pins, contamination, heat damage, or physical damage, breaking the sensor signal path.
- **Defective power card** The power card itself may fail internally, preventing the IGBT thermal sensor signal from reaching the gate-drive card.
- **Defective gate-drive card** The gate-drive card may fail and lose the ability to receive or process the heat-sink temperature feedback from the power section.
- **Failed or open IGBT thermal sensor path** The physical sensor or its traces on the power section can fail, preventing any temperature signal from being generated.

## Step-by-Step Fix {#fix}

1. **Power down the drive and lock out the supply** at the main disconnect, then wait at least five minutes for DC bus capacitors to discharge before opening the unit.
2. **Locate and inspect the ribbon cable** connecting the power card to the gate-drive card inside the drive enclosure, checking for physical damage, heat discoloration, bent pins, or contamination on the connectors.
3. **Reseat the ribbon cable** by unplugging both ends, inspecting each connector for corrosion or bent pins, and firmly reconnecting both ends to restore a clean electrical path.
4. **If the cable is intact, inspect the power card** for burn marks, swollen components, or obvious physical damage that would prevent sensor signal output.
5. **Replace the power card** if it shows damage or if reseating the ribbon cable does not clear the alarm, since Danfoss identifies the power card as the next most likely failed component.
6. **If the power card tests good, replace the gate-drive card** as the final suspect in the sensor feedback path, verifying each replacement by powering up and observing whether the alarm clears.
7. **Restore power and test** the drive under no-load or light-load conditions to confirm the IGBT thermal sensor signal is present and the alarm does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 ribbon cable (power card to gate-drive card) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-39-fault-code&k=Danfoss+FC302+ribbon+cable+%28power+card+to+gate-drive+card%29&tag=errorcodefixes-20) \| Specify your frame size and power rating when ordering to match the correct length and connector type. |
| Danfoss FC302 power card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-39-fault-code&k=Danfoss+FC302+power+card&tag=errorcodefixes-20) \| Match the exact frame size and voltage rating of your drive; power cards are not universal across all FC302 models. |
| Danfoss FC302 gate-drive card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-39-fault-code&k=Danfoss+FC302+gate-drive+card&tag=errorcodefixes-20) \| Confirm compatibility with your power card and frame size before ordering. |

## When to Call a Pro

Call a qualified VFD technician or industrial controls specialist if you are not trained to work inside live or recently live high-voltage equipment, if you cannot safely lock out the supply, or if you lack the tools and documentation to identify the power card and gate-drive card in your specific frame size. ALARM 39 is a hardware fault in the drive's internal electronics, and replacing the wrong module can be expensive. A professional can use Danfoss diagnostic software and a multimeter to isolate the failed section quickly and will have access to the exact replacement parts for your model and frame size.

## See Also

- [Danfoss FC302 VFD Alarm 16 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-16-fault-code/)
- [Danfoss FC302 VFD ALARM 18 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-18-fault-code/)
- [Danfoss VFD Fault OL — Causes & Fix](/posts/danfoss-vfd-fault-ol/)
- [Danfoss FC302 Alarm AL 29 — Causes & Fix](/posts/danfoss-fc302-fault-al-29/)
