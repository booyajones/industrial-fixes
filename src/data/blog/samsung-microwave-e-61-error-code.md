---
title: "Samsung Microwave E-61 Error - Causes & Fix"
description: "E-61 means an open humidity sensor error. The most common fix is replacing the humidity sensor or repairing its wiring harness."
pubDatetime: 2026-06-06T03:15:20Z
modDatetime: 2026-06-06T03:15:20Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - microwave
  - samsung
most_likely_cause: "failed humidity sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "Samsung microwave humidity sensor assembly"
---

## Samsung Microwave E-61 Error — What It Means

The E-61 code on a Samsung microwave indicates an open humidity sensor error. This means the control board is not detecting the humidity sensor circuit in its expected electrical state. The board has registered an open (broken or disconnected) condition in the sensor circuit, as opposed to a short or other fault.

The humidity sensor monitors steam levels inside the cavity during cooking cycles. When the control board cannot read the sensor at all, it throws E-61 and typically halts operation to prevent running cycles blind. Samsung distinguishes E-61 (open sensor) from E-62 (shorted sensor), so the fault is specifically a missing or interrupted signal rather than a sensor reading out of range.

## Before You Replace Anything

Many users replace the main control board first when E-61 appears, but the fault is usually at the humidity sensor itself or its connector. Always check sensor continuity and inspect the harness plug for corrosion before ordering a new board.

[Jump to Fix](#fix)

## Common Causes

- **Failed humidity sensor** The sensor element itself has gone open-circuit internally, so the control board sees no connection.
- **Disconnected or loose sensor connector** Vibration or service work can unseat the plug at the sensor or at the control board, breaking the circuit.
- **Corroded or moisture-damaged connector pins** Steam and heat can corrode the small pins in the sensor harness, creating an intermittent or permanent open.
- **Broken wire in the sensor harness** Flexing over time or accidental pinching can snap one of the fine wires between the sensor and the board.
- **Control board input fault** If the sensor circuit and wiring test normal but the code persists, a failed trace or input stage on the main PCB can also register as an open sensor.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the error clear for several minutes after you unplug the microwave for 60 seconds and then plug it back in?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board is booting normally and the fault may be intermittent. Inspect the humidity sensor connector for loose seating or light corrosion and reseat it firmly.<br><strong>No:</strong> The error returns immediately, which points to a hard open in the sensor circuit. Proceed to inspect the sensor and harness for visible damage or continuity faults.</div>
</details>

<details class="dtree"><summary>Can you locate the humidity sensor (usually a small cylindrical or rectangular module mounted near the vent or cavity ceiling) and see any visible burn marks, melted plastic, or disconnected wires?</summary>
<div class="dtree-body"><strong>Yes:</strong> Physical damage is present. Replace the humidity sensor assembly and repair or replace any damaged sections of the harness.<br><strong>No:</strong> No visible damage means the fault is electrical. Test the sensor for continuity and check connector pins for corrosion before replacing parts.</div>
</details>

<details class="dtree"><summary>With power off, do you measure infinite resistance (open circuit) across the humidity sensor terminals when you disconnect it from the harness and test it with a multimeter?</summary>
<div class="dtree-body"><strong>Yes:</strong> The sensor has failed open. Replace the humidity sensor assembly.<br><strong>No:</strong> The sensor shows some resistance, so the open fault is likely in the wiring harness, connector, or control board input. Inspect connectors and test harness continuity next.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** by unplugging the microwave or switching off the dedicated breaker, and leave it off for at least 60 seconds to clear volatile memory.
2. **Restore power** and observe whether E-61 returns immediately or after a few minutes of operation (an intermittent fault suggests a loose connection rather than a dead sensor).
3. **Access the humidity sensor** by removing the outer cabinet panels (typically side and top screws) to expose the control cavity and sensor assembly, which is usually mounted near the steam vent or on the ceiling of the cooking chamber.
4. **Inspect the sensor connector** at both the sensor end and the control board end for corrosion, bent pins, moisture intrusion, or incomplete seating, and clean or reseat as needed.
5. **Test sensor continuity** by disconnecting the sensor plug and measuring resistance across the sensor terminals with a multimeter (an open reading confirms sensor failure, while a finite resistance means the sensor may be good and the fault lies elsewhere).
6. **Replace the humidity sensor** if it tests open or shows visible damage, routing the new harness carefully to avoid pinch points and ensuring the connector locks securely.
7. **Verify the repair** by reassembling the cabinet, restoring power, and running a short cook cycle to confirm that E-61 does not return (if the code persists after sensor replacement and all wiring checks pass, the control board input stage is the remaining suspect and requires professional board-level diagnosis or replacement).

## Parts Often Needed

| Part | Notes |
|------|-------|
| Samsung microwave humidity sensor assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-samsung-microwave-e-61-error-code&k=Samsung+microwave+humidity+sensor+assembly&tag=errorcodefixes-20) \| Verify your exact model number on the door frame label and cross-reference the sensor part number in the service manual or on Samsung's parts site. |
| Wire harness or connector repair kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-samsung-microwave-e-61-error-code&k=Wire+harness+or+connector+repair+kit&tag=errorcodefixes-20) \| Only needed if you find broken wires or badly corroded pins that cannot be cleaned. |
| Main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-samsung-microwave-e-61-error-code&k=Main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Replace only after confirming the sensor and all wiring test normal but the E-61 fault remains. |

## When to Call a Pro

Call a qualified appliance technician if you are uncomfortable working inside the microwave cabinet around high-voltage components, if you cannot locate or access the humidity sensor, or if the fault persists after you have replaced the sensor and verified all wiring continuity. The magnetron, high-voltage capacitor, and transformer retain lethal charge even when unplugged, so any work beyond simple sensor replacement carries shock risk. A technician will also have model-specific service manuals with sensor resistance specifications and board-level diagnostic tools to isolate control board faults that a multimeter alone cannot pinpoint.

**Rough cost:** A pro service call runs about $150–300.
