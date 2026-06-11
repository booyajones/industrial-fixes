---
title: "Siemens G120 A05002 Fault - Causes & Fix"
description: "A05002 on a Siemens G120 VFD is a power module overtemperature alarm. Most often fixed by improving airflow and checking cooling fans."
pubDatetime: 2026-06-02T10:27:09Z
modDatetime: 2026-06-02T10:27:09Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 cooling fan"
---

## Siemens G120 A05002 Fault — What It Means

A05002 on a Siemens SINAMICS G120 is an alarm, not a fault trip, indicating power module overtemperature. The drive has detected that the power section temperature has exceeded safe operating limits. For air-cooled power units, Siemens documentation cites a threshold of 42 °C air intake temperature with 2 K hysteresis. Because this is an alarm rather than a fault, the drive may continue to run but will likely trip if the condition worsens. The alarm warns you that the power module is too hot and needs cooling or load reduction before damage occurs.

[Jump to Fix](#fix)

## Common Causes

- **Ambient temperature too high** The enclosure or room temperature around the drive exceeds the thermal limits for the G120, causing intake air to overheat the power module.
- **Restricted airflow or blocked ventilation** Dust-clogged filters, obstructed vents, or insufficient spacing around the drive prevent cooling air from flowing through the heatsink and power section.
- **Cooling fan inoperative or slow** The internal or cabinet cooling fan has failed, is running too slowly, or is not receiving power, reducing heat removal from the power module.
- **Load or duty cycle too high** The connected machine is drawing more current than the drive's thermal design can handle continuously, causing excessive heat dissipation in the power section.
- **Motor power and drive sizing mismatch** The motor power setting (p0307) does not match the inverter power (r0206), leading to thermal overload of the power module.
- **Pulse frequency set too high** A high switching frequency increases switching losses in the power semiconductors, generating more heat than the cooling system can remove.

## Step-by-Step Fix {#fix}

1. **Verify ambient and intake air temperature** at the drive and inside the enclosure using a thermometer, and compare readings to the G120's environmental limits in the manual.
2. **Inspect the airflow path** by checking filters, vents, heatsinks, and cabinet fans for dust buildup, blockages, or obstructions, and clean or clear as needed.
3. **Check the cooling fan** for operation by visually confirming it spins freely and moves air when the drive is powered, and test the fan power supply if it is not running.
4. **Review the load profile** by monitoring motor current and duty cycle to confirm the connected machine is not overloading the drive thermally during normal or peak operation.
5. **Check drive and motor power settings** by comparing parameter p0307 (motor power) with r0206 (inverter power rating) to confirm they match and the drive is correctly sized for the application.
6. **Reduce pulse frequency if possible** by lowering the switching frequency setting in the drive parameters if the application tolerates the change and noise is acceptable.
7. **Reset the alarm** using the control panel or parameter reset function, then monitor intake and module temperatures over the next operating cycle to confirm the condition does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05002-fault-code&k=Siemens+G120+cooling+fan&tag=errorcodefixes-20) \| Replacement fan for the specific G120 frame size if the original fan is inoperative or slow. |
| Cabinet ventilation fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05002-fault-code&k=Cabinet+ventilation+fan&tag=errorcodefixes-20) \| External enclosure fan or filter kit to improve airflow around the drive when ambient cooling is insufficient. |
| G120 power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-a05002-fault-code&k=G120+power+module&tag=errorcodefixes-20) \| Replacement power section if thermal damage has occurred and overtemperature alarms persist after airflow and load corrections. |

## When to Call a Pro

Call a qualified electrician or drive technician if the alarm returns after you have cleared obstructions and verified fan operation, if you cannot safely measure temperatures or access the enclosure, or if the load and power settings are beyond your familiarity with VFD commissioning. A professional can perform thermal imaging, verify parameter configuration, check for power module damage, and confirm that the drive is sized correctly for the application.

## See Also

- [Siemens Micromaster F0071 - Causes & Fix](/posts/siemens-micromaster-vfd-f0071-fault-code/)
- [Siemens Circuit Breaker Fault Codes - Complete Guide](/posts/siemens-circuit-breaker-fault-codes/)
- [Siemens SIPROTEC Protective Relay Faults: Complete Guide](/posts/siemens-siprotec-relay-faults/)
- [Siemens SINAMICS G120 F00001 Fault — Causes & Fix](/posts/siemens-sinamics-g120-fault-f00001/)
