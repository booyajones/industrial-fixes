---
title: "Manitowoc E32 Error - Causes & Fix"
description: "E32 on Manitowoc ice machines means an RS485 communication fault between control boards. Most often caused by loose or corroded harness connections."
pubDatetime: 2026-06-20T12:40:51Z
modDatetime: 2026-06-20T12:40:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - manitowoc
money_part: "Main control board"
most_likely_cause: "Loose, damaged, or corroded wiring harness connections on the RS485 communication circuit"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the machine and inspect the control compartment for loose plugs, moisture, or obvious connector damage"
  - "Reseat all harness connections on both the main board and display board, checking for corroded or bent pins"
  - "Cycle power and clear the fault to see if E32 returns immediately or only after operation begins"
---

## What this code means
E32 indicates an RS485 communication failure on the machine's control network. The main controller is not receiving valid communication from a connected board or module over the RS485 bus. This is an electrical or control problem involving the main board, display or interface board, or the interconnecting harness, rather than a refrigeration or ice-making performance issue. The machine will not operate until the communication link is restored.

## Before You Replace Anything

Technicians sometimes replace the main control board when the real issue is a loose or corroded connector or a faulty communication harness. Always inspect and reseat all harness connections and check for physical damage before condemning any board.

## Common Causes

- **Loose or corroded harness connections (~50%)** Vibration, moisture intrusion, or corrosion at the RS485 communication cable connectors prevents reliable board-to-board communication.
- **Failed main control board (~25%)** The main control board has stopped sending or receiving RS485 signals due to component failure or moisture damage.
- **Failed display or interface board (~15%)** The user interface or display board is not responding on the RS485 network, often due to water exposure or electrical fault.
- **Damaged communication harness (~10%)** The RS485 communication cable has broken conductors, physical damage, or internal wire faults that block signal transmission.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>After reseating all harness connections and cycling power, does the E32 fault clear and stay off?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue was a loose or intermittent connection. Monitor the machine over the next few cycles to confirm the repair is stable.<br><strong>No:</strong> The fault is persistent, which points to a failed board or damaged harness that needs component-level substitution testing.</div>
</details>

<details class="dtree"><summary>Are any connectors in the control compartment visibly corroded, wet, or showing burnt pins?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean or replace the affected connectors and harness. Moisture intrusion often causes RS485 faults and must be addressed at the source.<br><strong>No:</strong> The harness and connectors appear intact, so the fault is likely inside one of the boards. Substitute known-good boards one at a time.</div>
</details>

<details class="dtree"><summary>Does the main control board show any LED status indicators, and are they matching the normal boot sequence in the service manual?</summary>
<div class="dtree-body"><strong>Yes:</strong> The main board is powering up correctly, so focus testing on the display board and the communication cable between them.<br><strong>No:</strong> The main board may not be booting, which can trigger a communication fault. Check incoming power and board fuses before replacing the board.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the machine** at the breaker and lockout to work safely inside the control compartment.
2. **Remove the control panel cover** and inspect all visible harness connectors, looking for moisture, corrosion, bent pins, or physical damage.
3. **Unplug and reseat each RS485 harness connection** at both the main control board and the display or interface board, ensuring a firm click and no wiggle.
4. **Check for water intrusion or ice buildup** around the boards and inside the electrical box. Dry and clean any affected areas.
5. **Restore power and observe** whether the E32 fault clears. If it does, monitor the machine through a full ice-making cycle.
6. **If the fault persists**, substitute known-good components one at a time: start with the communication harness, then the display board, and finally the main control board.
7. **Consult the model-specific service manual** for any board LED diagnostic sequences or RS485 test procedures for your exact Indigo or NXT control platform.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e32-error-code&k=Main+control+board&tag=errorcodefixes-20) \| Match the exact model and revision printed on your current board. |
| Display or user interface board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e32-error-code&k=Display+or+user+interface+board&tag=errorcodefixes-20) \| Verify compatibility with your machine's control platform (Indigo, Indigo NXT, etc.). |
| RS485 communication harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e32-error-code&k=RS485+communication+harness&tag=errorcodefixes-20) \| Order the correct length and connector type for your model. |

## When to Call a Pro

Call a qualified commercial refrigeration technician for E32 faults. Diagnosing RS485 communication problems requires access to the service manual, knowledge of the machine's control architecture, and the ability to safely work inside energized electrical compartments. The technician will perform systematic component substitution and may need to verify board voltages or use specialized diagnostic tools. Attempting board-level troubleshooting without proper training risks creating additional faults or electrical hazards.

**Rough cost:** A pro service call runs about $200-500.
