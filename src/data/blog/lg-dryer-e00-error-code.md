---
title: "LG Dryer E00 Error Code - Causes & Fix"
description: "E00 means the display PCB cannot read software from the main control board. Unplug for 60 seconds and restart-if it returns, a board is faulty."
pubDatetime: 2026-06-08T03:38:00Z
modDatetime: 2026-06-08T03:38:00Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - dryer
  - lg
most_likely_cause: "Power interruption, surge, or control-board lockup leaving the boards out of sync"
likelihood: "the most common cause"
diy_or_pro: "diy"
money_part: "LG dryer main control board (PCB assembly)"
part_price: "$80-200"
---

## LG Dryer E00 Error Code — What It Means

The E00 code on an LG dryer signals a communication or software read failure between the display board and the main control board. The display PCB cannot successfully read firmware or software data from the main PCB. This is not a vent blockage, thermistor fault, door switch problem, or sensor issue. It is strictly a control-board communication failure.

LG's own error-code documentation instructs you to unplug the dryer for 60 seconds and restart it as the first step. If the code returns after that reset, LG indicates a repair is likely needed, which points to a board-level hardware or connector fault.

## Before You Replace Anything

Homeowners sometimes replace the display board first, but a poor connection or a failed main control board is just as likely. Always inspect the wiring harness between the two boards and verify stable 240 V supply power before ordering a board.

[Jump to Fix](#fix)

## Common Causes

- **Power interruption, surge, or control-board lockup (~45%)** A brief power interruption or surge can leave the display and main boards out of sync, blocking the display from reading firmware data until a full power cycle resets both boards.
- **Loose or corroded connector between boards (~25%)** The harness plug linking the display PCB to the main PCB can work loose, corrode, or develop oxidized pins, breaking the data path that carries software read commands.
- **Failed or corrupted firmware on the main PCB (~15%)** The main control board may hold unreadable or corrupted software data, so the display cannot successfully load it, which is the specific condition LG names for this code.
- **Defective main control board (~10%)** The main PCB itself may have a failed memory chip, processor fault, or solder crack that prevents it from responding to read requests from the display.
- **Defective display PCB (~5%)** The display board's communications circuit or processor may be faulty, rendering it unable to read software from a healthy main board.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the dryer still show E00 after unplugging for 60 seconds and restarting?</summary>
<div class="dtree-body"><strong>Yes:</strong> The power reset did not clear the fault, so move to connector inspection and voltage verification.<br><strong>No:</strong> The code was likely a temporary lockup or surge-related glitch. Run a full test cycle to confirm stable operation.</div>
</details>

<details class="dtree"><summary>Is the dryer plugged into a grounded 240 V outlet that matches the rating plate, and is the circuit breaker fully on?</summary>
<div class="dtree-body"><strong>Yes:</strong> Supply power is correct. Inspect the wiring harness and connectors between the display and main boards for damage or looseness.<br><strong>No:</strong> Correct the power supply issue first. Low voltage or a tripped breaker can cause communication faults between boards.</div>
</details>

<details class="dtree"><summary>Are the connectors between the display PCB and main PCB clean, fully seated, and free of corrosion or pinched wires?</summary>
<div class="dtree-body"><strong>Yes:</strong> The harness is good. If the code still returns after a power cycle, one of the boards is likely failed and requires replacement.<br><strong>No:</strong> Clean the connector pins with contact cleaner, reseat the plug firmly, and retry. A poor connection is a common cause of read failures.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Unplug the dryer** or turn off the circuit breaker, wait a full 60 seconds, then restore power and press the start button to see if the code clears.
2. **Verify the power supply.** Confirm the dryer is connected to a grounded outlet matching the rating plate (240 V) and check that the breaker has not tripped or been partially reset.
3. **Access the control boards.** Remove the top panel or console (consult your model's service manual for fastener locations) to expose the display PCB and main control board.
4. **Inspect the wiring harness.** Locate the multi-pin connector running from the display board to the main board and check for loose seating, bent pins, corrosion, or pinched wires. Disconnect the plug, clean the pins with electronic contact cleaner if oxidized, and reseat it firmly.
5. **Run a test cycle.** If the connector was loose or dirty and you have reseated it, restore power and start a normal dry cycle to verify the E00 code does not return.
6. **Replace the main control board** if the code persists after connector repair and a full power reset. The main PCB is the component that holds the software data the display cannot read.
7. **Replace the display PCB** if the main board is confirmed good (by swapping or professional diagnosis) and the code still appears, indicating the display's read circuit is faulty.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG dryer main control board (PCB assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-dryer-e00-error-code&k=LG+dryer+main+control+board+%28PCB+assembly%29&tag=errorcodefixes-20) \| Match by your model number. The main PCB stores the firmware the display must read. |
| LG dryer display board (user interface PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-dryer-e00-error-code&k=LG+dryer+display+board+%28user+interface+PCB%29&tag=errorcodefixes-20) \| Match by your model number. The display PCB attempts to read software from the main board. |
| Control-board wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-dryer-e00-error-code&k=Control-board+wiring+harness&tag=errorcodefixes-20) \| Only if the existing harness shows melted insulation, broken wires, or damaged connector housing. |

## When to Call a Pro

Call a technician if the E00 code returns after you have completed a 60-second power reset, verified stable 240 V supply, and inspected and reseated the connectors between the display and main boards. Board-level diagnosis often requires a multimeter, wiring diagram, and experience isolating which PCB has failed. If you are uncomfortable working inside the control console or tracing low-voltage data lines, a qualified appliance technician can test each board, confirm the fault, and replace only the defective component. Professional service also ensures you do not replace both boards unnecessarily.

**Rough cost:** DIY runs about $80–200 in parts (board), 30–60 min. A pro service call runs about $150–350.
