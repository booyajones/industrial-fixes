---
title: "Lochinvar Knight Boiler Error Messages — Complete Display Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-26T18:15:00Z
modDatetime: 2026-04-26T18:15:00Z
slug: lochinvar-knight-boiler-error-codes
featured: false
draft: false
tags:
  - lochinvar
  - boiler
  - heating
  - hvac
description: "Lochinvar Knight boiler display messages explained: Flame Fail Ign, Air Pressure SW, Fan Speed, Flow Switch LWCO, Fatal Error. Step-by-step diagnosis and fix guide."
---

## Lochinvar Knight Boiler Error Messages

The **Lochinvar Knight** is a high-efficiency condensing gas boiler used extensively in residential and light commercial hydronic heating systems. Unlike many boilers that display numeric fault codes, the Knight uses a text-based LCD display to show fault messages directly — which is helpful, but only if you know what each message means and what to check.

This guide covers the most common Knight boiler display messages and how to resolve them.

---

## Common Knight Display Messages

| Display Message | Description |
|----------------|-------------|
| Flame Fail Ign | Ignition failure — no flame detected |
| Air Pressure SW | Combustion air pressure switch fault |
| Fan Speed | Combustion fan not reaching target RPM |
| Flow Switch/LWCO | Water flow or low water condition |
| Fatal Error | Control board or critical system fault |

---

## Flame Fail Ign — Ignition Failure {#flame-fail-ign}

**What it means:** The Knight attempted to ignite the burner but did not detect a stable flame signal within the trial-for-ignition period. This is the most common service call on Knight boilers.

**Common causes:**
- Gas supply issue (low pressure, interrupted supply, closed manual shutoff)
- Dirty or fouled igniter/flame sensor electrode
- Failed igniter
- Incorrect gas type (NG vs. LP — check the gas conversion kit)
- Venting problem — blocked vent, incorrect length, or improper termination
- Condensate drain blocked (condensate can back up into the combustion chamber on cold starts)

**Diagnosis and fix:**
1. Confirm gas supply. Check that other gas appliances in the building are operating. Locate the manual gas shutoff on the boiler supply line and confirm it is fully open (handle parallel to pipe).
2. Inspect the igniter/flame sensor assembly. On the Knight, the igniter and flame sensor are typically a combined spark/sense electrode. Remove the electrode (one screw), clean the sensing rod with fine emery cloth, and inspect the ceramic insulator for cracks.
3. Verify vent termination. Go outside and check both the combustion air intake and exhaust vent pipes. Remove any obstructions — bird nests, leaves, and ice are common.
4. Check the condensate trap and drain line. On condensing boilers, the trap collects combustion condensate. A blocked trap causes water to back up and quench ignition. Clean the trap and ensure the drain line slopes downward continuously.
5. Reset the boiler via the display menu (or by cycling power) and observe the ignition sequence. If the spark fires but no flame is established, suspect the gas valve. If there is no spark, suspect the igniter or control board.
6. Verify gas pressure with a manometer at the gas valve test port. Dynamic pressure should meet the specification on the rating plate.

---

## Air Pressure SW — Air Pressure Switch Fault {#air-pressure-sw}

**What it means:** The combustion air pressure switch has not closed (or has opened unexpectedly) to confirm adequate combustion air flow. The switch verifies that the combustion fan is generating sufficient pressure differential before allowing ignition.

**Common causes:**
- Combustion fan not running or running slowly (see Fan Speed fault)
- Blocked air inlet vent or exhaust vent
- Failed or stuck air pressure switch
- Pressure switch tubing cracked, disconnected, or blocked with condensate
- Boiler installed with excessive equivalent vent length

**Diagnosis and fix:**
1. Check for a simultaneous Fan Speed fault — if the fan is not running, the pressure switch will never close. Address the fan issue first (see Fan Speed section below).
2. Inspect the pressure switch tubing. This is a small rubber or silicone tube connecting the combustion fan housing to the pressure switch. If it is cracked, pinched, or has accumulated condensate inside, the switch cannot sense fan pressure correctly. Remove the tube, blow it clear, and inspect for cracks.
3. Measure the vent system against the Knight installation manual's equivalent length table. Excessive vent length reduces fan static pressure below the switch setpoint.
4. Test the pressure switch by disconnecting one tube fitting and applying gentle pressure with a small hand pump (or by blowing gently). You should hear/feel the switch click at the specified pressure.
5. Replace the pressure switch if it fails to actuate at its rated setpoint.

**Parts:**
- [Lochinvar Knight Air Pressure Switch Replacement](https://www.amazon.com/s?k=Lochinvar+Knight+boiler+air+pressure+switch+replacement&tag=errorcodefixes-20)

---

## Fan Speed — Combustion Fan Fault {#fan-speed}

**What it means:** The combustion fan (inducer blower) is not reaching the target speed within the expected time, or the fan speed feedback signal has been lost. The Knight's control board monitors fan RPM via a tachometer signal and will not proceed to ignition if the fan is not at the correct speed.

**Common causes:**
- Fan motor bearing failure (worn or seized)
- Fan blade damaged or obstructed
- Wiring harness to fan motor loose or corroded
- Fan motor capacitor failed (on PSC motor types)
- Control board fan output relay failed

**Diagnosis and fix:**
1. With the boiler powered off, try to spin the combustion fan blade by hand. It should rotate freely with minimal resistance. Grinding, stiffness, or no movement indicates bearing failure.
2. Inspect the fan blade for debris — insulation fragments, paper, and spider webs are common.
3. Check the wiring connector at the fan motor for loose pins, corrosion, or damage.
4. If the fan spins freely but the fault persists, the tachometer feedback circuit may be at fault. Check the tach signal wires between the fan and control board.
5. Fan motor replacement is a moderate repair. The motor is mounted inside the boiler cabinet and accessible after removing the front cover. Replacement motors are available from Lochinvar parts distributors.

**Parts:**
- [Lochinvar Knight Combustion Fan Motor](https://www.amazon.com/s?k=Lochinvar+Knight+boiler+combustion+fan+inducer+motor&tag=errorcodefixes-20)

---

## Flow Switch/LWCO — Flow or Low Water Condition {#flow-switch-lwco}

**What it means:** The boiler's flow switch has not confirmed adequate water circulation through the heat exchanger, or the Low Water Cut-Off (LWCO) device has detected dangerously low water level. Either condition prevents the burner from firing to protect the heat exchanger from overheating.

**Common causes:**
- System pump not running or failed
- Closed isolation valve in the hydronic loop
- Air-bound heat exchanger or system piping
- Failed flow switch
- Actual low water condition in a closed system (leak, or failed fill valve)
- LWCO probe fouled with scale or corrosion

**Diagnosis and fix:**
1. Verify the system pump is running. Listen for it, check the pump indicator LED if present, and verify it is receiving power.
2. Check all isolation valves in the system are fully open.
3. Check system pressure gauge. Low system pressure (below 12 PSI on most residential systems) indicates a low water condition. Add water via the fill valve until pressure reaches 15–20 PSI cold.
4. Bleed air from the highest point in the system and from any air-bound radiators or zones.
5. If pressure and flow are correct, test the flow switch by checking its terminals for continuity while the pump is running.
6. Inspect and clean the LWCO probe — scale buildup on the probe can prevent accurate water level sensing.

---

## Fatal Error — Critical Control Fault {#fatal-error}

**What it means:** The Knight's control board has detected an internal fault that prevents safe operation. This is the boiler's way of saying it has found something it cannot safely work around and requires professional attention.

**Common causes:**
- Control board (IQ boiler control) failure
- Stack/flue sensor failure (reading extreme values)
- EEPROM data corruption (after a power surge or lightning strike)
- Multiple simultaneous sensor faults

**Diagnosis and fix:**
1. Power-cycle the boiler completely — disconnect 120 VAC power, wait 60 seconds, and restore. A power surge can cause the controller to lock up in a Fatal Error state, and a cold restart often clears it.
2. Check all sensor connectors on the control board for loose pins or corrosion. Pay particular attention to the stack temperature sensor connector.
3. If the Fatal Error persists after a cold restart, record any additional information shown on the display (some controllers show a sub-code). Contact Lochinvar technical support at 1-800-LOCHINV or your authorized service contractor.
4. Control board replacement is typically required for a genuine Fatal Error. The IQ boiler control board is a field-replaceable part.

**Parts:**
- [Lochinvar Knight IQ Control Board](https://www.amazon.com/s?k=Lochinvar+Knight+IQ+boiler+control+board+replacement&tag=errorcodefixes-20)

---

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|-------------|
| Igniter / Flame Sensor Electrode | $35–$70 | [Amazon](https://www.amazon.com/s?k=Lochinvar+Knight+igniter+flame+sensor+electrode&tag=errorcodefixes-20) |
| Air Pressure Switch | $25–$55 | [Amazon](https://www.amazon.com/s?k=Lochinvar+Knight+air+pressure+switch&tag=errorcodefixes-20) |
| Combustion Fan / Inducer Motor | $180–$350 | [Amazon](https://www.amazon.com/s?k=Lochinvar+Knight+inducer+blower+motor&tag=errorcodefixes-20) |
| IQ Control Board | $400–$700 | [Amazon](https://www.amazon.com/s?k=Lochinvar+Knight+IQ+control+board&tag=errorcodefixes-20) |
| Condensate Trap Kit | $20–$40 | [Amazon](https://www.amazon.com/s?k=Lochinvar+Knight+condensate+trap&tag=errorcodefixes-20) |

---

## When to Call a Technician

Gas pressure testing, gas valve replacement, heat exchanger inspection, and combustion analysis require licensed HVAC/gas contractors. A Fatal Error that persists after a power cycle is almost always a control board issue — control board replacement should be performed by a Lochinvar-certified technician to ensure proper configuration and warranty compliance.

> **Pro tip:** The Knight displays a fault history accessible through the Advanced Settings menu. Before clearing any fault, navigate to the fault log and record the timestamp and fault description — this history is invaluable for diagnosing intermittent problems and for warranty documentation.

## Related Articles

- [Lochinvar Boiler Flame Fail — Causes & Fix](/posts/lochinvar-boiler-flame-fail/)
- [Lochinvar Boiler Error Code E01](/posts/lochinvar-boiler-error-code-e01/)
- [Lochinvar Boiler Error Code E02 — Ignition Failure](/posts/lochinvar-boiler-error-code-e02-ignition-failure/)
