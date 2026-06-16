---
title: "Electrolux Washer E52 Error - Causes & Fix"
description: "E52 means the control isn't receiving motor-speed feedback from the tacho sensor. Most often a failed tachogenerator or loose motor wiring."
pubDatetime: 2026-06-14T05:38:27Z
modDatetime: 2026-06-14T05:38:27Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - washer
  - electrolux
money_part: "Electrolux washer drive motor"
most_likely_cause: "Failed or weak tachogenerator (tacho) on the drive motor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Unplug the washer for 5 minutes, then power it back on and retest to rule out a transient control glitch."
  - "Rotate the drum by hand to confirm it turns freely with no binding or obstruction."
  - "Inspect the motor connector for loose, corroded, or burned terminals and reseat the plug."
---

## Electrolux Washer E52 Error — What It Means

E52 on an Electrolux washer is a motor-speed feedback fault. The control board is not receiving the expected signal from the tachogenerator (tacho) on the drive motor, or the motor circuit is not behaving as commanded. The practical symptom is that the washer thinks the motor is not turning correctly or cannot confirm motor rotation feedback.

This is not a water fill or drain fault. It points to the motor tachogenerator, motor wiring harness, the motor itself (including worn carbon brushes on brushed motors), mechanical drag preventing drum rotation, or the main control board's motor-drive circuitry. The exact diagnostic path depends on your model, but the fault always centers on motor rotation and feedback.

## Before You Replace Anything

Many people replace the main control board first. Check the motor tacho resistance (often around 171–196 Ω on some models) and inspect motor wiring and brushes before replacing the board.

[Jump to Fix](#fix)

## Common Causes

- **Failed tachogenerator (tacho) (~35%)** The tacho sensor on the motor cannot generate the speed-feedback signal the control board expects, so the board throws E52.
- **Loose or damaged motor wiring harness (~25%)** Corroded, heat-damaged, or broken wires between the motor and control board interrupt the tacho signal or motor power.
- **Worn motor carbon brushes (~20%)** On brushed motors, worn brushes prevent the motor from starting or turning properly, and the control cannot confirm rotation.
- **Mechanical drag or obstruction (~10%)** A jammed drum bearing, stuck object, or seized motor bearing keeps the motor from turning, triggering the fault.
- **Failed drive motor (~5%)** An open winding, shorted coil, or thermal-overload condition in the motor itself can prevent normal rotation and feedback.
- **Main control board failure (~5%)** A fault in the board's motor-drive or tacho-sense circuitry can misread or fail to process a good signal from the motor.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the drum rotate freely by hand when you spin it with the washer unplugged?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drum and bearings are probably OK. Move on to electrical checks of the motor, tacho, and wiring.<br><strong>No:</strong> Something is binding the drum or motor. Remove the belt (if accessible) and test again. If the drum is still stuck, suspect a bearing or foreign object. If the motor shaft is stuck, the motor or motor bearing has failed.</div>
</details>

<details class="dtree"><summary>Is the motor wiring connector tight and free of corrosion or burn marks?</summary>
<div class="dtree-body"><strong>Yes:</strong> The harness connection is probably good. Measure tacho resistance at the motor connector (often 171–196 Ω on some models, consult your service manual).<br><strong>No:</strong> Clean or replace the connector terminals or the harness. A poor connection is a common intermittent cause of E52.</div>
</details>

<details class="dtree"><summary>Can you measure roughly 171–196 Ω across the tacho terminals on the motor connector (model-specific)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The tacho circuit looks OK at the motor. Check continuity from the motor connector to the control board connector to rule out a harness break, then suspect the control board if all wiring is good.<br><strong>No:</strong> The tacho or motor assembly is faulty. Replace the motor (or tacho if serviced separately on your model).</div>
</details>

## Step-by-Step Fix {#fix}

1. **Unplug the washer** and wait 5 minutes, then restore power and run a test cycle to confirm the fault is not a transient control glitch.
2. **Rotate the drum by hand** to verify it spins freely with no grinding, binding, or heavy resistance.
3. **Access the drive motor** (usually behind the front lower panel or rear panel, depending on model) and unplug the motor connector.
4. **Inspect the motor connector and harness** for loose pins, corrosion, heat damage, or broken wires, and reseat or repair as needed.
5. **Measure the tachogenerator resistance** across the tacho terminals at the motor connector using a multimeter (one source reports 171–196 Ω, but consult your model's service data for the correct range).
6. **Check motor brushes** if your motor uses carbon brushes by removing the brush caps and pulling the brushes out to measure remaining length (replace if worn short or chipped).
7. **Test continuity from motor connector to control-board connector** to confirm the harness carries the tacho signal without a break, then replace the motor or control board based on your findings.
8. **Run a full test cycle** after repair to verify stable agitation and spin with no return of E52.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Electrolux washer drive motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-electrolux-washer-e52-error-code&k=Electrolux+washer+drive+motor&tag=errorcodefixes-20) \| Match the exact model number and motor part number from your service label. |
| Motor carbon brushes | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-electrolux-washer-e52-error-code&k=Motor+carbon+brushes&tag=errorcodefixes-20) \| For brushed motors only; sold as a pair, model-specific. |
| Main control board / electronic module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-electrolux-washer-e52-error-code&k=Main+control+board+%2F+electronic+module&tag=errorcodefixes-20) \| Replace only after confirming motor, tacho, and wiring are good. |
| Motor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-electrolux-washer-e52-error-code&k=Motor+wiring+harness&tag=errorcodefixes-20) \| If connector terminals are heat-damaged or wires are broken and cannot be repaired in place. |

## When to Call a Pro

Call a pro when you are not comfortable working with 120 V or 240 V live circuits, accessing the motor (which often requires removing panels and sometimes the drum or tub), or using a multimeter to measure resistance and continuity. The diagnosis requires back-probing connectors, interpreting tacho resistance values that vary by model, and understanding motor-drive circuits. If you have confirmed the drum spins freely and reseated the motor connector but the fault persists, a technician with Electrolux-specific service documentation and a meter can quickly isolate whether the motor, tacho, harness, or control board is at fault and avoid replacing expensive parts by guess.

**Rough cost:** A pro service call runs about $150-350.
