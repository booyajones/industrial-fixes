---
title: "Frigidaire Washer E45 Error Code - Causes & Fix"
description: "E45 means a door-lock control circuit fault. Most often the door lock assembly or its PTC has failed. Replace the lock or control board."
pubDatetime: 2026-06-09T05:10:33Z
modDatetime: 2026-06-09T05:10:33Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - washer
  - frigidaire
<<<<<<< Updated upstream
most_likely_cause: "defective door lock assembly or PTC element"
likelihood: "the most common cause"
diy_or_pro: "diy"
=======
money_part: "Main electronic control board"
>>>>>>> Stashed changes
---

## Frigidaire Washer E45 Error Code — What It Means

E45 on a Frigidaire washer indicates a failure in the door-lock control circuit. According to Frigidaire's error-code documentation, this fault points to a problem with the controller or the door-lock mechanism itself. The control board cannot complete the lock circuit, so the washer will not start or advance.

The fault usually lies in the door lock assembly, the PTC element inside the lock, or the wiring path between the lock and the main control board. If those components test normal, the control board itself is defective. This is not a load-balance or drain issue despite the similar-sounding code name.

## Before You Replace Anything

Many people replace the control board first. Always test the door lock PTC resistance (should read about 1500 ohms) and inspect the lock wiring before replacing the expensive control board.

[Jump to Fix](#fix)

## Common Causes

- **Defective door lock assembly or PTC (~60%)** The lock mechanism or its internal PTC heater element is open, shorted, or mechanically broken so the control circuit cannot complete.
- **Open or shorted wiring to the door lock (~20%)** Damaged harness, loose connectors, or corrosion in the circuit path between the lock and the control board prevents proper communication.
- **Failed main control board (~15%)** The control board itself has a defective door-lock driver circuit or relay even though the lock and wiring test normal.
- **Corrosion or poor ground connection (~5%)** Rust or oxidation at the lock terminals or ground points creates high resistance that the controller reads as a fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the door latch close and you hear a click when you shut it?</summary>
<div class="dtree-body"><strong>Yes:</strong> The mechanical latch works but the electrical lock circuit is still failing. Proceed to resistance testing.<br><strong>No:</strong> The door lock mechanism itself is broken or misaligned. Replace the door lock assembly before further diagnosis.</div>
</details>

<details class="dtree"><summary>With power off and the lock unplugged, does the PTC in the lock measure about 1500 ohms?</summary>
<div class="dtree-body"><strong>Yes:</strong> The lock PTC is good. Check the wiring harness and connectors for damage, then suspect the control board.<br><strong>No:</strong> The PTC is open or shorted. Replace the door lock assembly.</div>
</details>

<details class="dtree"><summary>After replacing the door lock, does E45 still appear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board lock-driver circuit is defective. Replace the main control board.<br><strong>No:</strong> The door lock was the fault. Run a full test cycle to confirm the repair.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Unplug the washer** and wait two minutes for capacitors to discharge before opening any panels or touching wiring.
2. **Remove the top or front panel** to access the door lock assembly mounted inside the door frame.
3. **Disconnect the door lock harness** and inspect the terminals and wiring for burn marks, corrosion, or damage.
4. **Measure the PTC resistance** across the lock terminals with a multimeter. Frigidaire specifies about 1500 ohms for a good PTC.
5. **Replace the door lock assembly** if the PTC reads open (infinite resistance) or shorted (near zero), or if the lock mechanism is physically broken.
6. **Check the wiring path** from the lock to the control board for continuity and secure all connectors if the lock tested normal.
7. **Replace the main control board** if the lock, PTC, and wiring all test good but E45 persists after power cycling the machine.
8. **Reassemble the washer**, plug it in, and run a short test cycle to verify the door locks and the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Frigidaire washer door lock assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-frigidaire-washer-e45-error-code&k=Frigidaire+washer+door+lock+assembly&tag=errorcodefixes-20) \| Includes the latch mechanism and PTC heater element. Verify your model number for the correct lock style (top-load or front-load). |
| Frigidaire washer main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-frigidaire-washer-e45-error-code&k=Frigidaire+washer+main+control+board&tag=errorcodefixes-20) \| Only if the door lock and wiring test normal. Match your model and serial number exactly. |

## When to Call a Pro

Call a technician if you are not comfortable using a multimeter to measure resistance, if you cannot access the door lock without removing the entire cabinet, or if both the lock and control board test inconclusive and you need a systematic circuit trace. A pro can also update control-board firmware if a known bug affects your model. If the washer is still under warranty, use only factory-authorized service to preserve coverage.

**Rough cost:** DIY runs about $40-90 in parts, 30-60 min. A pro service call runs about $150-280.
