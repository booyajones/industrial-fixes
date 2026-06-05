---
title: "Siemens Micromaster F0070 - Causes & Fix"
description: "F0070 means the drive did not receive a valid setpoint from the communications board. Check the comms master, wiring, and parameters."
pubDatetime: 2026-06-03T10:35:05Z
modDatetime: 2026-06-03T10:35:05Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens Micromaster F0070 — What It Means

F0070 on a Siemens Micromaster drive is a communications board setpoint fault. The drive is configured to receive its speed or torque command over a fieldbus or serial link, but that setpoint is not arriving within the expected telegram timeout. This is a control and communications issue, not a motor overload or power circuit problem. The drive expects a valid data packet from a PLC, network master, or other controller, and when that packet stops or becomes invalid, it trips F0070 to protect against unintended operation. The fault does not indicate a damaged motor or inverter power stage, it points to a break or misconfiguration in the digital control path between the master device and the drive's communications board.

[Jump to Fix](#fix)

## Common Causes

- **Master or controller not sending setpoint** The PLC, HMI, or network master that should command the drive has stopped transmitting, is in a fault state, or is not in RUN mode.
- **Loose or damaged communications wiring** The cable connecting the drive's communications board to the fieldbus or serial master is open, intermittent, or corroded at terminals.
- **Communications board not seated or failed** The plug-in communications module (CB) is loose in its slot, has damaged connectors, or has failed internally.
- **Incorrect drive parameter configuration** The drive's control-source and setpoint-source parameters do not match the installed communications hardware or network topology.
- **Network termination or wiring fault** Missing or incorrect bus termination resistors, crossed wires, or excessive cable length are causing telegram errors on the fieldbus.
- **Drive electronics fault** If communications hardware and configuration are confirmed good but F0070 persists, the inverter control board may be defective.

## Step-by-Step Fix {#fix}

1. **Confirm the exact fault code** on the drive keypad or display is F0070, not a related code such as F0071 or F0072, which involve different communication paths.
2. **Inspect the communications board** in the drive for loose mounting, damaged connectors, or visible burn marks, and reseat the module firmly in its slot.
3. **Check the communications cable and terminals** between the drive and the master controller for loose wires, corrosion, broken insulation, or incorrect pinout.
4. **Verify the master controller or PLC** is powered on, in RUN mode, not faulted, and actively transmitting telegrams, using the controller's diagnostic LEDs or software monitor.
5. **Review the drive parameter settings** for control source and setpoint source to confirm they match the installed communications interface and network type.
6. **Observe the communications status LEDs** on the drive or fieldbus module and check network wiring for proper termination resistors and cable continuity according to the bus specification.
7. **Clear the fault and attempt a restart** after correcting any wiring, configuration, or master-controller issue, and replace the communications board or drive if F0070 returns immediately with known-good hardware and settings.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens Micromaster communications board (CB module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0070-fault-code&k=Siemens+Micromaster+communications+board+%28CB+module%29&tag=errorcodefixes-20) \| Match the module type (USS, Profibus, DeviceNet, etc.) to your drive model and network. |
| Fieldbus communication cable and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0070-fault-code&k=Fieldbus+communication+cable+and+connectors&tag=errorcodefixes-20) \| Use shielded twisted-pair cable rated for your bus type, with correct impedance and termination resistors. |
| Siemens Micromaster inverter drive | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-vfd-f0070-fault-code&k=Siemens+Micromaster+inverter+drive&tag=errorcodefixes-20) \| If the fault persists after communications hardware and configuration are verified good, the drive electronics may need replacement. |

## When to Call a Pro

Call a qualified electrician or automation technician if you are not trained in industrial communications protocols and drive parameter programming. F0070 diagnosis requires verifying network configuration, reading PLC or controller diagnostics, and interpreting drive parameter settings. Incorrect wiring or parameter changes can cause unexpected motor movement or damage to connected equipment. A technician with a laptop, drive-commissioning software, and network diagnostic tools can quickly identify whether the fault lies in the master controller, the fieldbus wiring, or the drive itself, and make the repair safely.
