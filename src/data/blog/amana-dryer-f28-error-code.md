---
title: "Amana Dryer F28 Error Code - Causes & Fix"
description: "F28 is a control communication fault. Most common fix: power reset and reseat all harness connectors between control boards."
pubDatetime: 2026-06-12T11:12:32Z
modDatetime: 2026-06-12T11:12:32Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - dryer
  - amana
money_part: "Main control board (electronic control)"
most_likely_cause: "Loose or poorly seated harness connector at the control boards"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Turn the circuit breaker(s) off for 5 minutes, then restore power"
  - "Unplug and firmly reseat every harness connector on the control boards"
  - "Inspect connector terminals for oxidation, corrosion, or heat damage and clean contact pads"
part_price: "$80-150"
no_buy_pct: "60%"
---

## What this code means
The F28 code on an Amana dryer signals a communication fault between control components. Amana's own troubleshooting starts with a full power reset rather than checking sensors or airflow. The code indicates that the main control board and user interface (or other boards in the communication path) are not exchanging data properly. This is an electronic fault requiring service after the power reset, not a maintenance code related to lint restriction, voltage, or gas pressure.

In practice, the fault is usually caused by loose or poor harness connections, oxidized terminals, or contaminated contact pads that interrupt low-level serial communication between boards. If reconnecting and reseating the wiring does not restore communication after a power cycle, a failed control board becomes the likely cause. Field service accounts consistently point to connector integrity as the first area to inspect, since many F28 faults clear after restoring proper terminal tension and cleaning contact surfaces.

## Before You Replace Anything

Many people replace the main control board first, but most F28 codes clear after simply unplugging and reseating each connector and cleaning oxidized terminals.

## Common Causes

- **Loose harness connector or terminal fit (~45%)** Vibration, heat, or partial insertion leaves the connector pins with poor contact, breaking the serial data link between boards.
- **Oxidized or contaminated contact pads (~25%)** Terminals can show oxidation or film buildup that interrupts low-level communication even when the harness ohms correctly.
- **Failed main control board (~20%)** If connector service and power reset do not clear the fault, the main electronic control or user-interface board has failed.
- **Damaged or heat-affected wire harness (~7%)** Wiring between boards can suffer internal breaks, melted insulation, or damaged conductors from heat or pinching.
- **Low terminal retention force (~3%)** Individual terminals in the connector lose spring tension over time, allowing intermittent contact that triggers the fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the F28 code clear after turning the breaker off for 5 minutes and restoring power?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was transient. Monitor the dryer. If it returns, proceed to connector inspection.<br><strong>No:</strong> The fault is persistent. Move on to inspecting and reseating all control-board harness connectors.</div>
</details>

<details class="dtree"><summary>Do the harness connectors feel loose or show visible corrosion, heat damage, or oxidation on the pins?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the terminals, reform pin tension if needed, reseat firmly, and test. Replace the harness if conductors are damaged.<br><strong>No:</strong> Connectors appear intact. Replace the main control board or user-interface board, whichever is suspect in the communication path.</div>
</details>

<details class="dtree"><summary>Does the code return after reseating connectors and replacing the main control board?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the other board in the serial link (user interface or secondary control) or the interconnecting harness if damaged.<br><strong>No:</strong> Repair is complete. Run a test cycle to confirm normal operation.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the circuit breaker(s) and wait 5 minutes, then restore power to perform Amana's recommended reset.
2. **Run a test cycle** to see if the F28 code returns; if it does not reappear, monitor the dryer and no further service is needed yet.
3. **Unplug the dryer** from power and pull it away from the wall to access the rear panel or top control area.
4. **Remove the cabinet or top panel** (typically 2-4 screws at the rear) to expose the main control board and user-interface board.
5. **Inspect every harness connector** on the control boards for loose fit, partial insertion, oxidation, heat discoloration, or corrosion on the terminals.
6. **Unplug and firmly reseat** each connector rather than only looking; many F28 faults clear after restoring proper contact by reseating.
7. **Check terminal retention** by gently tugging individual wires; if a terminal slides out easily, use a small pick to bend the terminal tab slightly to improve grip, then reinsert.
8. **Clean contact pads** with electrical contact cleaner or a pencil eraser if oxidation or film is visible, then reassemble and test.
9. **Replace the main control board** if the fault persists after power reset and connector service, as board failure is the next most likely cause.
10. **Reassemble the cabinet**, restore power, and run a full cycle to verify the F28 code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Main control board (electronic control) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f28-error-code&k=Main+control+board+%28electronic+control%29&tag=errorcodefixes-20) \| Match your model number; most common replacement if connector service fails. |
| User-interface control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f28-error-code&k=User-interface+control+board&tag=errorcodefixes-20) \| Replace if the main board is good but communication fault persists. |
| Wire harness (interconnect harness) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-amana-dryer-f28-error-code&k=Wire+harness+%28interconnect+harness%29&tag=errorcodefixes-20) \| Only if conductors are visibly damaged, melted, or broken. |

## When to Call a Pro

Call a pro if you are uncomfortable working inside the dryer cabinet, if you cannot safely disconnect power at the breaker, or if the fault returns after you have reseated connectors and replaced the main control board. A technician has the platform-specific wiring diagrams and board-substitution tools to isolate whether the issue is in the main control, the user interface, or a less common secondary board. Also call for help if the harness shows heat damage or melted insulation in areas near the heating element or blower, since that can indicate a separate airflow or thermal problem that needs diagnosis before the communication fault will stay cleared.

**Rough cost:** DIY runs about $80-180 in parts if board replacement is needed, 45-90 min. A pro service call runs about $150-350.
