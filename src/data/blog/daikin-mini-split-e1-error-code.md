---
title: "Daikin E1 Error Code - Causes & Fix"
description: "E1 on Daikin mini-splits means outdoor circuit board fault. Most common fix: replace the outdoor PCB or shorted EEV coil."
pubDatetime: 2026-06-30T09:49:52Z
modDatetime: 2026-06-30T09:49:52Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor control board (PCB)"
most_likely_cause: "Failed outdoor PCB"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify 240V power is present at the outdoor unit terminals (line, neutral, earth) using a multimeter"
  - "Inspect wiring between indoor and outdoor units for visible damage or loose connections"
part_price: "$150-400"
---

## Daikin E1 Error Code — What It Means

The E1 error code on Daikin mini-split systems indicates a circuit board fault in the outdoor unit. The system has detected an internal electronic malfunction within the outdoor PCB, such as a failure in the power supply section, driver logic, or a shorted component. The unit shuts down automatically to prevent damage to the compressor and other components. This is not a high-pressure fault or communication error, which E1 may represent on other brands. For Daikin, E1 specifically points to a problem with the outdoor unit's printed circuit board or a component connected to it, most often the electronic expansion valve coil.

## Before You Replace Anything

Many technicians replace the outdoor PCB immediately without first testing the electronic expansion valve (EEV) coil. A shorted EEV coil can damage the board, so always measure the coil resistance (should be around 47 Ω on each leg from common) before replacing the PCB.

[Jump to Fix](#fix)

## Common Causes

- **Failed outdoor PCB (~50%)** The outdoor circuit board develops internal faults such as blown capacitors, damaged MOSFETs, or failed voltage regulators that prevent normal operation.
- **Shorted EEV coil (S20) (~30%)** The electronic expansion valve coil overheats or shorts, drawing excessive current and damaging the outdoor PCB.
- **Power supply issues (~10%)** Incorrect voltage or missing phases at the outdoor unit input terminals cause the board to malfunction or shut down.
- **Shorted wiring (~10%)** Damaged or pinched wiring between the outdoor unit and connected components (like the EEV) creates a short circuit that triggers the board fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the outdoor fan run when you power on the system?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power is reaching the outdoor unit. The fault is likely in the PCB itself or the EEV coil. Proceed to test the EEV coil resistance.<br><strong>No:</strong> Check for 240V at the outdoor unit terminals. If voltage is missing, inspect the breaker, disconnect, and wiring from the indoor unit.</div>
</details>

<details class="dtree"><summary>Do you have a multimeter and feel comfortable measuring resistance?</summary>
<div class="dtree-body"><strong>Yes:</strong> Disconnect the EEV coil 5-pin connector and measure resistance from red (common) to each other wire. Should read around 47 Ω. If zero or infinite, replace the coil first.<br><strong>No:</strong> Call a qualified HVAC technician. This fault requires electrical diagnostics and refrigerant handling if components are replaced.</div>
</details>

<details class="dtree"><summary>Did the error appear after a power surge or lightning storm?</summary>
<div class="dtree-body"><strong>Yes:</strong> The outdoor PCB was likely damaged by the surge. You will need a new outdoor control board and possibly an EEV coil if it was also affected.<br><strong>No:</strong> The fault is likely age-related component failure on the PCB or a gradual EEV coil degradation. Test the EEV coil first before replacing the board.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the system** at the breaker and the disconnect switch at the outdoor unit.
2. **Verify input voltage** at the outdoor unit terminals using a multimeter. Confirm approximately 240V is present between line and neutral. If voltage is missing, trace back to the breaker and indoor unit.
3. **Remove the outdoor unit cover** and locate the electronic expansion valve (EEV) and its 5-pin connector (often labeled S20).
4. **Disconnect the EEV coil connector** and measure resistance from the red wire (common) to each of the other four wires (blue, orange, yellow, white). Each should read around 47 Ω. Also measure between non-common wires (e.g., blue to orange), which should read around 94 Ω.
5. **If the EEV coil is shorted** (0 Ω) or open (infinite resistance), replace the EEV coil and retest the system. If the coil reads correctly, the outdoor PCB is faulty and must be replaced.
6. **Replace the outdoor PCB** by removing mounting screws, disconnecting all wire harnesses (photograph connections first), and installing the new board. Apply heat sink paste to mounting surfaces if not pre-applied.
7. **Reconnect all wiring**, replace the cover, restore power, and run the system. Monitor for 15-20 minutes to confirm the E1 code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-e1-error-code&k=Daikin+outdoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Match your model number exactly. Some boards require separate heat sink paste. |
| Electronic expansion valve (EEV) coil | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-e1-error-code&k=Electronic+expansion+valve+%28EEV%29+coil&tag=errorcodefixes-20) \| Often labeled S20. Replace if resistance is outside 47 Ω spec before replacing the PCB. |

## When to Call a Pro

Call a licensed HVAC technician for this repair. Diagnosing an E1 error requires electrical testing with a multimeter, working inside the outdoor unit with high-voltage components, and verifying refrigerant system integrity after replacing parts. If the EEV coil or PCB is replaced, the technician may need to evacuate and recharge the refrigerant circuit or verify the system is still sealed. Misdiagnosis can lead to expensive part replacements that do not fix the fault, and improper handling of refrigerant violates EPA regulations. A qualified tech will test the EEV coil resistance first (around 47 Ω per leg), confirm input voltage, and replace only the failed component, saving you time and money.

**Rough cost:** A pro service call runs about $250-600.

## See Also

- [Daikin H0 Error Code - Causes & Fix](/posts/daikin-heat-pump-h0-error-code/)
- [Daikin A6 Error Code - Causes & Fix](/posts/daikin-heat-pump-a6-error-code/)
- [Daikin A3 Error Code - Causes & Fix](/posts/daikin-mini-split-a3-error-code/)
- [Daikin Mini Split Won't Turn On - Causes & Fix](/posts/daikin-mini-split-wont-turn-on/)
