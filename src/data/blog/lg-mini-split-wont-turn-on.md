---
title: "LG Mini Split Won't Turn On - Causes & Fix"
description: "Usually a tripped breaker or loose terminal connection cutting supply power. Verify the breaker, check voltage at both units, and inspect all wiring before checking sensors or boards."
pubDatetime: 2026-06-01T19:08:15Z
modDatetime: 2026-06-01T19:08:15Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - lg
  - symptom
---

## LG Mini Split Won't Turn On — What's Happening

When an LG mini split won't turn on, you may see no display, no LEDs, or an error code like CH12 (indoor thermistor fault) or a blinking LED. LG documentation explains that a completely dead unit is most often a power or wiring issue, while a unit that powers up but won't start cooling or heating can be caused by sensor faults, communication line failures, or inverter protection lockouts. If the display is on but the compressor never runs, the outdoor unit may be in a protection mode or have an inverter board fault.

LG service guidance recommends starting with a full power cycle (turn off the breaker for about 5 minutes) to clear temporary faults caused by electrical disturbances or unstable supply voltage. If the unit remains off or displays CH12 after the reset, the indoor return-air thermistor or indoor pipe thermistor circuit has either disconnected or shorted out, and the unit will not operate until the sensor is repaired or replaced.

[Jump to Fix](#fix)

## Most Likely Causes

- **No supply power or tripped breaker** A tripped circuit breaker, blown fuse, or loose connection at the disconnect or terminal block is the most common reason an LG mini split is completely dead with no display or LEDs.
- **Unstable or interrupted line voltage** Voltage sags, surges, or momentary interruptions from the utility or a loose neutral can put the unit into a fault state that requires a full power cycle to clear.
- **Failed indoor thermistor or sensor circuit (CH12)** The indoor return-air thermistor or indoor pipe thermistor has opened, shorted, or disconnected, causing CH12 and preventing the unit from starting.
- **Communication line failure between indoor and outdoor units** A broken, loose, or miswired communication cable between the indoor and outdoor units will prevent startup even if both units have power.
- **Outdoor inverter PCB or compressor protection lockout** The outdoor inverter board may have detected a compressor fault, insulation breakdown, or internal short and locked out operation to protect the system.
- **Dirty indoor filter or blocked airflow** Restricted airflow from a clogged filter can trigger protective shutdowns or prevent the unit from completing its startup sequence.
- **Defective control PCB or inverter board** A failed indoor control board or outdoor inverter PCB with damaged solder joints, burnt traces, or carbonized connectors will prevent power-up or compressor operation.

## How to Diagnose and Fix {#fix}

1. Verify the complaint by checking whether the indoor display is blank, whether any LEDs are lit or blinking, and whether you hear any fan or compressor noise.
2. Check the circuit breaker and disconnect switch at both the indoor and outdoor units, then measure supply voltage at the indoor and outdoor terminal blocks to confirm power is present.
3. Turn off the breaker, wait 5 minutes, then restore power to clear any temporary faults caused by electrical disturbances or voltage instability.
4. If the display shows CH12 or the unit still won't start, inspect the indoor thermistor connector and wiring harness for loose plugs, damaged wires, or corrosion, then test the sensor resistance if accessible.
5. Check the communication wiring between the indoor and outdoor units for loose terminals, breaks, or incorrect connections if the indoor unit powers on but the outdoor unit never responds.
6. If the outdoor unit has power but won't run, check the inverter PCB for diagnostic LEDs and measure DC link voltage at the P and N terminals (should read about 310 VDC on single-phase units).
7. Test compressor terminal resistance balance and insulation resistance to ground (should be above 10 MΩ between any phase and the outdoor piping) if the inverter board attempts to start and trips.
8. Inspect both the indoor control PCB and outdoor inverter PCB for burn marks, swollen capacitors, or damaged connectors, and replace the defective board if power and sensor checks are all normal.

## Parts You Might Need

| Part | Notes |
|------|-------|
| Indoor return-air thermistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-wont-turn-on&k=Indoor+return-air+thermistor&tag=errorcodefixes-20) \| Replacement sensor for CH12 faults, match your model number |
| Outdoor inverter PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-wont-turn-on&k=Outdoor+inverter+PCB&tag=errorcodefixes-20) \| Required if DC link voltage is absent or compressor won't start despite good insulation |
| Indoor control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-wont-turn-on&k=Indoor+control+board&tag=errorcodefixes-20) \| Replace if the display is dead with good supply voltage and no visible damage to wiring |

## Related Error Codes

If your appliance also shows a code on the display, these match this problem:

- [Lg Mini Split Ch 05 error code](/posts/lg-mini-split-ch-05-error-code/)
- [Lg Mini Split Ch 26 error code](/posts/lg-mini-split-ch-26-error-code/)
- [Lg Mini Split Ch 38 error code](/posts/lg-mini-split-ch-38-error-code/)
- [Lg Mini Split Ch01 error code](/posts/lg-mini-split-ch01-error-code/)
- [Lg Mini Split Ch02 error code](/posts/lg-mini-split-ch02-error-code/)
- [Lg Mini Split Ch03 error code](/posts/lg-mini-split-ch03-error-code/)
- [Lg Mini Split Ch04 error code](/posts/lg-mini-split-ch04-error-code/)
- [Lg Mini Split Ch05 error code](/posts/lg-mini-split-ch05-error-code/)
- [Lg Mini Split Ch06 error code](/posts/lg-mini-split-ch06-error-code/)
- [Lg Mini Split Ch07 error code](/posts/lg-mini-split-ch07-error-code/)
- [Lg Mini Split Ch09 error code](/posts/lg-mini-split-ch09-error-code/)
- [Lg Mini Split Ch10 error code](/posts/lg-mini-split-ch10-error-code/)

## When to Call a Pro

Call a qualified HVAC technician if you are not comfortable working with line voltage, if you do not have a multimeter to measure supply and DC link voltages, or if the unit shows good power and communication but still will not start. Inverter board diagnostics, compressor insulation testing, and refrigerant-side work all require specialized tools and EPA certification. If CH12 persists after you have reseated the thermistor connector, a tech will need to measure sensor resistance and trace the circuit to the control board. Any work on the inverter PCB or compressor terminals should be performed by a licensed professional to avoid shock and equipment damage.
