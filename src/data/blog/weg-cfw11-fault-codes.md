---
title: "WEG CFW11 VFD Fault Codes — What They Mean and How to Fix Them - What It Means and How to Fix It"
description: "WEG CFW11 drives use F-codes for trips and A-codes for warnings across power, current, temperature, feedback, and communication problems. This guide shows how to work through the full F001 to F090 and A001 to A090 ranges without guessing at the drive or the motor."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The WEG CFW11 is everywhere for a reason. It is a capable mid-tier AC drive that shows up on pumps, supply fans, exhaust fans, conveyors, cooling towers, and OEM skids that need vector control without the cost of a top-end platform. When it trips, the keypad usually gives you a direct code, and if you read that code correctly, the drive saves you a lot of time.

On the CFW11, **F-codes** are faults. They trip the drive and stop the motor. **A-codes** are alarms. They warn you that something is outside the preferred operating window, but the drive may keep running depending on how the application is configured. The hardest part is not reading the code. The hardest part is knowing whether the code points to the power source, the drive, the motor, the programming, or the network. That is what this guide is for.

## What Does WEG CFW11 VFD Fault Codes Mean?

The CFW11 fault and alarm list spans a wide range, but the code families are consistent enough that you can work fast even when firmware changes the exact wording.

**F001 through F010** usually cover core protection events tied to the power section, DC bus, output current, and basic hardware supervision. In the field, this is where you see the big repeat offenders: undervoltage, overvoltage, overcurrent, ground fault, and thermal trips.

**F011 through F030** usually cover motor overload logic, parameter mismatch, IGBT protection, encoder or feedback trouble, and other hardware-supervision events that affect drive performance more than line power.

**F031 through F060** often involve closed-loop control, memory, setup, and communication-related faults. If the drive is part of a PLC or BAS workflow, a code in this band often points you toward configuration or data flow.

**F061 through F090** usually involve accessory cards, special application functions, or board-level faults that do not show up on every CFW11 installation. Not every frame size or option stack will use every number.

The alarm side works the same way.

**A001 through A020** usually warn about command-source mismatch, reference-source issues, limit conditions, or values drifting toward a trip level.

**A021 through A050** usually cover thermal warnings, overload warnings, and protective thresholds that have not yet crossed into a full fault.

**A051 through A090** usually involve communication, option cards, encoder status, fieldbus supervision, and accessory-related warnings.

The codes technicians see most often are the same ones that eat the most downtime.

**F002, undervoltage.** The DC bus dropped too low. Start with incoming power, fuse health, loose lugs, single phasing, and feeder sag under load.

**F003, overvoltage.** The DC bus rose too high, often during deceleration on high-inertia loads. This is common on fans, flywheels, and applications with aggressive stop ramps and no braking resistor.

**F004, overcurrent.** The drive saw output current above safe threshold. Think shorted motor leads, mechanical jam, incorrect motor data, or acceleration set too aggressively.

**F005, ground fault.** Output current is leaking to ground. Motor insulation failure and damaged output cable are high on the list.

**F007, heatsink overtemperature.** The drive got too hot because the internal fan failed, the heatsink is dirty, ambient temperature is too high, or the drive is undersized for the load.

**F014, motor overload or electronic thermal model trip.** The drive believes the motor has exceeded safe thermal capacity. This often comes back to wrong motor-current programming or a load that is actually overloaded.

**F033, encoder feedback loss.** On vector applications, the drive lost clean encoder data. Check cable shielding, power supply to the encoder, routing near motor leads, and the encoder itself.

**F048 through F055, fieldbus or communication-family faults.** The exact number depends on option card and protocol, but this band often points to Modbus, CANopen, Profibus, EtherNet/IP, or communication-board supervision.

**A001 through A010, setup and command warnings.** These alarms tell you the drive does not like the command source, reference source, enable chain, or another setup element.

**A050 through A090, thermal and communication warnings.** These are the warnings you capture before they become real downtime. A drive that shows A-codes in this range is usually telling you the trip is coming.

The important pattern is this: if the code points to power, test the line. If it points to current, test the motor and mechanical load. If it points to temperature, test cooling and loading. If it points to communication, test the network before swapping the drive.

## How to Fix It

1. **Start with the code family, not just the exact number.** If you see F002, F003, or F004, you are in the power-and-current family. If you see F033 or A070-style communication and feedback warnings, move your attention to encoder, fieldbus, and controls wiring.

2. **Record the fault and the operating moment.** Did the drive trip on start, during steady run, or during stop? F003 during stop usually means regeneration. F004 the instant you hit RUN usually means a short, bad motor data, or a mechanical jam.

3. **Measure three-phase input power under load.** CFW11 drives can look fine at idle and still collapse under demand. Check line-to-line voltage on all phases while the drive tries to run. If one phase sags or disappears, F002 or current-related faults follow quickly.

4. **Inspect motor leads and meg the motor if your site procedure allows it.** F004 and F005 often come from damaged cable insulation, water in conduit, or a motor winding starting to fail. If insulation to ground is weak, stop there and deal with the motor side first.

5. **Check the mechanical load before you blame the drive.** Disconnect the motor from the load if the machine allows it, then spin the driven equipment by hand. A seized pump, sticky damper linkage, failed bearing, or loaded conveyor can create overcurrent and overload codes that look electrical at first glance.

6. **Review motor nameplate parameters.** Compare programmed voltage, current, frequency, RPM, and control mode against the actual motor nameplate. A CFW11 with the wrong motor current or base frequency can trip F004 or F014 even when the hardware is healthy.

7. **Fix cooling issues for F007 and related alarms.** Verify internal fans are running, blow out the heatsink, inspect panel filters, and measure cabinet temperature. If the drive is mounted in a hot enclosure beside other heat sources, the environment may be the real problem.

8. **Slow the ramps for F003 and F004.** Increase acceleration time if current spikes on start. Increase deceleration time if overvoltage hits during stop. If the application truly needs fast stops, install a properly sized braking resistor instead of forcing the drive to absorb energy it cannot dump.

9. **Treat encoder and communication faults as wiring jobs first.** For F033 and many A051 to A090 alarms, inspect shield grounding, route separation from motor leads, node address settings, termination resistors, and the health of option-card LEDs. Noise and addressing errors are more common than bad main boards.

10. **After repair, clear the fault log and retest the full duty cycle.** Start, run, stop, and restart the equipment. A drive that only faults on decel or only under heavy load tells you far more than one that was tested at no load for thirty seconds.

11. **Use the range logic for codes you do not know by memory.** F001 to F090 and A001 to A090 cover a lot of ground, but the bands stay predictable. Power and current faults live low in the range. Feedback, communication, and accessory faults tend to live higher. That alone can cut your troubleshooting time in half.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [WEG CFW11 cooling fan](https://www.amazon.com/s?ascsubtag=ecf-weg-cfw11-fault-codes&k=WEG+CFW11+cooling+fan&tag=errorcodefixes-20) | Replaces failed internal fan assemblies that cause F007 and repeated temperature alarms | $25 to $65 |
| [WEG CFW11 keypad HMI](https://www.amazon.com/s?ascsubtag=ecf-weg-cfw11-fault-codes&k=WEG+CFW11+keypad+HMI&tag=errorcodefixes-20) | Replaces damaged or intermittent operator interfaces and helps with local diagnostics | $70 to $180 |
| [Dynamic braking resistor for VFD](https://www.amazon.com/s?ascsubtag=ecf-weg-cfw11-fault-codes&k=dynamic+braking+resistor+vfd&tag=errorcodefixes-20) | Solves F003 overvoltage trips on high-inertia deceleration applications | $80 to $250 |
| [3-phase line reactor for VFD](https://www.amazon.com/s?ascsubtag=ecf-weg-cfw11-fault-codes&k=3+phase+line+reactor+vfd&tag=errorcodefixes-20) | Helps stabilize incoming power and reduce nuisance undervoltage or line-disturbance faults | $90 to $220 |
| [VFD output reactor 3-phase](https://www.amazon.com/s?ascsubtag=ecf-weg-cfw11-fault-codes&k=vfd+output+reactor+3+phase&tag=errorcodefixes-20) | Protects motors on long lead runs and reduces reflected-wave stress behind F004 and F005 complaints | $110 to $280 |
| [Incremental encoder 1024 PPR industrial](https://www.amazon.com/s?ascsubtag=ecf-weg-cfw11-fault-codes&k=incremental+encoder+1024+ppr+industrial&tag=errorcodefixes-20) | Replaces failed feedback devices behind F033 and higher-range encoder faults | $65 to $180 |
| [Shielded RS485 cable](https://www.amazon.com/s?ascsubtag=ecf-weg-cfw11-fault-codes&k=shielded+rs485+cable&tag=errorcodefixes-20) | Fixes intermittent Modbus and network alarms in the A050 to A090 communication range | $15 to $45 |

## When to Call a Pro

Call an industrial electrician or VFD technician if the CFW11 trips on overcurrent or ground fault the instant you press RUN, especially after you disconnect the motor and confirm the mechanical load is free. That pattern can point to a failed power module inside the drive.

You should also bring in help for persistent encoder faults on closed-loop systems, fieldbus issues owned by a PLC or BAS contractor, or any application where the drive serves a critical fan or pump and downtime has building or process consequences. Once you suspect the IGBT stage, control board, or accessory communication card, random resets do more harm than good.

## Frequently Asked Questions

**Q: What is the difference between an F-code and an A-code on a WEG CFW11?**  
An F-code is a trip that stops the drive. An A-code is a warning that tells you a problem is developing but may not have stopped the motor yet.

**Q: Do all CFW11 drives use every code from F001 to F090 and A001 to A090?**  
No. Firmware revision, frame size, and option cards change what you actually see. The families stay consistent, though, so the code ranges still help you narrow the problem fast.

**Q: Why does my CFW11 trip on overvoltage only when the fan stops?**  
That usually means the load is regenerating energy back into the DC bus during deceleration. Increase decel time or add braking hardware.

**Q: Can bad motor parameters really cause fault trips?**  
Yes. Wrong current, voltage, frequency, or control mode settings can create false overload and overcurrent behavior even when the motor and drive hardware are healthy.

**Q: What should I check first on a communication alarm?**  
Check node address, baud rate, termination, shield routing, and option-card LEDs before you replace boards. Wiring and network setup faults are far more common than a dead drive.