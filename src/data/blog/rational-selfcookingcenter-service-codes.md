---
title: "Rational SelfCookingCenter Service Codes: SCC WE, Legacy SCC and iCombi Reference (Service 10-121, Sub-Codes, Gas Lockout)"
description: "Rational combi service codes taken from the four OEM service references: legacy SCC 2004-2011, SCC whitefficiency, iCombi Pro and iCombi Classic. Service 10-14 water faults, the Service 20.x thermocouple sub-codes, CleanJet Service 25, the Service 28/29 temperature limits most lists get wrong, and the gas Service 140 lockout."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: rational-selfcookingcenter-service-codes
featured: false
draft: false
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

## Rational SelfCookingCenter Service Codes: What They Mean

Rational combi ovens report faults as numbered "Service" messages on the display. The numbers look identical across generations, but the meanings do not always carry over, and that is where most online code lists go wrong. Rational publishes a separate service reference for each platform, and the correct first step on any Service code is identifying which platform you are standing in front of.

Everything on this page is taken from the four OEM service references below, each of which we retrieved and read directly:

| Platform | OEM service reference | Range it covers |
|---|---|---|
| SCC / CombiMaster, 2004-2011 (legacy) | 80.51.028-A4, Edition 09/2008 | Service 10-44, 100, 110, 120 |
| SCC whitefficiency (SCC WE) / CombiMaster Plus | 80.51.720_SR_en, 11/2017 | Service 10-63, 110, 120; calibration errors 10/20/100/200; gas error displays; motor blink codes |
| iCombi Pro | 80.51.872_SR-iCombi Pro_en-GB, 05/2020 | Service 10-121 with sub-codes; diagnostic LED code tables; calibration errors |
| iCombi Classic | 80.51.885_ServiceReferenz_iCombi Classic_en-GB | Service 2-121 plus Classic-only display codes 90, 201, 1000-1033.x, 2000 |

Gas-specific detail for the current iCombi line comes from Rational's own portal document 80.51.859 (V05, 10/2025), *Service Reference iCombi Pro & iCombi Classic Gas*.

The older CombiMaster (non-Plus) line uses E-codes rather than Service numbers. Parts Town's distributor guide lists E1 through E24; we have not been able to verify the individual E-code meanings against an OEM document, so they are not reproduced here.

General Parts, which describes itself as a Rational Certified Authorized Service Agent, publishes the five codes its technicians are called out for most: Service 10, Service 12, Service 25, Service 40 and the gas RESET message. Four of those five sit in the water and cleaning circuit, which tells you a lot about what actually fails on these ovens: water supply, scale, and the drain path.

## Quick Reference: Verified Service Codes

Every meaning below is taken from the OEM service references named above. Applicability is listed per code because it genuinely differs between platforms.

| Code | What the OEM reference says | Applies to |
|---|---|---|
| Service 10 | Steam generator drain fault. Legacy: "SC-Pump without function." SCC WE: SC pump, level electrode, hose. iCombi: SC pump, Combi water box, pump-off hose | All four |
| Service 11 | Level electrode (osmosis water), or the check/venting valve above the steam generator leaking. iCombi adds CDS sensor flow rate and I/O board | All four |
| Service 12 | CDS sensor. Legacy states it explicitly: "CDS sensor no output signal" | All four |
| Service 13 | Change the water level electrode | Legacy, SCC WE, iCombi Pro |
| Service 14 | Level electrode / water conductivity. Legacy names osmosis water specifically | All four |
| Service 16 | Flash new software / software update of the board | Legacy, SCC WE, iCombi Pro |
| Service 17 | SCC WE: inform RATIONAL, flash or change the SD card. iCombi: inform RATIONAL, use Recovery Software. Legacy Service 17 is a different fault: external EEPROM faulty | SCC WE, iCombi (legacy differs) |
| Service 18 | Change SD card | SCC WE |
| Service 19 / 19.1 | Change SD card | SCC WE (19.1), iCombi Pro (19) |
| Service 20 / 20.x | Legacy: thermocouple B1 faulty. SCC WE and iCombi: thermocouple break, sub-code identifies the sensor (table below) | Sub-codes on SCC WE and iCombi only |
| Service 21 | Micro switch clima control faulty. Legacy reference only | Legacy SCC only |
| Service 23 | SSR steam short circuit | All four |
| Service 24 | SSR hot air short circuit | All four |
| Service 25 | CleanJet water circulation fault. Check water supply, pressure, hoses, CDS sensor, and position of GN racks / mobile oven racks | All four |
| Service 26 | Drain valve permanently closed (iCombi: ball valve does not open). Test in the function test, replace if necessary | Legacy, SCC WE, iCombi Pro |
| Service 27 | Drain valve does not close during initialisation; CleanJet without function | Legacy, SCC WE, iCombi Pro |
| Service 28 / 28.x | Legacy and SCC WE: thermocouple B5 in the steam generator above 180 C (356 F), descale the steam generator. iCombi 28.x: -1 B5 above 170 C; -2 cabinet B1 above 350 C; -3 cabinet B1 below 2 C | All four, thresholds differ |
| Service 29 | Control board temperature too high. Legacy states above 85 C (185 F). Change the air filter, check the cooling fan | All four |
| Service 40 | Care pump fault. Legacy: "CleanJet not possible, care pump faulty." SCC WE: care hose snapped off or care pump defective. iCombi: check the care pump M18 in the function test | All four |
| Service 46.x / 47.x / 48.x / 49.x | iCombi pump family: SC pump M4, waste water pump M15, circulation pump M17, care pump M18. Sub-code -1 fault, -2 output too low | iCombi only |
| Service 60 | Ignition box not initialised, or not initialised quickly. SCC WE: check gas settings. iCombi: error in the speed signal from the board to the fan burner; switch off and on, use SD Recovery Software if necessary | SCC WE, iCombi |
| Service 100 | Main contactor / board on-off switch | Legacy SCC only |
| Service 110 | SC pump fault. iCombi adds: while care chemical is in the steam generator. SCC WE and legacy: SC pump defective or level electrode calcified | All four |
| Service 120 | Level electrode fault. iCombi: level electrode without signal while care chemical is in the steam generator. SCC WE: Y1 or level electrode defective. Legacy: care pump M12 or level electrode defective | All four |

## Water System Codes: Service 10-14

**Service 10** is the most common field call on these ovens. The legacy reference reads simply "SC-Pump without function." The SCC WE reference lists SC pump, level electrode and hose; the iCombi references list SC pump, Combi water box and pump-off hose. In every generation the unit failed to drain or flush the steam generator. Run the drain in the function test and watch for actual flow, clear the pump-off hose, and descale the level electrode before condemning the pump. On the iCombi platform the SC pump is designated M4 and has its own code, Service 46.x (-1 fault, -2 output too low), so a 46.x logged alongside a 10 points at the pump itself rather than the hose or electrode.

**Service 11** points at the fill side rather than the drain side. The legacy reference is the most explicit: level electrode (osmosis water), or check the valve above the steam generator for leakage. The SCC WE reference words it as level electrode (osmosis water) or venting valve for the steam generator. The iCombi references list level electrode, CDS sensor flow rate and I/O board. Check the valve above the steam generator for leak-through, inspect the fill pipework, test the level electrode, and only then look at the I/O board.

**Service 12** is the CDS sensor. The legacy reference states the condition outright: "CDS sensor no output signal." The CDS is how these ovens meter water, and the iCombi Classic reference confirms the link in a separate code, Service 1022, "no water during the switch-on routine (via CDS measurement)." So before condemning the sensor, verify the oven actually has water: a closed shut-off valve or low supply pressure will starve the same measurement the code is complaining about.

**Service 13** is unambiguous in the legacy, SCC WE and iCombi Pro references: change the water level electrode. Electrodes wear and scale-bridge until the steam generator level is no longer recognized. On hard-water sites, descale the steam generator at the same time or the replacement will not last. Note that Service 13 does not appear in the iCombi Classic reference at all.

**Service 14** pairs the level electrode with water conductivity in the SCC WE and iCombi references; the legacy reference names osmosis water specifically. Reverse-osmosis and demineralised supplies are the context the OEM flags. Check the water treatment and the electrode together. We have not found a published Rational conductivity figure we can verify, so no threshold is quoted here.

## Software and SD Card Codes: Service 16-19

These form one family: a corrupt software image or a failing SD card on the control board. Service 16 asks for new software to be flashed. Service 17 escalates to informing Rational and using the Recovery Software, or flashing/changing the SD card on the SCC WE. Service 18 (SCC WE) and Service 19 / 19.1 both call for an SD card change.

Update software first: the SCC WE reference documents a USB-stick update, and the iCombi Classic reference documents the same. If the code persists, run the Recovery Software or fit a new card. A card swap is not a configuration loss on the iCombi platform: the board replacement procedure in the iCombi Pro reference has you move the existing micro SD card into the new board, after which "unit installs software backup from micro SD card to the board."

Be aware Service 17 is a trap across generations. On the legacy 2004-2011 reference it does not mean an SD card problem at all; it means the external EEPROM is faulty.

## Service 20.x: Identifying the Failed Thermocouple

On the legacy reference, Service 20 has no sub-code and means one thing: thermocouple B1 faulty. On the SCC WE and iCombi references the code carries a sub-code that identifies which sensor broke:

| Sub-code | Sensor |
|---|---|
| 1 | B1 cooking cabinet sensor |
| 2 | B2 control / quenching sensor |
| 4 | B4 moisture / humidity sensor |
| 8 | B5 steam generator sensor |
| 9 | Thermocouple B9 (iCombi Classic reference only) |

A word of caution about a claim that circulates widely: these sub-codes are often described online as an additive bitmask, so that a "20.3" supposedly means B1 plus B2. None of the four OEM references say that, and the iCombi Classic reference actively cuts against it, because it assigns 9 to its own sensor, B9, rather than to a combination of 1 and 8. Read the sub-code against the table your unit's reference publishes, and do not do arithmetic on it.

Whatever the sub-code, check the plug and lead continuity at the board before ordering a thermocouple. Two sensors dropping at once usually says loose plug or damaged loom rather than two simultaneous sensor deaths.

## Service 21: A Correction Worth Reading

Several code lists on the web, including an earlier version of our own, describe Service 21 as a voltage or current fault on the main board. The OEM documents do not support that. Service 21 appears only in the legacy SCC / CombiMaster reference (80.51.028-A4), where it means the micro switch for the clima control is faulty. We checked all three later references and it does not appear in the SCC WE, iCombi Pro or iCombi Classic code lists at all. If you see Service 21, you are on a 2004-2011 machine, and the fix is testing and replacing the clima-control micro switch, not board-level electrical diagnosis.

## Heating Relay and Drain Codes: Service 23, 24, 26, 27

**Service 23** is an SSR steam short circuit and **Service 24** is the same failure on the hot air SSR. Both the legacy and SCC WE references use the words "short circuit" explicitly. The repair is replacing the solid state relay and verifying heating current afterward. A shorted SSR can drive an element with the control demanding off, so do not keep running the oven on a 23 or 24.

This is live line-voltage work, and the iCombi Pro reference carries its own warning that residual charge remains after shutdown: "Beware of electric shock, even when the unit is switched off," naming the I/O power supply (A10), the pump board (A13), the eSTB (A15/A16) and the solenoid valve block. Isolate the unit, lock out and tag out, and allow the stored charge in those assemblies to bleed down before opening a panel. If you are not qualified for live commercial electrical work, this is where you stop and call a technician who is.

**Service 26** means the drain valve is permanently closed (worded as "ball valve does not open" on the iCombi). **Service 27** means it does not close during initialisation, and the SCC WE reference notes the consequence: CleanJet without function. Scale is the usual reason a ball valve seizes. Both iCombi references tell you to test the valve in the function test and replace it if necessary, which is the right order: prove it will not cycle before you buy one.

## Service 25: The CleanJet Circulation Fault

Service 25 is one of the top field-call codes per General Parts, and it is frequently not a broken oven. The iCombi references word it as fan wheels not running or no increase in performance at the fan motor when the water jet hits, and then give the check list directly: water supply, pressure, hoses, CDS sensor, and position of the GN conductors and mobile oven racks. The SCC WE reference words it as no water flow detected during CleanJet, with pump or circulation blocked by foreign particles, or rack/trolley not in cabinet. The legacy reference says the water does not hit the fan wheel, and to check the pump, foreign bodies in the water pipe, and that racks and trolley are inside the cabinet.

Work it in that order of cost: water supply and pressure, rack or trolley position, hoses, foreign particles in the pump, then the CDS sensor. The rack and trolley check matters because all three references name it, and an empty cabinet can throw the code with nothing else wrong.

## Temperature Codes: Service 28 and Service 29

These two are widely misreported as a matched pair of cooking over-temperature trips. They are not the same kind of fault.

**Service 28** is a steam generator temperature limit. The legacy and SCC WE references both state it identically: thermocouple B5 in the steam generator above 180 C (356 F), descale the steam generator. Scale insulates the element and drives B5 up, so the OEM remedy is descaling rather than a part. The iCombi references restructure it into sub-codes with different limits: 28.1 is B5 above 170 C, 28.2 is cabinet sensor B1 above 350 C, and 28.3 is B1 below 2 C.

**Service 29** is not a cooking temperature at all. It is the control board. The legacy reference gives both the value and the remedy: board temperature too high, above 85 C (185 F), change the air filter. The SCC WE reference says change the air filter and check the cooling fan; the iCombi references say board temperature too high, check the air filter, cooling fan and the seal on the control panel. Treat a Service 29 as a cooling and airflow problem around the electronics, not as a runaway heating circuit.

## Gas Codes and the Service 140 Lockout

Rational Technical Information TI_2220 ("New gas service messages 140," V02.1, 05/2023) documents two gas service messages added by software update to gas SelfCookingCenter units (Index H and I, from 09/2011), the iCombi Pro and the iCombi Classic. **Service 140.4** is a warning. **Service 140.8** blocks the unit from cooking. TI_2220 names the critical gas errors that drive the counter as 17, 18, 22, 37, 38 and 42, and gives a different service-menu reset path for each of the three series.

The SCC WE reference separately lists gas error displays for gas units, in hot-air/steam pairs: 19 and 29 for ignition electrode distance or a burner blocked from inside, and 22 and 32 for gas supply, gas stop valve, gas pressure or gas valve.

Treat every gas code as a stop sign. A gas lockout exists because the burner repeatedly failed in a way the controller considers unsafe, and resetting a 140.8 without diagnosing the underlying gas errors just re-arms the failure. Rational's own gas service reference is blunt about who may do this work: the settings and procedures it describes "may only be carried out by trained service technicians," and it instructs "always adhere to the local rules and regulations." If you find a leak, that document's instruction is to close the gas shut-off valve and look for the cause. Combustion diagnosis, gas valve work and burner repair belong to a licensed gas technician or a Rational-authorized service partner. Do not clear-and-retry your way through gas faults, and do not attempt to bypass the lockout.

Full detail on the trigger criteria, the critical gas errors and the per-series reset paths is in our dedicated write-up: [Rational Service 140.4 and 140.8 gas lockout](/posts/rational-service-140-gas-lockout).

## Codes We Have Not Decoded Here

We publish meanings we can verify against the OEM documentation. One set on this platform we could not:

- **CombiMaster E1-E24** — Parts Town's distributor guide indicates the non-Plus CombiMaster uses an E-code set running E1 to E24, but we could not verify the individual code meanings against a Rational-published document, so they are omitted rather than guessed.

For the record, several code groups that are often described as undocumented are in fact published, and we have used them above: the calibration errors (10 unit too hot with B1, B2 or B4 over 40 C; 20 differential pressure sensor faulty; 100 fan motor rpm detection faulty; 200 steam heating not working) appear in both the SCC WE and iCombi Classic references, the motor blink code table is in the SCC WE reference, and the diagnostic LED tables are in the iCombi Pro reference.

The iCombi Classic reference also carries a Classic-only display code block. Several entries simply redirect to a Service number: 1000 points to Service 14 or 120, 1001 and 1002 to Service 32 or 31, 1011 to Service 51, 1018 to Service 35.7, 1020 to Service 55-57, and 1024 to Service 31. Others stand alone, including 90 (perform calibration), 201 (carry out motor positioning), 1010 (check filter), 1012 (carry out humidity calibration), 1022 (no water during the switch-on routine, via CDS measurement) and 2000 (update attempt unsuccessful).

## How to Troubleshoot Any Rational Service Code

1. **Identify the series first.** Same number, different meaning. Service 21 and Service 17 are the proof. Match the oven to its document before trusting any code list, including this one.
2. **Check water before parts.** For Service 25 the OEM check list opens with water supply and pressure, ahead of any component. For Service 12 the code sits on the sensor that meters water flow, so an empty supply looks like a dead sensor.
3. **Use the function test.** All four references document a function test that runs the drain pump, valves and cleaning circulation individually. It shows you the failure instead of making you infer it. Note the OEM warning that components are not protected against overload during a function test.
4. **Manage scale.** Calcified level electrodes, scale-jammed valves and a Service 28 whose OEM remedy is literally "descale steam generator" recur throughout these tables. On hard-water sites, descaling is diagnosis.
5. **Do not reset-and-forget.** A code that clears and returns is data. That is especially true for gas codes, where repeated resets of a Service 140.8 without repair defeat a deliberate safety lockout.
6. **Know where your work ends.** Shorted SSRs (23/24) are live line-voltage work on assemblies the OEM warns hold charge after shutdown. Anything gas-side is licensed-gas-technician territory. When the fix crosses into either, stop and call a qualified pro.

## Frequently Asked Questions

### Is Service 21 a main-board voltage fault?

No. That meaning circulates widely online but is not supported by any of the four Rational service references. Service 21 exists only in the legacy SCC / CombiMaster (2004-2011) document, where it means the clima-control micro switch is faulty. It does not appear in the SCC WE, iCombi Pro or iCombi Classic code lists.

### What does the sub-code on a Service 20 mean?

It identifies the failed thermocouple: 1 is the B1 cabinet sensor, 2 is the B2 control (quenching) sensor, 4 is the B4 humidity sensor and 8 is the B5 steam generator sensor. The iCombi Classic reference adds 9 for thermocouple B9. The OEM documents do not describe these sub-codes as additive, so do not try to read a value as a sum of sensors. On the legacy 2004-2011 reference, Service 20 has no sub-code and means thermocouple B1.

### Why does Service 10 keep coming back after I reset it?

Because the cause is still there. Service 10 means the steam generator failed to drain, and the OEM candidate lists are the SC pump, the level electrode, and the water box or pump-off hose. Run the drain in the function test and watch for flow. On an iCombi, check whether a Service 46.x is logged alongside it: that code is specific to the SC pump M4 and separates a failed pump from a blocked hose.

### Are Service 28 and Service 29 both over-temperature trips?

No, and this is the most common mix-up on these ovens. Service 28 is a steam generator temperature limit, stated in the legacy and SCC WE references as thermocouple B5 above 180 C (356 F) with descaling as the remedy. Service 29 is the control board running hot, given in the legacy reference as above 85 C (185 F), with the remedy being a new air filter and a check of the cooling fan.

### My gas oven shows Service 140.8 and refuses to cook. What now?

Per Rational TI_2220, Service 140.8 is a cooking block that follows repeated critical gas errors, and it can only be reset by a service technician in the service menu. The reset is not the repair: the burner has been failing repeatedly. Have a licensed gas technician or a Rational-authorized service partner diagnose the gas system before the oven goes back into service. Do not attempt to bypass the lockout.

### My oven shows Service 12 every morning. Is the sensor bad?

Check the water first. Service 12 is the CDS sensor, and the legacy reference words it as "CDS sensor no output signal." The CDS is the flow-measuring device, and the iCombi Classic reference has a separate code (1022) for no water detected via CDS measurement. If someone closes the water at night, the oven has nothing to measure at startup. Verify supply and pressure before testing or replacing the sensor.

## Sources

All four service references below were retrieved and read in full. The keelingcatering.co.uk links are third-party mirrors of the Rational-published PDFs; the document number and edition date printed in each file's footer is given so you can match it against the copy on Rational's own service portal.

- RATIONAL Service Reference iCombi Pro, 80.51.872_SR-iCombi Pro_en-GB 05/2020 — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-iCombi-Pro-1.pdf
- RATIONAL Service Reference iCombi Classic, 80.51.885_ServiceReferenz_iCombi Classic_en-GB — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/80.51.855-ServiceReferenz-iCombi-Classic-en-GB-1.pdf
- RATIONAL Service Reference SelfCookingCenter whitefficiency / CombiMaster Plus, 80.51.720_SR_en 11/2017 — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCCWE-CM_P-1.pdf
- RATIONAL Service Reference SCC / CombiMaster 2004-2011, 80.51.028-A4 Edition 09/2008 — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCC-CM-1.pdf
- RATIONAL Service Reference iCombi Pro & iCombi Classic Gas, 80.51.859 V05 10/2025 (Rational service portal) — https://portal.rational-online.com/fs4p/media/service/3_dokumentationen/icombi_pro___icombi_classik/tm_icombi_pro___icombi_classic/en_gb/80.51.859_ServiceReferenz_iCombiProiCombiClassic_Gas_Q_en-GB.pdf
- RATIONAL Technical Information TI_2220: New gas service messages 140, V02.1 05/2023 (Rational service portal) — https://portal.rational-online.com/fs4p/media/service/3_dokumentationen/technische_infos_1/2022_1/2220/TI_2220_en-GB.pdf
- General Parts (Rational Certified Authorized Service Agent) — Top 5 Rational Error Codes — https://generalparts.com/top-5-rational-error-codes-and-what-they-mean-to-you/
- Parts Town — Rational Combi Oven Error Codes (used only for the existence of the CombiMaster E1-E24 code set) — https://www.partstown.com/cm/resource-center/guides/gd2/rational-combi-oven-error-codes
