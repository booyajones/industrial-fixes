---
title: "ABB ACH580 Fault Codes - What It Means and How to Fix It"
description: "ABB ACH580 drives use numeric fault families to point you toward power, temperature, fieldbus, and configuration problems. This guide focuses on the HVAC faults technicians see most and the parts that fix them."
pubDatetime: 2026-04-25T00:00:00Z
author: errorcodefixes.com
tags:
  - hvac
  - error-codes
---

The ABB ACH580 is not the same drive as the ACS580. The ACH580 is the HVAC-specific version. ABB built it for air handlers, chilled water pumps, cooling towers, condenser water loops, and building automation integrations. That means its fault patterns show up in a different kind of environment: noisy control cabinets, long motor leads, BAS network issues, dirty mechanical rooms, and operators who need the fan back online before the building starts getting hot.

If your ACH580 display is showing a 2001-series, 3000-series, or 7000-series fault, the code is giving you the shortest path to the failure. This guide helps you take that path.

## What Does ABB ACH580 Fault Codes Mean?

The ACH580 uses numeric fault and warning codes. In the field, most technicians see them grouped by family:

- **2001-2999** usually point to power, current, and hardware protection
- **3000-3999** usually involve temperature, motor model, and operating limits
- **5000-5999** often involve communication, option modules, or fieldbus control
- **7000-7999** usually involve application logic, internal software, accessory modules, or configuration mismatches

The single fastest way to troubleshoot an ACH580 is to answer three questions:

1. Did the fault happen on start, while running, or during stop?
2. Is the problem electrical, mechanical, or network-related?
3. Was anything changed before the fault started, such as a motor swap, a BAS update, or a parameter reset?

Those three answers narrow most ACH580 failures down faster than scrolling the keypad.

## How to Fix It

### Step 1: Capture the fault history before resetting

The ACH580 stores useful history. Before you reset the drive:

1. Record the active fault code
2. Record motor current, output frequency, DC bus voltage, and heatsink temperature if available
3. Note whether the drive was in HAND, OFF, or AUTO
4. Ask whether the BAS had control at the time of failure

Too many service calls stall because the first person hit RESET and erased the best clue.

### Step 2: Check the most common ACH580 faults first

#### 2001 / overcurrent

This is one of the most common trip codes on ACH580 drives. The drive saw output current above the safe limit.

**Typical causes**
1. Shorted motor cable or damaged insulation
2. Fan or pump mechanically bound
3. Acceleration ramp too short
4. Wrong motor data after commissioning or board replacement
5. Very long motor leads without reactor or filter

**What to do**
1. Lock out power and inspect motor leads for rubbed insulation, especially at conduit entries and VFD terminals
2. Turn the motor or driven load by hand if the application allows it
3. Compare programmed motor FLA, voltage, RPM, and frequency to the nameplate
4. Increase acceleration time and test again
5. Add or verify output reactor on long lead installations

#### 2002 / DC overvoltage

This fault usually appears during stopping. The rotating load regenerates back into the DC bus and drives the voltage too high.

**Common HVAC examples**
- Large supply fan with steep stop ramp
- Cooling tower fan coast-down with tight decel setting
- Pump with aggressive stop command and no flying start optimization

**What to do**
1. Lengthen decel time
2. Enable coast stop if the process allows it
3. Review flying start settings for fan applications
4. If the load has true regenerative energy, use proper braking hardware or redesign the stop sequence

#### 2003 / undervoltage

The DC bus voltage fell below the safe threshold.

**Typical causes**
1. Utility sag during building startup
2. Loose incoming power lugs
3. Phase imbalance from bad upstream fuse or breaker pole
4. Transformer tap mismatch

**What to do**
1. Measure all three input phases under load
2. Check fuses, disconnects, and terminals for heat damage
3. Tighten lugs to ABB torque specification
4. If the building has repeated sags, add line reactor or investigate feeder capacity

#### 2330 or similar ground fault family code

The exact number varies by firmware, but ground fault trips on ACH580 usually point to leakage from output to earth.

**What to do**
1. Inspect cable insulation and motor junction box
2. Test motor insulation to ground
3. Disconnect the motor leads from the drive and test components separately
4. If the motor checks clean and the fault remains with leads disconnected, suspect the drive power section

### Step 3: Check temperature-related 3000-series faults

#### 3001 / drive overtemperature

Mechanical rooms are brutal on ACH580 drives. Dust, clogged filters, and hot return air push them over the edge.

**Typical causes**
1. Failed cooling fan
2. Dirty heat sink
3. Panel temperature too high
4. Carrier frequency too high for the enclosure conditions
5. Drive undersized for motor current

**What to do**
1. Verify all internal fans run
2. Clean the heat sink fins and panel filters
3. Measure ambient temperature in the cabinet, not just the room
4. Lower carrier frequency if acoustic requirements allow it
5. Compare actual running current to drive rating

#### 3005 / motor thermal overload

The ACH580 thermal model believes the motor has exceeded safe temperature.

**What to do**
1. Verify motor FLA and service factor settings
2. Check for airflow restriction in the mechanical system, especially closed dampers or blocked strainers
3. Review starts per hour and low-speed cooling limits
4. On HVAC fans, confirm minimum speed is not so low that motor self-cooling disappears for long periods

### Step 4: Deal with communication and BAS faults in the 5000-series

This is where the ACH580 differs from a general-purpose drive. HVAC sites live on BACnet MS/TP, BACnet/IP, Modbus RTU, Modbus TCP, and building automation supervision.

#### 5001 / fieldbus communication lost

**Typical causes**
1. BAS controller offline
2. Wrong MAC address, baud rate, or IP settings
3. Duplicate address on RS-485 trunk
4. Bad shield or no termination resistor
5. Communication timeout parameter set too aggressively

**What to do**
1. Check whether the drive runs in HAND mode. If it does, the power section is fine and the network path is the issue
2. Inspect network LEDs on the option module
3. Confirm the BAS still sees the drive object online
4. Verify termination and biasing on RS-485
5. Look for grounding issues between VFD cabinet and BAS panel

#### BACnet-specific nuisance faults

The ACH580 often looks faulty when the real issue is control handoff. The drive is healthy, but the BAS is sending zero speed reference, wrong command source, or conflicting enable signals.

**Best field trick:** Put the drive in HAND and command a safe low speed. If the motor runs cleanly, the drive and motor are fine. The fault is upstream in BAS logic, addressing, or command mapping.

### Step 5: Handle 7000-series configuration and internal faults

These codes are less common, but they matter.

#### 7001 / parameter mismatch after board or keypad change

This happens after maintenance swaps a control board or copies parameters from the wrong template.

**What to do**
1. Compare motor nameplate values to programmed values
2. Confirm macro selection matches the application, such as fan or pump
3. Re-run motor identification if the manual recommends it
4. Restore from the correct backup, not just any backup from another AHU or pump

#### 7003 / internal memory or control board issue

If a hard reset does not clear this family of code, the control board may be failing.

**What to do**
1. Power down fully for 5 minutes
2. Reseat removable control connectors if the cabinet design allows it
3. Backup parameters if you still can
4. Plan for board replacement

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|--------------|
| [ABB ACH580 cooling fan kit](https://www.amazon.com/s?k=ABB+ACH580+cooling+fan+kit&tag=errorcodefixes-20) | Failed internal cooling fan causes 3001 overtemperature trips | $45–$110 |
| [3-phase line reactor for ABB VFD](https://www.amazon.com/s?k=3+phase+line+reactor+for+vfd&tag=errorcodefixes-20) | Helps prevent nuisance undervoltage and protects the drive from line disturbances | $90–$240 |
| [VFD output reactor for motor protection](https://www.amazon.com/s?k=vfd+output+reactor+motor+protection&tag=errorcodefixes-20) | Reduces reflected wave stress and overcurrent trips on long motor leads | $110–$280 |
| [Shielded RS-485 cable BACnet MS/TP](https://www.amazon.com/s?k=shielded+rs485+cable+bacnet+mstp&tag=errorcodefixes-20) | Fixes intermittent 5000-series fieldbus faults on noisy HVAC networks | $20–$55 |
| [Industrial DIN rail 24V power supply](https://www.amazon.com/s?k=industrial+din+rail+24v+power+supply&tag=errorcodefixes-20) | Replaces failing accessory supply feeding sensors, relays, or comm modules | $28–$75 |
| [Motor insulation resistance tester megohmmeter](https://www.amazon.com/s?k=motor+insulation+tester+megohmmeter&tag=errorcodefixes-20) | Required to confirm ground fault or insulation breakdown before condemning the drive | $85–$240 |

## When to Call a Pro

Bring in an ABB drive specialist or experienced controls electrician when:

1. The drive trips immediately on RUN with the motor disconnected
2. You suspect a failed power module or control board
3. The fault involves fieldbus integration and the BAS contractor owns the logic
4. The application serves a live hospital, data center, lab, or critical comfort zone
5. The site lacks a verified parameter backup

On ACH580 systems, the cleanest repair often comes from two people working together: the VFD tech at the drive and the BAS tech at the front end.

## Frequently Asked Questions

**Q: What is the difference between an ACH580 and an ACS580?**

The ACH580 is the HVAC-specific drive. ABB built it for fans, pumps, hand-off-auto workflows, and building automation integration. The ACS580 is a more general industrial drive. They share ABB design DNA, but the ACH580 includes HVAC application structure and common BAS workflows that do not always map cleanly from the ACS line.

**Q: Why does my ACH580 fault only in AUTO but run fine in HAND?**

That points to a controls problem, not a power problem. In HAND, the drive uses its local command and speed reference. In AUTO, it depends on BAS or fieldbus commands. Check command source, speed reference source, network timeouts, and BAS logic first.

**Q: Do long motor leads really matter on HVAC drives?**

Yes. Long leads increase reflected wave stress on the motor and can create nuisance overcurrent and ground-fault behavior. Large rooftop units and remote pump rooms are common offenders. Output reactors or dv/dt filters often solve problems that look random until you measure lead length.

**Q: Can I just reset an ACH580 and put it back in service?**

You can, but you should not do it blindly. Capture the code and operating condition first. If the code is a one-time nuisance undervoltage during a utility event, a reset is fine. If the code is overcurrent, ground fault, or repeated overtemperature, resetting without diagnosis risks bigger damage.
