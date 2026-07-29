---
title: "Burnham Alpine Fault Codes: Soft & Hard Lockout Fixes"
description: "Real Burnham Alpine boiler fault codes from the Sage2.1 control - what each soft and hard lockout number means, the likely cause, and how to fix it."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - boiler
  - burnham
money_part: "Flame sensor rod"
---

## Burnham Alpine Boiler Error Codes — What They Mean

The Burnham Alpine is a high-efficiency modulating condensing boiler using the IBC Controls platform (Burnham uses the IBC HC Series controls on the ALP series). The boiler displays fault codes on a backlit LCD control panel. Codes use an alphanumeric format: "E" codes are hard lockouts requiring manual reset; "W" codes are warnings that may self-clear. The Alpine is available in 80–300 MBH input sizes and fires on natural gas or propane.

## Common Error Codes and Causes

- **E01 — Ignition Failure** — The burner failed to light after the maximum number of tries. Most common causes: failed igniter, dirty or failed flame sensor, gas supply issue, or incorrect gas pressure. Clean the flame sensor rod and test the igniter before replacing components.
- **E02 — Flame Lost During Operation** — The burner lit but the flame was lost unexpectedly. Causes: contaminated flame sensor, gas supply fluctuation, or a cracked heat exchanger causing combustion instability.
- **E03 — High Limit Tripped** — The boiler's high-limit safety opened because water temperature exceeded the limit set-point. Causes: failed circulator pump, air-locked system, or a stuck zone valve. Bleed air from the system and verify all circulators are running.
- **E04 — Low Water Condition** — The low-water cutoff (LWCO) has detected inadequate water in the system. Check system pressure (should be 12–25 PSI cold), inspect for leaks, and check the automatic fill valve if installed.
- **E05 — Pressure Switch Fault** — The inducer pressure switch did not prove draft within the startup window. See the pressure switch diagnosis steps below.
- **W06 — Service Reminder** — The Alpine has accumulated the set number of run hours and is requesting routine service. Not a fault — reset via the service menu after completing maintenance.
- **E08 — Flue Gas Temperature High** — The flue temperature exceeded the safe limit. Check that the vent is the correct size, all joints are sealed, and the boiler is not short-cycling excessively.

## Step-by-Step Fix {#fix}

1. **Read and record the code** — Note the exact code and any supporting data (water temp, status) shown on the Alpine's LCD before resetting.
2. **For E01/E02 (ignition/flame faults)** — Inspect the flame sensor rod for oxidation and polish with steel wool. Check gas supply pressure at the manifold (should be 3.5" WC natural gas, 10" WC LP). If the igniter does not glow during trial, test its resistance.
3. **For E03 (high limit)** — Verify system pressure is normal (15–20 PSI operating). Check that all zone valves are open and all circulators run during a call for heat.
4. **For E04 (low water)** — Check the boiler pressure gauge. Add water via the fill valve until pressure reaches 15 PSI and the LWCO clears. Inspect all visible piping for leaks.
5. **For E05 (pressure switch)** — Inspect the pressure switch hose for blockage and the condensate drain for a backup. Test the inducer and pressure switch as described in the burnham-boiler-e2 guide.
6. **Reset the boiler** — After addressing the root cause, hold the reset button for 3 seconds or cycle power. The Alpine should restart and complete a normal firing sequence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flame sensor rod | [Amazon](https://www.amazon.com/s?k=Flame+sensor+rod&tag=errorcodefixes-20) \| Clean first; replace if resistance is abnormally high or the tip is pitted |
| Gas valve | [View on Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-burnham-alpine-error-codes&tag=errorcodefixes-20) \| Replace only after confirming 24VAC input and correct gas pressure |
| Pressure switch | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-burnham-alpine-error-codes&tag=errorcodefixes-20) \| Match WC rating for the Alpine model size |
| Circulator pump (Taco, Grundfos) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-burnham-alpine-error-codes&k=Circulator+pump+%28Taco%2C+Grundfos%29&tag=errorcodefixes-20) \| Required if pump is failed and E03 is caused by no-flow |
## When to Call a Pro

Alpine boilers operate at high efficiency by modulating gas input, and incorrect setup of gas pressure, combustion analysis (CO/CO2), or control parameters can cause safety hazards. For persistent E01/E02 faults or any combustion analysis work, call a licensed technician with Alpine experience.

## More Burnham Alpine fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| Soft Lockout 1 | Minimum time between starts has not been reached (normal anti-short-cycle delay). | The Sage2.1 control is enforcing the minimum off-time between burner starts. Not a fault; it self-clears. | Wait for the delay to expire. If it recurs constantly, check for an oversized boiler on a small load or a thermostat that is short-cycling. |
| Soft Lockout 2 | Boiler safety limit wired to terminals J6-1, 2 or 3 is OPEN. | A safety limit device in the J6 circuit (e.g. air pressure switch or auto-reset high limit) has opened. | Check the device wired to J6, the venting for blockage, and the condensate trap. The boiler auto-restarts when the limit closes. |
| Soft Lockout 3 | Boiler safety limit or external limit wired to terminal J5-1 is OPEN. | The external limit/interlock or flow switch in the J5 circuit has opened (or the external-limit jumper on terminals 11-12 is missing). | Verify circulation and that any external limit/flow switch is closed. Confirm the external-limit jumper is in place if no device is used, then let it auto-restart. |
| Soft Lockout 7 | Shorted or open return temperature sensor. | The return water sensor or its wiring has failed open or shorted. | Inspect the return sensor connector and wiring; measure sensor resistance against the manual's temp/resistance chart and replace if out of range. |
| Soft Lockout 8 | Shorted or open supply temperature sensor. | The supply water sensor or its wiring has failed open or shorted. | Check the supply sensor connector and wiring; test resistance and replace the sensor if it reads out of spec. |
| Soft Lockout 10 | Shorted or open flue gas (stack) temperature sensor. | The flue/stack temperature sensor or wiring has failed. | Inspect and test the stack sensor; replace if open or shorted. |
| Soft Lockout 11 | Flame failure after 5 tries to restart. | The burner could not establish or hold flame across repeated ignition attempts. Common causes: dirty/failed flame rod, low or interrupted gas supply, plugged condensate trap, or ignition electrode/spark issues. | Clean or replace the flame rod, confirm gas is on and at the correct manifold pressure, clear the condensate trap, and inspect the ignition electrode. Combustion setup should be verified by a technician. |
| Soft Lockout 13 | Flame rod shorted to ground. | The flame sensing rod is shorted, cracked at the insulator, or contacting a grounded surface. | Inspect the flame rod and its ceramic insulator for cracks or soot bridging; clean or replace the rod. |
| Soft Lockout 14 | Temperature rise between supply and return is too high. | Low system flow producing an excessive delta-T (air-bound loop, failed/undersized circulator, closed valve, or plugged strainer). | Purge air, confirm the circulator runs and is sized correctly, and check that all isolation and zone valves are open. |
| Soft Lockout 16 | Supply water temperature has risen too quickly. | A rapid supply-temperature spike, typically from little or no flow through the heat exchanger. | Restore proper circulation: bleed air, verify the pump, and clear any flow restriction before restarting. |
| Hard Lockout E04 | Supply high limit: the Sage2.1 supply sensor detected supply temperatures above 210 degrees F. | Overheating at the supply sensor, usually from loss of flow (failed circulator, air lock, closed valve) rather than a control fault. | Correct the flow problem, let the boiler cool, then manually reset with the RESET button. Persistent E04 needs a pro to check the pump and sensor. |
| Hard Lockout E05 | DHW high limit: the Sage2.1 DHW sensor detected domestic hot water temperature above setpoint. | Domestic hot water overheating or a faulty DHW sensor. | Check DHW circulation and the DHW sensor, correct the cause, then manually reset. |
| Hard Lockout E06 | Stack high limit: the Sage2.1 flue gas sensor detected stack temperatures above 204 degrees F. | Excessive flue temperature, often from a scaled/fouled heat exchanger or a venting problem. | Have a technician inspect and clean the heat exchanger and verify venting; reset after the cause is corrected. |
| Hard Lockout E12 | Flame detected out of sequence: a flame signal was present when no flame should exist. | A leaking or slow-closing gas valve, or a flame rod reading a false signal. | This is a safety lockout. Shut off gas and call a licensed technician to check the gas valve and flame-sensing circuit. |
| Hard Lockout E18 | Light-off rate proving failed: blower not running at light-off rate, or no fan speed signal. | Failed or obstructed blower, or a lost fan-speed/tach feedback signal. | Check the blower for obstruction and correct operation and inspect the fan wiring/connector; replace the blower if it will not hold light-off speed. |
| Hard Lockout E19 | Purge rate proving failed: blower not running at purge rate, or no fan speed signal. | Blower cannot reach purge speed or the control is not receiving a valid fan-speed signal. | Inspect the blower and its wiring/tach feedback; replace the blower if it cannot hold purge rate. |
| Hard Lockout E23 | 24VAC voltage low/high: control power is above or below acceptable levels. | Transformer, wiring, or supply voltage problem feeding the Sage2.1 control. | Check the transformer output and 24VAC wiring; correct the supply issue and reset. |
| Hard Lockout E24 | Fuel valve error: power detected at the fuel (gas) valve when it should be off. | A wiring fault or failed gas valve/relay leaving the valve energized when it should be de-energized. | Safety lockout. Have a technician check the gas valve wiring and the valve/relay; do not bypass. |

## How to troubleshoot Burnham Alpine

The Burnham Alpine (ALP series) runs on the Honeywell/Resideo Sage2.1 control, and its codes are numeric, not the "E01/W06" style some guides show. Read the display carefully first: a soft lockout alternates the digit "9" with the letter "b" followed by a two-digit code and clears on its own once the cause is corrected, while a hard lockout shows "E" plus a two-digit code and requires pressing the RESET button after the fault is fixed. Always record the exact number before resetting, because the boiler overwrites it.

Start with the cheap, common culprits before condemning parts. The most frequent Alpine complaints are ignition and flame-related (soft lockout 11, flame failure after five tries; soft lockout 13, flame rod shorted). Check that gas is on and at the correct manifold pressure, then remove and inspect the flame rod for soot, oxidation, or a cracked ceramic insulator. Because the Alpine is a condensing boiler, a plugged or slime-filled condensate trap is a classic hidden cause of nuisance ignition and pressure faults, so clear and flush it as part of routine diagnosis.

Overheat and flow faults (soft lockout 14 high delta-T, soft lockout 16 fast temperature rise, hard lockout E04 supply high limit) almost always trace back to loss of water flow rather than a bad control. Purge air from the loop, confirm the circulator actually spins on a call for heat, and verify every isolation and zone valve is open. Sensor codes (soft lockout 7, 8, 10) are usually a failed thermistor or a loose connector; test resistance against the chart in the manual before replacing. Blower codes (E18/E19) point to an obstructed or failing fan or a lost fan-speed signal.

Call a licensed technician for anything touching combustion or gas integrity: hard lockout E12 (flame out of sequence) and E24 (fuel valve error) are gas-valve safety lockouts and must never be bypassed. Setting manifold pressure, running a combustion analysis (CO/CO2), and adjusting the throttle/offset on a modulating boiler like the Alpine require a manometer and analyzer and are not DIY tasks. When in doubt on a repeated hard lockout, stop resetting and get a pro.

## Frequently asked questions

### What does a flashing "E" code mean on my Burnham Alpine versus a "9b" code?

An "E" plus a two-digit number is a hard lockout: the boiler stays off until you fix the cause and press the RESET button. A display that alternates "9" and "b" with a two-digit number is a soft lockout, which clears automatically once the condition corrects itself. Note the number before it disappears.

### Why does my Alpine keep showing soft lockout 11?

Code 11 is flame failure after five ignition tries. The usual causes are a dirty or failed flame rod, low or interrupted gas supply, a plugged condensate trap, or a worn ignition electrode. Clean or replace the flame rod, confirm gas pressure, and clear the condensate trap. If it persists, have the combustion checked.

### My Alpine is showing E04 supply high limit. Is the control bad?

Usually not. E04 means the supply sensor saw water above 210 degrees F, which almost always comes from loss of flow: an air-bound loop, a failed circulator, or a closed valve. Restore circulation, let it cool, and reset. Only suspect the sensor or control if flow is confirmed good.

### Can I fix a Burnham Alpine fault myself, or do I need a technician?

Cleaning the flame rod, clearing the condensate trap, purging air, and checking valves and system pressure are reasonable DIY steps. Anything involving the gas valve, manifold pressure, or combustion analysis (including hard lockouts E12 and E24) requires a licensed technician with the right instruments.

### How do I clear a hard lockout on the Alpine?

Fix the underlying cause first, then press and hold the RESET button on the display. The boiler will run its normal purge and ignition sequence. If it locks out again immediately, stop resetting and diagnose the root cause rather than repeatedly clearing it.
