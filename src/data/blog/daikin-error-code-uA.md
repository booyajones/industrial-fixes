---
title: "Daikin UA Error Code — Mismatched Indoor/Outdoor Unit Fix"
description: "Daikin UA means the indoor PCB and the outdoor PCB compared model IDs over the F1/F2 link and decided they aren't a compatible pair. It's almost always a..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: daikin-error-code-uA
featured: false
draft: false
tags:
  - daikin
  - hvac
  - error-codes
  - mismatched-indoor-outdoor-units
---
## Quick answer

Daikin UA means the indoor PCB and the outdoor PCB compared model IDs over the F1/F2 link and decided they aren't a compatible pair. It's almost always a real mismatch — the installer pulled the wrong indoor head out of stock, or a replacement PCB shipped without the right model-code DIP switches set — not a phantom fault.

## What UA means on a Daikin mini split

On power-up and at periodic intervals after, the indoor and outdoor PCBs exchange a handshake that includes each unit's model class, capacity in BTUH, and refrigerant type. Daikin's firmware compares those values against an internal compatibility matrix. If the indoor head and the outdoor condenser fall outside the allowed pairing (capacity mismatch beyond ±20%, wrong refrigerant family, wrong product class, or a multi-zone branch box mismatch), the indoor controller logs UA and refuses to start the compressor.

UA is *not* a wiring fault — F1/F2 is communicating fine, both units see each other, the issue is what they're saying to each other. That distinguishes UA from U4 (no communication at all) and from UH (unset address on multi-port systems).

UA is most common in three real-world situations: (1) a homeowner or installer mixed a 12k BTU MXS condenser with a 24k FTX head from a parts shelf because both were "Daikin" and that was close enough; (2) a service tech swapped a failed indoor or outdoor PCB and the new board shipped at factory defaults without the right capacity/model jumpers set; (3) a multi-zone installation where one indoor head was changed from a 9k to a 15k and now the total connected capacity exceeds the outdoor unit's rating.

The fourth, rarer case: an R-410A outdoor unit paired with an R-454B indoor head, or vice versa, by an installer who didn't check refrigerant on both nameplates. Daikin's newer R-454B equipment will throw UA hard if you try to mate it to an R-410A unit — and that's a *good* thing, because mixing refrigerants on a mini-split is a fire hazard with A2L equipment.

## Common causes (ranked by frequency)

1. **Replacement PCB shipped without correct model-code jumpers set** — service kits often arrive at factory defaults. Check the wiring diagram for required jumper positions (J8, J9, J11 on most platforms) and set them per the model nameplate before energizing.
2. **Wrong indoor head paired with outdoor condenser** — installer error at original install or after a swap.
3. **Multi-zone over-capacity** — a 3-zone MXS condenser rated for 24k total has had a head upsized so connected capacity now exceeds rating.
4. **Refrigerant family mismatch** — R-410A condenser with R-454B head (or vice versa). Will not run and *should* not run.
5. **Counterfeit or gray-market indoor head** — Daikin gray-market product sold for export to other regions may report a different model code than the matching domestic outdoor expects.
6. **Stale firmware on a remanufactured outdoor PCB** — rare, but a Daikin reman board may carry an older firmware that doesn't recognize a newer indoor model class.

## Step-by-step fix

1. **Pull both nameplates and write down the full model numbers.** Outdoor model from the side data plate, indoor model from the inside of the front cover or the bottom of the head. You need both complete model strings (e.g., RX12NMVJU on the outdoor, FTXS12LVJU on the indoor) — capacity codes and series letters matter.

2. **Look up the pairing in the Daikin compatibility chart for your region.** Daikin North America publishes a current matrix at the Daikincomfort dealer portal and most authorized distributors will look it up for you in 2 minutes. A 12k indoor must match to a 12k single-zone outdoor or be one head in an MXS multi-zone where total connected capacity falls within the outdoor's rated range (typically 80%-130% of nominal). If the chart says "incompatible," you have a real mismatch and one of the two units needs to be replaced.

3. **Verify refrigerant on both nameplates.** R-410A is printed clearly on the data plate. R-454B units carry an A2L warning label and the refrigerant designation. **Do not under any circumstance attempt to run an R-410A outdoor with an R-454B indoor or vice versa — the indoor coil pressure ratings and the metering devices are different, and on A2L equipment you can create a flammable refrigerant scenario.**

4. **If a PCB was recently replaced, check jumper and DIP-switch settings against the wiring diagram.** Daikin service PCBs (typical part numbers in the 4017019 and 5009566 series) commonly ship with jumpers J8/J9 in default position. The wiring diagram glued inside the service cover specifies the correct jumper positions for that model — for example, on a FTXS09 head the indoor controller PCB requires J9 cut for proper capacity reporting. If the installer didn't set the jumpers, the board reports default capacity and you get UA.

5. **For multi-zone MXS systems, sum the connected indoor capacity.** Add up the BTUH of each connected indoor head and compare to the outdoor nameplate. A 3MXS24 is rated 24,000 BTUH connected total; if you've got an 18k + 12k + 9k connected (39k total), you've exceeded rated and UA is the warning. Remove or downsize a head, or upsize the outdoor.

6. **Check for address conflicts on branch-box installations.** Where applicable, each indoor on an MXS branch system gets a unique address. Two indoors set to the same port will throw UA at one of them. The address is usually set via a rotary switch on the indoor PCB — verify each is unique.

7. **Cycle power at the breaker for 5 minutes and recheck.** After confirming model compatibility, jumper positions, and addressing, kill power at both indoor and outdoor breakers, wait 5 minutes for the inverter bus capacitors to bleed, and re-energize. UA should clear on the next handshake. If it doesn't, you have a real hardware mismatch that wiring resets won't fix.

8. **If UA persists with verified-correct equipment and jumpers, suspect outdoor PCB firmware.** This is the rare case. A remanufactured outdoor PCB carrying older firmware may not recognize a newer indoor model. Daikin tech support can confirm and either ship a current-firmware board or provide a flash-update procedure. This is a phone call, not a guess.

> **Field knowledge nugget:** I see UA most often after a homeowner DIY repair where the homeowner bought a "matching" indoor head off a marketplace site. The trap: Daikin sells very similar-looking FTXS, FTX, and CTXS wall heads with overlapping capacity codes but different metering devices and different refrigerant pre-charges. An FTXS09LVJU (R-410A, 9k BTU North American single zone) looks identical to an FTKR25 (R-32, 9k BTU Asian-market) from the front, and both will land on a Daikin single-zone outdoor mechanically — but the metering and refrigerant-family report mismatch trip UA hard. If you're inheriting a UA after a homeowner repair, always check that the indoor model string ends with -VJU or -VJUA (North American market) and that the refrigerant family matches the outdoor. Daikin does not warranty cross-market pairings even if they're both "Daikin" branded.

**Safety:** R-454B is an A2L mildly flammable refrigerant. If a UA diagnosis ends with refrigerant-circuit work to swap an indoor or outdoor unit, you must follow the A2L charge limits per UL 60335-2-40, ventilate the work area, eliminate ignition sources, recover refrigerant to a properly rated A2L recovery cylinder, and use leak detectors rated for A2L refrigerants. The lower flammability limit for R-454B is ~11.9% by volume. An installer not trained on A2L work should not be opening R-454B service ports. EPA 608 with A2L endorsement is the current requirement.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Outdoor inverter PCB (RX/RXS series) | 5009566-xx | $385–$620 | [HVAC Parts Shop](https://www.hvacpartsshop.com) / [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=daikin-error-code-uA) |
| Indoor controller PCB (FTX/FTXS) | 4017019-xx | $245–$380 | [HVAC Parts Shop](https://www.hvacpartsshop.com) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Wireless remote BRC082 | BRC082A43 | $95–$140 | [HVAC Parts Shop](https://www.hvacpartsshop.com) |
| Wall thermostat BRC1E73 | BRC1E73 | $175–$240 | [Grainger](https://www.grainger.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=daikin-error-code-uA) |
| Replacement nameplate decal | varies | $5–$15 | Daikin distributor |

For PCB swaps, order with the harness clip and gasket set — Daikin PCB kits often ship without and you need them for IP-rated reassembly.

## When to call a professional

Call a NATE-certified or Daikin-authorized installer if any of these apply:

- You believe you have a refrigerant mismatch (R-410A vs R-454B). Don't try to mate them and don't try to convert one to the other — replace the wrong-refrigerant unit.
- The indoor or outdoor unit is gray-market or sourced from outside North America. Daikin warranty doesn't cover cross-market pairings and the model strings don't always line up cleanly.
- You're on a Daikin VRV or Sky Air multi-zone system. Address conflicts and capacity-rating math on VRV are their own discipline.
- UA persists after verified-correct jumpers, model match, and a clean power cycle. That points to firmware or a PCB hardware problem worth a tech-support call rather than another board swap.
- The system is under the original 10-year parts warranty and an obvious mismatch points back to the original installer. Daikin will sometimes coordinate a warranty resolution with the installing contractor.

## FAQs

**Will Daikin UA go away if I cycle the breaker?**
No. UA is a configuration mismatch, not a transient fault. The handshake repeats on every power-up, finds the same mismatch, and re-logs UA. Fix the mismatch.

**Can I jumper around UA to force the system to run?**
Don't. UA is a safety-critical lockout on Daikin equipment, especially with R-454B refrigerant. Forcing a mismatched pair to run can over-pressure the indoor coil, cause oil-return problems for the compressor, and on A2L equipment can create a flammable scenario. There's no legitimate field workaround.

**Why did my Daikin throw UA only after I had service work done?**
Two common causes: the tech swapped a PCB without setting the model-code jumpers correctly, or the tech replaced one unit (indoor or outdoor) with a parts-bin substitute that wasn't in the compatibility matrix. Get the tech back to verify the swap was a correct pairing.

**Can I use a 12k indoor head on a 24k Daikin condenser?**
On a single-zone system, no — Daikin single-zone outdoors expect a matched single indoor at the same capacity. On a multi-zone MXS condenser, you can mix capacities as long as the total connected falls within the condenser's rated range, and the model strings are all from Daikin's compatibility matrix for that outdoor.

**Does UA mean I have to replace the whole system?**
No, just the mismatched piece. If you've got a correct outdoor and a wrong indoor, you replace the indoor head. The line set and electrical run usually stay (assuming no refrigerant mismatch).

## Related guides

- [Daikin U4 Error Code — Indoor-Outdoor Communication Fix](/posts/daikin-error-code-u4)
- [Daikin L5 Error Code — Compressor Lock Fix](/posts/daikin-error-code-l5)
- [Daikin A6 Error Code — Indoor Fan Motor Fix](/posts/daikin-error-code-a6)

## See Also

- [Daikin J3 Error Code — Discharge Pipe Temperature Sensor Fault Fix](/posts/daikin-j3-error-code/)
- [Daikin C4 Error Code — Heat Exchanger Coil Sensor: Causes & Fix](/posts/daikin-c4-error-code/)
- [Daikin U9 Error Code — Causes & Fix](/posts/daikin-u9-error-code/)
- [Daikin VRV IV Fault Codes - Commercial System Diagnostic Guide](/posts/daikin-vrv-iv-fault-codes/)
