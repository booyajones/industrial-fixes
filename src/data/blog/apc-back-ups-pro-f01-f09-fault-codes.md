---
title: "APC Back-UPS Pro F01-F09 Fault Codes: Official Meanings, Beep Patterns, and Fixes"
description: "Official APC F01-F09 System Fault table for Back-UPS Pro: F01 (on-battery overload) and F02 (output short) are the only user-fixable codes; F03-F09 mean contact APC. Plus beep patterns, the 2-second fault reset, and RBC battery part numbers."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: apc-back-ups-pro-f01-f09-fault-codes
featured: false
draft: true
tags:
  - apc
  - ups
  - electrical
  - power-quality
most_likely_cause: "F01: too much load on the Battery Backup outlets during an outage. F02/F04 at power-on: battery connector not fully seated."
money_part: "Replacement battery cartridge (APCRBC124 for BR1200GI/BR1500GI; APCRBC110/164/165/166 across the BR-MI family)"
free_checks:
  - "Reseat the battery connector"
  - "move non-essential loads off the Battery Backup outlets"
  - "hold POWER for 2 seconds to clear the fault display"
---

## APC Back-UPS Pro F01-F09 — What These Codes Mean

When an APC Back-UPS Pro (BR-series) detects a problem it displays **System Fault** on the LCD along with a code from **F01 to F09**. These codes come straight from APC's own System Faults table, which appears in the official manuals for both the international BR1200GI/BR1500GI models (APC document 990-3889B) and the BR650MI/BR900MI/BR1300MI/BR1600MI family (APC document 990-91253B).

The single most useful thing to know before you touch anything: **only F01 and F02 have an official user-side corrective action.** For every code from F03 through F09, both APC manuals say the same thing - the fault cannot be corrected by the user, contact APC (Schneider Electric) Technical Support. If the unit is in warranty, replacement is the usual outcome. Knowing that up front saves you an afternoon of unplugging and replugging things that will not change the code.

## F01-F09 System Fault Reference Table

Compiled from APC documents 990-3889B (BR1200GI/BR1500GI) and 990-91253B (BR650MI/BR900MI/BR1300MI/BR1600MI). Wording differs slightly between the two manuals; both variants are noted where they differ.

| Code | Official fault name | What it means | User-fixable? |
| --- | --- | --- | --- |
| F01 | On-Battery Overload | Load on the Battery Backup outlets exceeded the UPS capacity while running on battery | **Yes** - shed load (see below) |
| F02 | On-Battery Output Short | Short circuit detected on the output while on battery | **Yes** - isolate the shorted device; if shown at power-on, reseat the battery connector |
| F03 | On-Battery Xcap Overload | Internal fault | No - contact APC support |
| F04 | Clamp Short | Internal fault; at power-on it can also indicate the battery is not correctly connected | Reseat the battery and retry once; otherwise contact APC support |
| F05 | Charge Fault (990-3889B) / Charge Status (990-91253B) | Battery charging circuit fault | No - contact APC support |
| F06 | Relay Welding | Internal transfer relay contacts have welded | No - contact APC support |
| F07 | Temperature | Internal over-temperature fault | No - verify ventilation and ambient, then contact APC support |
| F08 | Fan Fault (990-3889B) / Fan Condition (990-91253B, BR1600MI only in that family) | Cooling fan failure | No - contact APC support |
| F09 | Internal Fault (990-3889B) / Internal Error (990-91253B) | General internal hardware fault | No - contact APC support |

A detail worth noting for mixed fleets: in the BR-MI family, the F08 fan fault applies only to the BR1600MI, because it is the model in that family with a fan.

## F01: The Overload You Can Actually Fix

F01 means the equipment plugged into the **Battery Backup outlets** drew more than the UPS could deliver at the moment it transferred to battery. The official corrective action from the manual is simple:

1. Turn the Back-UPS off.
2. Disconnect non-essential equipment from the Battery Backup outlets.
3. Turn the Back-UPS on again.

The classic culprits are laser printers and space heaters. Both draw large surges of current that a small UPS inverter cannot supply, and both belong on the **surge-only outlets** (or a plain wall outlet), never on the battery side. A unit that runs fine on utility power and only faults during an outage is the signature of this failure mode: the wall circuit can source the surge, the inverter cannot.

If the load is genuinely modest and F01 keeps appearing, count what is actually plugged into the battery side. Monitors, external drives, powered speakers, and desk accessories accumulate. Keep the battery outlets for the computer and anything you need alive long enough to shut down cleanly.

## F02: Output Short - Find the Offending Device

F02 while on battery means the UPS detected a short circuit on its output. The official procedure from the 990-91253B manual:

1. Turn the Back-UPS off.
2. Disconnect **all** equipment from the Battery Backup outlets.
3. Turn the Back-UPS on.
4. Reconnect equipment one item at a time, and note which device (or cable) brings the fault back.

Failed power supplies and pinched or damaged IEC cords are the usual finds. Swap the suspect cable first, since it is free to test.

## F02 or F04 at Power-On: Check the Battery Connector First

This is the exception that trips people up. Per Schneider Electric's official FAQ (FAQ000273815), an F02 or F04 shown **when you turn the unit on** - as opposed to during an outage - commonly means the **battery is not correctly connected**. This is common on brand-new units (many ship with the battery connector deliberately disconnected for transport) and after a battery replacement.

The sequence Schneider recommends:

1. Open the battery compartment and firmly reseat the battery connector.
2. Try turning the unit on again.
3. If the code persists, try again with the unit unplugged from the wall.
4. If it still shows F02/F04, contact support - at that point it is a genuine internal fault.

Do not skip step 1 and assume the unit is dead. A half-seated battery connector reproduces these codes exactly.

## F03 Through F09: What "Contact Support" Really Means

F03 (Xcap overload), F04 (clamp short, outside the power-on case above), F05 (charge fault), F06 (relay welding), F07 (temperature), F08 (fan), and F09 (internal fault) are all internal hardware failures. Both official manuals state plainly that these cannot be corrected by the user. There are no board-level repairs APC endorses on a Back-UPS Pro, and the chassis is not designed to be opened in the field.

Two of them deserve a moment of context before you call:

- **F07 (Temperature):** before writing the unit off, confirm the environment. The BR1200GI/BR1500GI manual specifies operation between 0 and 40 C. A UPS jammed into a closed cabinet, buried under paper, or sitting in direct sunlight can run hot enough to fault. Fix the ventilation and ambient conditions; if F07 returns in a proper environment, it is an internal fault and support is the answer.
- **F05 (Charge fault):** if this appeared right after you installed a replacement battery, and that battery was a cheap third-party cartridge rather than the specified APC RBC, the battery itself is a suspect. A failed or incompatible replacement battery can present as a charging fault.

**A plain safety note:** a UPS is a line-powered inverter wrapped around a battery. Capacitors inside can hold a charge even with the unit unplugged and the battery out, and the battery itself can source very high short-circuit current. Nothing inside the case beyond the battery door is user-serviceable. If a code in the F03-F09 range persists after the checks above, stop there and contact APC/Schneider support rather than opening the chassis.

## Clearing the Code: The 2-Second Fault Reset

Once a fault has been identified, pressing and holding the **POWER** button for **2 seconds** clears the visual fault indication and returns the unit to standby (Fault Reset, per manual 990-3889B). Two things to understand about this:

- It clears the **display**, not the cause. An F01 will come straight back on the next outage if the overload is still plugged in.
- It is still worth doing after you have corrected the cause (shed the overload, removed the shorted device, reseated the battery), because it returns the unit to a known state before you re-test.

## Beep and Chirp Patterns Decoded

The audible warnings are separate from the F-codes and mostly indicate normal operating conditions, not faults. From the official BR-GI manual:

| Sound | Meaning | What to do |
| --- | --- | --- |
| Four beeps every 30 seconds | Running on battery - utility power lost or out of range | Save work in progress. Normal behavior, not a fault |
| Continuous beeping | Low battery - remaining runtime is very low | Save work, exit applications, and shut the OS down promptly |
| Continuous tone | Battery Backup outlets are overloaded | Disconnect non-essential equipment until the tone stops |
| Chirps for 1 minute every 5 hours | Battery failed the automatic diagnostic test | Replace the battery |

The 5-hour chirp is the one people live with for months without realizing what it is telling them. It means the battery failed the self-test and should be replaced - and a UPS with a failed battery is just a surge strip with a false sense of security attached.

## Replacement Batteries: Use the Specified RBC

Per the manuals, typical battery service life is 3 to 5 years, and heat shortens it. The specified replacement cartridges:

| Model | Replacement battery cartridge |
| --- | --- |
| BR1200GI / BR1500GI | APCRBC124 |
| BR650MI / BR900MI / BR1300MI / BR1600MI | APCRBC110, APCRBC164, APCRBC165, or APCRBC166 depending on model - check the RBC listed in manual 990-91253B for your exact model |

Using the specified RBC matters here for a diagnostic reason, not just a warranty one: an off-spec battery can produce charge-circuit faults (F05) and power-on battery-connection errors that look exactly like hardware failure.

## Why the Unit Transfers to Battery So Often (Sensitivity)

Frequent transfers to battery are not a fault code, but they wear the battery and often precede the F01 call. On the BR1200GI/BR1500GI (230 V models), the transfer thresholds depend on the configured sensitivity setting:

| Sensitivity | Stays on utility power between |
| --- | --- |
| Low | 156-300 Vac |
| Medium (default) | 176-294 Vac |
| High | 176-288 Vac |

Transfer to battery takes at most 10 ms on these models. If your site has chronically sagging or swelling mains and the unit is constantly clicking over to battery, the sensitivity setting is the first thing to review - a unit on High sensitivity in a building with soft voltage will transfer far more often than one on Low. Equipment that is tolerant of wider voltage swings can run at Low sensitivity and save the battery for real outages.

## Not a Back-UPS Pro? Other APC Families Report Faults Differently

The F01-F09 scheme is specific to the Back-UPS Pro LCD models. If you searched an F-code and your unit does not match:

- **Smart-UPS (SMT/SMX series):** faults are reported through front-panel LED and beep indications and LCD messages - including Site Wiring Fault detection and internal-fault behavior - per APC operation manual 990-3534F.
- **Smart-UPS On-Line (SRT series):** the LCD shows text status and alert messages such as "Disconnected Battery," "Replace Battery," "Output Overload," "Site Wiring Fault," and "Power Sys Error" screens, with red-versus-amber backlight indicating severity, per manual 990-9739.
- **Symmetra LX:** the PowerView display reports plain-text messages with meanings and corrective actions listed in Chapter 4 of manual 990-1546.

Same manufacturer, entirely different fault vocabulary - do not map a Back-UPS F05 onto a Smart-UPS problem or vice versa.

## Frequently Asked Questions

### My brand-new Back-UPS Pro shows F02 or F04 the first time I turn it on. Is it defective?

Probably not. Per Schneider Electric FAQ000273815, F02 or F04 at power-on commonly means the battery is not correctly connected - and new units frequently ship with the battery connector disconnected for transport. Open the battery compartment, seat the connector firmly, and try again. If the code persists even with the unit unplugged from the wall, then contact support.

### Can I clear F03-F09 by unplugging the unit or holding the power button?

Holding POWER for 2 seconds clears the fault display and returns the unit to standby, but for F03-F09 the underlying condition is an internal hardware fault. Both official manuals state these codes cannot be corrected by the user. Expect the code to return, and contact APC/Schneider Technical Support - warranty replacement is the usual resolution.

### Why do I only see F01 during power outages?

Because F01 is specifically an **on-battery** overload. On utility power, the wall circuit supplies your equipment's surges directly. The moment the UPS transfers to battery, the inverter has to supply everything on the Battery Backup outlets by itself, and if the connected load exceeds the unit's capacity, F01 trips. Move high-draw devices (laser printers, heaters) to the surge-only outlets.

### What does the chirping once every few hours mean?

Chirping for about a minute every 5 hours means the battery failed the automatic diagnostic test and should be replaced. Typical service life is 3-5 years per the manual, less in hot environments. Replace with the specified cartridge - APCRBC124 for the BR1200GI/BR1500GI, or the RBC listed for your BR-MI model.

### Is it worth repairing a Back-UPS Pro that shows F06 or F09?

There is no APC-endorsed field repair for these internal faults, and the chassis contains stored energy that makes DIY board work genuinely hazardous. If the unit is in warranty, APC support handles it, typically by replacement. Out of warranty, weigh the support route against replacement - but do not open the case.

## Sources

- APC Back-UPS Pro BR1200GI/BR1500GI 230V Installation and Operation Manual (APC doc EN 990-3889B, 09/2019) - https://media.distributordatasolutions.com/apc/2020q3/documents/885d73f3aac6f5c1965eb953b67ed231734fdf01.pdf
- APC Back-UPS Pro BR650MI/BR900MI/BR1300MI/BR1600MI User Manual (APC doc EN 990-91253B) - https://www.battery-direct.fr/Datenblaetter/apc-back-ups-pro-manual.pdf
- APC Smart-UPS 750/1000/1500/2200/3000 VA 100/120/230 Vac Operation Manual (APC doc 990-3534F) - https://www.sos.state.co.us/pubs/elections/VotingSystems/DVS-DemocracySuite517/documentation/APCSMT1500OpsManual.pdf
- APC Smart-UPS On-Line SRT2200XLA/SRT3000XLA Operation Manual (APC doc 990-9739) - https://www.fullcompass.com/common/files/32312-APCSmartUPSOnLineSeriesUserManual.pdf
- APC Symmetra LX User's Manual (APC doc 990-1546, January 2004) - https://unitedpowerups.com/wp-content/uploads/2017/03/SymmetraLX_UsersManual-1.pdf
- Schneider Electric FAQ FAQ000273815: F02 or F04 Error Code When Turning on Back-UPS - https://www.se.com/us/en/faqs/FAQ000273815/
