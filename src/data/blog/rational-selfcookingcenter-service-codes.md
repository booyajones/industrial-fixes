---
title: "Rational SelfCookingCenter Service Codes: Complete SCC WE and Legacy SCC Reference (Service 10-120, E-Codes, Calibration Errors)"
description: "Verified Rational SelfCookingCenter service codes straight from the OEM service references: SCC WE Service 10-63, legacy SCC 2004-2011 codes, the Service 20.x thermocouple bitmask, CleanJet faults, and the gas Service 140.4/140.8 lockout, plus the series differences most code lists get wrong."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: rational-selfcookingcenter-service-codes
featured: false
draft: true
tags:
  - rational
  - oven
  - combi-oven
  - foodservice
  - commercial-kitchen
money_part: "Level electrode"
free_checks:
  - "Confirm the water shut-off valve is fully open and supply pressure is present before chasing Service 12 or Service 25"
  - "Run the drain pump in the function test and watch for actual flow before replacing parts on a Service 10"
  - "Check the pump-off hose for kinks or blockage"
  - "Confirm the GN racks or mobile trolley are in the cabinet before starting a CleanJet cycle"
---

## Rational SelfCookingCenter Service Codes — What They Mean

Rational combi ovens report faults as numbered "Service" messages on the display. The numbers look identical across generations, but the meanings do not always carry over, and that is where most online code lists go wrong. Rational has published a separate official service reference for each platform, and the correct first step on any Service code is identifying which platform you are standing in front of.

The four OEM quick references this guide is built on:

| Platform | OEM service reference | Codes it lists |
|---|---|---|
| SCC / CombiMaster, 2004-2011 (legacy) | Doc 80.51.028-A4 (09/2008) | Service 10-44, 100, 110, 120 |
| SCC whitefficiency (SCC WE) / CombiMaster Plus | Doc 80.51.720 (11/2017) | Service 10-63, 110, 120; calibration errors 10/20/100/200; gas error displays; motor blink codes |
| iCombi Pro | Doc 80.51.872 (05/2020) | Service 10-121 with sub-code bitmasks; diagnostic LED codes 1-8; calibration errors |
| iCombi Classic | Doc 80.51.855 | Service 2-121 plus Classic-only display codes 1000-1033.x, 2000, 201, 90 |

The older CombiMaster (non-Plus) line uses E-codes (E1-E24) rather than Service numbers; Parts Town's distributor guide covers those separately.

According to General Parts, an authorized Rational service company, the codes technicians actually call about most are Service 10, Service 12, Service 25, Service 40, and the gas RESET message. Four of those five are water-related, which tells you a lot about what actually fails on these ovens: water supply, scale, and the drain path.

## Quick Reference: Verified Service Codes

Every meaning below is taken from the official Rational service references (or, where noted, an authorized distributor guide). Codes not listed here are covered in the "codes we have not decoded" section rather than guessed at.

| Code | What it means | Applies to |
|---|---|---|
| Service 10 | SC pump / steam generator drain fault (pump, water box, pump-off hose, level electrode) | All series |
| Service 11 | Level electrode / fill-path fault; SCC WE: venting valve above steam generator leaking; iCombi adds CDS flow rate, I/O board | SCC WE, iCombi |
| Service 12 | CDS water-metering sensor gives no output signal | All series |
| Service 13 | Change water level electrode | All series |
| Service 14 | Water conductivity too low for the level electrode to detect | All series |
| Service 16 | Flash new software / software update of the board | SCC WE, iCombi |
| Service 17 | Inform Rational; use Recovery Software (flash or change SD card on SCC WE) | SCC WE, iCombi |
| Service 18 | Change SD card | SCC WE |
| Service 19 (19.1) | Change SD card | SCC WE, iCombi |
| Service 20.x | Thermocouple break; x identifies the failed sensor(s) — see bitmask table below | All series |
| Service 21 | Micro switch clima control faulty — legacy SCC 2004-2011 ONLY | Legacy SCC only |
| Service 23 | Solid state relay (SSR) for steam heating short-circuited | All series |
| Service 24 | Solid state relay (SSR) for hot-air heating short-circuited | All series |
| Service 25 | CleanJet water circulation fault — water not reaching / not driving the fan wheel | All series |
| Service 26 | Drain / ball valve does not open | All series |
| Service 28 | Over-temperature trip; Parts Town lists the threshold as above 356 F (180 C) | Per OEM reference |
| Service 29 | Over-temperature trip; Parts Town lists the threshold as above 185 F (85 C) | Per OEM reference |

## Water System Codes: Service 10-14

**Service 10** is the most common field call on these ovens. On the iCombi Pro and Classic the reference lists SC pump, Combi water box, and pump-off hose; on the SCC WE it is SC pump, level electrode, and hose; on the legacy SCC it simply reads "SC-Pump without function." In every generation it means the unit failed to drain or flush the steam generator. The usual culprits are a blocked or kinked pump-off hose, a failed SC pump motor, or a calcified level electrode giving a false level reading. Run the drain in the function test and watch for actual flow, clear the pump-off hose, and descale the level electrode before condemning the pump. Replace the SC pump only if it produces no output with correct supply. On the iCombi the pump is designated M4, and Service 46.x is the direct M4 fault code, so a 46.x alongside a 10 points you straight at the pump itself.

**Service 11** points at the fill side rather than the drain side. On the SCC WE it flags the level electrode (osmosis water) or a venting valve above the steam generator that is leaking water through when it should not. The iCombi references add the CDS sensor flow rate and the I/O board as candidates. Check the venting (air-break) valve above the steam generator for leak-through, inspect the fill pipework, test the level electrode, and only then look at the I/O board.

**Service 12** means the CDS water-metering sensor produced no output signal. The meaning is identical on legacy SCC, SCC WE, and iCombi. Before touching the sensor, confirm the water supply: a closed shut-off valve or low supply pressure produces exactly this code. If water is verified, test or replace the CDS sensor.

**Service 13** is unambiguous in every reference: change the water level electrode. Electrodes wear and scale-bridge until the steam generator level is no longer recognized. On hard-water sites, descale the steam generator at the same time or the replacement will not last.

**Service 14** is the inverse water-quality problem: the conductivity of the supply water is too low for the level electrode to detect. This shows up on sites feeding the oven straight RO or demineralized water. Check the water treatment and blend RO water back up to a detectable conductivity per Rational's water specification, then test the electrode.

## Software and SD Card Codes: Service 16-19

These four form one family: a corrupt software image or a failing SD card on the control board. Service 16 asks for a software update of the board. Service 17 escalates: inform Rational and use the Recovery Software (on the SCC WE, flash or change the SD card). Service 18 (SCC WE) and Service 19 / 19.1 both call for an SD card change. Update software from the Rational portal or USB first; if the code persists, run the SD Recovery Software or fit a new SD card. Board data restores from the micro SD backup, so a card swap is not a configuration loss on these platforms.

## Decoding Service 20.x: The Thermocouple Bitmask

Service 20 sub-codes are not sequential model variants; they are an additive bitmask identifying which thermocouple failed:

| Sub-code value | Sensor |
|---|---|
| .1 | B1 cooking cabinet sensor |
| .2 | B2 control (quenching) sensor |
| .4 | B4 moisture / humidity sensor |
| .8 | B5 steam generator sensor |
| .9 (iCombi Classic) | Thermocouple B9 |

Combinations add: Service 20.5 is B1 plus B4 (1 + 4). A Service 20.3 is B1 plus B2. Identify the sensor(s) from the sub-code, check the plug and lead continuity at the board, and replace the failed thermocouple. Two or more sensors dropping at once usually says loose plug or damaged loom, not two simultaneous sensor deaths.

## Service 21: A Correction Worth Reading

Several code lists on the web, including an earlier version of our own, describe Service 21 as a voltage or current fault on the main board. The official documents do not support that. Service 21 appears only in the legacy SCC / CombiMaster reference (doc 80.51.028-A4), where it means the micro switch for the clima control is faulty. It does not exist at all in the SCC WE or iCombi service references. If you see Service 21, you are on a 2004-2011 machine, and the fix is testing and replacing the clima-control micro switch — not board-level electrical diagnosis.

## Heating Relay and Drain Codes: Service 23, 24, 26

**Service 23** means the solid state relay for steam heating has short-circuited; **Service 24** is the same failure on the hot-air heating SSR. The repair is replacing the SSR and verifying heating current afterward. This is line-voltage work inside a live heating circuit: qualified electrician or service technician only. A shorted SSR can drive an element with the control demanding off, so do not keep running the oven on a 23 or 24.

**Service 26** means the drain valve (ball valve on iCombi) does not open. Scale is the usual reason a ball valve seizes. Inspect and descale the valve and confirm it actually cycles in the function test before replacing it.

## Service 25: The CleanJet Circulation Fault

Service 25 is one of the top field-call codes per General Parts, and it is frequently not a broken oven. The references describe it as a CleanJet water circulation fault: on the iCombi, the fan wheels are not running or show no performance increase when the water jet hits; on the SCC WE, no water flow was detected during CleanJet; on the legacy SCC, the water is not hitting the fan wheel. Work the list in order of cost: water supply off or pressure low; GN racks or the mobile trolley not positioned in the cabinet during the clean; blocked hoses or circulation path; foreign particles in the circulation pump; and finally the CDS sensor. The rack/trolley check matters because the cleaning cycle expects them in place — an empty cabinet can throw the code with nothing wrong.

## Over-Temperature Codes: Service 28 and 29

Parts Town's distributor guide lists Service 28 as tripping above 356 F (180 C) and Service 29 above 185 F (85 C). The official reference for your specific series identifies which sensor and zone each threshold protects, so pull the matching OEM document before replacing anything. Repeated over-temperature trips are a symptom to be diagnosed, not a nuisance to be reset.

## Gas Codes and the Service 140 Lockout (TI_2220)

Rational Technical Information TI_2220 (V02.1, 05/2023) introduced two gas service messages on affected software versions. **Service 140.4** is a warning. **Service 140.8** is a cooking lockout: the oven stops cooking until it is properly reset. Both are triggered by accumulated critical gas errors — the TI lists gas error codes 17, 18, 22, 37, 38, and 42 as the critical set — and TI_2220 defines the reset menu path for each series along with the affected software versions.

The SCC WE reference additionally lists gas error displays in 19/29 and 22/32 pairs for gas units; consult doc 80.51.720 for those burner tables.

Treat every gas code as a stop sign. A gas lockout exists because the burner repeatedly failed in a way the controller considers unsafe. Resetting a 140.8 without diagnosing the underlying gas errors just re-arms the failure. Combustion diagnosis, gas valve work, and burner repair belong to a licensed gas technician or Rational-authorized service partner — do not clear-and-retry your way through gas faults.

## Codes We Have Not Decoded Here

We only publish meanings we can verify against official documentation, so the following are named but deliberately not interpreted:

- **Service 40** — among the most-called codes per General Parts; its meaning is in the OEM reference for your series.
- **Service 110 and 120** — listed in both the legacy SCC and SCC WE references.
- **Calibration errors 10, 20, 100, 200** — listed in the SCC WE reference (doc 80.51.720).
- **CombiMaster E1-E24** — the non-Plus CombiMaster code set, covered in Parts Town's guide.
- **iCombi Classic display codes 1000-1033.x, 2000, 201, 90** — Classic-only codes in doc 80.51.855.
- **Diagnostic LED codes 1-8** — in the iCombi Pro reference.
- **Motor blink codes** — in the SCC WE reference.

All four service references are OEM quick-reference documents, and the Classic document's footer points to portal.rational-online.com, Rational's service portal, for the full service documentation behind each code.

## How to Troubleshoot Any Rational Service Code

1. **Identify the series first.** Same number, different meaning: Service 21 is the proof. Match the oven to its document before trusting any code list, including this one.
2. **Check water before parts.** The most common codes (10, 12, 25) all have "water supply off, pressure low, or hose blocked" ahead of any component failure in the OEM cause lists.
3. **Use the function test.** Running the drain pump, valves, and cleaning circulation in the service function test shows you the failure instead of making you infer it.
4. **Manage scale.** Calcified level electrodes, scale-bridged sensors, and scale-jammed valves recur throughout these code tables. On hard-water sites, descaling is diagnosis.
5. **Do not reset-and-forget.** A code that clears and returns is data. That is especially true for gas codes, where repeated resets of a Service 140.8 without repair defeat a deliberate lockout.
6. **Know where your work ends.** Shorted SSRs (23/24) are live line-voltage work. Anything gas-side (140.x, gas error codes) is licensed-gas-technician territory. When the fix crosses into either, stop and call a qualified pro.

## Frequently Asked Questions

### What does Service 20.3 mean on a Rational oven?

The Service 20 sub-code is additive: .1 is the B1 cabinet sensor and .2 is the B2 control (quenching) sensor, so 20.3 means both B1 and B2 read as broken. Two thermocouples failing simultaneously usually points at a common cause — a loose plug on the board or a damaged sensor loom — rather than two dead sensors.

### Why does Service 10 keep coming back after I reset it?

Because the cause is still there. Service 10 means the steam generator failed to drain, and the OEM cause list is a blocked or kinked pump-off hose, a failed SC pump, or a calcified level electrode falsely reporting the water level. Run the drain in the function test and watch for flow; if the hose and electrode check out and the pump produces nothing with correct supply, replace the pump.

### Is Service 21 a main-board voltage fault?

No. That meaning circulates widely online but is not supported by any official Rational service reference. Service 21 exists only in the legacy SCC / CombiMaster (2004-2011) document, where it means the clima-control micro switch is faulty.

### My gas oven shows Service 140.8 and refuses to cook. What now?

Per Rational TI_2220, Service 140.8 is a cooking lockout triggered after critical gas errors (codes 17, 18, 22, 37, 38, 42). The TI defines the reset menu path for each series, but the reset is not the repair: the burner has been failing repeatedly. Have a licensed gas technician or Rational-authorized service partner diagnose the gas system before returning the oven to service.

### My oven shows Service 12 every morning. Is the sensor bad?

Check the water first. Service 12 means the CDS water-metering sensor gave no output signal, and a closed shut-off valve or low supply pressure produces exactly that. If someone closes the water at night, the oven will fault at startup. Only after verifying supply and pressure should you test or replace the CDS sensor.

## Sources

- RATIONAL Service Reference iCombi Pro, doc 80.51.872_SR-iCombi Pro_en-GB (05/2020) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-iCombi-Pro-1.pdf
- RATIONAL Service Reference iCombi Classic, doc 80.51.855, en-GB — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/80.51.855-ServiceReferenz-iCombi-Classic-en-GB-1.pdf
- RATIONAL Service Reference SelfCookingCenter whitefficiency / CombiMaster Plus, doc 80.51.720_SR_en (11/2017) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCCWE-CM_P-1.pdf
- RATIONAL Service Reference SCC / CombiMaster 2004-2011, doc 80.51.028-A4 (09/2008) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCC-CM-1.pdf
- RATIONAL Technical Information TI_2220: New gas service messages 140, V02.1 (05/2023) — https://portal.rational-online.com/fs4p/media/service/3_dokumentationen/technische_infos_1/2022_1/2220/TI_2220_en-GB.pdf
- Parts Town — Rational Combi Oven Error Codes (authorized distributor guide) — https://www.partstown.com/cm/resource-center/guides/gd2/rational-combi-oven-error-codes
- General Parts — Top 5 Rational Error Codes (authorized service company) — https://generalparts.com/top-5-rational-error-codes-and-what-they-mean-to-you/
