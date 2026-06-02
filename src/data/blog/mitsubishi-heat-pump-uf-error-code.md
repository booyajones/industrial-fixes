---
title: "Mitsubishi UF Error Code - Causes & Fix"
description: "UF means compressor overcurrent interruption. The outdoor unit shut down due to excessive current. Most often fixed by replacing the PCB."
pubDatetime: 2026-05-31T08:55:32Z
modDatetime: 2026-05-31T08:55:32Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - mitsubishi
---

## Mitsubishi UF Error Code — What It Means

The UF error code on a Mitsubishi Electric heat pump indicates compressor overcurrent interruption. The outdoor unit has detected excessive electrical current in the compressor circuit and shut the compressor down to protect itself. This fault occurs when the compressor is effectively locked or drawing abnormal current during startup.

Mitsubishi groups this code with related faults like U6 (power module abnormal) and UP (compressor overcurrent after running), so field technicians sometimes see these codes together. In all cases, the inverter or compressor has experienced an electrical fault that triggered the protective shutdown.

[Jump to Fix](#fix)

## Common Causes

- **Failed outdoor inverter or power PCB** The power module or inverter board has failed and is either sending abnormal current or incorrectly reading normal current as a fault.
- **Compressor electrical failure or seized bearings** The compressor itself has failed mechanically (locked up) or electrically (shorted windings), causing it to draw excessive current when it tries to start.
- **Damaged wiring between PCB and compressor** Broken, disconnected, or heat-damaged wires in the harness from the power board to the compressor create opens or shorts that trigger the overcurrent fault.
- **Closed outdoor service valves** If the service valves on the refrigerant lines are shut, the compressor operates under abnormal pressure and draws excessive current.
- **Low supply voltage at the outdoor unit** Incoming power below the rated voltage (240 V or 415 V depending on model) causes the compressor to draw higher-than-normal current to do its work.
- **Rodent or insect damage to boards or wiring** Animals chewing through wires or nesting on circuit boards cause shorts and open circuits that lead to overcurrent faults.

## Step-by-Step Fix {#fix}

1. **Check the fault history** in the indoor controller service menu and note whether the UF code is repeating after you clear it.
2. **Measure supply voltage** at the outdoor unit terminal block and confirm it matches the unit's nameplate rating (typically 240 V or 415 V depending on model).
3. **Verify both outdoor service valves are fully open** by turning the stems counterclockwise until they stop, then confirm refrigerant flow is not restricted.
4. **Inspect the outdoor power PCB** for visible burn marks, failed capacitors, insect nests, or rodent damage, and look for any signs of moisture or corrosion.
5. **Check compressor wiring** from the power board terminals to the compressor connector for loose terminals, broken wires, heat damage, or chewed insulation.
6. **Test the compressor electrically** by disconnecting it from the PCB and checking for shorts to ground or between windings, and verify the PCB outputs are balanced if you have inverter test equipment.
7. **Replace the faulty component** (power PCB if the board shows damage or failed output, compressor if it is seized or electrically failed, or wiring harness if damaged), then clear the fault history and run the system to confirm the code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor power PCB / inverter board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-uf-error-code&k=Outdoor+power+PCB+%2F+inverter+board&tag=errorcodefixes-20) \| Match the part number on your existing board label. This is the most common repair for UF codes. |
| Compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-uf-error-code&k=Compressor&tag=errorcodefixes-20) \| Order by outdoor unit model number. Required only if the compressor is mechanically seized or electrically failed after confirming the PCB is good. |
| Compressor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-heat-pump-uf-error-code&k=Compressor+wiring+harness&tag=errorcodefixes-20) \| Replacement harness from power board to compressor if wires are damaged or chewed through. |

## When to Call a Pro

Call a licensed HVAC technician for any UF code. Diagnosing this fault requires a multimeter, knowledge of inverter-driven compressor systems, and the ability to safely work with high-voltage outdoor power boards. Misdiagnosing the fault and replacing the wrong part (PCB when the compressor is bad, or compressor when the board is bad) is expensive. A qualified technician has the inverter test equipment to isolate whether the fault is in the power module or the compressor, can safely discharge capacitors, and can handle refrigerant recovery if compressor replacement is needed. Do not attempt this repair yourself.
