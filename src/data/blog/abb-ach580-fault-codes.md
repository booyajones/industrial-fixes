---
title: "ABB ACH580 HVAC VFD Fault Codes — Full Diagnostic Guide - What It Means and How to Fix It"
description: "ABB ACH580 drives use numeric fault families to flag power, motor, temperature, fieldbus, and configuration problems in HVAC applications. This guide explains the key 2001 to 7999 fault ranges, the common trips technicians actually see, and the reset procedure that makes sense after a real diagnosis."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The ABB ACH580 is the HVAC-specific branch of ABB's all-compatible drive family. It is built for air handlers, cooling towers, condenser-water pumps, chilled-water loops, exhaust systems, and other building loads that live inside a hand-off-auto world. That makes its fault patterns different from what you see on a general industrial drive. On an ACH580, network timeouts, BAS handoff problems, long motor leads, and dirty mechanical-room cabinets are just as important as raw motor current.

If you are staring at an ACH580 fault, the number is doing two jobs at once. It is telling you what protection family tripped, and it is telling you where to begin. Codes in the 2000 range usually send you toward power and current. Codes in the 3000 range usually point toward heat, overload, and operating limits. Codes in the 5000 range often involve fieldbus or control interfaces. Codes in the 7000 range often point toward application logic, memory, or configuration mismatch.

## What Does ABB ACH580 HVAC VFD Fault Codes Mean?

The ACH580 uses numeric codes rather than simple letter prefixes, and the code ranges matter.

**2001 through 2999** usually cover current, voltage, ground fault, and hardware protection. This is where the most common electrical faults live.

**3000 through 3999** usually cover temperature, overload, stall, motor model, and other limit or protection events tied to how the drive and motor are operating together.

**5000 through 5999** usually cover communications, fieldbus supervision, option modules, and control-interface problems. On an ACH580 with BACnet or Modbus integration, this range deserves serious attention.

**7000 through 7999** usually cover internal software, parameter consistency, accessory mismatch, memory, and application-level issues. These are the codes you often see after board swaps, bad backups, or changes made by multiple contractors.

The most common ACH580 faults in real HVAC work are these.

**2001, overcurrent.** The drive saw output current beyond the safe threshold. That can mean a shorted motor lead, a jammed pump or fan, wrong motor data, or an acceleration time that is far too aggressive.

**2002 or DC bus overvoltage family faults.** These show up when a rotating load regenerates energy during stop. Large fans with short decel times do this all the time.

**2003 or undervoltage family faults.** The DC bus dropped too low. Think utility sag, loose incoming lugs, phase imbalance, or a weak feeder.

**2330 and ground-fault family trips.** The exact wording can vary by firmware, but this family points to leakage from output to ground. Motor insulation, wet cable, and damaged conduit entries are common causes.

**3001, drive overtemperature.** The ACH580 is running too hot. Mechanical rooms full of dust, clogged panel filters, failed internal fans, and hot rooftop enclosures are repeat offenders.

**3005 or motor thermal overload or stall family faults.** The drive believes the motor is overheating or not accelerating as expected. Wrong motor data, blocked airflow, shut valves, closed dampers, or high static can drive this code.

**5001, fieldbus communication lost.** The drive stopped hearing from BACnet MS/TP, BACnet/IP, Modbus RTU, or Modbus TCP supervision. This is where bad addressing, missing termination, and duplicate nodes show up.

**5004 and similar I/O or communication option faults.** The drive may be healthy, but the option card, network wiring, or BAS command mapping is not.

**7001, parameter mismatch.** This often appears after a board replacement or parameter restore from the wrong backup. The drive is basically telling you the configuration no longer matches the application.

**7003 and other internal memory or control-board faults.** These are the codes that make you back up parameters fast, because the control section may be starting to fail.

When you combine the code family with the moment of failure, the drive becomes a lot easier to troubleshoot. A 2001 at startup points you one direction. A 2002 during stop points you another. A 5001 only in AUTO mode points you away from the power section and straight toward BAS communication.

## How to Fix It

1. **Capture the active fault and the drive state before reset.** Record the code, motor current, output frequency, DC bus value if available, heatsink temperature, and whether the drive was in HAND, OFF, or AUTO. On ACH580 jobs, those details matter.

2. **Check whether the drive runs locally in HAND mode.** This is the fastest separator between a power problem and a controls problem. If the motor runs normally in HAND but faults in AUTO, look hard at BAS command source, speed reference, timeout settings, and fieldbus health.

3. **For 2001 overcurrent, inspect the motor circuit first.** Lock out power, inspect the output leads, check conduit entries, test insulation if site policy allows, and make sure the motor or driven load is not mechanically bound. Then verify motor nameplate data inside the drive.

4. **For 2002 overvoltage family faults, slow the stop.** Increase deceleration time, allow coast stop if the sequence permits it, and review whether a large fan or pump is regenerating energy into the DC bus. In HVAC, this often happens because someone wanted a fast stop that the drive was never designed to absorb.

5. **For 2003 undervoltage family faults, test the line under load.** Measure all three input phases while the drive is trying to start or accelerate. Look for loose lugs, weak fuses, failing disconnects, and building-wide voltage sag.

6. **For 3001 temperature faults, fix the environment before replacing the drive.** Confirm internal fans run, clean heatsink fins, replace dirty panel filters, and measure actual cabinet temperature. If the drive lives in a hot rooftop enclosure or packed mechanical room, the enclosure design may be the real problem.

7. **For 3005 overload or stall-type faults, inspect the HVAC process.** Closed dampers, stuck valves, blocked strainers, bearing drag, and fans running below safe self-cooling speed can all trip the motor model. This is not always an electrical repair.

8. **For 5001 and other network faults, diagnose the BAS path in order.** Check node address, baud rate, IP settings if used, termination, biasing, shield grounding, and option-card LEDs. Then verify the BAS can still see the drive object and is sending a sensible command.

9. **For 7001 and 7003 family faults, protect the parameters.** If the drive still communicates, back up the parameter set immediately. Then compare the installed application macro, motor data, control-source setup, and copied values against the actual fan or pump being served.

10. **Use the correct reset procedure after you diagnose the cause.** For most ACH580 faults, press RESET on the keypad or issue a reset command through the configured digital input or BAS object after the fault condition is gone. If the fault is sticky, remove command, stop the drive, power down fully, wait for the DC bus to discharge, then restore power. Do not use power cycling as your first move on repeated 2001, ground-fault, or internal-memory faults.

11. **Retest the entire operating sequence.** Run the drive in HAND, then return it to AUTO. Confirm the BAS can command speed, start, stop, and handoff cleanly. A repair is not complete until the ACH580 behaves correctly in both local and network-controlled operation.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| [ABB ACH580 cooling fan kit](https://www.amazon.com/s?k=ABB+ACH580+cooling+fan+kit&tag=errorcodefixes-20) | Replaces failed internal cooling fans behind 3001 overtemperature faults | $45 to $120 |
| [ABB ACH580 control panel keypad](https://www.amazon.com/s?k=ABB+ACH580+control+panel&tag=errorcodefixes-20) | Replaces damaged operator panels and helps with local diagnostics and resets | $140 to $260 |
| [3-phase line reactor for VFD](https://www.amazon.com/s?k=3+phase+line+reactor+vfd&tag=errorcodefixes-20) | Helps stabilize poor incoming power and reduce nuisance undervoltage events | $90 to $240 |
| [VFD output reactor for motor protection](https://www.amazon.com/s?k=vfd+output+reactor+motor+protection&tag=errorcodefixes-20) | Reduces reflected-wave stress and overcurrent issues on long motor leads | $110 to $280 |
| [Shielded RS485 cable for BACnet Modbus](https://www.amazon.com/s?k=shielded+rs485+cable+bacnet+modbus&tag=errorcodefixes-20) | Fixes intermittent 5000-series communication faults on noisy BAS trunks | $20 to $55 |
| [DIN rail 24V power supply](https://www.amazon.com/s?k=din+rail+24v+power+supply&tag=errorcodefixes-20) | Replaces weak accessory power feeding relays, sensors, or communication modules | $25 to $80 |
| [Motor insulation tester megohmmeter](https://www.amazon.com/s?k=motor+insulation+tester+megohmmeter&tag=errorcodefixes-20) | Helps confirm motor and cable health before condemning the drive on ground or overcurrent faults | $85 to $240 |

## When to Call a Pro

Call an ABB drive specialist, experienced controls electrician, or BAS contractor when the ACH580 trips the instant you hit RUN, when it faults with the motor disconnected, or when 5000-series communication faults involve a building automation network you do not control. Those cases move beyond basic reset-and-retry troubleshooting.

You should also bring in help for repeated 7000-series internal faults, suspected power-module failure, or any application feeding a hospital air handler, data-center fan wall, critical exhaust system, or chilled-water pump where downtime carries real operational risk. On ACH580 jobs, the cleanest repair often comes from two people working together: one at the drive and one at the BAS front end.

## Frequently Asked Questions

**Q: What is the difference between an ACH580 and an ACS580?**  
The ACH580 is the HVAC-focused version. It is built around fan, pump, hand-off-auto, and BAS integration workflows. The ACS580 is more general-purpose industrial.

**Q: Why does my ACH580 run in HAND but fault in AUTO?**  
That usually points to a controls problem, not a power-section problem. Check command source, speed reference, network timeout settings, and BAS communication first.

**Q: Do long motor leads matter on HVAC drives?**  
Yes. Long leads can create reflected-wave stress, nuisance overcurrent trips, and motor insulation problems. Large rooftop units and remote pump rooms are common examples.

**Q: Can I just power-cycle the drive to clear a fault?**  
You can, but you should not start there. Record the code first, correct the cause, then use the keypad or configured reset command. Blind power cycles hide useful evidence.

**Q: What codes should make me stop resetting and call for help?**  
Repeated overcurrent, ground-fault, internal-memory, and fieldbus faults tied to critical building systems all deserve a deeper diagnosis before anyone keeps trying resets.