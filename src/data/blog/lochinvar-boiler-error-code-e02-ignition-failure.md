---
title: "Lochinvar Boiler Error Code E02 — Ignition Failure Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: lochinvar-boiler-error-code-e02-ignition-failure
featured: false
draft: false
tags:
  - boiler
  - lochinvar
  - ignition
  - heating
description: "Lochinvar boiler error code E02 means ignition failure lockout on Knight, Crest, and SYNC series boilers — here's how to diagnose and fix it."
---

## Error Code: Lochinvar Boiler Error Code E02

**What it means:** Error code E02 on Lochinvar Knight, Crest, and SYNC series condensing boilers indicates ignition failure — the boiler attempted to ignite, the igniter energized, the gas valve opened, but the control board did not receive a valid flame signal within the required ignition trial period (typically 4 seconds). After two or three failed ignition attempts, the boiler locks out and displays E02.

Lochinvar Knight (WH/WB series), Crest (CH series), and SYNC (SNA series) boilers all use the same SMART System control board and share the same fault code structure, so E02 diagnosis is consistent across the entire Lochinvar condensing boiler line.

## Common Causes

- **Dirty or failed flame sensor** — The most common cause. The flame sensor rod (a stainless probe in the burner assembly) accumulates oxidation or condensate residue and can no longer send a sufficient microamp signal to the control board. Same mechanism as a furnace flame sensor but in a higher-condensate environment.
- **Failed hot surface igniter** — The igniter element has cracked or its resistance has drifted out of range. A healthy Lochinvar igniter glows orange-hot within 20–30 seconds of energizing. A failed igniter stays dark or glows faintly red and won't produce enough heat to light the gas.
- **Gas supply issue** — Low gas pressure at the boiler inlet, a closed shutoff valve, or a failed gas valve prevents fuel from reaching the burner. Check that the manual shutoff upstream of the boiler is fully open and that gas pressure meets Lochinvar's specifications (4–14" W.C. for natural gas inlet).
- **Blocked flue or condensate drain** — Lochinvar condensing boilers vent via PVC and produce significant condensate. A blocked vent pipe or a frozen condensate drain can prevent combustion air from reaching the burner or prevent the inducer from creating the proper combustion environment.
- **Failed gas valve** — The valve's internal solenoid has failed open or closed, preventing gas flow to the burner even when the control board commands it open.
- **Control board fault** — The board's ignition relay or flame sense circuit has failed, preventing either the igniter or gas valve from energizing, or preventing a valid flame signal from being read.

## Step-by-Step Fix {#step-by-step-fix}

1. **Confirm E02 and check for preceding faults.** On Lochinvar's SMART System display, navigate to the fault history (Menu → Fault History). E02 should appear as the most recent fault. Look for any preceding faults that might indicate the root cause (E05 = gas valve fault, E01 = pressure switch, etc.).

2. **Verify gas supply.** Confirm the manual gas shutoff to the boiler is fully open. On a Knight boiler, the shutoff is typically within 18" of the gas valve on the supply line. Check gas pressure at the boiler inlet service port — Knight boilers require 4–14" W.C. inlet natural gas pressure. If you have other gas appliances in the building, verify they light normally as a quick gas supply sanity check.

3. **Inspect the flame sensor.** The flame sensor is a single stainless rod mounted on a ceramic insulator, located inside the burner access panel on the front of the boiler. Disconnect the sensor lead wire, remove the single mounting screw, and pull the sensor. Inspect the rod for white, gray, or greenish oxidation. Clean with fine emery cloth (#400) until the rod is bright metal. Reinstall and test.

4. **Test igniter resistance.** With power off, disconnect the igniter leads and measure resistance across the igniter terminals with a multimeter. Lochinvar hot surface igniters (silicon nitride type) typically read 50–100 ohms when cold. A reading of OL (open) means the element is cracked or broken. Very low resistance (under 10 ohms) can also indicate a failing element. Part number **S001003001** (~$75) is the standard Lochinvar igniter.

5. **Observe the ignition sequence with the burner access panel slightly open (caution).** On a manual override attempt (or by initiating a call for heat at the thermostat), watch: (1) the inducer should start within 5 seconds of a heat call, (2) approximately 30 seconds later, the igniter should glow, (3) 4 seconds after the igniter glows, the gas valve should click open and flame should appear at the burner. If any step is absent, you've identified the failure point.

6. **Check the vent and condensate system.** Inspect the PVC flue pipe from the boiler to its termination at the exterior wall. Look for blockages, sagging sections (should slope minimum 1/4" per foot back to the boiler), or ice at the termination in cold weather. Check the condensate trap and drain line — a Lochinvar condensing boiler produces 1–2 gallons of condensate per hour at full fire. A blocked trap causes water to back up and can interfere with combustion.

7. **Replace the flame sensor if cleaning didn't resolve the fault.** Part number **S001001001** (~$40) is the OEM Lochinvar flame sensor. Replace any sensor that cleans up and still fails, or that has visible physical damage.

8. **Reset and test through two complete heat cycles.** After repair, navigate to Menu → Reset on the SMART System display and confirm E02 is cleared. Run the boiler through two full heat cycles (fire on, satisfied, fire on again) and verify no E02 recurrence.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|-------------|
| Lochinvar Flame Sensor | S001001001 | $35–$50 | [Amazon](https://www.amazon.com/s?k=S001001001+Lochinvar+Flame+Sensor&tag=errorcodefixes-20) \| Repair Clinic / Lochinvar dealer |
| Lochinvar Hot Surface Igniter | S001003001 | $70–$90 | [Amazon](https://www.amazon.com/s?k=S001003001+Lochinvar+Hot+Surface+Igniter&tag=errorcodefixes-20) \| Repair Clinic / Lochinvar dealer |
| Gas Valve (if failed) | Contact Lochinvar for model-specific | $180–$280 | [Amazon](https://www.amazon.com/s?k=Contact+Lochinvar+for+model-specific+Gas+Valve+%28if+failed%29&tag=errorcodefixes-20) \| Lochinvar dealer |
| SMART System Control Board | Contact Lochinvar for model-specific | $400–$650 | [Amazon](https://www.amazon.com/s?k=Contact+Lochinvar+for+model-specific+SMART+System+Control+Board&tag=errorcodefixes-20) \| Lochinvar dealer |
## When to Call a Professional

Gas valve replacement, gas line work, and combustion testing require a licensed HVAC/plumbing contractor in most jurisdictions. Lochinvar condensing boilers also require combustion analysis (CO2, O2, CO levels) after any repair that affects the combustion system — a proper combustion analysis requires a calibrated flue gas analyzer that most homeowners don't have. If E02 persists after flame sensor cleaning and igniter verification, the gas valve or control board is the likely culprit, and both require professional service. Do not continue to manually reset an E02 lockout and run the boiler — repeated failed ignition attempts dump raw gas into the combustion chamber, creating a hazard.

> **Pro tip:** Lochinvar Knight boilers in hard water areas frequently experience E02 from condensate drain blockage more than from flame sensor or igniter issues. The condensate is slightly acidic, and calcium from hard water precipitates out as the condensate evaporates, gradually plugging the drain trap. Flushing the condensate trap with a cup of white vinegar every six months keeps it clear and eliminates this entire class of E02 faults.
