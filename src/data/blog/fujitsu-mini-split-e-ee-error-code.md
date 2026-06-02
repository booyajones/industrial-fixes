---
title: "Fujitsu E:EE Error Code - Causes & Fix"
description: "E:EE on Fujitsu mini-splits is a placeholder. Interrogate the controller to reveal the real fault, often EE:00 (high pressure)."
pubDatetime: 2026-05-30T23:35:55Z
modDatetime: 2026-05-30T23:35:55Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - fujitsu
---

## Fujitsu E:EE Error Code — What It Means

When you see E:EE or EE:EE on a Fujitsu hard-wired remote controller, you are not looking at the actual fault code. It is a generic fault-display placeholder. You must enter interrogation mode on the controller to read the underlying code and address. Once interrogated, the most common result is EE:00, which means the system has detected a high-pressure problem in the refrigerant circuit.

High pressure in a mini-split typically points to restricted airflow across the outdoor coil, a failed condenser fan, a dirty coil, overcharge, or a blockage somewhere in the refrigerant circuit. The fix depends entirely on what the interrogation reveals and what physical condition you find during inspection.

[Jump to Fix](#fix)

## Common Causes

- **Dirty or blocked outdoor coil** Leaves, grass clippings, cottonwood, or mud caked on the condenser fins restrict airflow and drive head pressure up fast.
- **Failed outdoor fan motor or capacitor** If the condenser fan is not spinning or runs slowly, the coil cannot reject heat and pressure climbs.
- **Refrigerant overcharge** Too much refrigerant in the system raises condensing pressure beyond the switch or sensor setpoint.
- **Blocked liquid line or filter drier** A restriction downstream of the condenser traps refrigerant and raises outdoor coil pressure.
- **Non-condensable gas in the system** Air or other gases contaminate the refrigerant and cause abnormally high head pressure even when airflow is good.
- **Faulty high-pressure sensor or switch** The sensor itself may be out of calibration or shorted, signaling high pressure when conditions are normal.

## Step-by-Step Fix {#fix}

1. **Turn the unit off** at the breaker or disconnect and confirm you have a Fujitsu hard-wired remote controller where E:EE is displayed.
2. **Enter interrogation mode** by pressing the specified button combination for your controller family (consult your controller manual) to reveal the underlying fault code and unit address.
3. **Record the actual code.** If the display shows EE:00, you are diagnosing a high-pressure fault and can proceed to airflow and refrigerant checks.
4. **Inspect the outdoor unit.** Clean the coil with coil cleaner and a soft brush, remove any debris blocking airflow, and verify the condenser fan spins freely and runs at full speed when powered.
5. **Check refrigerant charge and pressures** using manifold gauges on the service ports. Compare readings to the nameplate subcooling or superheat target for your model. If pressures are high across the board, recover refrigerant to the correct charge or check for non-condensables.
6. **Test the high-pressure switch or sensor** with a multimeter if airflow and charge both check out. Replace the sensor if it reads open or out of range when pressure is normal.
7. **Exit interrogation mode** by pressing the same button combination again, restore power, and monitor the system through a full cooling cycle to confirm the fault does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor fan motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-ee-error-code&k=Outdoor+fan+motor&tag=errorcodefixes-20) \| Match the frame size, voltage, and RPM on the nameplate of the original motor. |
| Fan run capacitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-ee-error-code&k=Fan+run+capacitor&tag=errorcodefixes-20) \| Check the microfarad rating printed on the old capacitor and replace with the same value. |
| High-pressure switch or sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-ee-error-code&k=High-pressure+switch+or+sensor&tag=errorcodefixes-20) \| Order by your indoor or outdoor unit model number to make sure correct connector and thread. |
| Coil cleaning solution | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fujitsu-mini-split-e-ee-error-code&k=Coil+cleaning+solution&tag=errorcodefixes-20) \| Use a foaming coil cleaner safe for aluminum fins, not acid-based household cleaners. |

## When to Call a Pro

Call a licensed HVAC technician if you cannot safely access the controller's interrogation mode, if you see EE:00 but airflow and the fan both look normal, or if manifold pressures indicate overcharge or non-condensables. Refrigerant work requires EPA certification, recovery equipment, a vacuum pump, and refrigerant scales. If the fault code you retrieve is anything other than EE:00, the diagnosis tree changes completely and professional tools and software are usually required to pinpoint the failure. Do not guess at charge or replace boards without confirming the root cause first.
