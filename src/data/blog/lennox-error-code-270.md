---
title: "Lennox Error Code 270 — Flame Signal Lost Fix"
description: "Lennox error 270 — on G24M, G50, G60, SLP98V, EL296V boards — means the burners initially lit (flame established and the board confirmed it) but then the..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: lennox-error-code-270
featured: false
draft: false
tags:
  - lennox
  - hvac
  - error-codes
  - flame-signal-lost
---
## Quick answer

Lennox error 270 — on G24M, G50, G60, SLP98V, EL296V boards — means the burners initially lit (flame established and the board confirmed it) but then the flame signal dropped below threshold mid-run. The board reads the flame sensor's rectified microamps (µA DC) continuously while running; when it drops below about 0.6-1.0 µA depending on board firmware, the board declares flame loss, closes the gas valve, and retries. Three retries within an hour locks the unit out on 270. The most common single cause is a dirty flame sensor rod — same fix as any flame rectification issue, but the board's logic for "lost during run" vs "never proved at startup" is slightly different.

## What 270 means on a Lennox

Lennox alphanumeric code 270 displays as digits. The installer manual labels it "Flame Signal Lost After Established" or "Loss of Flame During Run." On boards displaying as Lennox iComfort or Bryant/Carrier-cousin systems with a thermostat readout, you may see it as "Flame Dropout" or with a text message.

The flame sensor is a single metal rod (usually nickel-chromium or Kanthal alloy) projecting into the leftmost burner flame path. AC voltage is applied between the rod and the burner ground; ionized hot flame conducts the AC asymmetrically (flame rectification), producing a small DC current that the board measures in microamps. Lennox boards expect:
- During startup: signal must rise above threshold within 4 seconds of trial-for-ignition or board declares "no ignition" (typically error 200, not 270).
- During run: signal must remain above threshold continuously. A drop below threshold for more than ~0.8 seconds triggers flame loss logic.

The board's response to flame loss:
1. Immediately closes the gas valve
2. Logs the flame loss event
3. Begins purge cycle
4. Retries ignition automatically
5. After three flame-loss-during-run events in a 60-minute window, locks out on error 270.

Error 270 is a hard lockout — requires power cycle to clear. This is different from a single flame loss followed by a successful retry; the code only appears after the lockout threshold.

## Common causes (ranked by frequency)

1. **Oxidized flame sensor rod** — about 50%. The rod's conducting surface degrades from combustion byproducts. The signal starts marginal, then drops mid-cycle as the burner cabinet temperature shifts the conduction characteristics.
2. **Cracked sensor ceramic insulator** — about 15%. The ceramic at the rod's base cracks, sensor intermittently shorts to ground or loses isolation.
3. **Burner cell drift / partial blockage** — about 10%. Spider webs, dust, or rust scale in burner Venturis change flame shape; sensor sees less flame.
4. **Gas pressure dropping mid-cycle** — about 8%. Inlet gas pressure marginal; when other gas appliances run (water heater, range), pressure drops and burner flame shrinks below sensor.
5. **Ground path issue** — about 5%. The burner assembly to cabinet ground bond is degraded — rust, paint, loose mounting. Flame rectification needs solid ground.
6. **Failed sensor rod** — about 5%. Cleaning doesn't help; replacement needed.
7. **Wrong gas type configuration** — about 3%. Recent service didn't change orifices or pressure for actual fuel (NG vs LP), flame characteristics off.
8. **Vent / combustion air issue** — about 4%. Inadequate combustion air shifts flame, sensor sees marginal conduction.

**Pro nugget:** Lennox SLP98V and EL296V units in homes that also have a gas water heater or gas range can see error 270 specifically when the water heater or range fires up mid-furnace-cycle. The shared gas line drops pressure briefly, the burner flame shrinks slightly, sensor µA drops below threshold for the critical second, and the board declares flame loss. After 3 events the lockout fires. Diagnosis: install a manometer on the furnace gas valve inlet, observe inlet pressure during a heat call while someone runs hot water or lights the range. If you see inlet pressure drop below 5" WC for natural gas (or 11" WC for LP) during co-incident appliance use, you have a gas supply sizing problem — line is undersized for combined loads. Fix is either upsize the gas line or the meter regulator, not a sensor cleaning.

## Step-by-step fix

Before you start: power off at the furnace switch and gas off at the gas valve. The flame sensor is hot immediately after a cycle.

1. **Confirm the code on the display.** "270" digits.

2. **Remove and clean the flame sensor first.** This is the most likely fix and costs nothing.
   - Remove the burner cover
   - Locate the flame sensor: single thin rod on the leftmost burner, with one wire connection (not the HSI, which is thicker with two wires)
   - Disconnect the sensor wire (note orientation)
   - Remove the sensor mounting screw
   - Pull the sensor straight out
   - Inspect rod tip and full insertion length — coating, discoloration, deposits
   - Wrap with 0000-grade steel wool and pull lengthwise base to tip several times
   - Wipe clean with lint-free cloth (don't touch with bare fingers)
   - Inspect ceramic for cracks
   - Reinstall, reconnect

3. **Measure flame µA with a meter.** With everything reinstalled, put a multimeter set to µA DC in series with the sensor wire. Restore gas and power. Call for heat. Watch the µA reading once flame is established. Target on a Lennox: 4-6 µA on a clean sensor. Below 2 µA = marginal; below 1 µA = your problem.

4. **Verify ground bond.** Power off. Inspect the burner assembly mounting screws and the cabinet ground stud. Tighten anything loose. Use a Sharpie or paint pen to mark the connection (helps next service confirm).

5. **Measure gas inlet pressure at the gas valve.** Tee a digital manometer into the inlet pressure tap on the gas valve (the tap nearest the gas line, marked "IN" or "INLET"). Restore gas, call for heat, observe pressure during a heat cycle. NG should hold 5-7" WC; LP should hold 11-13" WC. Pressure dropping below those minimums during operation indicates a supply issue.

6. **Run a co-incident load test.** With furnace running, have someone turn on a hot water tap (water heater fires), or run the range. Watch furnace inlet pressure. A drop of more than 1" WC during co-incident operation indicates undersized gas piping.

7. **Inspect burner cells.** Look at each cell with a flashlight while the burners run. Flames should be steady, blue with light yellow tips, all cells lit, no flame impingement on heat exchanger entry. Wavering, lifting, or cells partially lit suggests a deeper combustion issue.

8. **Replace the sensor if cleaning didn't fix it.** Order Lennox flame sensor part number for your specific model. Confirm by ohm-testing the rod (should be a low-impedance connection from terminal to rod tip — verify no internal break).

9. **After repair, verify with a full operating cycle and observe for 15-20 minutes.** The 270 code requires three flame loss events to lock out, so a 15-20 minute observation should reveal whether the issue is fixed or recurring.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Flame sensor (Lennox) | Lennox 24L8501 | $35-55 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lennox-error-code-270), [Amazon](https://www.amazon.com) |
| Flame sensor bracket | Lennox 50J27 | $25-45 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lennox-error-code-270) |
| Hot surface ignitor (nitride) | Lennox 27W92 / 78H56 | $45-75 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lennox-error-code-270), [Amazon](https://www.amazon.com) |
| Burner assembly (single cell) | Lennox 10G73 | $45-85 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lennox-error-code-270), [Amazon](https://www.amazon.com) |
| Gas valve (Honeywell VR8205 for Lennox) | Lennox 14T70 | $245-345 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lennox-error-code-270), [Amazon](https://www.amazon.com) |
| Integrated control board (varies by model) | Lennox 81W03 / 67M41 | $295-680 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lennox-error-code-270), [Amazon](https://www.amazon.com) |
| Digital manometer | Testo 510i / Fieldpiece SDMN6 | $130-275 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lennox-error-code-270) |
| 0000-grade steel wool | Generic | $5-8 | [Amazon](https://www.amazon.com), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=lennox-error-code-270) |

## When to call a professional

Call a licensed HVAC pro for 270 if:

- You cleaned and replaced the sensor and 270 returns. That points to combustion or gas pressure issues requiring combustion analyzer testing.
- You measured gas pressure drop below minimum during co-incident appliance operation. Gas piping or meter regulator sizing is a licensed gas fitting task.
- You see yellow flame, lifting flame, or sooting at any burner cell. Combustion problem requiring analyzer testing — not a sensor cleaning issue.
- The furnace is a Lennox iComfort communicating system. The thermostat may show additional diagnostic info accessible only via iComfort service tools.
- The unit is under warranty.
- You don't have a digital manometer for gas pressure testing. Pressure measurement is critical for diagnosing intermittent 270; without it, you're guessing.

## FAQs

**Why does my Lennox throw 270 only when the gas water heater is running?**
Gas supply sizing. The shared gas line, meter regulator, or both can't supply both appliances at peak demand. Furnace inlet pressure drops below minimum, burner flame shrinks, sensor signal drops, eventually three flame loss events lock out as 270.

**How often should I clean my Lennox flame sensor?**
Every 1-3 years on average. Annual cleaning in hard water areas, coastal homes, or with high indoor humidity. Add it to your annual furnace service.

**Will a stronger sensor signal prevent 270?**
Yes — a clean rod gives 4-6 µA reading. Once below 2 µA, you're in marginal territory where small flame variations can trip the threshold. Keep the sensor reading well above threshold.

**Can I just power-cycle every time 270 comes up and call it good?**
You can, but the flame loss events are real. Whatever's causing the flame to drop will keep happening. You're treating the symptom, not the cause. Fix the underlying issue.

**Difference between 270 and 200?**
200 = no ignition at startup (HSI lit, gas opened, no flame proved within trial window). 270 = flame proved at startup but lost during run (after 3 events in 60 min). Different timing, different diagnostic implications.

## Related guides

- [Lennox Error Code 224 — HSI Relay Failure Fix](/posts/lennox-error-code-224)
- [Lennox Error Code 240 — Ignitor Failed Fix](/posts/lennox-error-code-240)
- [Goodman 8-Flash Error Code — Low Flame Signal Fix](/posts/goodman-8-flash-error-code)

## See Also

- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Error Code 223 — Causes & Fix](/posts/lennox-error-code-223/)
- [Lennox iComfort Error Code 225 — Communication Fault Fix Guide](/posts/lennox-icomfort-error-code-225/)
- [Lennox Error Code 231 — Causes & Fix](/posts/lennox-error-code-231/)
