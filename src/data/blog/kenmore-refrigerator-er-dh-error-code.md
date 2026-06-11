---
title: "Kenmore Er dH Error Code - Causes & Fix"
description: "Er dH signals defrost failure: evaporator didn't warm up during defrost. Most often a blown thermal fuse. Check sensor, heater, and drain."
pubDatetime: 2026-06-08T06:48:10Z
modDatetime: 2026-06-08T06:48:10Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - kenmore
most_likely_cause: "Open thermal fuse in the defrost sensor assembly"
likelihood: "the most common cause"
diy_or_pro: "diy"
money_part: "Defrost sensor / thermal fuse assembly"
---

## Kenmore Er dH Error Code — What It Means

The Er dH code on Kenmore refrigerators built on the LG platform means the defrost system failed to bring the evaporator area up to the required temperature within the defrost window. LG documentation specifies that normal temperature (46°F or 8°C) must be detected within one hour after defrost starts, or the control flags a defrosting-related fault. When the code appears, the unit often becomes unresponsive and the UI may lock until the problem is cleared.

The error indicates that something in the defrost circuit is preventing proper heating or temperature sensing. LG lists ice accumulation, blocked drain hole, temperature fuse disconnection, heater disconnection, or main PCB failure as the root causes. In real-world service calls, the code is most often tied to heavy frost buildup on the evaporator coil, an open thermal fuse in the sensor assembly, or a failed defrost heater. The control board cannot confirm that the ice melted, so it shuts down to protect the system.

## Before You Replace Anything

Many people replace the main control board first when the real culprit is the inexpensive thermal fuse in the sensor assembly. Always check fuse continuity and heater resistance before swapping the PCB.

[Jump to Fix](#fix)

## Common Causes

- **Open thermal fuse / temperature fuse (~45%)** The thermal fuse in the defrost sensor assembly blows when the evaporator overheats or the defrost cycle runs too long, breaking the circuit and preventing the control from reading the sensor.
- **Failed defrost heater (~25%)** The heater element or its wiring opens, so the evaporator never warms up and ice never melts during the defrost cycle.
- **Heavy frost or ice buildup on the evaporator (~15%)** Repeated incomplete defrost cycles or a blocked drain hole let ice pack the coil, and the heater cannot raise the temperature enough to satisfy the sensor threshold.
- **Blocked or frozen drain hole (~10%)** Meltwater cannot exit the evaporator compartment, refreezes on the coil, and the next defrost cycle cannot clear the ice.
- **Main control board / PCB failure (~5%)** The board fails to energize the heater circuit or misreads the sensor feedback, even though the components themselves test good.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the evaporator coil heavily frosted or covered in solid ice when you remove the freezer rear panel?</summary>
<div class="dtree-body"><strong>Yes:</strong> The defrost system has failed to melt ice for multiple cycles. Proceed to test the heater and sensor assembly.<br><strong>No:</strong> The defrost circuit may have intermittent failure or the control board is misreading the sensor. Check wiring and test the sensor resistance.</div>
</details>

<details class="dtree"><summary>Does the thermal fuse (usually part of the sensor assembly) show continuity across its terminals with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fuse is good. Move on to test the defrost heater resistance and check for 115 VAC at the heater output on the control board during a forced defrost cycle.<br><strong>No:</strong> The fuse is open. Replace the defrost sensor/fuse assembly. This is the most common fix for Er dH.</div>
</details>

<details class="dtree"><summary>Does the defrost heater measure infinite resistance (open circuit) when disconnected and tested with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The heater element has failed. Replace the defrost heater.<br><strong>No:</strong> The heater tests good. Verify the control board is supplying 115 VAC to the heater terminals during defrost. If not, replace the main PCB.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Unplug the refrigerator** and allow it to sit for a few minutes to make sure capacitors discharge and the system is safe to work on.
2. **Remove the rear access panel** inside the freezer compartment to expose the evaporator coil, defrost heater, and sensor assembly.
3. **Inspect the evaporator coil** for heavy frost or solid ice. If the coil is packed, manually defrost by leaving the compartment open or using a hair dryer on low heat (never high, which can damage plastic). Clear the drain hole at the bottom of the evaporator trough with warm water and a pipe cleaner.
4. **Locate the defrost sensor assembly** (usually a small cylindrical thermistor with attached thermal fuse, clipped or screwed to the evaporator). Disconnect its plug and test continuity across the fuse leads (often black and blue wires). If the fuse shows no continuity, it is open and the assembly must be replaced.
5. **Test the defrost heater resistance** by disconnecting its wiring harness and measuring across the heater terminals. A good heater will show a finite resistance (typically tens to low hundreds of ohms depending on wattage). An infinite reading means the heater is open and must be replaced.
6. **Check the defrost thermistor resistance** if the fuse tested good. At freezing temperature the thermistor should read around 30 kΩ. Compare your reading to the service manual table for your model. A wildly out-of-spec reading means the sensor is bad.
7. **Test for heater output voltage** at the control board if all components test good. Force a defrost cycle (consult your service manual for the button sequence or pin jumper) and measure 115 VAC at the heater output terminals on the main PCB. No voltage during defrost points to board failure.
8. **Reassemble and power on** once the faulty part is replaced. Monitor the unit through one full defrost cycle to confirm the code does not return and the evaporator stays clear.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Defrost sensor / thermal fuse assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kenmore-refrigerator-er-dh-error-code&k=Defrost+sensor+%2F+thermal+fuse+assembly&tag=errorcodefixes-20) \| Includes thermistor and inline thermal fuse. Match your model number. LG part number varies by refrigerator series. |
| Defrost heater element | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kenmore-refrigerator-er-dh-error-code&k=Defrost+heater+element&tag=errorcodefixes-20) \| Glass-sheathed or aluminum-sheathed element mounted below or behind the evaporator coil. Verify wattage and length for your model. |
| Main control board / PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kenmore-refrigerator-er-dh-error-code&k=Main+control+board+%2F+PCB&tag=errorcodefixes-20) \| Only if heater, sensor, and wiring test good but the board does not supply 115 VAC to the heater circuit during defrost. |

## When to Call a Pro

Call a professional if you are uncomfortable working inside the freezer compartment, testing live voltage, or interpreting multimeter readings. A technician can force a defrost cycle, measure heater output at the board, and quickly isolate whether the fault is in the sensor assembly, heater, or control board. If the drain tube is frozen solid deep into the cabinet or the evaporator fan motor also needs replacement, a pro has the tools and experience to disassemble the airflow plenum safely. Also call if the code returns after you replace the sensor and heater, since that points to a control board failure or a wiring short that requires methodical tracing.

**Rough cost:** DIY runs about $15–50 in parts (fuse/sensor assembly or heater), 1–2 hours. A pro service call runs about $150–300 for diagnosis and part replacement.
