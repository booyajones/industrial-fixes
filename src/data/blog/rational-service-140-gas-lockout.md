---
title: "Rational Service 140.4 and 140.8: The Gas Lockout Codes That Block Your Combi Oven From Cooking (SCC, iCombi Pro, iCombi Classic)"
description: "Service 140.4 warns of repeated gas combustion faults on Rational combi ovens; a third trigger within 72 hours produces Service 140.8 and blocks cooking. The official trigger criteria from TI_2220, the critical gas errors behind it (17/18/22/37/38/42), and the per-series service-menu reset paths."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: rational-service-140-gas-lockout
featured: false
draft: false
tags:
  - rational
  - combi-oven
  - oven
  - foodservice
  - commercial-kitchen
  - gas
most_likely_cause: "Repeated hot-air burner ignition faults from gas supply, ignition/ground electrodes, burner, gas valve, gas blower or heat exchanger"
money_part: "Hot-air burner ignition and ground electrodes"
diy_or_pro: "pro"
free_checks:
  - "Confirm the gas shut-off valve feeding the oven is fully open and that other gas appliances on the same line are working normally."
  - "Write down the exact service message, the sub-code (.4 or .8), and how many times Service 140.4 has appeared before calling for service — the trigger history matters."
  - "Stop acknowledging Service 140.4 and continuing to cook. A third trigger within 72 hours escalates to a full Service 140.8 cooking block."
---

## What this code means

Service 140.4 and Service 140.8 are gas combustion supervisory messages that Rational added to its combi ovens by software update, documented in Rational Technical Information TI_2220, "New gas service messages 140." TI_2220 states their purpose plainly: they "serve to protect against damage to the gas combustion system."

They apply to gas units once the unit is running the software that introduced the function:

| Series | Index | Software version |
|---|---|---|
| SelfCookingCenter | Index H and I, from 09/2011 | SCC-07-00-10.6.34 |
| iCombi Pro | Index J, from 05/2020 | LM100-16.3.28 |
| iCombi Classic | Index J, from 05/2020 | LM200-8.0.0 |

The two sub-codes are escalation stages of the same supervisory function, not two different faults:

| Code | Level | What the oven does |
|---|---|---|
| Service 140.4 | Warning levels 1 and 2 | Indicates a fault in the gas combustion system, warns that the unit will be blocked if the fault remains, and instructs you to contact customer service. Cooking still works. |
| Service 140.8 | Warning level 3 and block | Issued after a further trigger within 72 hours. Blocks the unit for cooking and instructs you to contact customer service. Can only be reset by a service technician in the service menu. |

Before the update, an unsuccessful hot-air burner ignition produced a "GAS RESET" message, or the Service 32.1 introduced with the iCombi line, and TI_2220 notes that message "could be acknowledged without restrictions on the number of messages." That is what changed. The fault could always happen; now the oven counts it and eventually stops.

This matters in the field for one practical reason: an oven that ran fine for years can start showing Service 140.4 after a software update. The update did not create the misfires. It made the oven start counting them.

Service 140 is a gas combustion fault. Everything past the free checks below, meaning electrodes, burner, gas valve, gas blower and heat exchanger, is work for a licensed gas technician. Do not open the combustion system yourself, and do not attempt to bypass the lockout.

## The exact trigger criteria

Per TI_2220, the software raises Service 140 when either of two criteria is met:

- **Criterion A:** several gas resets of the hot air system in succession.
- **Criterion B:** a short circuit on the ignition electrodes of the hot air system for at least 60 seconds.

The escalation runs in three steps. Criterion A or B produces the Service 140.4 warning. Another occurrence of criterion A or B within 72 hours produces Service 140.4 again. A further occurrence within 72 hours produces Service 140.8 and blocks the unit from cooking.

TI_2220 carries an explicit notice that the detailed implementation of criterion A **varies between units**, and it spells out the difference:

| Series | Implementation of criterion A |
|---|---|
| iCombi Pro and iCombi Classic | Critical gas error reset 7 times within 32 minutes |
| SelfCookingCenter | Critical gas error reset 4 times, resulting in Service 33.x which requires the unit to be restarted, then critical gas error reset 4 times |

The 7-in-32-minutes figure is not arbitrary. TI_2220 explains it as the maximum number of gas errors permitted by the manufacturer of the automatic ignition controller within that window, and adds that the gas errors must relate to ignition problems in one of the hot air heat exchangers.

Rational puts the whole sequence in practical terms: "A total of 105...120 misfires within 72 h and ignoring the associated service messages is therefore required to generate Service 140.8 and block the unit from operation." This is not a hair trigger. An oven that reaches 140.8 has been failing to light, over and over, for days, with someone acknowledging the warnings each time.

That is also why acknowledging the 140.4 warning and continuing to cook is the wrong move. The warning does not reset the underlying problem. It just delays the block, usually into the middle of a service window when the oven is loaded.

## The critical gas errors behind it

Criterion A counts "critical gas errors." TI_2220 defines exactly which internal gas error codes qualify:

| Critical gas error | Burner system | What TI_2220 says it means |
|---|---|---|
| 17 | Hot air top | Flame current measured 1 s before opening the gas valve |
| 37 | Hot air bottom | Flame current measured 1 s before opening the gas valve |
| 18 | Hot air top | Flame current measured 10 s after closing the gas valve |
| 38 | Hot air bottom | Flame current measured 10 s after closing the gas valve |
| 22 | Hot air top | 5x unsuccessful ignition process |
| 42 | Hot air bottom | 5x unsuccessful ignition process |

These fall into two families. Errors 22 and 42 are straightforward failure to light: the burner tried five times and never established a flame. Errors 17/37 and 18/38 are flame-signal plausibility errors, where the ignition controller sees flame current when there should be none, either just before the valve opens or well after it closed.

Per TI_2220, if Service 140.4 or 140.8 is displayed, the components to check for damage and replace if necessary are:

- Heat exchanger
- Ignition and ground electrode
- Burner
- Gas valve
- Gas blower

TI_2220 also names the upstream conditions that produce this state in the first place: defects or fluctuations in the gas supply, and faulty components in the gas combustion system. It notes that a fluctuating gas supply composition can lead to sub-optimal combustion and damage to combustion system components, and that insufficient gas supply can lead to delayed ignition and noise development.

## What you can check before the service call

None of these involve opening the combustion system, and all of them make the service visit faster:

1. **Confirm the gas supply.** Check that the shut-off valve feeding the oven is fully open. If other gas appliances share the line, check whether they are also struggling. TI_2220 puts gas supply defects and fluctuations at the head of its cause list, and a supply pressure problem can misfire a perfectly healthy burner. If the whole line is suspect, that is a gas-fitter call rather than an oven repair.
2. **Record the history.** Note the exact message, whether it is 140.4 or 140.8, when each warning appeared, and whether it correlates with anything: first cook of the morning, peak load, windy days on roof-terminated flues. The 72-hour escalation logic means the pattern is diagnostic information.
3. **Smell test.** If you smell gas at any point, stop, close the gas shut-off valve to the appliance, ventilate, and follow your gas emergency procedure. Rational's gas service reference gives the same instruction for a confirmed leak: close the gas shut-off valve and look for the cause. Do not keep cycling an appliance that is misfiring and smells of gas.
4. **Stop acknowledging and cooking.** Every additional trigger marches the unit toward the 140.8 block. Book the service call at 140.4, while the oven still cooks.

Everything else, meaning pulling the burner, checking electrode gap and insulation, inspecting the heat exchanger, and testing the gas valve or blower, is licensed-gas-technician work. Rational's own gas service reference (80.51.859) states that the settings and work it describes "may only be carried out by trained service technicians" and instructs "always adhere to the local rules and regulations."

## The reset paths (service technician, after repair)

TI_2220 is explicit: "Service 140.8 can only be reset by service technicians in the service menu." It gives a different path per series:

| Series | Reset path |
|---|---|
| SelfCookingCenter | Diagnosis > Service History > Reset Service 140 |
| iCombi Pro | Gas > Gas Parameters > Reset Service 140 |
| iCombi Classic | Basic Settings > Reset Service 140 |

The reset is the last step, not the fix. If a technician resets Service 140 without finding and repairing the combustion fault, the counters simply start again: the same misfires accumulate, 140.4 comes back, and a further trigger inside 72 hours blocks the oven again. A proper visit is diagnose, repair, verify, then reset.

On verification, Rational's gas service reference sets out when a flue gas analysis is required and what it must show. A flue gas analysis must be carried out after a successful self-test on gas units, and after any gas type change. The document specifies a calibrated analyser capable of reading CO2, O2 and CO, requires the oven door to be kept open during the measurement, and sets maximum CO levels of 400 ppm for steam heating and 150 ppm for any hot air heating system. It also gives permissible dynamic gas pressure ranges of 30 to 57 mbar for liquid gas and 18 to 25 mbar for natural gas, with the warning that the gas valve is damaged internally above 65 mbar.

## Related gas codes you may see alongside

Service 140 counts critical gas errors over time. The oven can also display these gas-side service codes in the same episode.

On the current iCombi Pro and iCombi Classic gas reference (80.51.859), the Service 32 sub-code identifies the **type** of gas error rather than a burner branch, and each sub-code covers all three burner systems:

| Code | Gas errors it covers | Cause per the OEM |
|---|---|---|
| Service 32.1 | 22 hot air top, 32 steam, 42 hot air bottom | 5x unsuccessful ignition process |
| Service 32.2 | 17/18/49 hot air top, 27/28/52 steam, 37/38/55 hot air bottom | Flame current measured with gas valve closed |
| Service 32.3 | 19 hot air top, 29 steam, 39 hot air bottom | Burner went out 5 times during the burning phase |
| Service 32.4 | 20 hot air top, 30 steam, 40 hot air bottom | Speed of the gas blower deviates from the target speed by more than 150 rpm |
| Service 33.1 | — | 7x Service 32.x detected within 32 minutes, or Service 33.x detected for at least 20 hours. Requires restart and, if necessary, reset |
| Service 33.2 / 33.3 | — | Automatic burner control initialised with incorrect gas speeds |
| Service 33.4 | — | Polarity error: phase and neutral conductor reversed |
| Service 33.5 | — | Automatic ignition controller control defective |

Note that the older quick-reference documents map these codes differently, which is a live source of confusion. On the legacy SCC (2004-2011) and SCC whitefficiency references, the Service 32.x and 33.x sub-code is a burner position: 0 is top, 1 is bottom, 2 is both. Check which document matches the unit in front of you before acting on a sub-code.

Two more worth knowing:

| Code | What it means | How to approach it |
|---|---|---|
| Service 32.x (iCombi quick reference) | Ignition box fault. The reference instruction is to close the gas tap, and to "only replace the ignition box if gas errors 33, 36, 39 or 42 have occurred more than 5 times" | Check the error history in the service menu before swapping the box on spec. Licensed gas technician only. |
| Service 60 | Ignition box not initialised, or not initialised quickly. The iCombi references describe an error in the speed signal from the circuit board to the fan burner; the SCC WE reference says check the gas settings | Verify the gas type and settings, switch the unit off and on, use the SD Recovery Software if necessary. Anything beyond settings verification is licensed-gas-technician work. |

There is a useful overlap here. Gas error 42 (5x unsuccessful ignition, hot air bottom) appears both in TI_2220's Service 140 critical-error list and in the "more than 5 times" replacement criterion for the ignition box. An oven throwing Service 140.4 alongside a Service 32.x is telling a coherent story about one failing burner system, and the error history in the service menu is the map.

## When to call a pro

For Service 140.4 and 140.8, effectively immediately. This is a gas combustion system on a commercial appliance. Rational's gas service reference restricts the work to trained service technicians and directs you to local rules and regulations, the OEM requires a flue gas analysis with a calibrated analyser as part of returning a gas unit to service, and the 140.8 reset lives in a service menu that requires service-level access anyway.

Your realistic scope as an operator or in-house maintenance tech is the gas-supply sanity check, the history capture, and making the service call at the 140.4 stage instead of the 140.8 stage. That difference is whether the kitchen still has a working combi oven while it waits for parts.

## Frequently asked questions

### Can I just reset Service 140.8 myself and keep cooking?

No. TI_2220 states that Service 140.8 can only be reset by service technicians in the service menu, and the reset is intended to follow the repair, not replace it. Resetting without a repair only restarts the counters. Rational's own figure is that roughly 105 to 120 misfires inside 72 hours are needed to reach 140.8, so a unit that got there has a real, active combustion problem and will block again. Repeatedly forcing a misfiring gas burner to retry is exactly the situation the block exists to prevent. Do not look for a way around it.

### Why did Service 140.4 appear on an oven that never showed it before?

Because the code did not exist on the oven's previous software. TI_2220 introduced Service 140 by software update (SCC-07-00-10.6.34, iCombi Pro LM100-16.3.28, iCombi Classic LM200-8.0.0). The update did not cause the misfires; it made the oven start counting them. Units with marginal electrodes, supply issues or combustion-side wear that previously just ran a little rough now surface it as a service message.

### Is Service 140 the same as Service 32 or Service 33?

No. Service 32.x and Service 33.x are individual gas faults, and on the current iCombi gas reference the sub-code tells you the error type: 32.1 unsuccessful ignition, 32.2 flame current with the gas valve closed, 32.3 burner going out during the burning phase, 32.4 gas blower speed deviation. Service 140 is a supervisory function that counts critical gas errors (17, 18, 22, 37, 38, 42) over time and escalates from warning to cooking block. You can see them together, and when you do they usually point at the same burner system.

### What is the difference between the 140.4 warning and the 140.8 block?

Occurrence count and time. Either trigger criterion, meaning several successive gas resets of the hot air system or a short circuit on the hot-air ignition electrodes lasting at least 60 seconds, produces the 140.4 warning at warning levels 1 and 2. A further occurrence within 72 hours produces 140.8, which blocks the unit for cooking until a technician repairs the cause and resets Service 140 in the service menu.

### Which Rational models can show Service 140?

Per TI_2220: gas SelfCookingCenter units at Index H and I (from 09/2011), the iCombi Pro at Index J (from 05/2020), and the iCombi Classic at Index J (from 05/2020), once each is on the software version listed in the TI or later. Older units that never receive the update will not show Service 140. On those, an unsuccessful hot-air ignition surfaces the way it always did, as a "GAS RESET" message or, on the iCombi line, as Service 32.1.

## Sources

- RATIONAL Technical Information TI_2220: New gas service messages 140, V02.1 05/2023 (Rational service portal) — https://portal.rational-online.com/fs4p/media/service/3_dokumentationen/technische_infos_1/2022_1/2220/TI_2220_en-GB.pdf
- RATIONAL Service Reference iCombi Pro & iCombi Classic Gas, 80.51.859 V05 10/2025 (Rational service portal) — https://portal.rational-online.com/fs4p/media/service/3_dokumentationen/icombi_pro___icombi_classik/tm_icombi_pro___icombi_classic/en_gb/80.51.859_ServiceReferenz_iCombiProiCombiClassic_Gas_Q_en-GB.pdf
- RATIONAL Service Reference iCombi Pro, 80.51.872_SR-iCombi Pro_en-GB 05/2020 — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-iCombi-Pro-1.pdf
- RATIONAL Service Reference iCombi Classic, 80.51.885_ServiceReferenz_iCombi Classic_en-GB — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/80.51.855-ServiceReferenz-iCombi-Classic-en-GB-1.pdf
- RATIONAL Service Reference SelfCookingCenter whitefficiency / CombiMaster Plus, 80.51.720_SR_en 11/2017 — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCCWE-CM_P-1.pdf
- RATIONAL Service Reference SCC / CombiMaster 2004-2011, 80.51.028-A4 Edition 09/2008 — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCC-CM-1.pdf
