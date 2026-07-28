---
title: "Manitowoc E21 Error Code - Causes & Fix"
description: "E21 means the T1 temperature sensor circuit has failed or is reading abnormally. The most common fix is reconnecting or replacing the sensor."
pubDatetime: 2026-06-19T10:37:22Z
modDatetime: 2026-06-19T10:37:22Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - manitowoc
money_part: "Manitowoc T1 evaporator temperature sensor"
most_likely_cause: "loose, corroded, or failed T1 temperature sensor connector"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the machine and check whether the code clears after a full restart."
  - "Inspect the T1 sensor connector for loose seating, bent pins, corrosion, or visible water intrusion."
part_price: "$40-80"
---

## What this code means
The E21 code on Manitowoc Indigo and related ice machines indicates a T1 temperature sensor issue. The control board is seeing an abnormal or failed reading from the evaporator temperature sensing circuit. This is a sensor fault code, not a general cleaning or refrigeration problem. The machine has detected that the T1 sensor signal is out of range, missing, or electrically incorrect.

Because the code points to the sensor circuit itself, the problem is usually a failed sensor, loose or corroded connector, damaged wiring between the sensor and the control board, or a failed input on the board. Ice machines operate in wet, cold environments that can cause connectors to corrode and wiring insulation to crack over time. The code will not clear until the sensor circuit reads correctly again.

## Before You Replace Anything

Techs sometimes replace the control board first when the real problem is a corroded or loose sensor connector. Always ohm-check the sensor and inspect the harness connector for damage or poor pin contact before condemning the board.

## Common Causes

- **Loose, corroded, or damaged sensor connector (~40%)** Wet environments cause corrosion or pin spread at the T1 sensor plug, breaking continuity or creating intermittent contact that the board reads as a sensor fault.
- **Failed T1 temperature sensor (~35%)** The sensor itself can drift out of spec or open internally, causing the control board to log an E21 fault.
- **Broken or shorted sensor wiring harness (~15%)** Vibration, water intrusion, or physical damage can break insulation or create an open circuit between the sensor and the board.
- **Control board input failure (~10%)** If the sensor and wiring test good but the code persists, the T1 input channel on the board has failed and the board needs replacement.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the code clear after a full power-cycle and restart?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may have been a transient glitch. Monitor the machine through one full ice cycle. If the code returns, proceed to connector and sensor checks.<br><strong>No:</strong> The fault is persistent. Move on to inspect the T1 sensor connector and harness for damage or corrosion.</div>
</details>

<details class="dtree"><summary>Is the T1 sensor connector firmly seated with no visible corrosion or bent pins?</summary>
<div class="dtree-body"><strong>Yes:</strong> The connector is mechanically sound. Test the sensor resistance and harness continuity with a multimeter.<br><strong>No:</strong> Clean corrosion with contact cleaner, straighten pins, and reseat the connector firmly. Restart and check whether the code clears.</div>
</details>

<details class="dtree"><summary>Does the T1 sensor resistance match the manufacturer's temperature-resistance chart for the current evaporator temperature?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is reading correctly. Check harness continuity back to the control board. If the harness is good, suspect a failed board input.<br><strong>No:</strong> The sensor has drifted or failed. Replace the T1 sensor and retest.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the machine** at the disconnect switch and verify zero voltage before working on any electrical components.
2. **Locate the T1 temperature sensor** on the evaporator assembly and trace its harness back to the control board connector.
3. **Inspect the sensor connector** for loose seating, bent or spread pins, corrosion, or cracked insulation at the plug body.
4. **Clean and reseat the connector** if you find corrosion or poor contact. Use electrical contact cleaner and make sure pins make firm contact.
5. **Ohm-test the sensor** at the harness connector with a multimeter and compare the reading to your model's temperature-resistance table in the service manual.
6. **Check harness continuity** from the sensor plug all the way to the control board pins to rule out an open or intermittent wire.
7. **Replace the T1 sensor** if it reads out of spec or open, then power on and run a test cycle to verify the code clears.
8. **Replace the control board** if the sensor and wiring test correctly but the E21 code persists after restarting the machine.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Manitowoc T1 evaporator temperature sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e21-error-code&k=Manitowoc+T1+evaporator+temperature+sensor&tag=errorcodefixes-20) \| Verify compatibility with your exact model number before ordering. |
| Sensor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e21-error-code&k=Sensor+wiring+harness&tag=errorcodefixes-20) \| Order only if the harness is physically damaged or corroded beyond cleaning. |
| Manitowoc control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e21-error-code&k=Manitowoc+control+board&tag=errorcodefixes-20) \| Replace only after confirming the sensor and harness test good but the fault remains. |

## When to Call a Pro

Call a qualified refrigeration technician if you are not comfortable working with refrigeration controls, multimeter diagnostics, or electrical troubleshooting in a wet commercial environment. The T1 sensor sits on the evaporator inside the sealed refrigeration system, and while the sensor itself is accessible, any work that accidentally damages refrigerant lines or requires pressure testing demands an EPA-certified tech with recovery equipment. If you replace the sensor and wiring but the code persists, the control board input is likely failed and board replacement on a commercial ice machine is best left to a service professional who can verify correct operation of all safety and refrigeration circuits after the repair.

**Rough cost:** A pro service call runs about $150-350.
