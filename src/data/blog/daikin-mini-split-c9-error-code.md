---
title: "Daikin C9 Error Code - Causes & Fix"
description: "C9 means faulty suction air temperature sensor in the indoor unit. Most common fix: clean and reseat the sensor connector."
pubDatetime: 2026-06-30T09:49:07Z
modDatetime: 2026-06-30T09:49:07Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin suction air thermistor (indoor unit)"
most_likely_cause: "Loose or dirty sensor connector"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Clean dust from the sensor bulb tip with a soft cloth"
  - "Remove and firmly reseat the sensor jack on the PCB"
  - "Inspect the sensor wire for visible cuts or disconnections"
part_price: "$20-50"
no_buy_pct: "60%"
---

## What this code means
The C9 error code on a Daikin mini split signals that the suction air temperature sensor (thermistor) in the indoor unit is reading abnormal values. The system uses this sensor to detect return air temperature. When the resistance value falls outside the expected range for the current temperature, the control board cannot accurately read air temperature and will prevent the compressor and outdoor unit from starting.

In non-inverter models the code is labeled as room temperature thermistor abnormality, while inverter models define it as suction air temperature sensor fault. Either way, the indoor unit becomes blind to air temperature and the AC will not cool. The system cannot operate safely without accurate temperature readings from this sensor.

## Before You Replace Anything

Many people replace the indoor PCB first when the actual problem is a disconnected wire or dirty connector at the sensor. Always test the thermistor resistance with a multimeter and inspect the wiring before replacing any circuit board.

## Common Causes

- **Loose or dirty connector (~35%)** The sensor jack is not plugged firmly into the PCB or the connector pins are dirty or corroded, breaking the circuit.
- **Failed thermistor (~30%)** The sensor itself has degraded and its resistance no longer changes with temperature or reads zero ohms (shorted).
- **Dust accumulation (~15%)** The sensor bulb tip is covered in dust, insulating it from the air and causing false temperature readings.
- **Disconnected or cut wire (~12%)** The sensor lead wire is disconnected or cut, often by rodents chewing through the insulation.
- **PCB foil peeling (~5%)** The foil at the thermistor connecting point on the indoor PCB has peeled off, breaking the circuit path.
- **Indoor PCB fault (~3%)** The circuit on the indoor board that reads the thermistor signal is faulty and cannot process the sensor data.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the sensor wire have any visible cuts or damage?</summary>
<div class="dtree-body"><strong>Yes:</strong> The wire is broken and must be repaired or the sensor replaced. Call a technician to splice the wire or install a new sensor.<br><strong>No:</strong> The wire is intact. Proceed to clean the sensor bulb and check the connector at the PCB.</div>
</details>

<details class="dtree"><summary>After reseating the connector, does the error clear when you power on?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was a loose connection. Monitor the system to confirm cooling starts and the error does not return.<br><strong>No:</strong> The connector was not the issue. Test the sensor resistance with a multimeter to determine if the thermistor has failed.</div>
</details>

<details class="dtree"><summary>Does the sensor read approximately 10 kΩ at room temperature and decrease when warmed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor is working correctly. The problem is likely a peeled PCB foil or a faulty board circuit. Call a pro to inspect and repair the PCB.<br><strong>No:</strong> The sensor is out of value or shorted. Replace the suction air thermistor.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** and unplug the mini split before starting any work.
2. **Open the front cover** and remove the filters to access the indoor unit interior. Locate the thin black sensor wire with a bulb tip behind the filters.
3. **Clean the sensor bulb** gently with a soft cloth if dust has accumulated on it. Dust acts as insulation and prevents accurate temperature readings.
4. **Remove the indoor unit cover** to access the PCB. Locate the sensor connector on the board and unplug it, then plug it back in firmly. Check for corrosion or dirt on the pins.
5. **Inspect the sensor wire** for cuts, disconnections, or rodent damage along its entire length from the bulb to the PCB.
6. **Test the thermistor resistance** with a digital multimeter set to 20 kΩ range. Disconnect the sensor from the PCB first (never test while connected). Place probes on the two terminals. At room temperature (20-25°C) it should read approximately 10 kΩ. Warm the sensor with your hand and confirm the resistance decreases. If it reads zero ohms or does not change, the sensor is faulty.
7. **Inspect the PCB foil** at the thermistor connection point for peeling or breaks. If found, solder the connection to restore the circuit. If the sensor tests good and the PCB shows no peeling, the board circuit may be faulty.
8. **Replace the sensor** if resistance testing shows it is out of value or shorted. Install the new thermistor in the same location and route the wire identically to the original.
9. **Restore power** and turn on the system. The C9 error should clear and the outdoor unit should start. Verify cooling begins and monitor for 15-20 minutes to confirm the error does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin suction air thermistor (indoor unit) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-c9-error-code&k=Daikin+suction+air+thermistor+%28indoor+unit%29&tag=errorcodefixes-20) \| Match the part number to your specific Daikin model; resistance spec is typically 10 kΩ at 25°C. |
| Daikin indoor unit PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-c9-error-code&k=Daikin+indoor+unit+PCB&tag=errorcodefixes-20) \| Only replace if the sensor tests good and PCB foil repair fails; verify model compatibility. |

## When to Call a Pro

Call a licensed HVAC technician if you are uncomfortable working inside the indoor unit or testing electrical components with a multimeter. Refrigerant systems require EPA certification to service, and while the C9 code does not directly involve refrigerant, the repair requires opening the unit and working with control wiring. A pro should handle any PCB repair or replacement, especially soldering peeled foil traces. If you have tested the sensor and found it working correctly but the error persists, the indoor board circuit is likely faulty and requires professional diagnosis. Technicians have the tools to verify board signals and can source the correct replacement PCB for your model.

**Rough cost:** A pro service call runs about $150-300.
