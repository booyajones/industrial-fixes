---
title: "True GDM-23 Error Codes - What It Means and How to Fix It"
description: "The True GDM-23 is a common single-door cooler that uses digital fault codes to flag sensor, defrost, and temperature control problems. This guide shows what the codes mean and what to inspect first."
pubDatetime: 2026-04-25T00:00:00Z
author: "James Rutherford"
tags:
  - hvac
  - error-codes
---

The True GDM-23 is a single-section, 23-cubic-foot glass door reach-in merchandiser. It's one of the most deployed units in American convenience stores, small delis, and foodservice operations. When one of these fails, you've got approximately $500–$1,500 in beverage product at risk. Here's what the error codes mean and how to get it back online fast.

## What Does True GDM-23 Error Codes Mean?

The True GDM-23 with an electronic controller displays alphanumeric error codes on the temperature readout. The digital display normally shows the cabinet temperature in °F (or °C on some models). When the controller detects a fault, it replaces the temperature reading with an error code.

**Important distinction:** The GDM-23 has been produced across multiple generations:

- **Earlier GDM-23 models** use mechanical thermostats — these do NOT display error codes. If your GDM-23 has a simple dial or mechanical control (no digital readout), it fails silently.
- **GDM-23 with digital controller** (Ranco ETC or equivalent) — displays E1–E6 codes as described below.
- **GDM-23SSL** — stainless steel variant; same controller as standard GDM-23.
- **GDM-23-HC** — high-capacity variant; same error code structure.

---

## How to Fix It — GDM-23 Specific Error Codes

### E1 — Cabinet Temperature Sensor Failure

**What it means on the GDM-23:** The cabinet air sensor (mounted in the return air plenum, typically at the top rear of the interior) has failed or lost continuity with the controller.

**GDM-23 specific location:** On the GDM-23, the cabinet thermistor is accessible by removing the interior back panel. The sensor is mounted near the evaporator coil on a plastic bracket, with a 2-wire harness running to the control box at the top of the unit.

**Testing:** Disconnect the sensor connector from the control harness. Measure resistance:
- At room temperature (70°F): approximately **12,500 ohms** (12.5kΩ) — varies slightly by manufacturer
- If you measure open circuit or 0 ohms, replace the sensor

**GDM-23 replacement sensor:** True part **800271**. This is the standard True thermistor used across GDM product lines. Length: approximately 6 inches with a 24-inch wire lead.

**Time to repair:** 15–25 minutes. No refrigerant work required.

---

### E2 — Defrost Termination Sensor Failure

**What it means on the GDM-23:** The defrost termination sensor (clipped to the evaporator coil fins) has failed. Without this sensor, the defrost cycle cannot terminate when the coil reaches thaw temperature — it either runs too long or not at all.

**GDM-23 specific detail:** The GDM-23 uses a time-initiated, temperature-terminated defrost system. The defrost clock initiates defrost (typically 1–2 cycles per 24 hours, at preset times). The defrost termination sensor tells the controller when to end the cycle — usually when the coil surface reaches 48–55°F. If the sensor fails, the controller times out at the maximum defrost duration (typically 30 minutes) instead.

**Result:** With a failed defrost sensor, you'll see E2 and may notice the coil is heavily iced (defrost not completing properly) or product is slightly warm (defrost ran too long and the cabinet temperature spiked during each defrost cycle).

**Fix:** Replace defrost termination sensor — same **True 800271** thermistor as the cabinet sensor, re-clipped to the evaporator coil fins.

---

### E3 — High Temperature Alarm

**What it means on the GDM-23:** The cabinet temperature has risen above the acceptable range. On a unit set to 35°F, this typically triggers around 45–50°F.

**GDM-23 specific diagnosis:**

**Step 1 — Check the condenser coil.** On the GDM-23, the condenser coil is located at the bottom rear of the unit. This location makes it particularly vulnerable to dust, pet hair, and debris accumulation in high-traffic commercial environments. In many cases, pulling the unit away from the wall and cleaning the condenser with compressed air or a coil brush resolves the E3 alarm.

**Cleaning frequency:** Every 60–90 days in high-traffic environments. Monthly in stores with heavy foot traffic or dusty conditions (near bakeries, produce sections, etc.).

**Step 2 — Verify condenser fan.** The condenser fan is located adjacent to the condenser coil. If it's not running, the condenser can't reject heat. Check the fan motor: **True 800452** is the common condenser fan motor for many GDM models. Also check the fan motor starting capacitor if equipped.

**Step 3 — Check door gaskets.** A failing door gasket on the GDM-23 allows warm humid air into the cabinet, overworking the system and causing the coil to ice up from excessive moisture infiltration. The GDM-23 has a single gasket running around the full door opening. Test by running a dollar bill around the perimeter — it should have consistent resistance. Replace if worn or torn.

**Step 4 — Verify the evaporator fan is running.** Open the door. You should hear the evaporator fan. If it's silent, the fan motor has failed. True GDM-23 evaporator fan motor: **True 800452** (same part used for both fans on many GDM units — verify your model).

---

### E4 — Defrost Heater Fault / Defrost Timeout

**What it means on the GDM-23:** The defrost cycle ran for the maximum allowed duration without the defrost sensor reaching termination temperature. Possible causes: defrost heater failure, or the coil was so heavily iced that even a working heater couldn't thaw it in time.

**GDM-23 defrost heater:** The GDM-23 uses a glass-tube defrost heater mounted to the evaporator coil (wired in parallel on some configurations). The heater gets extremely hot — hot enough to melt ice — and failure is common after years of thermal cycling.

**How to test the heater:**
1. Disconnect power at the main disconnect
2. Access the evaporator section (remove interior back panel)
3. Disconnect the heater wires
4. Measure resistance across the heater terminals
   - A working heater should show **10–40 ohms** (depending on wattage)
   - Open circuit (∞ ohms) = failed heater

**GDM-23 defrost heater part numbers:**
- **True 993289** — 120V glass tube defrost heater (verify against your unit's wiring diagram inside the control box)
- **True 800270** — alternate defrost heater (used on some GDM-23 variants)

Always verify the correct part against the wiring diagram and serial plate inside the GDM-23 control panel. Ordering the wrong wattage heater will either under-defrost (too low) or overheat the cabinet (too high).

---

### E5 — Low Temperature Alarm

**What it means on the GDM-23:** Cabinet temperature has dropped below the low-alarm threshold. For a beer cooler set at 35°F, this typically triggers at 25°F.

**Common causes specific to GDM-23:**
- Thermostat setpoint is incorrectly programmed (setpoint too low, especially after a controller reset)
- Failed temperature controller running the compressor continuously
- Blocked thermistor — if the cabinet sensor is buried in ice or frost, it may read artificially low, tricking the controller into thinking the cabinet is warmer than it is and continuing to run the compressor

**Quick check:** Confirm the setpoint on the controller. On the Ranco ETC controller: press SET to display the current setpoint. If it reads -5°F when it should be 35°F, someone changed the setpoint or the controller EEPROM has corrupted. Reset to the correct value.

---

### E6 — Controller/Communication Error

**What it means on the GDM-23:** Internal controller fault or EEPROM memory corruption.

**First step:** Power cycle. Disconnect the GDM-23 from power (unplug or shut off at the outlet) for 5 full minutes, then restore power. If E6 clears and normal operation resumes, the error was a transient spike — likely from a power surge.

**If E6 returns immediately after power-up:** The Ranco ETC controller has failed. Replacement: **True 843009** or the equivalent **Ranco ETC-211000** temperature controller.

**Controller replacement on the GDM-23:** The control box is accessible from inside the unit at the top of the cabinet. You'll need to photograph or label the wiring before disconnecting (sensor wire, power wire, compressor contactor wire, defrost heater wire). The Ranco ETC-211000 replacement comes with instructions. Allow 45–60 minutes for the replacement including programming the new controller to the correct setpoint and defrost schedule.

---

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|--------------|
| [True 800271 Thermistor Sensor](https://www.amazon.com/s?ascsubtag=ecf-true-gdm-23-error-codes&k=True+800271+thermistor+sensor&tag=errorcodefixes-20) | E1 or E2 — cabinet or defrost sensor failure | $15–$30 |
| [True 800270 Defrost Heater](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-true-gdm-23-error-codes&tag=errorcodefixes-20) | E4 defrost fault — coil icing up, heater failed | $28–$55 |
| [True 800452 Evaporator Fan Motor](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-true-gdm-23-error-codes&tag=errorcodefixes-20) | Silent evaporator fan causes high cabinet temperature | $35–$70 |
| [Ranco ETC-211000 Controller](https://www.amazon.com/s?ascsubtag=ecf-true-gdm-23-error-codes&k=Ranco+ETC-211000+temperature+controller&tag=errorcodefixes-20) | E6 or erratic temperature control | $45–$85 |
| [True GDM Door Gasket Replacement](https://www.amazon.com/dp/B0FPF84HQP?ascsubtag=ecf-true-gdm-23-error-codes&tag=errorcodefixes-20) | Failed gasket causes moisture infiltration and E3 high temp | $35–$65 |
| [Refrigeration Coil Brush Set](https://www.amazon.com/s?ascsubtag=ecf-true-gdm-23-error-codes&k=refrigeration+condenser+coil+brush+cleaning&tag=errorcodefixes-20) | Clean condenser coil — most common cause of E3 high temp | $15–$25 |

---

## When to Call a Pro

- Any refrigerant-related diagnosis (low charge, leak) requires EPA 608 certification
- Compressor replacement (GDM-23 uses a hermetic compressor — typically an **Embraco or Tecumseh** — that requires refrigerant handling for replacement)
- If multiple components have failed simultaneously on a GDM-23 over 12 years old, evaluate replacement. A new GDM-23 retails for approximately $2,200–$2,800 and comes with a True warranty.

---

## Frequently Asked Questions

**Q: My GDM-23 runs but the back interior panel is covered in ice. What does that mean?**

A: Heavy ice buildup on the evaporator panel means the defrost system has failed. Either the defrost heater has burned out, the defrost timer/clock has failed, or the defrost termination sensor is giving a bad reading and allowing defrost to run too short. Manually initiate a defrost cycle first (see controller instructions). If the ice doesn't clear, the heater has likely failed — test with a multimeter as described in the E4 section.

**Q: How often should I clean the condenser on a GDM-23?**

A: At minimum, every 90 days. In high-traffic convenience stores or dusty environments, monthly. Dirty condensers are the leading cause of premature compressor failure on GDM units. This is a 15-minute task with a vacuum and compressed air — the highest-ROI maintenance you can do.

**Q: The GDM-23 light flickered and now shows E6. Is the whole controller fried?**

A: Not necessarily. Power fluctuations (surges, brownouts) can cause E6. Power-cycle the unit completely for 5 minutes and see if the error clears. If it does, the controller is fine. If E6 returns immediately, the controller has failed. A surge protector/line conditioner on GDM units in lightning-prone areas is worth the $40–$80 investment.
