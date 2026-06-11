---
title: "Cooper & Hunter Mini Split P4 Error - Causes & Fix"
description: "P4 means inverter compressor drive fault. Most often caused by wiring problems, failed IPM module, or compressor failure. Reset first."
pubDatetime: 2026-05-31T14:49:26Z
modDatetime: 2026-05-31T14:49:26Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - cooper-and-hunter
money_part: "IPM inverter power module"
---

## Cooper & Hunter Mini Split P4 Error — What It Means

The P4 error code on a Cooper & Hunter mini split indicates an inverter compressor drive fault. The system has detected an abnormal condition in the compressor drive circuit, typically involving the IPM or IGBT inverter module, compressor drive feedback, or related outdoor unit circuitry. This is an outdoor unit protection issue, not a simple sensor fault.

The code is reported as an abnormal inverter compressor drive detected by a special detection circuit. In real-world service, this usually points to problems with the inverter power module, wiring between the main board and compressor, the compressor itself, or issues with heat rejection that push the drive into protection mode.

[Jump to Fix](#fix)

## Common Causes

- **Wiring mistakes or loose connections** Loose plugs, miswiring, or burnt terminals between the main PCB, IPM, and compressor are common field causes of P4 faults.
- **Failed IPM or inverter module** The inverter power module or related driver circuitry can fail and trigger the compressor drive protection.
- **Compressor electrical failure** Compressor winding problems or internal electrical faults will prevent the drive from operating normally.
- **Outdoor fan or condenser blockage** Poor heat rejection from a failed outdoor fan or dirty condenser can overload the inverter drive and trigger protection.
- **Low or abnormal line voltage** Inadequate supply voltage at the outdoor unit can prevent proper compressor start and cause drive faults.
- **Main outdoor PCB failure** Bad feedback or communication between the control board and inverter section can report a drive fault.

## Step-by-Step Fix {#fix}

1. **Cycle power** by turning the unit off at the breaker or disconnect, wait two minutes, and restore power to see if the fault returns.
2. **Verify incoming supply voltage** at the outdoor unit terminals against the nameplate rating and confirm both legs are balanced, with no voltage drop at the breaker or disconnect.
3. **Inspect outdoor wiring** from the main PCB to the compressor and IPM for loose connectors, burnt terminals, damaged harnesses, or miswiring.
4. **Check the condenser and outdoor fan** to confirm the coil is clean and the fan motor runs properly, since poor heat rejection can overload the inverter drive.
5. **Ohm the compressor windings** by disconnecting power and measuring phase-to-phase resistance on all three terminals, looking for balanced readings with no short to ground.
6. **Test the IPM and inverter section** by checking resistance between P and U/V/W and between N and U/V/W, expecting megohm-order readings that are equal (consult your model's service manual for exact values).
7. **Replace the failed component** once testing isolates the problem: if compressor windings are abnormal, replace the compressor, or if drive board checks fail but the compressor is good, replace the outdoor main PCB or IPM assembly as applicable.

## Parts Often Needed

| Part | Notes |
|------|-------|
| IPM inverter power module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p4-error-code&k=IPM+inverter+power+module&tag=errorcodefixes-20) \| Replace if resistance tests show unequal or low readings and compressor is good. |
| Outdoor main PCB or inverter PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p4-error-code&k=Outdoor+main+PCB+or+inverter+PCB&tag=errorcodefixes-20) \| May be combined with the IPM on some models, check your unit's layout. |
| Compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p4-error-code&k=Compressor&tag=errorcodefixes-20) \| Replace if windings are open, shorted, or unbalanced. |
| Outdoor fan motor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-cooper-and-hunter-mini-split-p4-error-code&k=Outdoor+fan+motor&tag=errorcodefixes-20) \| Replace if fan failure contributed to overheating and drive protection. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working with high voltage, if you do not own a multimeter and the tools to safely open the outdoor unit, or if initial power cycling and visual inspection do not resolve the fault. Inverter drive and compressor diagnostics require specific resistance and voltage checks that are difficult without training. If you have already verified incoming power and wiring and the fault persists, a technician with inverter mini split experience and access to Cooper & Hunter service documentation will be able to isolate whether the IPM, main board, or compressor has failed and perform the replacement safely.
