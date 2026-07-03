---
title: "Daikin H6 Error Code - Causes & Fix"
description: "H6 means compressor position sensor fault. Most likely fix: inspect and repair loose or corroded compressor wiring to the outdoor PCB."
pubDatetime: 2026-06-30T09:53:37Z
modDatetime: 2026-06-30T09:53:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - daikin
money_part: "Daikin outdoor unit PCB (control board)"
most_likely_cause: "Loose, corroded, or broken wiring between the compressor and outdoor PCB"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Turn off the system at the breaker for 10 minutes, then power back on to reset any phantom errors."
  - "Check for loose or visibly corroded wire terminals at the outdoor unit compressor and PCB connections."
---

## Daikin H6 Error Code — What It Means

The Daikin H6 error code signals a malfunction of the position detection sensor in the outdoor unit compressor. This sensor monitors the rotational position of the compressor motor for the inverter drive. When it fails or loses signal, the system halts operation to prevent damage. The fault can stem from faulty contact in the compressor cable, a defective compressor, or a problem with the outdoor unit PCB control board.

Daikin defines H6 as an operation halt due to a faulty position detection sensor. Do not confuse this with blower motor issues (a common misunderstanding in online forums). H6 is strictly a compressor position sensor fault, not related to refrigerant pressure or air-side components.

## Before You Replace Anything

Some homeowners wrongly suspect the indoor blower motor or air filter. H6 is a compressor position sensor fault, not an airflow issue. Power-cycle the system first to rule out a phantom glitch before replacing expensive parts.

[Jump to Fix](#fix)

## Common Causes

- **Faulty compressor cable contact (~40%)** Loose, corroded, or broken wiring between the compressor and outdoor PCB interrupts the position detection signal.
- **Defective outdoor unit PCB (~30%)** The control board's position detection circuit fails to supply proper voltage or read sensor output.
- **Defective compressor (~20%)** Internal failure of the compressor's position sensor or motor prevents signal generation.
- **Transmission error between units (~7%)** Communication fault between indoor and outdoor units causes the H6 code to appear alongside other errors.
- **One-time phantom glitch (~3%)** Transient electrical spike or phantom power issue triggers the code once but clears after power cycling.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the system run normally after turning it off at the breaker for 10 minutes and restarting?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was likely a one-time phantom error. Monitor for recurring codes and note when they appear.<br><strong>No:</strong> The fault is persistent. Proceed to inspect compressor wiring and outdoor PCB connections.</div>
</details>

<details class="dtree"><summary>Are the compressor cable terminals at the outdoor unit tight and free of corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring is probably fine. Test the outdoor PCB voltage at the position sensor pins or suspect the compressor itself.<br><strong>No:</strong> Clean or repair the corroded or loose wiring connections first. This often resolves the H6 code.</div>
</details>

<details class="dtree"><summary>Does the outdoor unit display other error codes or fail to communicate with the indoor unit?</summary>
<div class="dtree-body"><strong>Yes:</strong> Check the transmission cable between indoor and outdoor units for damage or loose connections.<br><strong>No:</strong> Focus on the compressor position sensor circuit: PCB, compressor internal sensor, or wiring between them.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power cycle the system** by turning off the breaker or disconnecting power for 10 minutes, then restart. This clears many phantom H6 errors.
2. **Inspect compressor wiring** at the outdoor unit. Look for loose terminals, broken wires, or green corrosion on connectors between the compressor and the PCB.
3. **Measure sensor voltage** at the outdoor PCB position detection pins (typically 0.5 to 4.5V DC, but consult your model's service manual for exact specs).
4. **Test compressor windings** with a multimeter. Measure resistance (typically 1 to 10Ω, model-dependent). Open or out-of-range readings indicate internal compressor failure.
5. **Replace the outdoor unit PCB** if sensor voltage is absent or erratic and wiring is intact. The position detection circuit on the board has failed.
6. **Replace the compressor** if wiring and PCB tests are normal but the sensor signal is missing. The internal position sensor or motor is defective.
7. **Check transmission cables** between indoor and outdoor units if the system also reports communication errors. Replace damaged or loose cables.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Daikin outdoor unit PCB (control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h6-error-code&k=Daikin+outdoor+unit+PCB+%28control+board%29&tag=errorcodefixes-20) \| Match your model number exactly. Order from Daikin dealer or authorized parts supplier. |
| Daikin compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h6-error-code&k=Daikin+compressor&tag=errorcodefixes-20) \| Requires refrigerant recovery and recharge. Professional installation mandatory. |
| Compressor wire harness or connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-daikin-mini-split-h6-error-code&k=Compressor+wire+harness+or+connectors&tag=errorcodefixes-20) \| Replace if terminals are broken or corroded beyond cleaning. |

## When to Call a Pro

Call a licensed HVAC technician immediately for H6 errors. This code involves the sealed refrigerant system, high-voltage outdoor unit work, and specialized diagnostics. Testing the position sensor circuit requires a multimeter and knowledge of your model's service manual voltage specs. Compressor replacement demands refrigerant recovery, brazing, evacuation, and recharge under EPA regulations. Even wiring repairs at the outdoor PCB can expose you to 240V power and refrigerant lines. Do not attempt this repair unless you hold an EPA 608 certification and have HVAC training.

**Rough cost:** A pro service call runs about $200-600 for wiring repair or PCB replacement, $800-1,800 for compressor replacement.

## See Also

- [Daikin UH Error Code - Causes & Fix](/posts/daikin-heat-pump-uh-error-code/)
- [Daikin VRV / VRF U4 Error Code — Communication Fault Fix](/posts/daikin-vrv-vrf-u4-error-code/)
- [Daikin F3 Error Code - Causes & Fix](/posts/daikin-mini-split-f3-error-code/)
- [Daikin Mini Split Not Responding to Remote - Causes & Fix](/posts/daikin-mini-split-not-responding-to-remote/)
