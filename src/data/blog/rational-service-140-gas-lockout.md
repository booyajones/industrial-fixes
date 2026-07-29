---
title: "Rational Service 140.4 and 140.8: The Gas Lockout Codes That Block Your Combi Oven From Cooking (SCC, iCombi Pro, iCombi Classic)"
description: "Service 140.4 warns of repeated gas ignition failures on Rational combi ovens; a third event within 72 hours triggers Service 140.8 and blocks cooking entirely. The official trigger criteria, the critical gas errors behind it (17/18/22/37/38/42), and the per-series service-menu reset paths."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: rational-service-140-gas-lockout
featured: false
draft: true
tags:
  - rational
  - combi-oven
  - oven
  - foodservice
  - commercial-kitchen
  - gas
most_likely_cause: "Repeated hot-air burner ignition failures from gas supply, ignition/ground electrodes, burner, gas valve, or gas blower"
money_part: "Hot-air burner ignition and ground electrodes"
diy_or_pro: "pro"
free_checks:
  - "Confirm the gas shut-off valve feeding the oven is fully open and that other gas appliances on the same line are working normally."
  - "Write down the exact service message, the sub-code (.4 or .8), and how many times Service 140.4 has appeared before calling for service — the trigger history matters."
  - "Stop acknowledging Service 140.4 and continuing to cook. A third trigger within 72 hours escalates to a full Service 140.8 cooking lockout."
---

## What this code means

Service 140.4 and Service 140.8 are gas combustion supervisory messages that Rational added to its combi ovens by software update, documented in Rational Technical Information TI_2220 ("New gas service messages 140"). They apply to gas versions of the SelfCookingCenter (units built from 09/2011 onward), the iCombi Pro, and the iCombi Classic once the unit is running the software that introduced the function:

- SelfCookingCenter: SCC-07-00-10.6.34
- iCombi Pro: LM100-16.3.28
- iCombi Classic: LM200-8.0.0

The two sub-codes are escalation stages of the same fault, not two different faults:

| Code | Level | What the oven does |
|---|---|---|
| Service 140.4 | Warning | The unit has detected repeated hot-air burner ignition failures. It displays a warning that the unit will be blocked if the fault persists and instructs you to contact customer service. Cooking still works. |
| Service 140.8 | Cooking lockout | The trigger condition occurred a third time within 72 hours. The unit is blocked from cooking entirely and stays blocked until a service technician resets Service 140 in the service menu — after repairing the cause. |

This matters for two reasons. First, an oven that ran fine for years can suddenly start showing Service 140.4 after a software update — the burner problem was already there, but older software never counted it. Second, because these codes only exist on 2022-era and later software, most third-party code lists don't include them at all, and a tech who has never seen one can lose a day figuring out why a combi oven refuses to cook with no obvious hard fault.

Service 140 is a gas combustion fault. Everything past the free checks below — electrodes, burner, gas valve, gas blower, heat exchanger — is work for a licensed gas technician. Do not open the combustion system yourself.

## The exact trigger criteria

Per TI_2220, the software raises Service 140 when either of two criteria is met:

- **Criterion A:** 7 consecutive critical gas errors within 32 minutes.
- **Criterion B:** a short circuit on the hot-air ignition electrodes lasting at least 60 seconds.

The first and second occurrences produce the Service 140.4 warning. The **third occurrence of criterion A or B within 72 hours** produces Service 140.8 and blocks cooking. Rational's technical information puts that in practical terms as roughly 105 to 120 misfires within 72 hours before the unit locks out — this is not a hair trigger. An oven that reaches 140.8 has been failing to light, over and over, for days.

That is also why acknowledging the 140.4 warning and continuing to cook is the wrong move. The warning does not reset the underlying problem; it just delays the lockout, usually into the middle of a service window when the oven is loaded.

## The critical gas errors behind it

Criterion A counts "critical gas errors." TI_2220 defines exactly which internal gas errors qualify, in top/bottom burner pairs:

| Critical gas error | Burner | What it means |
|---|---|---|
| 17 | Top | Flame current detected 1 second before the gas valve opens |
| 37 | Bottom | Flame current detected 1 second before the gas valve opens |
| 18 | Top | Flame current still present 10 seconds after the gas valve closes |
| 38 | Bottom | Flame current still present 10 seconds after the gas valve closes |
| 22 | Top | 5x unsuccessful ignition |
| 42 | Bottom | 5x unsuccessful ignition |

These fall into two families. Errors 22/42 are straightforward failure to light — the burner tried five times and never established a flame. Errors 17/37 and 18/38 are flame-signal plausibility errors: the ignition box sees flame current when there should be none (before the valve opens, or long after it closed). A flame signal at the wrong time points at the ignition/ground electrodes, their insulation and grounding, or combustion-side damage — which is exactly the parts list Rational gives for Service 140.

Per TI_2220, the underlying causes to investigate are:

- Fluctuating or insufficient gas supply
- Damaged heat exchanger
- Ignition electrode or ground electrode
- Burner
- Gas valve
- Gas blower

## What you can check before the service call

None of these involve opening the combustion system, and all of them make the service visit faster:

1. **Confirm the gas supply.** Check that the shut-off valve feeding the oven is fully open. If other gas appliances share the line, check whether they are also struggling — a supply pressure problem (a failing regulator, an undersized line under peak load, an LP tank running low) can misfire a perfectly healthy burner. If the whole line is suspect, that is a plumber/gas-fitter call, not an oven repair.
2. **Record the history.** Note the exact message, whether it is 140.4 or 140.8, when each warning appeared, and whether it correlates with anything (first cook of the morning, peak load, windy days for roof-terminated flues). The 72-hour/third-occurrence logic means the pattern is diagnostic information.
3. **Smell test.** If you smell gas at any point, stop, close the gas tap to the appliance, ventilate, and follow your gas emergency procedure. Do not keep cycling an appliance that is misfiring and smells of gas.
4. **Stop acknowledging and cooking.** Every additional trigger marches the unit toward the 140.8 lockout. Book the service call at 140.4, while the oven still cooks.

Everything else — pulling the burner, checking electrode gap and insulation, inspecting the heat exchanger, testing the gas valve or blower — is licensed-gas-technician work, and Rational's own documentation requires a flue gas analysis after any gas-side repair.

## The reset paths (service technician, after repair)

Service 140.8 does not clear with a power cycle, and it does not clear from the customer-facing acknowledgment. Per TI_2220 it is reset by a service technician in the service menu, with a different path per series:

| Series | Reset path |
|---|---|
| SelfCookingCenter | Diagnosis > Service History > Reset Service 140 |
| iCombi Pro | Gas > Gas Parameters > Reset Service 140 |
| iCombi Classic | Basic Settings > Reset Service 140 |

The reset is the last step, not the fix. If a technician resets Service 140 without finding and repairing the combustion fault, the counters simply start again: the same misfires accumulate, 140.4 comes back, and the third trigger inside 72 hours locks the oven out again — typically within days on a burner that is genuinely failing. A proper visit is: diagnose the combustion system (gas supply, electrodes, burner, gas valve, gas blower, heat exchanger), repair, verify with a flue gas analysis, then reset Service 140.

## Related gas codes you may see alongside

Service 140 counts internal gas errors, but the oven can also display these gas-side service codes in the same episode. From the official Rational service references:

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| Service 32.x | Gas ignition box fault. The x identifies the burner branch (legacy/whitefficiency units: 0 = top, 1 = bottom, 2 = both; iCombi: branch number). | Internal ignition box fault, or repeated upstream gas errors. | Close the gas tap and call a licensed gas technician. Rational's instruction is specific: only replace the ignition box if gas errors 33, 36, 39, or 42 have occurred more than 5 times — check the error history first rather than swapping the box on spec. |
| Service 33.x | Gas burner error on burner branch x — gas tap, gas valve, or the ignition-box-to-gas-valve control circuit. | Gas supply off, gas valve fault, or wiring between the ignition box and the gas valve. | Confirm the gas supply is open. Beyond that, a licensed gas technician checks the gas valve and the ignition-box control circuit, with a flue gas analysis after any gas repair per the OEM. |
| Service 60 | Ignition box not initialised, or not initialised quickly — an error in the speed signal from the circuit board to the fan burner. | Wrong gas settings after board or software work, a speed-signal fault to the gas blower, or ignition box initialisation failure. | Verify the gas type/settings, switch the unit off and on, and use the SD Recovery Software if necessary. Anything beyond settings verification is licensed-gas-technician work. |

The overlap is worth understanding: gas error 42 (5x unsuccessful ignition, bottom burner) appears both in the Service 140 critical-error list and in the "more than 5 times" replacement criterion for the ignition box under Service 32.x. An oven throwing Service 140.4 alongside Service 32.x or 33.x is telling a coherent story about one failing burner branch, and the error history in the service menu is the map.

## When to call a pro

For Service 140.4 and 140.8, effectively immediately. This is a gas combustion system on a commercial appliance: diagnosis and repair of the burner, ignition and ground electrodes, gas valve, gas blower, and heat exchanger belong to a licensed gas technician (in most jurisdictions this is a legal requirement, not just a recommendation), the OEM requires a flue gas analysis after gas-side repairs, and the 140.8 reset lives in the service menu anyway. Your realistic scope as an operator or in-house maintenance tech is the gas-supply sanity check, the history capture, and making the service call at the 140.4 stage instead of the 140.8 stage — that difference is whether the kitchen still has a working combi oven while waiting for parts.

## Frequently asked questions

### Can I just reset Service 140.8 myself and keep cooking?

The reset is in the service menu and is intended for service technicians after the combustion fault is repaired. Even where a menu path is reachable, resetting without a repair only restarts the counters: the oven needs roughly 105 to 120 misfires inside 72 hours to lock out, so a unit that reached 140.8 has a real, active combustion problem and will lock out again. Repeatedly forcing a misfiring gas burner to retry is exactly the situation the lockout exists to prevent.

### Why did Service 140.4 appear on an oven that never showed it before?

Because the code did not exist on the oven's previous software. TI_2220 introduced Service 140 by software update (SCC-07-00-10.6.34, iCombi Pro LM100-16.3.28, iCombi Classic LM200-8.0.0). An update did not cause the misfires — it made the oven start counting them. Units with marginal electrodes, supply issues, or combustion-side wear that previously just cooked a little rough now surface it as a service message.

### Is Service 140 the same as Service 32 or Service 33?

No. Service 32.x is an ignition box fault and Service 33.x is a gas burner/gas valve error on a specific burner branch — individual hard faults. Service 140 is a supervisory function that counts critical gas errors (17/18/22 top, 37/38/42 bottom) over time and escalates from warning (140.4) to cooking lockout (140.8). You can see them together, and when you do, they usually point at the same burner branch.

### What is the difference between the 140.4 warning and the 140.8 lockout?

Occurrence count and time. Either trigger criterion — 7 consecutive critical gas errors within 32 minutes, or a 60-second-plus short circuit on the hot-air ignition electrodes — produces the 140.4 warning on the first and second occurrence. The third occurrence within 72 hours produces 140.8 and blocks cooking until a technician repairs the cause and resets Service 140 in the service menu.

### Which Rational models can show Service 140?

Gas units of the SelfCookingCenter built from 09/2011 onward, the iCombi Pro, and the iCombi Classic — once they are on the software versions listed in TI_2220 or later. Older units that never receive the update will not show Service 140, but they can still show the underlying gas faults as Service 32.x, 33.x, or 60.

## Sources

- RATIONAL Technical Information TI_2220: New gas service messages 140 (V02.1, 05/2023) — https://portal.rational-online.com/fs4p/media/service/3_dokumentationen/technische_infos_1/2022_1/2220/TI_2220_en-GB.pdf
- RATIONAL Service Reference iCombi Pro (doc 80.51.872_SR-iCombi Pro_en-GB, 05/2020) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-iCombi-Pro-1.pdf
- RATIONAL Service Reference iCombi Classic (doc 80.51.855, en-GB) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/80.51.855-ServiceReferenz-iCombi-Classic-en-GB-1.pdf
- RATIONAL Service Reference SelfCookingCenter whitefficiency / CombiMaster Plus (doc 80.51.720_SR_en, 11/2017) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCCWE-CM_P-1.pdf
- RATIONAL Service Reference SCC / CombiMaster 2004-2011 (doc 80.51.028-A4, 09/2008) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCC-CM-1.pdf
- Parts Town — Rational Combi Oven Error Codes — https://www.partstown.com/cm/resource-center/guides/gd2/rational-combi-oven-error-codes
- General Parts — Top 5 Rational Error Codes — https://generalparts.com/top-5-rational-error-codes-and-what-they-mean-to-you/
