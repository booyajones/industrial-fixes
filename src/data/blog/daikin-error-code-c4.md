---
title: "Daikin C4 Error Code — Indoor Heat Exchanger Thermistor Fix"
description: "Daikin C4 means the indoor heat-exchanger thermistor (R2T or the equivalent coil sensor depending on platform) reads open, shorted, or out of the expected..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: daikin-error-code-c4
featured: false
draft: false
tags:
  - daikin
  - hvac
  - error-codes
  - indoor-heat-exchanger-thermistor-fault
---
## Quick answer

Daikin C4 means the indoor heat-exchanger thermistor (R2T or the equivalent coil sensor depending on platform) reads open, shorted, or out of the expected resistance range. It's almost always the thermistor itself, which clips to the indoor evaporator coil and degrades from condensate exposure over time. Ohm it cold — it should read about 10 kΩ at 77 °F — and replace it if it reads OL or near zero.

## What C4 means on a Daikin mini split

Daikin C-codes are thermistor input faults read at the indoor PCB. The indoor unit carries multiple temperature sensors: a return-air thermistor (R1T) that sets the room control loop, and one or two coil thermistors (R2T, R3T) that monitor the evaporator/condenser coil temperature for defrost timing, freeze protection, and heating thermal-off control. C4 specifically targets the heat-exchanger coil thermistor — the one clipped to the indoor coil between two return bends, typically partway down the slab on wall-mount heads or near the air inlet of the coil on cassettes.

The PCB drives that thermistor as part of a voltage-divider circuit, reading the divider midpoint through an ADC pin. If the input reads close to either rail (open or short), firmware logs C4 and disables compressor operation to prevent uncontrolled freezing or overheating of the coil.

The good news: C4 is almost never a board failure. The indoor coil thermistor sits in a damp environment, gets soaked with condensate on every cooling cycle, and the thermistor lead-to-body junction is the standard failure point. Five to seven years is typical service life. Outdoor coil thermistors (R3T, R4T on the outdoor side) fail less often because they don't see as much condensate.

C4 is the same code logic on most M-Series wall mounts (FTX, FTXS, FTXN, MTKN), MLZ cassettes, and SEZ ducted heads. On Sky Air and VRV equipment the code may be reported as C4-XX with a sub-code, but the diagnostic is the same — find the coil thermistor, verify resistance against the curve, replace if out.

## Common causes (ranked by frequency)

1. **Failed thermistor element from condensate corrosion** — most common. Reads open or wildly out of range.
2. **Chafed or pinched thermistor harness** — usually where the harness routes past the blower wheel housing or under the drain pan. Shows as intermittent C4 that comes and goes with vibration.
3. **Disconnected thermistor at the PCB connector** — typically CN21 or similar on indoor PCB. Often after recent service where the tech didn't fully re-seat the plug.
4. **Failed PCB thermistor input** — rare, but the ADC pin or the divider resistor on the board can fail. Last suspicion, not first.
5. **Wrong thermistor part used in a previous repair** — a 5 kΩ thermistor in place of the correct 10 kΩ (or vice versa) will read out of range for the firmware's expected curve.

## Step-by-step fix

1. **Power down the indoor head at the breaker.** Open the front cover, remove the air filter, and pull the front panel off the unit. On most FTX/FTXS wall mounts, the front panel pops at four clips and lifts off the hinge. You don't need to drain refrigerant for C4 — the thermistor is on the air side of the coil.

2. **Locate the coil thermistor.** It's a small bead (about 4 mm diameter) inside a heat-shrink sleeve, clipped between two return bends of the evaporator coil. The lead exits the coil and runs in a harness up to the PCB on the right side of the head. The R2T (coil) thermistor is usually the second from the right in the connector — verify with the wiring diagram glued inside the front cover.

3. **Unplug the thermistor at the PCB and measure resistance.** With the room at 75-80 °F, a healthy 10 kΩ NTC thermistor should read approximately 10 kΩ — anywhere from 8 to 12 kΩ is within tolerance. Daikin's spec table:
   - 32 °F (0 °C): ~33 kΩ
   - 50 °F (10 °C): ~20 kΩ
   - 77 °F (25 °C): ~10 kΩ
   - 95 °F (35 °C): ~6.5 kΩ
   - 122 °F (50 °C): ~3.5 kΩ

   If you read OL (open) or near 0 (shorted), or significantly outside the curve at known temperature, the thermistor is bad.

4. **If the thermistor reads normal at room temp, flex the harness and recheck.** Intermittent C4s often trace to a chafed harness inside the head. Wiggle the harness at the PCB connector and at the strain reliefs along its run while watching the meter. Any flicker or jump confirms a damaged conductor.

5. **Replace the thermistor with the OEM part for your model.** Daikin coil thermistor kits commonly carry part numbers in the 168000J series (the "J" suffix indicates lead length and connector style — get the one for your platform). Use the OEM part — third-party thermistors with the wrong NTC curve will trigger C4 just like an open sensor.

6. **Re-clip the thermistor to the coil in the original location.** This matters more than it sounds. The PCB uses coil temperature for defrost timing and freeze protection; if you clip the new thermistor onto a different return bend (or worse, just dangle it in the air), the system will run but make bad defrost decisions. Mark the original location with a pencil before pulling the old one.

7. **Re-seat the PCB connector with a positive click and reassemble.** Make sure the harness routes back through its original strain reliefs and doesn't lay against the blower wheel housing. Pinch test the harness as you replace the front panel — Daikin's clip-on front panels can pinch a misrouted harness against a chassis edge.

8. **Restore power and clear the fault.** On a wall-mount with handheld remote, C4 clears on the next power-up if the thermistor input is back in range. On systems with a wall thermostat (BRC1E), navigate to the maintenance menu and clear the fault history. Run a cooling call for 10 minutes and verify the coil thermistor reading on the maintenance display tracks the actual coil temperature within a couple of degrees.

> **Field knowledge nugget:** On Daikin FTXS and FTKR series wall-mount heads built between roughly 2017 and 2022, I've found a specific C4 pattern related to condensate wicking up the thermistor lead. The trap is that the thermistor element itself still ohms out OK at room temp, but the lead insulation has degraded and during a cooling cycle moisture wicks into the heat-shrink boot, momentarily shorting the lead and triggering C4. The diagnostic tell: C4 only appears during cooling operation, never in dry-run or heating, and the room-temp resistance check passes clean. Fix is the same — replace the thermistor — but you'll save a callback if you also seal the new thermistor's heat-shrink boot with dielectric grease before clipping it to the coil. That nugget alone has saved me probably 15 repeat trips. The 168000J series replacement kits include a small dielectric grease packet for exactly this reason; use it.

**Safety:** Newer Daikin residential equipment is R-454B (A2L mildly flammable). C4 is an air-side repair and doesn't touch the refrigerant circuit, but be aware that if you find scorching, burnt insulation, or odd smells while inside the indoor head on an R-454B system, stop work, ventilate, and verify there's no refrigerant present (use an A2L-rated leak detector). Indoor coil leaks on A2L equipment leak into the conditioned space and can accumulate to LFL (~11.9% by volume) in a small bedroom. EPA 608 with A2L endorsement is the current requirement for any sealed-system work.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Indoor coil thermistor R2T | 168000J series (model specific) | $35–$75 | [HVAC Parts Shop](https://www.hvacpartsshop.com) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Thermistor harness extension | 4017019 family | $25–$45 | [HVAC Parts Shop](https://www.hvacpartsshop.com) |
| Indoor controller PCB | 4017019-xx | $245–$380 | [HVAC Parts Shop](https://www.hvacpartsshop.com) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Dielectric grease, 1 oz tube | Permatex 22058 | $4–$10 | [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=daikin-error-code-c4) / [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |
| Heat shrink tubing kit | 3M FP-301 assortment | $15–$25 | [Amazon](https://www.amazon.com/?tag=errorcodefixes-20) |

Always order the thermistor kit with the harness clip — Daikin sells the bare thermistor and the kit at similar price, and the kit gives you a fresh clip that won't break on reinstallation.

## When to call a professional

Call a NATE-certified mini-split tech if any of these apply:

- You replace the thermistor with verified-good OEM parts and C4 returns within hours. That points to a PCB input failure and a board swap.
- The harness shows obvious damage inside the head and there's no clear OEM repair part — you may need a full harness assembly which on some Daikin models is integrated with the PCB.
- The system is under the original 10-year parts warranty. Daikin parts warranty covers thermistors and PCBs but requires authorized servicer documentation.
- You see oil staining anywhere on the indoor coil or condensate that smells acrid (a refrigerant-tinged condensate is a slow indoor coil leak — on R-454B systems this is a serious concern).
- The thermistor connector itself looks damaged or melted, indicating an electrical fault upstream that may have damaged the board too.

## FAQs

**Will Daikin C4 clear on its own?**
On a transient cause (a momentarily flexed harness, a loose connector), C4 can clear after a power cycle and stay clear. On a real thermistor failure, C4 returns on every power-up. Don't keep clearing the fault and walking away — sustained out-of-range thermistor readings mess with defrost timing and can cause indoor coil icing.

**Can I use a generic 10 kΩ NTC thermistor as a Daikin replacement?**
Electrically you can, but Daikin uses a specific NTC curve (Beta value around 3950 on most platforms) and the PCB lookup tables expect that exact curve. A 10 kΩ thermistor with a different Beta will read room-temp resistance fine but be off by several degrees at coil temperatures — leading to bad defrost timing and possible nuisance faults. Use the OEM part.

**Where exactly is the C4 thermistor on a wall-mount Daikin?**
On FTX/FTXS/FTKR wall mounts, it's clipped between the second and third return bends from the right end of the evaporator slab, viewed from the front with the front panel off. Lead routes up through a strain relief, into the PCB cavity on the right side, plugs into the indoor PCB at CN21 or equivalent.

**Will C4 stop the system or just throw a warning?**
On most Daikin platforms, C4 disables compressor operation until the fault is cleared. The fan may still run for circulation, but no cooling or heating. This is intentional — without a valid coil temperature signal, the firmware can't safely manage defrost or freeze protection.

**My Daikin only throws C4 in heating mode — is that different?**
Same code, different stress condition. In heating, the indoor coil runs warm (condenser duty) and the thermistor sees higher temperatures and lower resistance. If the thermistor lead has a partial short that only manifests at the lower-resistance end of the curve, you'll see C4 in heating only. Still a thermistor replacement.

## Related guides

- [Daikin U4 Error Code — Indoor-Outdoor Communication Fix](/posts/daikin-error-code-u4)
- [Daikin A6 Error Code — Indoor Fan Motor Fix](/posts/daikin-error-code-a6)
- [Daikin UA Error Code — Mismatched Indoor/Outdoor Unit Fix](/posts/daikin-error-code-uA)
