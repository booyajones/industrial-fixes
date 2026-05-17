---
title: "Cleveland Range Steamer Error Codes — Complete Fix Guide"
description: "Cleveland Range steamer error codes for SteamCraft, convection steamers, and combi ovens. What each code means and how to fix it."
pubDatetime: 2026-04-27T22:00:00Z
modDatetime: 2026-04-27T22:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - commercial-kitchen
  - cleveland
---

Cleveland Range has manufactured commercial steamers and cooking equipment since 1847. Their SteamCraft and convection steamer lines are workhorses in commercial kitchens, hospitals, schools, and large-scale food production. When a Cleveland steamer faults, the symptoms tend to fall into a handful of recognizable patterns — low water, temperature sensor issues, door interlocks, drain problems, or ignition failures on gas models.

This guide covers the SteamCraft III and Ultra, SteamCraft countertop convection steamers (21CET/22CET series), full-size floor steamers (24CGM/24CDP series), gas convection steamers (22CGT series), and the KEL/KDL kettle series. Where a fault has an LED indicator or buzzer pattern, that's noted.

---

## Jump to Fix

- [Low Water / No Water Fault](#low-water--no-water-fault)
- [High Limit / Over-Temperature Fault](#high-limit--over-temperature-fault)
- [Temperature Sensor Fault](#temperature-sensor-fault)
- [Door Interlock Fault](#door-interlock-fault)
- [Steam Generator Fault](#steam-generator-fault)
- [Drain Fault / Drain Solenoid](#drain-fault--drain-solenoid)
- [Ignition Failure (Gas Models)](#ignition-failure-gas-models)
- [Power Indicator On, No Steam](#power-indicator-on-no-steam)
- [Timer / Control Board Faults](#timer--control-board-faults)
- [Parts Table](#parts-table)

---

## How Cleveland Range Displays Faults

Cleveland Range steamers use a combination of visual indicators (LED lights on the control panel) and buzzers rather than alphanumeric error codes on most models. The SteamCraft III and older countertop models use a single red "Reset" indicator light plus a buzzer. Newer models with digital controls (SteamCraft Ultra, some 24-series floor models) add LED displays that can show abbreviated messages.

**Key panel indicators:**
- **Green POWER light** — Power is on, normal operation
- **Red RESET light + buzzer** — High limit tripped or overtemperature condition
- **No POWER light** — No power reaching control panel or main switch off
- **POWER light on, no steam, no buzzer** — Low water, door interlock, or solenoid fault

---

## Low Water / No Water Fault

**Display/Indication:** Power light on, steamer not filling, may have intermittent buzzer. On digital models: "Lo H2O" or "LOW WATER."

**What it means:** The water probe (level sensor) inside the steam generator is not detecting water at the minimum operating level. The steamer will not produce steam to protect the generator from dry-fire damage.

**Causes in order of frequency:**

1. Water supply valve is closed — the most common cause by far
2. Water supply pressure too low (minimum 35 psi dynamic; maximum 60 psi static)
3. Water line strainer clogged — every Cleveland steamer has an inline strainer at the water inlet fitting
4. Water fill solenoid valve stuck closed or failed
5. Water probe (level sensor) coated with scale or detergent film — reads "no water" even when water is present
6. Defective water probe or broken probe wire

**Fix steps:**

1. Verify the water supply shut-off valve is fully open
2. Check incoming water pressure with a gauge at the supply valve — must be 35+ psi flowing
3. Remove and clean the inlet water strainer — unscrew the cap at the inlet fitting, pull the screen basket, rinse under running water, reinstall
4. With power off and water supply on, listen for the fill solenoid to click when power is restored — a click with no water flow indicates the solenoid is stuck; no click indicates an electrical/control fault
5. Descale the water probe assembly: turn off water supply, remove the probe, soak in a 50/50 white vinegar and water solution for 30 minutes, rinse and reinstall. The probe is typically a pair of stainless rods inside the generator cavity
6. Test probe continuity with a multimeter — there should be continuity (low resistance) between the probe terminals when submerged in water, open circuit when dry

**Important:** Never manually bypass the low-water protection. Cleveland generators that dry-fire will require generator replacement.

---

## High Limit / Over-Temperature Fault

**Display/Indication:** Buzzer sounds continuously + red RESET light illuminated. Some models: buzzer and all panel lights flash.

**What it means:** The high-limit safety thermostat or thermal cutoff tripped. This device opens if the steam generator or cooking compartment reaches an unsafe temperature — typically 225°F (107°C) for the cooking compartment or 250°F (121°C) for the generator.

**Causes:**

1. Water supply interrupted during operation — generator ran dry
2. Water probe failure caused dry-fire condition
3. Actual thermostat failure (less common)
4. Heavy scale buildup on generator walls — scale acts as insulation, causing localized overheating

**Fix steps:**

1. **Allow to cool.** Do not reset while unit is still hot — the reset button will not latch until the thermostat cools
2. Press the red RESET button firmly. On older models it is a physical push-button on the front panel or control box. On some models you must open the front panel to access the manual reset
3. Restore the unit to normal operation and monitor the first fill cycle — verify water is filling properly and the level probe is working
4. If the high limit trips again within a day: descale the generator (see maintenance section) and test the water probe
5. If the high limit trips on every cycle: the high-limit thermostat itself may have a lower trip point than spec after repeated trips — replace the high-limit thermostat

**High limit thermostat location:** On SteamCraft III/Ultra countertop models, the high-limit thermostat is mounted on the outside of the generator body, inside the lower front cabinet. On floor-model 24-series, it is inside the lower access panel.

---

## Temperature Sensor Fault

**Display/Indication:** On digital control models: "TEMP SENSOR FAULT," "PROBE FAULT," "F2," or "E2" depending on model year.

**What it means:** The cooking compartment temperature probe (PT100 or thermocouple) is reading outside its expected range — either open circuit (broken wire), short circuit (shorted probe), or a value outside the sensor's calibration range.

**Causes:**

1. Temperature probe connector loose or corroded — especially on models with a quick-disconnect probe plug
2. Probe physically damaged — steam environment causes gradual degradation of probe insulation
3. Control board input circuit failure
4. Probe out of calibration (rare, typically only affects older units with high cycle counts)

**Fix steps:**

1. With the steamer off and cooled, locate the temperature probe — on most SteamCraft models it is a stainless steel rod protruding through the back wall of the cooking compartment, with a 2-wire connection at the control board
2. Disconnect the probe connector at the control board and measure resistance across the probe leads with a multimeter:
   - PT100 probe: should read approximately 100Ω at 0°C (32°F), 110Ω at 25°C (77°F)
   - Thermocouple: use a millivolt meter — Type K reads approximately 0 mV at 0°C
3. Open circuit (infinite resistance) or dead short (0Ω) means a failed probe — replace
4. If probe tests good, check wiring harness continuity from probe to board — look for pinched wires or corroded terminals
5. If wiring is good and fault persists, the control board input circuit has failed

---

## Door Interlock Fault

**Display/Indication:** Power light on, steamer will not cycle (no fill, no heat, no steam). No buzzer. On some digital models: "DOOR" or "DOOR FAULT."

**What it means:** The door interlock switch (also called door safety switch) is not detecting the door as closed. Cleveland steamers require the door to be fully latched before the water fill and heating circuit will energize.

**Causes:**

1. Door not fully closed and latched — most common cause
2. Door interlock switch misaligned — door closes but plunger does not fully depress the switch
3. Door interlock switch failed — can fail mechanically or electrically
4. Door gasket worn or damaged — door won't close tightly enough to actuate switch
5. Door hinge worn — door sags and no longer aligns with latch

**Fix steps:**

1. Open and firmly reclose the door, ensuring the latch engages fully. On SteamCraft models, the door latch is a spring-loaded mechanism — it should snap closed with a distinct click
2. With power on, manually depress the door interlock switch plunger with a screwdriver while keeping the door open — if the steamer begins to fill, the switch is working and the problem is door alignment
3. Adjust door interlock switch position if possible — most are on slotted mounting brackets allowing minor repositioning
4. Inspect door gasket around the full perimeter — look for cuts, compression set (gasket permanently flattened), or sections that have pulled away from the channel. Gasket should provide a uniform seal
5. Test door interlock switch continuity: unplug connectors and use a multimeter. Should be open circuit (door open), closed circuit (door closed / switch actuated)
6. If the switch tests intermittent or the plunger travel is reduced, replace the switch

---

## Steam Generator Fault

**Display/Indication:** Unit fills with water but does not produce steam; or steam is produced but greatly reduced. No error code on most models — symptom-based diagnosis.

**What it means:** The steam generator (boiler element on electric models, heat exchanger on gas) is unable to produce steam at rated output.

### Electric Models (21CET, 24CEA, 24CEP, SteamCraft Electric)

**Causes:**
1. Scale buildup on heating elements — heavy calcium/lime scale reduces heat transfer significantly
2. One or more heating elements failed — open circuit
3. Contactor failed — elements are not receiving power even when called for
4. Thermal cutoff on element housing open

**Fix steps:**
1. Check element resistance with power off: disconnect element leads, measure resistance. Typical element resistance is 5–20Ω depending on wattage. Open circuit (infinite resistance) = failed element
2. Descale elements: shut off water, drain generator, fill with Cleveland descaling solution (or commercial descaler appropriate for food equipment), soak per Cleveland maintenance schedule (typically 4–8 hours), drain and flush
3. Verify contactor closes when heat is called for — with power on, listen for contactor click when thermostat calls for heat. No click = control board or thermostat fault. Click with no current to elements = failed contactor

### Gas Models (22CGT, 24CGP, 24CDP Gas)

**Causes:**
1. Gas supply pressure too low or shut off
2. Igniter failure — no spark at burner
3. Flame sensor/thermocouple not sensing flame
4. Gas valve failure

**See:** [Ignition Failure (Gas Models)](#ignition-failure-gas-models) section below for full gas troubleshooting.

---

## Drain Fault / Drain Solenoid

**Display/Indication:** Water continuously draining during operation; water not draining after cycle; "DRAIN" fault on digital models.

**What it means:** The drain solenoid valve is either stuck open (water drains during operation) or stuck closed (water cannot drain at end of cycle or during blow-down).

**Causes:**

1. Scale or debris lodged in drain solenoid seat — most common for both stuck-open and stuck-closed conditions
2. Drain solenoid coil burned out — solenoid will not open when called for
3. Control board relay failed — solenoid is not receiving the open/close command
4. Drain line blocked or kinked — slow drain that looks like a solenoid fault

**Fix steps:**

**Drain running during operation (solenoid stuck open):**
1. Turn off water supply and power. Remove the drain solenoid (typically on the underside of the generator, accessible from the lower cabinet)
2. Inspect the valve seat and plunger for scale deposits, food debris, or rubber gasket damage. A piece of scale as small as 1 mm can hold a solenoid open
3. Clean or replace the solenoid. If the rubber plunger seat is damaged, rebuild kit or full solenoid replacement

**Unit not draining (solenoid stuck closed):**
1. Verify the drain line from the steamer to the floor drain is clear — check for kinks in flexible drain hose
2. With power on, apply drain command (end of cycle or manual blow-down) and listen for solenoid click. No click = control fault or coil failure
3. Check solenoid coil resistance — typically 8–15Ω. Open circuit = failed coil; replace solenoid
4. If coil is fine, check control board output voltage when drain is commanded — 24V AC or 120V AC depending on model

---

## Ignition Failure (Gas Models)

**Display/Indication:** Unit fills with water, burner tries to light (clicking/sparking sound), no flame established. Red fault light or "IGNITION FAIL" on digital models. Some models will attempt 3 ignition tries then lock out.

**What it means:** The gas burner failed to establish a flame within the ignition trial period.

**Causes in order of frequency:**

1. Gas supply shut off or gas pressure too low
2. Igniter electrode gap too wide or electrode damaged/fouled
3. Igniter module (spark igniter) failed
4. Flame sensor (thermocouple or ionization rod) not detecting the pilot/main flame
5. Gas valve coil failed
6. Burner orifice clogged

**Fix steps:**

1. Check the gas supply shut-off valve at the appliance — must be fully open. Check gas pressure with a manometer at the appliance: natural gas should be 7" W.C. (inches water column) supply, 4" W.C. manifold; LP should be 11" W.C. supply, 10" W.C. manifold
2. Inspect the igniter electrode: should be clean and dry with a 1/8" to 3/16" gap between electrode tip and ground rod. Clean with dry cloth — do not use water or solvents
3. Test igniter module by listening/watching for spark at the electrode during ignition trial. Weak or absent spark = igniter module failure
4. Check flame sensor (thermocouple or ionization rod): clean with very fine steel wool or Scotch-Brite. A thermocouple should generate at least 18 mV DC when in a full flame; replace if output is below 12 mV
5. If spark is strong and gas is confirmed on, check the gas valve by measuring voltage at the valve coil leads during ignition — should see 24V AC or 120V AC when the valve is commanded open
6. If the unit locks out after three tries, the lockout must be cleared: on most models, turn the unit off, wait 30 seconds, turn on again. Some digital models require holding a reset combination on the keypad

---

## Power Indicator On, No Steam

This symptom — panel powered but no steam production and no fault codes — can have multiple causes. Use this checklist:

| Check | What to Look For |
|-------|-----------------|
| Water supply | Is valve open? Is strainer clean? |
| Fill solenoid | Listen for click on power-up. No click = control or solenoid fault |
| Door interlock | Is door fully latched? Does interlock switch actuate? |
| Mode selection | Is unit in Manual or Timed mode? On timed models, timer must be set |
| High limit | Has red RESET button been pressed and reset? |
| Element/burner | Is the heating element/burner receiving power when fill is complete? |
| Water probe | Is probe clean? Does probe detect water? |

---

## Timer / Control Board Faults

**Symptom:** Timer display blank or incorrect. Unit fills but timer does not count down. Controls unresponsive.

**Causes:**
1. Timer transformer failed (older dial timer models) — transformer supplies low-voltage AC to the timer motor
2. Control board failed — modern solid-state controller
3. Power interruption during operation damaged control board

**Fix steps:**
1. On dial timer models (SteamCraft III older versions): check the timer transformer — typically a small 24V/120V transformer in the control box. Test secondary voltage with multimeter while primary power is on
2. On electronic control board models: check for any burning smell or visually damaged components on the board (swollen capacitors, burned traces). Control boards on Cleveland steamers are generally not user-repairable — replace the board
3. Before replacing the board, verify the power supply to the board is correct (typically 120V AC at board input terminals)

---

## Maintenance That Prevents Most Faults

**Descaling (monthly to quarterly based on water hardness):**
Cleveland recommends periodic descaling of the steam generator. Hard water areas (above 7 grains/gallon hardness) may require monthly descaling. Scale buildup is the root cause of most high-limit trips, low water faults (from probe coating), and reduced steam output.

**Descaling procedure:**
1. Turn off water supply and drain the generator
2. Fill generator with approved descaling solution (Cleveland part number or food-safe commercial descaler)
3. Allow to soak per solution manufacturer's directions (typically 4–8 hours)
4. Drain and flush with clean water — at least three full fill-and-drain cycles
5. Check water probe contacts — clean manually if coated

**Door gasket inspection (monthly):**
Run a finger around the full gasket perimeter. Any cracked, missing, or compressed-flat sections need replacement. A deteriorated gasket allows steam to escape, reduces efficiency, and can cause the door interlock to misalign.

---

## Parts Table

| Component | Fits | Part Notes |
|-----------|------|------------|
| **Water level probe / sensor** | All SteamCraft and convection steamer models | Stainless steel rod probe assembly. Cleveland OEM part or equivalent. Part varies by model — specify full model number. Common for 21CET/22CET: probe and bracket assembly |
| **Temperature probe (PT100)** | 21CET, 22CET, 24CEA, 24CEP electric models | PT100 RTD probe, stainless steel well, typically 4" insertion length. Cleveland part or generic PT100 3-wire |
| **Door gasket** | SteamCraft III / countertop models | Silicone gasket, door-perimeter channel. Measure door opening dimensions and order to length or buy full perimeter kit |
| **Door interlock switch** | All models with door interlock | SPST or SPDT microswitch, 15A 125V rating. Standard industrial microswitch — specify plunger style and mounting hole centers |
| **Fill solenoid valve** | All SteamCraft and convection steamers | 120V AC or 24V AC depending on model (check wiring diagram). Normally closed solenoid, 3/8" or 1/2" NPT inlet. Cleveland OEM or equivalent Parker/Asco |
| **Drain solenoid valve** | All models | Same specification as fill solenoid — normally closed, same voltage. Check model-specific wiring diagram for voltage |
| **Heating element** | 21CET, 22CET, 24CEA electric | Specify model, voltage, and wattage from element nameplate. Typically stainless sheath, threaded flange mount |
| **High-limit thermostat** | All models | Manual-reset safety thermostat. Specify trip temperature (typically 225°F for compartment, 250°F for generator). Klixon or equivalent |
| **Igniter module** | 22CGT, 24CGP, 24CDP gas models | 120V AC spark igniter. Fenwal or equivalent. Verify module spark rate and dwell match original |
| **Thermocouple / flame sensor** | Gas models with pilot | Type K thermocouple, 18" or 24" length (measure original). Standard commercial thermocouple |
| **Gas valve** | Gas models | 24V AC or 120V AC operator coil. Specify manifold pressure and orifice size from gas train label |
| **Control board** | Electronic timer models | Model-specific PCB. Cleveland part number required — not generic. Specify full model number and serial number |
| **Timer transformer** | Older dial timer models | 120V primary, 24V AC secondary, typically 20–40 VA. Standard chassis-mount transformer |

---

## Model Quick Reference

| Model Series | Type | Control Type | Common Faults |
|-------------|------|-------------|---------------|
| SteamCraft III (21CET8/16) | Countertop electric convection | Dial timer or electronic | Low water probe, high limit, door interlock |
| SteamCraft Ultra (22CET3.1/6.1) | Countertop electric | Electronic | Low water, temperature probe, control board |
| 22CGT3.1/6.1 | Countertop gas convection | Electronic | Ignition failure, gas valve, flame sensor |
| 24CGM200 | Floor convection electric | Digital | Low water, heating element, fill solenoid |
| 24CDP | Floor convection gas | Digital | Ignition, gas valve, combustion |
| 24CEA / 24CEP | Floor electric | Electronic | Heating elements, high limit, level probe |
| KEL / KDL Kettle | Tilt kettle | Analog / Digital | Steam supply (from boiler), temperature control, safety valve |

---

## When to Call Service

Cleveland Range steamers involve pressurized steam, high-voltage heating elements (up to 480V three-phase on floor models), and gas systems. Call a qualified commercial kitchen technician for:

- Any gas-related fault on gas models — especially if you smell gas
- Element replacement on 208V/480V floor models
- Generator replacement after dry-fire damage
- Control board replacement (requires calibration on some models)
- Any repair that requires accessing inside the generator vessel

Note 1 in Cleveland manuals refers to calling a Cleveland Range Authorized Service Representative. Most internal repairs are within reach of qualified commercial kitchen technicians, but generator replacement and high-voltage three-phase work require licensed technicians in most jurisdictions.

## Where to Buy Replacement Parts

Find replacement parts for Cleveland Range steamers on Amazon:

- [Cleveland Range Steamer Parts](https://www.amazon.com/s?ascsubtag=ecf-cleveland-range-steamer-error-codes&k=Cleveland+Range+commercial+steamer+parts&tag=errorcodefixes-20)
- [Commercial Steamer Door Gasket & Seals](https://www.amazon.com/dp/B0FPF84HQP?ascsubtag=ecf-cleveland-range-steamer-error-codes&tag=errorcodefixes-20)
- [Commercial Steamer Heating Element](https://www.amazon.com/s?ascsubtag=ecf-cleveland-range-steamer-error-codes&k=commercial+steamer+heating+element+replacement&tag=errorcodefixes-20)