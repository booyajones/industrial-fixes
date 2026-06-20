---
title: "Weil-McLain A168 Error Code - Causes & Fix"
description: "A168 (or A-16) means outdoor sensor missing on central-heating-only boiler. Install sensor or change control parameter, then reset."
pubDatetime: 2026-06-18T10:18:42Z
modDatetime: 2026-06-18T10:18:42Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Outdoor temperature sensor assembly"
most_likely_cause: "Outdoor sensor not installed on a boiler configured to expect one"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Confirm your boiler model and control type from the nameplate and manual to verify whether A168 or A-16 applies."
  - "Inspect the outdoor sensor terminal block on the boiler control to see if wires are present or if terminals are empty."
  - "Check the control parameter menu (if accessible) to see if outdoor reset is enabled when no sensor is installed."
---

## Weil-McLain A168 Error Code — What It Means

On Weil-McLain boilers, especially the Aqua Balance series, the display A-16 appears when a central-heating-only boiler is powered up and the outdoor sensor is not installed. If your display shows A168 instead of A-16, the exact meaning is model and control specific, so verify your boiler model and control manual before taking action. The code indicates the control board expects an outdoor temperature sensor input but cannot find one connected.

In most cases the boiler is either configured to use outdoor reset (where the supply temperature adjusts based on outdoor temperature) but the sensor was never installed, or the sensor is present but faulty or disconnected. The Weil-McLain Aqua Balance Quick Start Guide instructs technicians to install the outdoor sensor and press the reset button for 1.5 seconds to clear the error. Alternatively, if your installation does not require outdoor reset, the control parameter can be changed to exempt the sensor input.

## Before You Replace Anything

Homeowners sometimes replace the control board or gas valve without checking whether the outdoor sensor is simply missing or unplugged. Always verify sensor presence and wiring before ordering expensive control components.

[Jump to Fix](#fix)

## Common Causes

- **Outdoor sensor omitted on a configuration that expects it (~50%)** The boiler control is set for outdoor reset but the sensor was never physically installed during commissioning.
- **Outdoor sensor faulty or disconnected (~25%)** The sensor is installed but has failed, or its wiring has come loose at the terminal block.
- **Control parameter configured for outdoor sensor when not used (~20%)** The boiler is set up for central heating only but a zero value in the outdoor reset parameter tells the control to expect a sensor.
- **Wrong boiler configuration selected during setup (~5%)** The installer selected the wrong boiler application in the control menu, triggering the outdoor sensor requirement.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the exact code displayed A-16 or A168, and do you have your boiler model nameplate handy?</summary>
<div class="dtree-body"><strong>Yes:</strong> Look up the model (Aqua Balance, Ultra, GVF, EG, CGa, or WM97+) in the manual to confirm the code meaning before proceeding.<br><strong>No:</strong> Take a photo of the display and nameplate, then call a Weil-McLain service technician to decode the exact fault.</div>
</details>

<details class="dtree"><summary>Can you see an outdoor sensor (small box with a probe) mounted outside your home with wires running to the boiler?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the sensor wiring at the boiler terminal block for loose or corroded connections, then test or replace the sensor.<br><strong>No:</strong> Your system likely does not use outdoor reset; have a technician adjust the control parameter to exempt the sensor input.</div>
</details>

<details class="dtree"><summary>Does your boiler use outdoor reset (modulating supply temperature based on weather)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Install a new outdoor sensor, wire it to the control, and press reset for 1.5 seconds to clear the code.<br><strong>No:</strong> Enter the control menu and change the outdoor reset parameter to disable sensor monitoring, then exit and reset.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify boiler model and control type** by reading the nameplate and opening the manual to confirm whether your system uses outdoor reset or central-heating-only configuration.
2. **Inspect the outdoor sensor location** (typically mounted on a north-facing exterior wall) and trace wiring back to the boiler control terminal block.
3. **Check terminal connections** for the outdoor sensor at the control board; look for loose, corroded, or missing wires on the sensor input terminals.
4. **If no sensor is required**, access the control parameter menu per the Aqua Balance procedure and change the outdoor reset setting to exempt the sensor, then exit the menu.
5. **If sensor is required but missing**, install a compatible outdoor temperature sensor assembly and wire it to the control per the manual.
6. **Press the reset button for 1.5 seconds** to clear the A-16 or A168 error code after installing or configuring the sensor.
7. **Power-cycle the boiler** by turning it off at the service switch, waiting thirty seconds, and turning it back on to confirm normal operation and that the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor temperature sensor assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a168-error-code&k=Outdoor+temperature+sensor+assembly&tag=errorcodefixes-20) \| Match Weil-McLain part number for your boiler model and control type; consult the manual or parts diagram. |
| Sensor wire and terminal connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a168-error-code&k=Sensor+wire+and+terminal+connectors&tag=errorcodefixes-20) \| If existing sensor wire is damaged or corroded; use manufacturer-approved wire gauge. |

## When to Call a Pro

Call a qualified boiler technician if you do not have your boiler model manual, cannot identify whether your system uses outdoor reset, or are uncomfortable working inside the boiler control panel. Gas-fired boilers require licensed service for any work involving gas connections, combustion settings, or control board replacement. A technician will verify the exact code meaning for your model, test or install the outdoor sensor correctly, adjust control parameters if needed, and confirm safe operation after clearing the fault. If the code persists after sensor installation or parameter changes, the control board itself may need diagnostic testing or replacement, which requires specialized tools and factory training.

**Rough cost:** A pro service call runs about $150-300.
