---
title: "Yaskawa GA800 E08 Fault - Causes & Fix"
description: "E08 on a Yaskawa GA800 VFD indicates a control power or internal supply fault. Check incoming line power and reset the drive first."
pubDatetime: 2026-06-04T09:25:45Z
modDatetime: 2026-06-04T09:25:45Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA800 E08 Fault — What It Means

The E08 fault code on a Yaskawa GA800 variable frequency drive is a major fault related to the drive's internal control power or power supply circuitry. This is not a motor overload or simple parameter error. The fault indicates a problem with the electronics that regulate and distribute control voltage inside the drive cabinet. Because published GA800 documentation does not always list every fault code verbatim in all manuals, consult your specific drive's fault table or contact Yaskawa technical support to confirm the exact wording for E08 on your model and firmware version. The drive will typically shut down and require a reset before it can restart.

[Jump to Fix](#fix)

## Common Causes

- **Incoming line power loss or instability** Low voltage, voltage sags, phase loss, or poor power quality can starve the control supply and trigger an internal fault.
- **Failed internal power supply components** Capacitors, rectifiers, or switching regulators on the control board can degrade over time and no longer maintain stable DC rails.
- **Damaged or aged control board** Heat, humidity, or component fatigue can damage traces, solder joints, or ICs on the main control printed circuit board.
- **Loose or corroded control wiring connections** Poor connections at terminal blocks or internal connectors can create intermittent faults that appear as control power issues.
- **Cooling fan failure causing overheating** If the internal fan stops or runs slowly, excess heat can damage control electronics and trigger supply faults.
- **Persistent fault state after a transient event** A momentary line disturbance or surge may latch the fault even after the external condition clears.

## Step-by-Step Fix {#fix}

1. **Document the fault** by writing down the exact code, the load condition when it occurred, and any alarms or warnings that appeared before E08.
2. **Check incoming line voltage** at the drive input terminals using a multimeter to confirm all three phases are present, balanced, and within the nameplate voltage range.
3. **Inspect all control wiring and terminal connections** for tightness, corrosion, or damage, paying special attention to the control power input terminals if your model uses external control power.
4. **Clear the fault and reset the drive** by cycling the control power or using the keypad reset function, then observe whether the fault returns immediately or only under load.
5. **Verify cooling fan operation** by listening for airflow and checking that the fan spins freely when the drive powers up.
6. **Review the drive's elementary wiring diagram** to confirm that all control circuits, fuses, and auxiliary power supplies are wired and functioning as designed.
7. **Replace the control board** if the fault is repeatable, incoming power is clean, and no external wiring issues are found, since field repair of internal power supply circuits is not practical and the control board is the primary field-replaceable component for this type of fault.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 Control Board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e08-fault-code&k=GA800+Control+Board+%28PCB%29&tag=errorcodefixes-20) \| Main logic and power supply board; consult your drive's model code and serial number for the correct part number. |
| GA800 Cooling Fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e08-fault-code&k=GA800+Cooling+Fan&tag=errorcodefixes-20) \| Standard internal fan; replace if airflow is weak or the fan does not spin freely. |

## When to Call a Pro

Call a qualified industrial electrician or Yaskawa-authorized service technician if you are not trained to work on live three-phase power, if the fault persists after verifying line power and resetting the drive, or if you need to replace the control board. Control board replacement requires safe lockout of high voltage, careful handling of static-sensitive components, and often reprogramming of parameters from a backup. If your facility does not have the GA800 documentation, parameter backup, or replacement board in stock, professional support will save time and reduce the risk of further damage.

## See Also

- [Yaskawa U1000 Fault Codes: Complete Guide](/posts/yaskawa-u1000-fault-codes/)
- [Yaskawa GA800 E28 Fault - Serial Watchdog Timeout Fix](/posts/yaskawa-ga800-e28-fault-code/)
- [Yaskawa V1000 OV Fault - What It Means and How to Fix It](/posts/yaskawa-v1000-fault-ov/)
- [Yaskawa VFD Fault ER — Causes & Fix](/posts/yaskawa-vfd-fault-er/)
