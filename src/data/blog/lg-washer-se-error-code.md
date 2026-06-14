---
title: "LG Washer SE Error Code - Causes & Fix"
description: "SE means sensor error. Power off, unplug for 10 seconds, reconnect, and retry. If the code returns, call LG service for diagnosis."
pubDatetime: 2026-06-08T04:40:49Z
modDatetime: 2026-06-08T04:40:49Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - washer
  - lg
diy_or_pro: "pro"
free_checks:
  - "Unplug 30 sec, check for tangled or severely unbalanced load causing rotor position sensor confusion"
  - "Inspect Hall sensor connector on stator for corrosion, moisture, or looseness"
  - "Run empty spin cycle to rule out overload-triggered false SE code"
no_buy_pct: "30%"
part_price: "$120-220"
money_part: "LG direct-drive motor / stator assembly"
most_likely_cause: "Loose or corroded motor harness connector"
---

## LG Washer SE Error Code — What It Means

LG defines SE as a sensor error. The code does not point to one specific component across all models. LG's official guidance is to perform a hard reset by unplugging the washer for about ten seconds, then restoring power and restarting the cycle. If the code clears, the fault was transient. If SE returns, LG directs you to professional service because the exact failed sensor or circuit depends on your model.

Some repair sources describe SE as a motor-related fault involving the hall sensor, stator, or main control board, but those interpretations are model-specific and not stated on LG's own support pages. Without your exact model number and wiring diagram, guessing which component failed can lead to unnecessary parts replacement. The safest path is the power reset, then professional diagnosis if the error persists.

## Before You Replace Anything

Homeowners sometimes replace the main control board first, but a loose motor harness connector or a failed hall sensor on the motor assembly can also trigger SE. Inspect all motor wiring and connectors before ordering expensive boards.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded motor harness connector (~30%)** Vibration or moisture can unseat the plug between the direct-drive motor and the main PCB, breaking the hall-sensor signal.
- **Transient control-board glitch (~25%)** A brief firmware hang or noise spike can log a false sensor error that clears with a power cycle.
- **Failed hall sensor or rotor position sensor (~20%)** The sensor that tells the control board where the motor rotor is located can fail, especially on high-cycle machines.
- **Stator or motor assembly fault (~15%)** Winding shorts, broken magnets, or rotor damage prevent proper motor commutation and trigger a sensor fault.
- **Main PCB failure (~10%)** The control board's motor-driver circuit or sensor input stage can fail and misread or lose the hall signal.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the SE code disappear after unplugging the washer for ten seconds and restarting?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was transient. Run a full test cycle and monitor. If SE does not return, no repair is needed.<br><strong>No:</strong> The fault is persistent. Move to the next check.</div>
</details>

<details class="dtree"><summary>Can you rotate the drum smoothly by hand with the washer off and empty?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor rotor is free. The problem is electrical-check connectors, then suspect the hall sensor or main board.<br><strong>No:</strong> A mechanical bind (foreign object, bad bearing) may be stalling the motor and confusing the sensor. Inspect the drum and tub.</div>
</details>

<details class="dtree"><summary>Is the motor harness connector at the back of the tub firmly seated and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is intact. The fault is likely the hall sensor, stator assembly, or main PCB. Call a technician for component-level testing.<br><strong>No:</strong> Clean the pins, reseat the connector, and retest. A poor connection often mimics a sensor failure.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off and unplug** the washer at the wall outlet, then wait ten full seconds to allow the control board to reset.
2. **Restore power** and select a rinse-and-spin or normal cycle to see if the SE code reappears.
3. **If the code returns immediately**, pull the washer away from the wall and remove the rear service panel or top cover (depending on your model) to access the motor harness.
4. **Inspect the motor connector** where the wire harness plugs into the stator assembly or motor hub. Look for loose pins, green corrosion, or backed-out terminals.
5. **Disconnect and reconnect** the motor plug. Wipe both the plug and socket with contact cleaner if you see any oxidation.
6. **Reassemble and retest** the cycle. If SE persists after the connector check, the hall sensor, stator, or main board has failed and requires part-level diagnosis.
7. **Record your model and serial number** from the door frame or tub rim, then call LG service or a qualified technician with that information so they can order the correct sensor or motor assembly for your machine.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG direct-drive motor / stator assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-se-error-code&k=LG+direct-drive+motor+%2F+stator+assembly&tag=errorcodefixes-20) \| Model-specific. Verify your exact part number from the service label before ordering. |
| LG washer main control board / PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-washer-se-error-code&k=LG+washer+main+control+board+%2F+PCB&tag=errorcodefixes-20) \| Also model-specific. Test motor and harness first to avoid replacing a good board. |

## When to Call a Pro

Call a professional when the SE code returns after a power reset and you have verified that all visible connectors are seated. Diagnosing a failed hall sensor versus a bad stator winding versus a main-board fault requires a multimeter, knowledge of your model's wiring diagram, and sometimes an oscilloscope to watch the commutation signals. LG's own guidance stops at professional service for persistent SE faults because the exact sensor or circuit varies by model. Attempting to replace the motor or control board without proper testing often wastes money on the wrong part.

**Rough cost:** A pro service call runs about $150-350 depending on the part diagnosed.
