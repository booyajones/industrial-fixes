---
title: "LG Refrigerator Error Codes — Complete Fix Guide"
description: "LG refrigerator error codes for French door, side-by-side, and InstaView models including LFX, LMX, LRFXS, and Signature LSXS series. Covers Er CF, Er FF, Er RF, Er rS, Er IF, Er DH, Er HS, Er gF and compressor / fan / sensor faults."
pubDatetime: 2026-05-17T20:30:00Z
modDatetime: 2026-05-17T20:30:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - lg
  - refrigerator
  - fridge
  - appliances
---
<!-- VOICE-GUARD-OFF -->

## LG Refrigerator Error Code Reference

LG refrigerators across the LFX, LMX, LRFXS, LSXS, and Signature LSFXC lines share the same Er-prefix fault dictionary at the controller level. Codes appear on the front display panel, usually as `Er` followed by a 2-letter or 2-character suffix.

| Code | Fault | Most Likely Cause | First Action |
|------|-------|-------------------|--------------|
| Er CF | Condenser fan fault | Failed condenser fan motor or wiring | Pull rear access, listen for fan |
| Er FF | Freezer fan fault | Iced-over fan blade or failed motor | Run forced defrost, inspect fan |
| Er RF | Refrigerator fan fault | Failed evaporator fan motor (fridge compartment) | Replace evaporator fan |
| Er rS | Refrigerator sensor (thermistor) | Open or shorted fridge thermistor | Test sensor resistance |
| Er FS | Freezer sensor (thermistor) | Open or shorted freezer thermistor | Test sensor resistance |
| Er IF | Ice maker fan fault | Ice maker compartment fan failure | Test fan, check connector |
| Er IS | Ice maker sensor fault | Failed ice maker temp sensor | Replace sensor |
| Er DH | Defrost heater fault | Open defrost heater element | Test heater continuity |
| Er HS | Humidity sensor fault | Failed door-area humidity sensor | Replace humidity board |
| Er gF | Gas (refrigerant) flow fault | Low refrigerant or compressor not pumping | Sealed-system service |
| Er dH | Defrost sensor fault | Open defrost termination thermistor | Test, replace |
| Er CO | Communication error (main to UI board) | Failed ribbon cable or one of the boards | Re-seat ribbon, test boards |
| Er IT | Ice making time exceeded | Water supply issue or heater pad fault | Verify water line, test heater |
| F dS | Defrost system failure (FF/RF combined) | Defrost heater + sensor both faulty | Replace defrost assembly |

## The 5 Most Common LG Refrigerator Faults

### Er FF / Er RF — Fan Faults (most common)

If the freezer is warming but the compressor is running, the most likely fault is an iced-over evaporator fan. LG's auto-defrost runs every 8-10 hours; if a defrost cycle fails, frost builds up around the evaporator fan blade and stalls it. The board reads zero fan RPM and trips Er FF.

Workflow:
1. Empty the freezer, unplug the unit, leave the doors open for 24 hours.
2. While defrosting, inspect the back interior panel of the freezer. Remove it and look at the evaporator coil + fan. Frost should be off the fan blade after the thaw.
3. Power the unit back on. If Er FF clears, the defrost system was the root cause. Run again in 48 hours; if Er FF returns, the defrost heater, defrost sensor, or main board has failed.

### Er CF — Condenser Fan Fault

The condenser fan sits at the bottom rear, behind the kick plate. Symptoms: warm refrigerator + freezer simultaneously, compressor running hot, Er CF on display.

1. Pull the unit away from the wall. Remove the rear lower panel.
2. Locate the condenser fan (next to the compressor). Try spinning it by hand with the power OFF. It should spin freely. If it's seized or rubs, the motor or bushing has failed.
3. With power on, listen — the fan should run continuously whenever the compressor runs. A dead fan = motor replacement (~$45-$95 part).

### Er gF — Refrigerant / Compressor Fault

This is the worst one. Er gF means the controller has detected that the compressor is running but the system isn't pulling heat. Two possible causes:

1. **Linear compressor failure.** LG's linear compressors have a known field failure mode (settled 2019-2022 class action). The compressor runs but doesn't compress. Symptoms: no humming-and-cooling cycle, just constant run. Replacement is a $400-$700 sealed-system job.
2. **Refrigerant leak.** Less common but present on units 6+ years old. Symptoms: gradual warming over weeks, then Er gF. Requires a sealed-system technician with EPA 608 certification.

If the unit is under the 10-year linear compressor warranty (most LG fridges sold 2014-2023), the part is covered — homeowner pays labor only.

### Er rS / Er FS — Sensor Faults

Thermistors fail open or shorted. The fix is identical to the Mitsubishi mini-split sensor swap workflow: pull the connector, measure resistance with a multimeter, replace if outside the 10K ohm @ 25°C nominal value. LG thermistors are about $15-$30 each.

### Er CO — Communication Error

The main board talks to the UI/display board over a ribbon cable. Er CO means a packet isn't getting through. Workflow:

1. Power off. Locate the ribbon cable between the door (UI) and main board. Re-seat both ends.
2. Power on. If Er CO clears, the cable was the issue (~$8 part if it doesn't reseat cleanly).
3. If Er CO returns, the UI board or main board is faulty. Swap UI first (~$120) since it's cheaper.

## Parts That May Need Replacement {#parts}

| Part | Where to Buy | Typical Cost |
|------|--------------|--------------|
| Condenser fan motor (LG 4681JB1029A-style) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-error-codes&k=%224681JB1029A%22&tag=errorcodefixes-20) \| RepairClinic | $45-$95 |
| Evaporator fan motor (LG EAU60905401-style) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-error-codes&k=%22EAU60905401%22&tag=errorcodefixes-20) | $35-$80 |
| Defrost heater assembly (LG MEE62385106) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-error-codes&k=%22MEE62385106%22&tag=errorcodefixes-20) | $40-$95 |
| Thermistor sensor (single, 10K ohm) | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-error-codes&k=%22LG+refrigerator+thermistor%22&tag=errorcodefixes-20) | $15-$30 |
| Main control board (LG EBR-series, model-specific) | RepairClinic, LG parts | $180-$450 |
| UI / display board | [Check price on Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-refrigerator-error-codes&k=%22LG+refrigerator+UI+board%22&tag=errorcodefixes-20) | $90-$220 |
| Linear compressor (10-year warranty most 2014-2023 units) | LG parts / authorized servicer | $250-$550 part / $300-$500 labor |

## Technician Tips

- **Don't run the test mode unless you know what it does.** LG's `Test Mode` (entered by holding Ice Plus + Refrigerator for 5 seconds on most models) bypasses safety interlocks. Used by technicians; can damage compressors if left on.
- The `Smart Diagnosis` feature on LG ThinQ-enabled fridges plays an acoustic code through the LG app via the phone microphone. Useful for first-line diagnosis without opening the unit — but the Er-codes on the panel are more accurate than the app's interpretation.
- For chronic Er FF that returns within 48 hours after manual defrost: the defrost termination thermistor is the next failure point, not the heater. Replace the thermistor (~$15) before the heater (~$60).
- LG's 10-year linear compressor warranty covers the compressor part for the original purchaser. Labor was historically excluded but the 2022 class-action settlement extended labor coverage on many models — check serial number against the settlement registry.

## Common Code Combinations

- **Er FF + Er DH**: Defrost heater is open AND the fan stalled because frost built up over the next cycle. Replace both as a defrost-assembly kit.
- **Er rS + Er FS**: Both thermistors reading the same fault. Usually a wiring harness break at the door hinge, not two simultaneous sensor failures.
- **Er CO returning after board swap**: The ribbon cable was damaged during the original disconnect. Replace the cable.

If error code recovers after manual reset but returns within 7 days, the underlying part is failing — not a glitch. Schedule the diagnostic visit before warmth ruins another fridge of food.

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error codes (complete guide)](/posts/lg-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [LG washer error code 31 (pressure / suspension fault)](/posts/lg-washer-error-code-31/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Bosch dishwasher error codes](/posts/bosch-dishwasher-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Whirlpool washer error codes (F-codes + Cabrio)](/posts/whirlpool-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Maytag washer error codes (Bravos + Centennial)](/posts/maytag-washer-error-codes/)

<!-- INTERNAL-LINK-AUTO -->
**Related:** [Samsung refrigerator error codes](/posts/samsung-refrigerator-error-codes/)

