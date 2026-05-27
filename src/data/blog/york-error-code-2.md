---
title: "York 2-Blink Error Code — Pressure Switch Stuck Open Fix"
description: "A York 2-blink fault means the integrated furnace control did not see the pressure switch close after the inducer (draft motor) started running — meaning..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: york-error-code-2
featured: false
draft: false
tags:
  - york
  - hvac
  - error-codes
  - pressure-switch-stuck-open
---
## Quick answer

A York 2-blink fault means the integrated furnace control did not see the pressure switch close after the inducer (draft motor) started running — meaning the switch is "stuck open" from the board's perspective. On York (and the related Coleman, Luxaire, and Champion brands that share boards under the same parent company), this is most often a plugged condensate trap on 90% AFUE units, an aging pressure switch, or a tubing issue. York uses S1-prefix part numbers for most replacement components.

## What 2-blink means on a York

York alphanumeric and blink-coded boards both appear in the field — older units (pre-2010) use LED blink codes, newer units (S1-prefix board family) display alphanumeric codes on a small 7-segment display. The 2-blink code on a blink-code board corresponds to the alphanumeric "21" on a newer S1-board display. Both mean "Pressure Switch Stuck Open" — the board sees the switch open after the inducer should have established draft.

The pressure switch on a York furnace is a normally-open diaphragm switch. The board energizes the inducer for a defined startup window (typically 30 seconds), then checks the switch state. If the switch hasn't closed within that window, the board declares the 2-blink fault.

York's S1 board family has slightly different timing and retry behavior than other manufacturers' boards:
- First failure: log fault, retry inducer after 60-second purge
- Three consecutive failures: hard lockout requiring power cycle
- The board displays the most recent fault until cleared

The fault may resolve itself on a retry (a marginal switch might close on the second attempt), so the homeowner sometimes sees a furnace that "fails sometimes" rather than fails consistently. Don't ignore intermittent 2-blink — it's a switch that's going to fail completely soon.

## Common causes (ranked by frequency)

1. **Plugged condensate trap (90% AFUE)** — about 35%. York's trap design with the white PVC body collects biofilm rapidly, restricts draft.
2. **Aging pressure switch with drifted setpoint** — about 25%. Diaphragm flexibility degrades, switch's "close" pressure point rises above what normal draft can produce.
3. **Cracked or kinked switch tubing** — about 15%. The silicone hose has split, kinked, or melted against the inducer body.
4. **Inducer wheel buildup or dragging bearings** — about 10%. Reduced draft from compromised inducer.
5. **Vent restriction** — about 8%. Nest, ice, debris at termination or in horizontal run.
6. **Loose switch wiring** — about 4%. Spade terminals back off.
7. **Failed pressure switch (open contacts permanently)** — about 3%.

**Pro nugget:** York furnaces with the secondary heat exchanger on the bottom (downflow / horizontal applications) have a specific failure mode where the condensate trap exit tube develops a slow biofilm restriction that's invisible on inspection — the trap looks clean when you pop it off, water flows through it apparently fine, but during the inducer's pressurization the back-pressure from a partially-clogged exit tube starves draft. The fix isn't just cleaning the trap; it's also flushing the exit tube to the floor drain or condensate pump. Run a 50/50 vinegar flush from the trap down through the exit tube while the furnace is off, let it sit 30 minutes, then water-flush. I solved a chronic 2-blink call at a Phoenix downflow install by clearing the exit tube — the trap itself was fine but the downstream path was 80% restricted.

## Step-by-step fix

Before you start: power off at the furnace switch, gas off at the gas valve. Wait 5 minutes for inducer to fully stop.

1. **Confirm the code.** 2-blink on the LED, or "21" on alphanumeric display. Photograph the wiring diagram in the lower blower door.

2. **Inspect switch hose first (free fix).** Pull the silicone hose from both ends — inducer barb and switch port. Look for: kinks, melt marks, water droplets inside, scale residue. Blow through; should be wide open. Replace if anything questionable — silicone hose is cheap.

3. **Test switch state at rest with a meter.** Power off, wires off the switch, ohm across the terminals. Should read open (OL) at rest. If it reads anything else — including 0 ohms (stuck closed) or fluctuating values — replace.

4. **Clean the condensate trap (90% AFUE).** Pop off the U-shaped trap. Dump into a bucket. Flush with 50/50 vinegar-water, gentle brush on the orifices. Re-prime with fresh water.

5. **Flush the condensate exit path.** This is the step that often gets missed. After the trap, the exit line drains to a floor drain, condensate pump, or PVC trap on the floor. Pour 50/50 vinegar-water down the exit line while the furnace is off, let it sit 30 minutes, then water-flush. Any restriction downstream of the trap shows up as a draft starve at the inducer.

6. **Measure draft with a digital manometer.** Tee the manometer into the switch hose. Power on, call for heat, watch reading during inducer startup. York 90% AFUE inducers should pull -0.50" to -0.95" WC steady-state. 80% AFUE typically -0.30" to -0.60". Below your model's target = inadequate draft, keep looking.

7. **Inspect inducer wheel.** Power off. Disconnect inducer (typically four mounting screws and a harness). Look at squirrel cage blades — dust, web, scale. Wipe clean. Spin by hand — should be smooth and free.

8. **Walk the vent termination.** Outside, check the PVC vent for nests, ice, vegetation. Confirm concentric vents are clear at both inner and outer pipe.

9. **Replace the switch if needed.** York switch is part S1-02437196000 family — match exact OEM number stamped on the switch body. Bench-test new switch for open at rest before installing.

10. **Restore power and gas, verify with a full cycle.**

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Pressure switch (90% AFUE) | York S1-02437196000 | $55-95 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-2), [Amazon](https://www.amazon.com) |
| Pressure switch (80% AFUE) | York S1-024-37196-000 | $45-75 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-2), [Amazon](https://www.amazon.com) |
| Pressure switch hose (silicone) | Generic 1/4" silicone | $5-10 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-2) |
| Inducer motor assembly | York S1-32643951000 | $245-385 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-2), [Amazon](https://www.amazon.com) |
| Condensate trap | York S1-1NP0411 | $45-75 | [Amazon](https://www.amazon.com), [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-2) |
| Integrated furnace control (S1 board family) | York S1-03101264000 | $245-385 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-2), [Amazon](https://www.amazon.com) |
| Digital manometer | Testo 510i | $130-220 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=york-error-code-2) |

## When to call a professional

Call a licensed HVAC pro if:

- Replaced switch, cleaned trap, flushed exit line, and 2-blink returns. That points to deeper draft issues — vent sizing, inducer motor wear, or heat exchanger restriction.
- The furnace is a York Affinity or LX variable-speed communicating system. These have additional thermostat-based diagnostics requiring York's service tool.
- You smell flue gas anywhere — sweet/acrid smell near the furnace closet. Vent leak or partial blockage that needs CO testing.
- The unit is more than 18 years old. Aging vent and heat exchanger components often need professional evaluation.
- York warranty is in effect. Most factory warranties require licensed service for board or safety component replacement.

## FAQs

**Why does my York fail only on the coldest nights?**
Cold air is denser, increasing the back-pressure required for adequate draft. A switch and trap that work fine at 30°F may fail at 0°F because draft is marginal. Replace the switch and clean the system before the cold snap.

**Can I jumper the switch to test?**
No. Pressure switch is a primary CO safety. Jumpering means burners light into a potentially blocked vent. Use space heaters and fix in daylight.

**My switch ohms open at rest correctly. Why is 2-blink still appearing?**
Switch electrical is fine, but the switch may have a drifted close-pressure point — closes at -0.65" WC instead of the stamped -0.40" WC. Or the trap/tubing isn't allowing the inducer to develop full draft. Manometer measurement of actual draft is the next step.

**Difference between York 2-blink and 3-blink?**
2-blink is pressure switch stuck open (didn't close after inducer started). 3-blink on most York boards is pressure switch stuck closed (closed at startup before inducer ran). Opposite problems with different diagnostic paths.

**Do Coleman and Luxaire share these codes?**
Yes — York, Coleman, Luxaire, and Champion are all under the same parent and use the same boards and codes. Part numbers are typically identical. Cross-reference by S1-prefix part number stamped on the component.

## Related guides

- [Carrier 31 Error Code — Pressure Switch Did Not Open Fix](/posts/carrier-31-error-code)
- [Goodman 3-Flash Error Code — Pressure Switch Open Fix](/posts/goodman-3-flash-error-code)
- [Trane 3-Blink Error Code — Pressure Switch Fault Fix](/posts/trane-3-blink-error-code)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Carrier vs Trane furnaces compared](/posts/carrier-vs-trane-furnaces/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Goodman vs Bryant furnaces compared](/posts/goodman-vs-bryant-furnaces/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Mitsubishi vs Daikin mini splits](/posts/mitsubishi-vs-daikin-mini-splits/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best combustion analyzer (2026)](/posts/best-combustion-analyzer/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best HVAC manometer (2026)](/posts/best-manometer-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigerant gauge set (2026)](/posts/best-refrigerant-gauge-set/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best thermal imager for HVAC](/posts/best-thermal-imager-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigerant leak detector](/posts/best-refrigerant-leak-detector/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best boiler test kit](/posts/best-boiler-test-kit/)

## See Also

- [York 5 Flashes Error Code — Causes & Fix](/posts/york-5-flashes-error-code/)
- [York Chiller Fault Codes — Complete Troubleshooting Guide](/posts/york-chiller-fault-codes/)
- [York 3 Flashes Error Code — Causes & Fix](/posts/york-3-flashes-error-code/)
- [York Affinity Error Codes - What It Means and How to Fix It](/posts/york-affinity-error-codes/)
