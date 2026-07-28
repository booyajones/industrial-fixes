---
title: "Electrolux Washer E24 Error Code - Causes & Fix"
description: "E24 means a fault in the drain pump triac sensing circuit on the control board. The most common fix is replacing the main control board."
pubDatetime: 2026-06-10T18:22:32Z
modDatetime: 2026-06-10T18:22:32Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - washer
  - electrolux
money_part: "Main control board (PCB)"
part_price: "$150-300"
most_likely_cause: "Failed main control board"
likelihood: "the most common cause"
diy_or_pro: "diy"
---

## What this code means
The E24 error code indicates a fault in the sensing circuit of the drain pump triac on the main control board. The triac is the electronic switch that powers the drain pump, and the board uses an internal sensor to monitor whether the triac is working correctly. When the board detects a mismatch between the triac status and the triac sensing signal, it throws E24. This is an electronic control fault, not a mechanical drain problem. The board cannot reliably command the drain pump or verify its operation even if the pump itself is physically intact.

While the code points to internal board circuitry, the fault can originate from a failed triac component on the board, damaged wiring between the board and pump, or rarely from a pump that is mechanically jammed and drawing abnormal current. E24 is distinct from E21, which signals a long pump-out time due to blockage. E24 is almost always an electrical issue requiring board or wiring repair.

## Before You Replace Anything

Many people replace the drain pump first because the code mentions the pump. Test wiring continuity and check for mechanical blockage before buying a new pump. If the pump spins freely and the wiring is intact, the board is the real problem.

## Common Causes

- **Failed main control board (~65%)** The triac component or its internal sensing circuitry on the PCB has burned out, shorted, or developed an open circuit that the board cannot self-correct.
- **Faulty wiring or loose connection (~20%)** Damaged, corroded, or loose wires between the control board and drain pump send false signals that the board interprets as a triac sensing fault.
- **Stuck or blocked drain pump (~10%)** A mechanically jammed pump impeller (from debris like coins or zippers) can cause abnormal current draw that triggers a triac status mismatch, though this is rare with E24.
- **Power supply voltage spikes (~5%)** Intermittent surges or brown-outs from the home electrical supply can damage the sensitive triac sensing circuit on the control board over time.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drain pump hum or spin when you manually advance the washer to the drain cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The pump motor is receiving power and trying to work, which points to a control board sensing fault rather than a mechanical jam. Inspect wiring and then plan to replace the control board.<br><strong>No:</strong> The pump may be jammed with debris or the wiring is broken. Check the pump filter and impeller for blockage and test wiring continuity before replacing the board.</div>
</details>

<details class="dtree"><summary>Are there any visible burns, scorch marks, or melted spots on the main control board near the pump connections?</summary>
<div class="dtree-body"><strong>Yes:</strong> The triac or surrounding circuitry has physically failed. Replace the main control board.<br><strong>No:</strong> The failure is internal to the board or in the wiring harness. Continue with wiring checks and resistance tests.</div>
</details>

<details class="dtree"><summary>Do you have a multimeter and can you measure the resistance across the drain pump terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> A reading between 100Ω and 300Ω is typical for a healthy pump (varies by model). Infinite resistance means an open pump motor, zero means a short. If the pump tests good, the board is at fault.<br><strong>No:</strong> Call a technician to test the pump electrically and confirm whether the board or pump needs replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Unplug the washer** and turn off the water supply to eliminate shock and flood risk.
2. **Check the drain pump filter and impeller** by opening the small access door at the lower front of the washer, removing any debris like coins, hair clips, or fabric, and spinning the impeller by hand to confirm it rotates freely.
3. **Inspect the drain hose** from the pump to the standpipe or laundry sink for kinks, clogs, or restrictions that could cause back-pressure and abnormal pump behavior.
4. **Remove the top or rear panel** (depending on your model) to access the main control board and the wiring harness that connects to the drain pump, noting the location of the pump connector on the board.
5. **Examine all wires and connectors** between the control board and pump for broken strands, corroded terminals, or loose pins, and repair or replace any damaged harness sections before proceeding.
6. **Test the drain pump resistance** with a multimeter set to ohms by disconnecting the pump wires and measuring across the motor terminals; a typical reading is 100 to 300 ohms, and if you see infinite resistance the pump is open and needs replacement.
7. **Replace the main control board** if the pump is mechanically free, the wiring is intact, and the pump resistance is within spec, because the triac sensing circuit inside the board has failed and cannot be repaired in the field.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Main control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-electrolux-washer-e24-error-code&k=Main+control+board+%28PCB%29&tag=errorcodefixes-20) \| Order by your washer's full model number; boards are model-specific and often include the triac circuit as a soldered component. |
| Drain pump assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-electrolux-washer-e24-error-code&k=Drain+pump+assembly&tag=errorcodefixes-20) \| Only needed if the pump impeller is cracked, the motor windings test open or shorted, or the pump housing is damaged. |
| Wiring harness (pump to board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-electrolux-washer-e24-error-code&k=Wiring+harness+%28pump+to+board%29&tag=errorcodefixes-20) \| Replacement harness if wires are corroded or broken; some techs splice and solder individual conductors instead. |

## When to Call a Pro

Call a professional if you are uncomfortable working inside the washer cabinet, if you cannot safely disconnect and test electrical components with a multimeter, or if you have replaced the wiring and pump but the E24 code persists. A technician can quickly isolate whether the board, pump, or an intermittent power supply issue is at fault. Also call a pro if your washer is still under warranty or if you see evidence of water damage inside the control box, since moisture can cause secondary failures that require thorough inspection.

**Rough cost:** DIY runs about $150-300 for control board, 45-90 min. A pro service call runs about $250-450 including service call and board.
