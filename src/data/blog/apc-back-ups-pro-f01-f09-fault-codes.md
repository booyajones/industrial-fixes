---
title: "APC Back-UPS Pro F01-F09 Fault Codes: Official Meanings, Beep Patterns, and Fixes"
description: "The official APC F01-F09 System Fault table for Back-UPS Pro, cross-checked against four Schneider Electric sources. F01 and F02 are the only codes with a published user action; F03-F09 are contact-support faults. Plus beep patterns, the 2-second fault reset, and the exact RBC part number per model."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: apc-back-ups-pro-f01-f09-fault-codes
featured: false
draft: false
tags:
  - apc
  - ups
  - electrical
  - power-quality
most_likely_cause: "F01: too much load on the Battery Backup outlets at the moment the UPS transferred to battery. F02: a shorted device or damaged cable on the Battery Backup outlets."
money_part: "Replacement battery cartridge: APCRBC124 (BR1200GI/BR1500GI), APCRBC110 (BR650MI), APCRBC164 (BR900MI), APCRBC165 (BR1300MI), APCRBC166 (BR1600MI)"
free_checks:
  - "Move non-essential equipment off the Battery Backup outlets and onto the surge-only outlets"
  - "For F02, disconnect everything from the Battery Backup outlets, restart, then reconnect one item at a time"
  - "After correcting the cause, hold POWER for 2 seconds to clear the fault display"
---

## APC Back-UPS Pro F01-F09 - What These Codes Mean

When an APC Back-UPS Pro detects a problem it illuminates a **System Fault** (or, in newer wording, **Detected System Error**) icon on the LCD together with a number from **F01 to F09**.

The table below is not reconstructed from forum posts. It is cross-checked against four Schneider Electric sources that each publish the same numbering:

- **APC document 990-3889B** (09/2019), the Back-UPS Pro BR1200GI / BR1500GI 230 V installation and operation manual, which calls the section *System Faults*.
- **APC document 990-91253B**, the Back-UPS Pro BR650MI / BR900MI / BR1300MI / BR1600MI manual, which calls it *Detected System errors*.
- **Schneider Electric FAQ000264323**, the current support article for Back-UPS Pro BR 1000/1350/1500 MS/MS2 and Back-UPS Pro BN 1100/1350/1375/1400/1500 M2 and M2-CA models.
- **APC document 990-4994A**, the Back-UPS BX1300LCD-CN / BX1500LCD-CN manual, which prints the same F01-F09 numbering on a non-Pro model (its only wording difference is F05, printed there as "Charger Fault").

The single most useful thing to know before you touch anything: **only F01 and F02 carry a published corrective action.** All three of the Back-UPS Pro sources state, in almost identical words, that errors F03 through F09 cannot be corrected by the user and that you should contact Schneider Electric (APC) technical support. If the unit is in warranty, replacement is the usual outcome. Knowing that up front saves you an afternoon of unplugging things that will not change the code.

One published-erratum note, because it confuses people who read the manual carefully: the 990-3889B System Faults table is introduced with the line "For faults F01 and F02, contact APC Technical Support," yet the same table then prints a user corrective action for F01 and F02 and says F03-F09 cannot be corrected by the user. The BR-MI manual and FAQ000264323 both phrase it the other way round ("Except for errors F01 and F02, contact ... Technical Support"), which is the reading consistent with the table itself.

## F01-F09 System Fault Reference Table

Wording differs slightly between documents; both variants are given where they differ.

| Code | Official fault name | What it means | Published user action? |
| --- | --- | --- | --- |
| F01 | On-Battery Overload | The load on the Battery Backup outlets exceeded what the UPS could deliver while running on battery | **Yes** - shed load (see below) |
| F02 | On-Battery Output Short | A short circuit was detected on the output while on battery | **Yes** - isolate the offending load (see below) |
| F03 | On-Battery Xcap Overload (also printed "XCap") | Internal fault | No - contact APC/Schneider support |
| F04 | Clamp Short | Internal fault | No - contact APC/Schneider support |
| F05 | Charge Fault (990-3889B) / Charge Status (990-91253B) / Charge Error (FAQ000264323) | Battery charging circuit fault | No - contact APC/Schneider support |
| F06 | Relay Welding | Internal transfer relay contacts have welded | No - contact APC/Schneider support |
| F07 | Temperature | Over-temperature fault | No - contact APC/Schneider support |
| F08 | Fan Fault (990-3889B) / Fan Condition, for BR1600MI only (990-91253B) | Cooling fan fault | No - contact APC/Schneider support |
| F09 | Internal Fault (990-3889B) / Internal Error (990-91253B) | General internal hardware fault | No - contact APC/Schneider support |

Two model-scope details worth carrying into a mixed fleet:

- In the BR-MI family, 990-91253B prints F08 as **"Fan Condition (for BR1600MI only)"**. On the other three models in that manual the code is not listed.
- FAQ000264323, covering the BR/BN MS/MS2/M2/M2-CA models, lists F01-F07 and F09 and **omits F08 entirely**, while still stating that errors F03-F09 are not user-correctable.

## F01: The Overload You Can Actually Fix

F01 means the equipment plugged into the **Battery Backup outlets** drew more than the UPS could deliver at the moment it transferred to battery. The corrective action published in 990-3889B and 990-91253B is the same three steps:

1. Turn the Back-UPS off.
2. Disconnect non-essential equipment from the Battery Backup outlets.
3. Turn the Back-UPS on again.

The signature of this failure mode is a unit that runs fine on utility power and only faults during an outage: the wall circuit can source a surge that the inverter cannot. High-draw equipment belongs on the **surge-only outlets** or a plain wall outlet. Both manuals make the same point from the other direction in their troubleshooting tables: when the Back-UPS "does not provide the expected amount of backup time," the listed cause is that the Battery Backup outlets are fully or improperly loaded, and the listed fix is to move that equipment to the surge outlets.

If the load is genuinely modest and F01 keeps appearing, count what is actually on the battery side. Monitors, external drives, powered speakers and desk accessories accumulate.

## F02: Output Short - Find the Offending Device

F02 while on battery means the UPS detected a short circuit on its output. 990-91253B and FAQ000264323 publish a fuller isolation procedure than the GI manual does:

1. Turn the Back-UPS off.
2. Disconnect **all** equipment from the Battery Backup outlets.
3. Turn the Back-UPS on.
4. Reconnect equipment one item at a time. If the output trips again, disconnect the device that caused the error.

Failed power supplies and pinched or damaged cords are the usual finds. Swap the suspect cable first, since it costs nothing to test.

## About F02 or F04 at Power-On: Read the Model Scope Carefully

Schneider publishes **FAQ000273815, "F02 or F04 Error Code When Turning on Back-UPS,"** which states that if the battery has not been correctly connected to the UPS, the unit may display an F02 or F04 error code when it is turned on. Its published sequence is:

1. Ensure the battery connectors in the Back-UPS are firmly connected to the battery, and try turning it on again.
2. If it still shows F02 or F04, turn the UPS off and unplug it from the wall socket.
3. With the power cord removed from the wall, try turning it on again.
4. If it still displays the error code, contact customer support.

**The scope matters, and this is where most write-ups go wrong.** Schneider tags that FAQ to the Back-UPS models **BN1350M2, BN1500M2 and BX1500M**. It is not published against the Back-UPS Pro BR-GI or BR-MI families, and neither BR manual lists a battery-connection cause for F02 or F04. In the BR documents F04 is "Clamp Short," flatly listed as not user-correctable.

So: if you own a BN or BX unit in that list, the reseat-the-connector step is the documented first move. If you own a BR-series Back-UPS Pro, treat it as a reasonable but undocumented thing to check rather than the official answer, and do not let it stop you from reporting an F04 to support.

What *is* documented for BR units is adjacent and useful:

- 990-91253B states plainly that **"The UPS is shipped with the battery disconnected,"** and the manuals include a "Connect the Battery" installation step. A brand-new unit that will not start is very often simply not connected yet.
- Both BR manuals list "The internal battery is not connected" as a cause under **"Back-UPS will not switch on,"** with the corrective action "Connect the battery."
- On the BR-MI models, a disconnected battery has its own distinct indication and is not an F-code at all: **chirps every 2 seconds with the Load Capacity bar flashing.**

## F03 Through F09: What "Contact Support" Really Means

F03 (Xcap overload), F04 (clamp short), F05 (charge fault), F06 (relay welding), F07 (temperature), F08 (fan) and F09 (internal fault) are internal hardware failures. All three Back-UPS Pro sources state that these cannot be corrected by the user.

One piece of genuine context before you call about **F07 (Temperature)**: confirm the environment first. 990-3889B specifies an operating temperature of **0 to 40 C (32 to 104 F)**, and both manuals instruct that the air vents must not be blocked and that adequate space be allowed for ventilation. A UPS in a closed cabinet, buried under paper, or in direct sunlight is outside its published operating conditions. Fixing that is not APC's listed corrective action for F07, but it is a condition worth correcting regardless before you conclude the hardware has failed.

**Safety, in the manufacturer's own words.** The 990-91253B safety section carries a **DANGER** notice headed "HAZARD OF ELECTRIC SHOCK, EXPLOSION, OR ARC FLASH," and states that servicing of batteries should be performed or supervised by personnel knowledgeable about batteries and the required precautions, that a battery can present a risk of electric shock and burns by high short-circuit current, and that failed batteries can reach temperatures exceeding the burn thresholds for touchable surfaces. It closes with "Failure to follow these instructions will result in death or serious injury." The same manual carries a separate **CAUTION** for battery replacement headed "RISK OF HYDROGEN SULPHIDE GAS AND EXCESSIVE SMOKE," which instructs you to replace the battery immediately if the UPS indicates a battery over-temperature condition or if there is evidence of electrolyte leakage: power off the UPS, unplug it from the AC input, disconnect the batteries, and do not operate the UPS until the batteries have been replaced.

Take that at face value. If a code in the F03-F09 range persists after the checks above, stop and contact APC/Schneider support rather than opening the chassis. Both manuals' service instructions say the same thing: do not return the unit to the dealer, work through troubleshooting, then contact technical support for an RMA.

## Clearing the Code: The 2-Second Fault Reset

Both manuals document a two-second button hold to clear the fault display:

- 990-3889B calls it **Fault Reset**: with the unit in a fault state, "After a fault has been identified, press POWER to remove the visual indication and return to standby status" (2 seconds).
- 990-91253B calls it **Status Reset**: "After an error has been detected and identified, press POWER to remove the visual indication and return to standby status" (2 seconds).

Note what both sentences actually say: it removes the *visual indication*. It does not repair anything. An F01 will return on the next outage if the overload is still plugged in. It is still worth doing after you have corrected the cause, because it returns the unit to a known state before you re-test.

## Beep and Chirp Patterns Decoded

The audible warnings are separate from the F-codes, and **they are not the same between the two Back-UPS Pro families.** This is a real difference, not a wording variation, so check which table applies to your unit.

BR1200GI / BR1500GI, per 990-3889B:

| Sound | Meaning |
| --- | --- |
| Four beeps every 30 seconds | Running on battery. Consider saving any work in progress |
| Continuous beeping | Low battery condition and battery runtime is very low. Save work, exit applications, shut down the OS |
| Continuous tone | Battery Backup outputs are overloaded |
| Chirps for 1 minute every 5 hours | Battery failed the automatic diagnostic test and should be replaced |

BR650MI / BR900MI / BR1300MI / BR1600MI, per 990-91253B:

| Sound | Meaning |
| --- | --- |
| Four beeps every 30 seconds | Running on battery. Consider saving any work in progress |
| Continuous beeping | Low battery condition and battery runtime is very low |
| Continuous tone | Battery Backup outputs are overloaded |
| Chirps every 2 seconds, Load Capacity bar flashing | Battery is disconnected |
| Continuous chirping, Load Capacity bar and Replace Battery icon alternately flashing | Battery did not pass the automatic diagnostic test and should be replaced as early as possible. Pressing MUTE pauses the chirping |

The failed-self-test chirp is the one people live with for months without realising what it is telling them. A UPS with a failed battery is a surge strip with a false sense of security attached.

## Replacement Batteries: Use the Specified RBC

Both manuals state that the battery typically lasts three to five years, and both name the environmental factors that shorten it: elevated ambient temperatures, poor quality AC power, and frequent short-duration discharges (990-3889B) or frequent outages and elevated temperatures (990-91253B). 990-91253B additionally instructs that the battery be replaced at least every 5 years or at the end of its service life, whichever is earlier.

| Model | Replacement battery cartridge |
| --- | --- |
| BR1200GI / BR1500GI | APCRBC124 |
| BR650MI | APCRBC110 |
| BR900MI | APCRBC164 |
| BR1300MI | APCRBC165 |
| BR1600MI | APCRBC166 |

990-3889B also instructs that the used battery be replaced with an APC by Schneider Electric approved battery and delivered to a recycling facility.

## Why the Unit Transfers to Battery So Often (Sensitivity)

Frequent transfers are not a fault code, but they wear the battery and often precede the F01 call. On the BR1200GI/BR1500GI, the sensitivity setting (POWER held for six seconds with the unit off) selects the input window the UPS will tolerate before switching to battery:

| Sensitivity | Stays on utility power between | 990-3889B guidance |
| --- | --- | --- |
| Low | 156-300 Vac | Input voltage is extremely low or high. Not recommended for computer loads |
| Medium (default) | 176-294 Vac | The Back-UPS frequently switches to battery power |
| High | 176-288 Vac | The connected equipment is sensitive to voltage fluctuations |

For reference, the same manual gives the BR1200GI/BR1500GI online input voltage range as 176-294 V and transfer time as **10 ms maximum**. Note APC's own caution above: Low sensitivity is explicitly not recommended for computer loads, so widening the window to stop nuisance transfers is a trade-off, not a free fix.

## Not a Back-UPS Pro? Other APC Families Report Faults Differently

The F01-F09 scheme belongs to the Back-UPS and Back-UPS Pro LCD models. If you searched an F-code and your unit does not match:

- **Smart-UPS 750/1000/1500/2200/3000 VA (100/120/230 Vac) and 500 VA (100 Vac)**, per operation manual 990-3534F: no F-codes. Faults surface through front-panel LEDs (Online, On Battery, Site Wiring Fault, Replace Battery) plus display messages. An internal fault is handled bluntly: "Do not attempt to use the UPS. Unplug the UPS and have it serviced immediately." A site wiring fault covers missing ground, hot-neutral, polarity reversal and overloaded neutral circuit, is applicable to 120 V units only, and the published action is to have a qualified electrician inspect the building wiring.
- **Smart-UPS On-Line SRT2200XLA / SRT3000XLA (120 Vac)**, per operation manual 990-9739: plain-text LCD alerts such as "Disconnected Battery," "Replace Battery," "Output Overload," "Site Wiring Fault" and "Power Sys Error - 00100." The backlight encodes severity: red indicates an alarm requiring immediate attention, amber an alarm requiring attention.
- **Symmetra LX**, per operations manual 990-1546: plain-text PowerView messages, listed with meanings and corrective actions in Chapter 4.

Same manufacturer, entirely different fault vocabularies. Do not map a Back-UPS F05 onto a Smart-UPS problem or vice versa.

## Frequently Asked Questions

### My Back-UPS shows F02 or F04 the first time I turn it on. Is it defective?

Check which model you have first. Schneider's FAQ000273815 says an F02 or F04 at power-on can mean the battery is not correctly connected, and its published fix is to reseat the battery connector, then retry once with the unit unplugged from the wall, then contact support. That FAQ is tagged to the BN1350M2, BN1500M2 and BX1500M models. On a Back-UPS Pro BR unit the manuals do not document that cause, so verify the battery is connected (990-91253B confirms the UPS ships with the battery disconnected) and then treat a persistent F04 as the internal fault the manual says it is.

### Can I clear F03-F09 by holding the power button?

Holding POWER for 2 seconds removes the visual fault indication and returns the unit to standby, but that is all it does. For F03-F09 the underlying condition is an internal hardware fault that all three official Back-UPS Pro sources say cannot be corrected by the user. Expect the code to return, and contact technical support.

### Why do I only see F01 during power outages?

Because F01 is specifically an **on-battery** overload. On utility power the wall circuit supplies your equipment directly. The moment the UPS transfers to battery, the inverter has to supply everything on the Battery Backup outlets by itself, and if the connected load exceeds capacity, F01 trips. Move high-draw devices to the surge-only outlets.

### What does the chirping every few hours mean?

On a BR1200GI/BR1500GI, chirping for one minute every 5 hours means the battery failed the automatic diagnostic test and should be replaced. On the BR-MI models the failed-test indication is continuous chirping with the Load Capacity bar and Replace Battery icon flashing alternately, while chirps every 2 seconds with the Load Capacity bar flashing means the battery is disconnected. Replace with the cartridge listed for your exact model.

### Is it worth repairing a Back-UPS Pro that shows F06 or F09?

The manuals publish no field repair for these, and the safety section warns of electric shock, explosion or arc flash hazard and of a battery that can deliver very high short-circuit current. If the unit is in warranty, support handles it. Out of warranty, weigh the support route against replacement, but do not open the case.

## Sources

Every URL below was retrieved and read while writing this page.

- APC Back-UPS Pro BR1200GI/BR1500GI 230 V Installation and Operation Manual (APC doc EN 990-3889B, 09/2019): https://media.distributordatasolutions.com/apc/2020q3/documents/885d73f3aac6f5c1965eb953b67ed231734fdf01.pdf
- APC Back-UPS Pro BR650MI/BR900MI/BR1300MI/BR1600MI User Manual (APC doc EN 990-91253B): https://www.battery-direct.fr/Datenblaetter/apc-back-ups-pro-manual.pdf
- Schneider Electric FAQ000264323, "What are the basic troubleshooting steps for the Back-UPS Pro BR/BN MS/MS2/M2/M2-CA models?": https://www.se.com/us/en/faqs/FAQ000264323/
- Schneider Electric FAQ000273815, "F02 or F04 Error Code When Turning on Back-UPS" (tagged BN1350M2, BN1500M2, BX1500M): https://www.se.com/us/en/faqs/FAQ000273815/
- APC Back-UPS BX1300LCD-CN / BX1500LCD-CN User Manual (APC doc 990-4994A), hosted by Schneider Electric: https://download.schneider-electric.com/files?p_Doc_Ref=SPD_JHSH-74ABL6_EN
- APC Smart-UPS 750/1000/1500/2200/3000 VA 100/120/230 Vac Operation Manual (APC doc 990-3534F): https://www.sos.state.co.us/pubs/elections/VotingSystems/DVS-DemocracySuite517/documentation/APCSMT1500OpsManual.pdf
- APC Smart-UPS On-Line SRT2200XLA/SRT3000XLA Operation Manual (APC doc 990-9739): https://www.fullcompass.com/common/files/32312-APCSmartUPSOnLineSeriesUserManual.pdf
- APC Symmetra LX Operations Manual, 200/208/230 V, 4-16 kVA (APC doc 990-1546, January 2004): https://unitedpowerups.com/wp-content/uploads/2017/03/SymmetraLX_UsersManual-1.pdf
