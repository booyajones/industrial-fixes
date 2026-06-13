---
title: "Kenmore F28 Error Code - Causes & Fix"
description: "F28 means the main control board can't talk to the motor board. Most often it's a loose or corroded wiring connector between the two."
pubDatetime: 2026-06-10T11:55:05Z
modDatetime: 2026-06-10T11:55:05Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - kenmore
money_part: "Central Control Unit (CCU) / Main Electronic Control Board"
part_price: "$80-200"
most_likely_cause: "Loose, oxidized, or unseated wiring connectors between the CCU and MCU"
likelihood: "the most common cause"
diy_or_pro: "diy"
---

## Kenmore F28 Error Code — What It Means

The F28 code on Kenmore front-load washers (built by Whirlpool) is a serial communication error between the central control unit (CCU, the main board) and the motor control unit (MCU, the motor drive board). The two boards exchange data to coordinate spin speeds and cycle stages. When the CCU cannot successfully talk to the MCU, the washer stops mid-cycle or refuses to start, and F28 appears on the display.

This is not a motor failure in most cases. It is a break in the signal path between the two electronic boards. The motor itself may be fine, but the control system cannot command it because the communication link is interrupted.

## Before You Replace Anything

Many people replace the main control board or motor control board first. Before buying a board, unplug and reseat every connector at both the CCU and MCU, and visually inspect the harness for pinched or broken wires. A bad connection often costs nothing to fix.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded connectors (~50%)** Vibration, humidity, or age can loosen or oxidize the multi-pin connectors linking the CCU and MCU, breaking the serial data line.
- **Damaged wiring harness (~25%)** Pinched, chafed, or broken conductors in the communication harness interrupt the signal path even if the connectors look intact.
- **Failed central control unit (CCU) (~15%)** The main board's communication driver or microcontroller can fail, preventing it from sending or receiving data.
- **Failed motor control unit (MCU) (~10%)** The motor drive board's receiver circuit or burnt components (such as resistors or contacts) can stop it from responding to the CCU.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the washer display F28 immediately on power-up, or only after trying to start a cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> Immediate fault suggests a persistent hardware issue (bad board or harness damage). Inspect connectors and wiring first, then test boards.<br><strong>No:</strong> Intermittent fault during operation often points to a loose connector or vibration-sensitive wire. Reseat all plugs and secure the harness.</div>
</details>

<details class="dtree"><summary>After unplugging and firmly reseating all CCU and MCU connectors, does the code clear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem was a poor connection. Run a test cycle; if F28 returns, inspect the harness for internal breaks.<br><strong>No:</strong> Move to harness continuity checks and board isolation tests. One of the control boards is likely failed.</div>
</details>

<details class="dtree"><summary>Can you see any burnt, discolored, or heat-damaged components on the motor control board?</summary>
<div class="dtree-body"><strong>Yes:</strong> Replace the MCU. Visible damage (burnt resistors, melted solder) confirms a board-level fault.<br><strong>No:</strong> If no visible damage and connectors are good, swap or replace the CCU first, since it initiates communication.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** at the circuit breaker or unplug the washer completely before opening any panels or touching any connectors.
2. **Remove the top and rear panels** to access the main control board (CCU, usually behind the control panel) and the motor control board (MCU, usually mounted on or near the motor at the bottom rear).
3. **Unplug each connector** at both the CCU and the MCU. Examine the pins and sockets for corrosion (green or white deposits), bent pins, or heat marks. Clean any oxidation with electrical contact cleaner and a small brush.
4. **Reconnect each plug firmly** until it clicks or seats fully. Wiggle gently to confirm a solid fit. Loose or half-seated connectors are the leading cause of F28.
5. **Inspect the entire wiring harness** running between the two boards. Look for pinched wires where the harness passes through sheet-metal holes, chafing against the tub, or any broken insulation. Repair or replace damaged sections.
6. **Restore power and run a test cycle**. If F28 clears, the repair is complete. If the code returns, isolate the boards by swapping in a known-good CCU or MCU one at a time to identify the failed component.
7. **Replace the failed control board** if connector and harness checks pass but communication remains broken. In most cases where both connectors and wiring are sound, either the CCU or the MCU has an internal failure and must be replaced.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Central Control Unit (CCU) / Main Electronic Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kenmore-dryer-f28-error-code&k=Central+Control+Unit+%28CCU%29+%2F+Main+Electronic+Control+Board&tag=errorcodefixes-20) \| Match the part number on your existing board; CCU designs vary by Kenmore model and year. |
| Motor Control Unit (MCU) / Motor Drive Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kenmore-dryer-f28-error-code&k=Motor+Control+Unit+%28MCU%29+%2F+Motor+Drive+Board&tag=errorcodefixes-20) \| Verify compatibility with your washer's motor type and model number before ordering. |
| Wiring Harness (CCU to MCU communication harness) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-kenmore-dryer-f28-error-code&k=Wiring+Harness+%28CCU+to+MCU+communication+harness%29&tag=errorcodefixes-20) \| Order if conductors are broken or insulation is badly damaged; repair with solder and heat-shrink if damage is localized. |

## When to Call a Pro

Call a professional if you are uncomfortable working inside the washer cabinet, if you cannot locate or access the CCU or MCU, or if board-level troubleshooting is beyond your skill set. A technician can use diagnostic software or known-good swap boards to isolate the fault quickly. Also call a pro if the machine shows additional error codes or symptoms (such as burning smells or tripped breakers) that suggest deeper electrical damage. If you have already reseated connectors and inspected the harness but the code persists, a pro with manufacturer service manuals and board-testing tools will save time and prevent misdiagnosis.

**Rough cost:** DIY runs about $80–200 in parts (if a control board is needed), 30–90 min. A pro service call runs about $200–400.
