---
title: "HVAC Pressure Switch Fault - Diagnosis and Fix Guide"
description: "Diagnose and fix pressure switch faults on gas furnaces. Covers draft inducer diagnosis, condensate drain blockage, cracked pressure switch hoses, and stuck switches."
pubDatetime: 2026-04-25T00:00:00Z
author: "Marcus Webb"
tags:
  - hvac
  - error-codes
---

A pressure switch fault is one of the most common gas furnace error codes, and also one of the most misdiagnosed. The pressure switch itself rarely fails. Most of the time, the fault traces back to a blocked condensate drain, a cracked hose, or a struggling draft inducer motor — all of which the pressure switch is correctly detecting as a real problem. This guide shows you how to trace the fault back to the actual root cause and fix it for good.

## What Does a Pressure Switch Fault Mean?

The pressure switch is a safety device that proves the draft inducer motor is running and creating sufficient negative pressure (draft) in the flue system before the gas valve is allowed to open. The furnace control sequence works like this:

1. Control board calls for heat.
2. Draft inducer motor starts.
3. **Pressure switch closes** (confirming negative pressure is established).
4. Hot surface igniter heats up.
5. Gas valve opens, burners light.
6. Flame sensor confirms flame.

If step 3 doesn't happen — if the pressure switch doesn't close within a few seconds of the inducer starting — the board sees a pressure switch fault and shuts down. The furnace won't allow gas to flow without proven draft, because unburned gas in a furnace with poor flue draft is a carbon monoxide risk.

**Flash codes for pressure switch fault:**

| Brand | Flash Code |
|-------|-----------|
| Carrier / Bryant | 31 |
| Lennox | 225 |
| Trane / American Standard | 3 flashes |
| Goodman / Amana | 3 flashes |
| Rheem / Ruud | 3 flashes |
| York / Coleman | 3 flashes |

## How to Fix It

Always start with the easiest and most common causes before assuming the switch itself has failed.

**Step 1: Check the Condensate Drain**

High-efficiency furnaces (90%+ AFUE) produce condensate — acidic water extracted from the exhaust gases. This condensate drains through a PVC pipe to a floor drain or condensate pump. When this drain clogs, condensate backs up into the inducer housing, and the water physically blocks the pressure port on the pressure switch.

**How to check and clear:**
- Locate the condensate drain line (typically a white PVC pipe, 3/4-inch to 1-inch diameter, running from the furnace to a floor drain or condensate pump).
- Disconnect the drain line at the furnace or at the first accessible coupling.
- Blow compressed air into the line or use a wet/dry vacuum to pull debris from the drain end.
- Inspect the inducer housing drain port — it's a small barbed fitting at the bottom of the inducer housing. Clear any debris or standing water.
- If there's a condensate pump, check that it's running and its reservoir isn't full.

A clogged condensate drain is the #1 cause of pressure switch faults on high-efficiency furnaces, particularly at the start of the heating season after the furnace has sat idle all summer.

**Step 2: Inspect the Pressure Switch Hoses**

The pressure switch connects to the inducer housing via one or two small rubber or plastic hoses (typically 1/4-inch to 3/8-inch ID). These hoses transmit the negative pressure signal from the inducer to the switch diaphragm.

**What to look for:**
- Cracks, splits, or holes anywhere along the hose length. Hold a hose up to a light and look for splits.
- Kinks or collapses — kinked hoses block pressure transmission.
- Disconnected ends — hoses pop off the barbed fittings if they soften with age.
- Water in the hose — condensate water in the pressure hose blocks the pneumatic signal and holds the switch open.

**Fix:** Remove the hoses, blow them clear, inspect for damage. Replace any cracked or kinked hoses. Use the same diameter replacement hose — hardware store or HVAC supply rubber tubing works fine.

**Step 3: Check the Draft Inducer Motor**

The draft inducer (also called the inducer fan or combustion air blower) is an electrically driven fan that creates the negative pressure the pressure switch monitors. If the inducer motor is running at reduced speed or not running at all, the pressure switch correctly stays open.

**How to diagnose:**
- Listen: when the furnace starts a heating cycle, you should hear the inducer spin up to a noticeably higher pitch than a typical fan. A worn motor may run at half speed or sound labored.
- Check motor current: clamp a meter around one of the inducer motor's power wires while it's running. Compare to the nameplate rated amps. A motor drawing 50% more than nameplate current is failing.
- Check the inducer wheel: remove the intake (usually a flexible duct connecting to the flue pipe) and inspect the blower wheel. A wheel packed with dust and debris spins less efficiently and creates less draft. Clean it with a brush.
- Check for a seized motor: with power off, spin the inducer wheel by hand. It should spin freely with no resistance. Resistance indicates bearing failure.

**Step 4: Test the Pressure Switch Itself**

After ruling out the condensate drain, hoses, and inducer motor, test the switch:

**Using a multimeter:**
- With power OFF and the hose disconnected from the switch, use a multimeter set to continuity/resistance mode on the switch terminals.
- The switch should be OPEN (no continuity) at rest.
- Apply suction to the hose port with your mouth (or a hand vacuum pump). The switch should CLOSE (continuity) when sufficient suction is applied.
- If the switch stays open regardless of suction, or if it's closed at rest (stuck closed — which can cause a different fault), replace it.

**Using a manometer:**
- Connect a digital manometer to the pressure switch hose port and check the pressure reading while the inducer runs.
- Compare to the pressure switch's rated trip point (printed on the switch body, typically -0.10" to -0.80" water column for draft switches).
- If the inducer creates adequate pressure but the switch doesn't close, replace the switch.

**Step 5: Check the Flue Vent**

A blocked or undersized flue vent reduces draft and can cause pressure switch faults even with a fully functional inducer. Check:
- Bird/animal nests in the flue termination cap (very common in shoulder seasons when the furnace hasn't run in months).
- Ice blockage at the flue termination (furnaces with horizontal PVC exhaust can ice over in extreme cold, especially if the termination is close to the ground).
- Undersized or overly long flue runs that create high static pressure the inducer must work against.

For induced-draft (80% efficiency) furnaces, check the metal flue pipe for disconnected joints or debris accumulation. For condensing (90%+ efficiency) furnaces with PVC exhaust, check both the combustion air intake and the exhaust for blockages.

**Step 6: Check for a Cracked Inducer Housing**

On older furnaces, the plastic or cast inducer housing can crack. A cracked housing allows air to bypass the pressure switch measurement point, so the switch never sees adequate negative pressure even with a functional inducer.

Inspect the inducer housing for cracks, particularly around the pressure port fitting. A cracked housing requires replacement.

## Parts You May Need

| Part | Use | Amazon Link |
|------|-----|-------------|
| Universal Furnace Pressure Switch (adjustable) | Replace failed pressure switch | [View on Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-hvac-pressure-switch-fault&tag=errorcodefixes-20) |
| Draft Inducer Motor (universal or OEM match) | Replace failed or weak inducer motor | [View on Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-hvac-pressure-switch-fault&tag=errorcodefixes-20) |
| Rubber Pressure Hose Tubing (1/4-inch ID) | Replace cracked or brittle pressure hoses | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hvac-pressure-switch-fault&k=1+4+inch+rubber+tubing+HVAC+pressure+hose&tag=errorcodefixes-20) |
| Condensate Pump (115V, 1/30 HP) | Replace failed condensate pump | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hvac-pressure-switch-fault&k=HVAC+condensate+pump+115V&tag=errorcodefixes-20) |
| Digital Manometer (HVAC) | Measure actual draft pressure at switch | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-hvac-pressure-switch-fault&k=digital+manometer+HVAC+draft&tag=errorcodefixes-20) |

## When to Call a Pro

- **Blocked flue or intake:** If a bird nest or ice buildup is inside the flue pipe where you can't reach it safely, a technician has the tools to clear it without damaging the vent.
- **Inducer motor replacement:** Replacing a draft inducer requires matching the correct motor (CFM, static pressure, electrical specs) to your specific furnace and sealing the housing properly. An incorrectly installed inducer can create carbon monoxide risks.
- **Cracked heat exchanger linked to pressure faults:** In some cases, a cracked heat exchanger allows exhaust gases to pressurize the heat exchanger cavity, interfering with inducer draft. This is a safety emergency requiring professional evaluation.
- **Repeated pressure switch faults on a new furnace:** May indicate a vent design problem (too long, too many elbows, incorrect diameter) that requires a professional evaluation and possible vent redesign.

## FAQ

**Q: My furnace has a 3-flash pressure switch code but the inducer is definitely running. What's wrong?**

A: If the inducer is clearly running (you can hear it and feel airflow from the flue), the most likely culprits in order are: (1) condensate backed up into the pressure switch hose, (2) a cracked or disconnected pressure hose, (3) a failed pressure switch diaphragm. Use a hand vacuum or manometer to verify suction is actually reaching the switch port.

**Q: Can I bypass a pressure switch to test if it's the problem?**

A: Technically yes — technicians sometimes temporarily jumper a pressure switch for diagnostic purposes. However, we do not recommend this for homeowners because a bypassed pressure switch allows the gas valve to open without proven draft. If the real problem is flue blockage, this creates a carbon monoxide risk. Test the switch properly with a manometer instead of bypassing it.

**Q: The pressure switch hose has water in it. Is that normal?**

A: No. Water in the pressure switch hose is a sign that condensate is backing up from the inducer housing. The immediate fix is to clear the hose and the condensate drain. Long term, make sure the condensate drain has a proper slope, there are no clogs in the drain line, and the condensate pump (if installed) is working.

**Q: I replaced the pressure switch and still getting a fault. Did I get a bad switch?**

A: Possibly, but more likely the underlying problem (condensate drain, cracked hose, inducer performance) wasn't fully resolved. A new switch won't solve a problem caused by insufficient draft. Go back and verify inducer suction with a manometer before concluding the new switch is defective.
