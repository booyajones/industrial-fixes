---
title: "Siemens SINAMICS G120 Fault F30021, Ground Fault Causes & Fix"
description: "What Siemens SINAMICS G120 Fault F30021 means, why the power unit detects a ground fault, and how to isolate the motor, cable, or brake wiring problem."
pubDatetime: 2026-04-24T23:50:00Z
modDatetime: 2026-04-24T23:50:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - siemens
  - sinamics
---

## Siemens SINAMICS G120 Fault F30021, What It Means

Siemens SINAMICS G120 **Fault F30021** means the **power unit detected a ground fault**. The drive sees leakage or a grounded condition in the motor circuit, power cable, brake circuit, or connected output components. The trip is there to protect the power module from catastrophic output-stage damage.

In the field, F30021 usually traces back to a motor winding fault, wet or damaged cable, contaminated terminal box, or brake wiring issue rather than a bad parameter.

[Jump to Fix](#fix)

## Common Causes

- **Motor winding short to ground**. This is especially common on older motors running on long VFD leads.
- **Damaged output cable**. Crushed tray cable, liquid intrusion, or poor terminations can leak to ground.
- **Moisture in the motor junction box**. Outdoor fans and pumps often trip after washdown or weather changes.
- **Brake resistor or brake wiring fault**. Broken insulation or bad wiring around braking components can trigger F30021.
- **Failed output reactor or filter**. Downstream components can create a ground path the power unit detects immediately.
- **Internal current transformer or power module problem**. Less common, but possible if the fault remains with the load removed.

## Step-by-Step Fix {#fix}

1. **Lock out the equipment and disconnect the motor circuit from the drive**. Separate the G120 from the motor leads before doing insulation testing.
2. **Megger the cable and motor separately**. Test each phase conductor to ground on the cable, then test the motor windings independently. This is the fastest way to stop guessing.
3. **Inspect the motor terminal box**. Look for moisture, conductive dust, carbon tracking, damaged insulation sleeves, or a loose ground lug touching a phase conductor.
4. **Check brake resistor and brake wiring**. If the application uses dynamic braking, inspect those conductors and terminations carefully. Grounded brake wiring can look like a power unit fault.
5. **Inspect any output reactor, du/dt filter, or sine filter**. Disconnect and test these components if present. A failed output accessory can trip the G120 even when the motor is healthy.
6. **Power the drive with the motor still isolated**. If F30021 clears, the problem is downstream. If the fault stays active with nothing connected, suspect the power unit.
7. **Review cable routing and shielding**. Poor VFD cable practice, damaged armor, or liquid-filled conduit can create repeat failures that come and go with temperature and humidity.
8. **Reconnect and perform a controlled test run**. Bring the motor up slowly and watch whether the fault returns immediately or only under heat and load. That timing helps distinguish cable damage from motor insulation breakdown.

## Parts Often Needed

| Part | Notes |
|------|-------|
| VFD-rated motor cable | [Amazon](https://www.amazon.com/s?k=VFD+rated+motor+cable&tag=errorcodefixes-20) \| Best replacement when tray or conduit cable is leaking to ground |
| Insulation resistance tester | [Amazon](https://www.amazon.com/s?k=megohmmeter+insulation+tester&tag=errorcodefixes-20) \| Essential for proving whether the motor or cable is the culprit |
| Brake resistor assembly | [Amazon](https://www.amazon.com/s?k=braking+resistor+assembly+vfd&tag=errorcodefixes-20) \| Relevant where the brake circuit wiring has failed |
| Output reactor / du-dt filter | [Amazon](https://www.amazon.com/s?k=du+dt+filter+vfd&tag=errorcodefixes-20) \| Useful on long leads and can be the failed component itself |
| Replacement inverter-duty motor | [Amazon](https://www.amazon.com/s?k=inverter+duty+3+phase+motor&tag=errorcodefixes-20) \| Needed when megger results show winding breakdown |

## When to Call a Professional

Call Siemens support or a qualified drive shop if F30021 remains with the motor and downstream components disconnected. That usually points to an internal power module or sensing issue, and continued field resets can turn a repairable problem into a full drive replacement.

## See Also

- [Siemens SINAMICS G120 Fault F00001, Overcurrent Guide](/posts/siemens-sinamics-g120-fault-f00001/)
- [Siemens G120C Fault Codes, Common Trip Guide](/posts/siemens-g120c-fault-codes/)
- [Siemens VFD Fault Codes, What They Mean](/posts/siemens-vfd-fault-codes/)
- [Siemens Micromaster Fault F001, Overcurrent Causes and Fix](/posts/siemens-micromaster-fault-f001/)
