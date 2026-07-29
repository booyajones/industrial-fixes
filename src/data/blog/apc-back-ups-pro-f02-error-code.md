---
title: "APC Back-UPS Pro F02 Error (On-Battery Output Short): Causes and the Fix That Works"
description: "APC Back-UPS Pro F02 means the UPS detected a short circuit on its output while running on battery. The published fix is load isolation: unplug every device from the Battery Backup outlets, restart, and reconnect one item at a time until the fault returns."
slug: apc-back-ups-pro-f02-error-code
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - apc
  - ups
  - power-systems
most_likely_cause: "A shorted or faulty device, or a damaged power cable, plugged into a Battery Backup outlet"
free_checks:
  - "Turn the UPS off, unplug every device from the Battery Backup outlets, then turn it back on with no load"
  - "Reconnect loads one at a time until the fault returns. The last device you reconnected is the culprit"
  - "Confirm the internal battery is actually connected. APC ships Back-UPS Pro units with the battery disconnected"
---

## What this code means

APC Back-UPS Pro units report detected system errors as F-codes, F01 through F09, on the LCD. **F02 is "On-Battery Output Short": while the UPS was running on battery power, it detected a short circuit on its output.**

That definition is not folklore. It is printed identically in three Schneider Electric sources:

- **APC document 990-91253B**, the Back-UPS Pro BR650MI / BR900MI / BR1300MI / BR1600MI manual.
- **APC document 990-3889B** (09/2019), the Back-UPS Pro BR1200GI / BR1500GI 230 V manual.
- **Schneider Electric FAQ000264323**, the current support article for the Back-UPS Pro BR 1000/1350/1500 MS/MS2 and BN 1100/1350/1375/1400/1500 M2 / M2-CA models.

The same F02 label also appears on non-Pro Back-UPS hardware: APC document 990-4994A, the BX1300LCD-CN / BX1500LCD-CN manual, prints the same F01-F09 numbering with F02 as On-Battery Output Short. The numbering is stable across the Back-UPS LCD line.

F02 matters because it is one of only two codes in the whole table with a published user-side fix. Every source says the same thing about the rest: errors F03 through F09 cannot be corrected by the user, contact technical support.

## The official isolation sequence

This is the corrective action as published in 990-91253B and repeated verbatim in FAQ000264323:

1. **Turn the UPS off.**
2. **Disconnect all equipment from the Battery Backup outlets.** Everything: computers, monitors, network gear, chargers, and any power strips. The fault is a short on the UPS output, so the output must start empty.
3. **Turn the UPS on.** With no load connected, a healthy unit should start without the fault.
4. **Reconnect equipment one item at a time.** If the output is tripped again, disconnect the device that caused the error.

The 990-3889B table for the BR1200GI/BR1500GI gives a shorter version of the same instruction ("turn the Back-UPS off, disconnect non-essential equipment from the Battery Backup outlets, then turn the Back-UPS on"), so if you own a GI unit, the fuller MI sequence above is the one to follow.

Practical notes from the bench:

- **Suspect the cable as much as the device.** A crushed or pinched cord, a cord run under a desk foot or chair wheel, or insulation chafed against a sharp edge can short without the device itself being dead. Inspect each cord as you reconnect it.
- **Remove power strips from the test entirely.** A surge strip or daisy-chained power strip on a Battery Backup outlet adds a whole extra set of cords and contacts to the fault path. Test devices plugged directly into the UPS first.
- **A failed power supply is a common offender.** If one specific device reliably brings F02 back, do not keep re-plugging it in to confirm. Have it repaired or replaced.
- **Only the Battery Backup outlets are in scope.** The fault is defined against the battery-backed output, which is what the inverter drives when the unit is on battery. The surge-only outlets are not part of this test.

Once you have identified the offending device, the UPS itself normally needs nothing. Clear the fault display (see below) with the bad load removed, then reconnect the known-good equipment.

## Clearing the fault display

Both Back-UPS Pro manuals document a 2-second POWER hold that clears the indication:

- 990-3889B calls it **Fault Reset**: "After a fault has been identified, press POWER to remove the visual indication and return to standby status."
- 990-91253B calls it **Status Reset**: "After an error has been detected and identified, press POWER to remove the visual indication and return to standby status."

Read that literally. It removes the *visual indication*. It repairs nothing. If the shorted load is still plugged in, F02 comes back the next time the unit transfers to battery.

## F02 at power-on: check the model scope before you act on advice

You will find widespread advice that an F02 shown the moment you switch a Back-UPS on means the internal battery is not properly connected. That advice traces to a real Schneider document, **FAQ000273815, "F02 or F04 Error Code When Turning on Back-UPS,"** which states that if the battery has not been correctly connected to the UPS, the unit may display an F02 or F04 error code when turned on. Its published sequence:

1. Ensure the battery connectors in the Back-UPS are firmly connected to the battery, and try turning it on again.
2. If it still shows F02 or F04, turn the UPS off and unplug it from the wall socket.
3. With the power cord removed from the wall, try turning it on again.
4. If it still displays the error code, contact customer support.

**But note the scope.** Schneider tags that FAQ to the Back-UPS models **BN1350M2, BN1500M2 and BX1500M**. It is not published against the Back-UPS Pro BR-GI or BR-MI families, and neither BR manual lists a battery-connection cause for F02. If you own one of the models the FAQ names, that sequence is the documented first move. If you own a BR-series Back-UPS Pro, treat it as a sensible thing to check, not as the manufacturer's answer for your unit.

What the Back-UPS Pro manuals *do* document about battery connection is worth knowing either way:

- 990-91253B states plainly: **"The UPS is shipped with the battery disconnected."** A new unit that will not start correctly is very often simply not connected yet.
- Both BR manuals list "The internal battery is not connected" as a cause under **"Back-UPS will not switch on,"** with the corrective action "Connect the battery."
- On BR-MI models a disconnected battery has its own indication and is not an F-code at all: **chirps every 2 seconds with the Load Capacity bar flashing.**

## F02 vs F04: do not mix them up

| Code | Official name (BR manuals) | What it means | Your first move |
| --- | --- | --- | --- |
| F02 | On-Battery Output Short | Short circuit detected on the output while the UPS was on battery | Run the isolation sequence above |
| F04 | Clamp Short | Internal fault | Not user-correctable per every Back-UPS Pro source. Contact APC/Schneider Technical Support |

They travel together in FAQ000273815 because on the BN/BX models that FAQ covers, both can appear at power-on with a poorly seated battery. On a Back-UPS Pro the documents do not extend that to F04: it sits in the F03-F09 block that the manuals say the user cannot correct.

For context, 990-91253B labels F05 as "Charge Status," F08 as "Fan Condition (for BR1600MI only)," and F09 as "Internal Error." F02 is the only code in the table you fix by unplugging your own equipment.

## F02 is not a "replace battery" code

Do not buy a battery to chase this fault. F02 is defined as an output short, not a battery health warning. The Back-UPS Pro manuals give the battery-replacement indications separately: an illuminated Replace Battery indicator, and on the BR-MI models continuous chirping with the Load Capacity bar and Replace Battery icon flashing alternately.

If you do need a cartridge, the manuals specify: **APCRBC124** for BR1200GI/BR1500GI, **APCRBC110** for BR650MI, **APCRBC164** for BR900MI, **APCRBC165** for BR1300MI, and **APCRBC166** for BR1600MI. Both manuals put typical battery life at three to five years, shorter with frequent outages or elevated temperatures, and 990-91253B instructs replacement at least every 5 years or at end of service life, whichever comes first.

## When to stop and contact support

Stop troubleshooting and contact APC/Schneider Technical Support when:

- **F02 persists with nothing at all connected to the Battery Backup outlets.** You have exhausted the published fix; the fault is internal.
- **You see or smell any evidence of damage**: a burnt smell, discoloured or melted outlet faces, or a hot chassis. Take the unit out of service.

**Safety, in the manufacturer's own words.** The 990-91253B safety section carries a **DANGER** notice headed "HAZARD OF ELECTRIC SHOCK, EXPLOSION, OR ARC FLASH." It states that servicing of batteries should be performed or supervised by personnel knowledgeable about batteries and the required precautions, that a battery can present a risk of electric shock and burns by high short-circuit current, and that failed batteries can reach temperatures exceeding the burn thresholds for touchable surfaces. It closes: "Failure to follow these instructions will result in death or serious injury."

The same manual carries a **CAUTION** headed "RISK OF HYDROGEN SULPHIDE GAS AND EXCESSIVE SMOKE," instructing that if the UPS indicates a battery over-temperature condition, or if there is evidence of electrolyte leakage, you must power off the UPS, unplug it from the AC input, disconnect the batteries, and not operate the UPS until the batteries have been replaced.

Do not go past the battery compartment. Both manuals' service instructions are the same: do not return the unit to the dealer, work through the troubleshooting table, then contact technical support, who will issue an RMA if needed.

## Frequently asked questions

### Does F02 mean my APC battery is bad?

Not by definition. F02 is an output short fault. The Back-UPS Pro manuals signal a battery that needs replacing through the Replace Battery indicator and the failed-self-test chirp pattern, not through F02. The battery only enters the picture in the power-on scenario documented in FAQ000273815, and that FAQ is published for the BN1350M2, BN1500M2 and BX1500M models rather than the BR series.

### Can a single plugged-in device really cause F02?

Yes, and that is exactly what the published corrective action assumes. Disconnect all equipment from the Battery Backup outlets, power the UPS back on, and reconnect one item at a time. If the output trips again, the device you just reconnected is your fault source.

### Why does F02 only show up when the power goes out?

Because the fault condition is defined as a short detected while on battery. In normal operation the load sits on utility power; during an outage or a transfer the inverter drives the output directly and detects the short. A marginal or shorted load can therefore hide until the exact moment you need the UPS. If you have had one F02 event, run the isolation procedure now rather than waiting for the next outage to repeat it.

### I unplugged everything and F02 is still there. Now what?

Then the published user fix is exhausted. Verify the internal battery is connected (990-91253B confirms units ship with it disconnected), and if the code persists with no load attached, contact APC/Schneider Technical Support. Do not open the unit beyond the battery compartment to hunt for it.

## Sources

Every URL below was retrieved and read while writing this page.

- APC Back-UPS Pro BR650MI/BR900MI/BR1300MI/BR1600MI User Manual (APC doc EN 990-91253B): https://www.battery-direct.fr/Datenblaetter/apc-back-ups-pro-manual.pdf
- APC Back-UPS Pro BR1200GI/BR1500GI 230 V Installation and Operation Manual (APC doc EN 990-3889B, 09/2019): https://media.distributordatasolutions.com/apc/2020q3/documents/885d73f3aac6f5c1965eb953b67ed231734fdf01.pdf
- Schneider Electric FAQ000264323, "What are the basic troubleshooting steps for the Back-UPS Pro BR/BN MS/MS2/M2/M2-CA models?": https://www.se.com/us/en/faqs/FAQ000264323/
- Schneider Electric FAQ000273815, "F02 or F04 Error Code When Turning on Back-UPS" (tagged BN1350M2, BN1500M2, BX1500M): https://www.se.com/us/en/faqs/FAQ000273815/
- APC Back-UPS BX1300LCD-CN / BX1500LCD-CN User Manual (APC doc 990-4994A), hosted by Schneider Electric: https://download.schneider-electric.com/files?p_Doc_Ref=SPD_JHSH-74ABL6_EN
