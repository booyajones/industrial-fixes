---
title: "True GDM-49 Glass Door Merchandiser Error Codes - Full Fault Guide"
description: "True GDM-49 glass door merchandiser error codes E1-E6 guide. Covers temperature controller faults, evaporator fan failures, defrost issues, and replacement parts."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The True GDM-49 is one of the most common two-section glass door merchandisers in convenience stores, cafeterias, break rooms, and retail food environments. It uses a digital temperature controller, an evaporator fan system inside the cabinet, a condenser fan near the compressor compartment, and one or more NTC temperature probes to monitor cabinet and evaporator conditions. When something fails, the controller displays an error code, usually E1 through E6. This guide explains what each code means, what is actually failing inside the cooler, and how to fix it.

## What Does a True GDM-49 Error Code Mean?

The GDM-49's controller watches cabinet temperature, evaporator coil temperature, compressor run time, and defrost timing. If it loses a sensor input or detects a condition outside its programmed range, it throws an error code.

Different controller revisions exist on the GDM-49. Older units may use LAE or Dixell controllers, while newer revisions use True-branded or Carel-style displays. The exact code text can vary by controller, but the common field interpretation stays consistent.

### Common Error Codes on the True GDM-49

| Code | Meaning |
|------|---------|
| E1 | Cabinet air temperature probe failed or disconnected |
| E2 | Evaporator coil probe failed or disconnected |
| E3 | High cabinet temperature alarm |
| E4 | Low cabinet temperature alarm or freeze condition |
| E5 | Defrost fault, evaporator did not reach target temp during defrost |
| E6 | Controller communication or internal memory fault |

### What Each Code Tells You

**E1** means the controller cannot read the main cabinet temperature sensor. On a GDM-49, that probe typically sits in the return air path inside the refrigerated cabinet. If the probe opens or shorts, the controller loses the main input it uses to cycle the compressor. The unit may default into a timed backup mode where it runs the compressor on a schedule instead of true temperature control.

**E2** points to the evaporator probe. That probe clips to the evaporator coil and tells the controller when to terminate defrost. If it fails, the merchandiser may stay in defrost too long, not defrost long enough, or start building ice on the evaporator because the controller no longer knows the coil temperature.

**E3** is a high temperature alarm. This is not always a failed part. The controller throws E3 when the cabinet temperature rises above its programmed high limit for a certain amount of time. Dirty condenser coils, a failed condenser fan motor, warm product loading, doors left open, or refrigerant loss can all cause it.

**E4** is the opposite problem. The cabinet got too cold. On a GDM-49, this can happen if the controller relay sticks closed and keeps the compressor running, if the cabinet sensor is reading too warm, or if the evaporator fan never cycles off and drives the case temperature below setpoint.

**E5** means the controller expected the evaporator to warm up during defrost and it didn't. In plain language, the cooler went into defrost but the coil stayed too cold. That usually means a failed defrost heater on models equipped with one, a failed evaporator fan that's choking airflow and creating a solid ice mass, or a failed evaporator sensor that never reports the correct temperature.

**E6** is the least common but most annoying. It points to internal controller failure, memory corruption, or a wiring communication fault on some controller revisions. Power surges often trigger E6. If you see E6 after a storm or power outage, start with power quality and controller reset before replacing parts.

### Fan and Airflow Problems That Trigger Codes

The GDM-49 relies on both **evaporator fans** and a **condenser fan**. The evaporator fans pull air across the evaporator coil and circulate cold air through both cabinet sections. The condenser fan moves heat out of the condenser coil near the compressor compartment.

A failed evaporator fan motor can lead to:
- E3 high cabinet temp alarm because cold air never circulates properly
- E5 defrost fault because the coil ices over faster
- Product temperature differences between the top and bottom shelves

A failed condenser fan motor can lead to:
- E3 high temp alarm from poor heat rejection
- Hot compressor compartment
- Compressor overload trips
- Short cycling and eventually compressor damage

If the compressor compartment feels unusually hot, the condenser fan is the first thing to inspect.

## How to Fix It

1. Unplug the merchandiser or switch off the dedicated circuit before opening the control housing or fan compartments.
2. For E1 or E2, locate the failed probe, inspect the wiring, and measure resistance. Most GDM-49 probes are 10k NTC thermistors and should read about 10,000 ohms at 77°F.
3. For E3, clean the condenser coil, confirm the condenser fan runs with the compressor, and inspect door gaskets for warm-air leaks.
4. For E4, verify the controller setpoint, compare displayed temperature to a separate thermometer, and watch whether the compressor runs past setpoint.
5. For E5, remove the evaporator cover, check for heavy ice, confirm the evaporator probe is clipped correctly, and test the defrost heater or off-cycle defrost behavior.
6. For E6, shut power off for 5 minutes, restore power, and replace the controller if the fault returns immediately.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [True GDM Temperature Probe 10K NTC](https://www.amazon.com/s?k=True+GDM+49+temperature+probe+10k+NTC&tag=errorcodefixes-20) | Replaces failed cabinet or evaporator probe for E1 and E2 errors | $15–$35 |
| [True Evaporator Fan Motor 115V](https://www.amazon.com/dp/B01N0J3ZEH?tag=errorcodefixes-20) | Restores cabinet airflow and helps prevent E3 and E5 faults | $35–$90 |
| [True Condenser Fan Motor 115V](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) | Required when compressor section overheats and E3 keeps returning | $40–$95 |
| [Commercial Refrigeration Coil Brush Kit](https://www.amazon.com/s?k=commercial+refrigeration+coil+brush+kit&tag=errorcodefixes-20) | Cleans clogged condenser fins that drive cabinet temperature high | $10–$25 |
| [Dixell or LAE Refrigeration Controller Replacement](https://www.amazon.com/s?k=True+GDM+49+refrigeration+controller&tag=errorcodefixes-20) | Fixes E6 controller memory or relay faults on many GDM-49 revisions | $60–$180 |
| [True Door Gasket for GDM-49](https://www.amazon.com/dp/B0FPF84HQP?tag=errorcodefixes-20) | Stops warm air infiltration that triggers high temp alarms | $45–$110 |

## When to Call a Pro

Call a commercial refrigeration tech when:

- The condenser fan and evaporator fans run, the coils are clean, and the box still throws E3. That points to low refrigerant charge, a restriction, or weak compressor.
- The evaporator is a solid block of ice and returns to that condition right after defrost troubleshooting. A tech needs to check the refrigeration circuit and controller programming.
- E6 returns after a new controller or after voltage checks look normal. That can point to wiring damage deeper in the harness or a power quality issue in the building.
- You suspect a refrigerant leak. GDM-49 units use sealed refrigeration systems. Leak search, repair, evacuation, and recharge require refrigeration tools and EPA certification.

Sensor swaps, fan motor replacement, coil cleaning, and gasket replacement are reasonable field repairs for a store owner, maintenance tech, or experienced DIYer.

## Frequently Asked Questions

**Q: My True GDM-49 shows E3 every afternoon but clears at night. Why?**
A: Afternoon E3 alarms usually point to heat load, not a dead part. Check whether the store gets direct sunlight on the doors, whether staff prop the doors open during stocking, or whether the condenser coil clogs fast from dust in the space. A weak condenser fan also shows up this way because the compressor compartment gets hottest during the warmest part of the day.

**Q: Can I keep running the cooler with E1 or E2 on the display?**
A: You can for a short time, but you should not leave it that way. The controller often switches into a timed backup mode when it loses a sensor. That might keep product cold enough for a day or two, but it will not control temperature accurately. Replace the sensor quickly if the cooler stores anything temperature-sensitive.

**Q: How do I know if the condenser fan is bad on a True GDM-49?**
A: Watch the unit while the compressor is running. The condenser fan should run any time the compressor runs. If the compressor is hot, the coil is dirty, and the fan is still or humming without spinning, the motor has failed or the blade is jammed.

**Q: What temperature should a GDM-49 run at?**
A: Most beverage and merchandiser setups target a cabinet temperature around 33°F to 38°F. Product temperature is what matters most. Use a thermometer in a liquid-filled bottle on a middle shelf to confirm the actual product temp instead of relying only on the controller display.
