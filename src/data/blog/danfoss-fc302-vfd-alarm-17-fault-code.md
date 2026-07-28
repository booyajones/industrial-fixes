---
title: "Danfoss FC302 Alarm 17 - Causes & Fix"
description: "Alarm 17 on Danfoss FC302 VFD means control word timeout (lost communication from PLC or fieldbus). Check master controller first."
pubDatetime: 2026-06-02T10:44:42Z
modDatetime: 2026-06-02T10:44:42Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Fieldbus communication cable"
most_likely_cause: "PLC or master controller stopped"
---

## What this code means
Alarm 17 on the Danfoss VLT AutomationDrive FC 302 signals a control word timeout. This means the drive stopped receiving the expected cyclic control word updates from its communication source within the configured timeout period. The control source is typically a PLC, fieldbus master, or another controller that sends control commands over the network. When communication is lost, the drive trips or stops to prevent unintended operation.

Danfoss documentation also calls this fault "Std bus timeout" in some service materials. The alarm indicates no communication is reaching the frequency converter from the configured control source. The drive expects regular updates and will fault when those updates stop arriving.

## Common Causes

- **PLC or master controller stopped** The controller that sends the control word has crashed, been turned off, or stopped its scan cycle so no commands are being transmitted.
- **Fieldbus network wiring problem** A broken cable, loose terminal connection, failed network switch, or poor shielding and grounding interrupts the communication path.
- **Controller programming or firmware work in progress** Communication halts temporarily during PLC program downloads, updates, or startup sequences that suspend normal scanning.
- **Incorrect timeout parameter setting** The timeout value in parameter 8-04 is too short for the actual network scan time, causing the drive to trip on normal communication delays.
- **No active communication source configured** The drive is set to fieldbus control mode but the network is not connected, the option card is missing, or the bus is not actually communicating.
- **Failed communication option card or control board** The drive's internal fieldbus interface card or main control card has failed and can no longer receive or process incoming control words.

## Step-by-Step Fix {#fix}

1. {'lead': "Verify the drive's control mode configuration", 'text': 'to confirm the FC 302 is set to receive control words from fieldbus or serial communication and not from the local keypad or hardwired inputs.'}
2. {'lead': 'Check the PLC or master controller status', 'text': 'to confirm it is powered on, running its scan cycle, and actively sending control words to the drive over the network.'}
3. {'lead': 'Inspect all fieldbus wiring and connections', 'text': 'for continuity, secure terminals, proper cable termination, intact shielding, and any signs of physical damage or poor grounding that could interrupt communication.'}
4. {'lead': 'Test network health and infrastructure', 'text': 'by checking for failed switches, disconnected nodes, or controller task faults that would stop the cyclic data exchange with the drive.'}
5. {'lead': 'Review and adjust the control word timeout parameter', 'text': 'if the timeout setting is too short for your network scan time, extend it to accommodate normal communication delays without tripping the drive.'}
6. {'lead': 'Cycle power and clear the fault', 'text': 'after correcting the communication issue, then monitor the drive to confirm Alarm 17 does not return during normal operation.'}
7. {'lead': 'Check the communication option card and control board', 'text': 'if the alarm persists with verified good wiring and a functioning master controller, as a defective card or internal control fault may prevent proper communication.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Fieldbus communication cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-17-fault-code&k=Fieldbus+communication+cable&tag=errorcodefixes-20) \| Replace if continuity testing shows breaks or if shielding is damaged. |
| Danfoss FC 302 fieldbus option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-17-fault-code&k=Danfoss+FC+302+fieldbus+option+card&tag=errorcodefixes-20) \| Required if the installed communication module is defective and cannot receive control words. |
| Danfoss FC 302 control card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-alarm-17-fault-code&k=Danfoss+FC+302+control+card&tag=errorcodefixes-20) \| Needed if internal logic or communication circuitry has failed and external wiring and master are both confirmed good. |

## When to Call a Pro

Call a qualified automation technician or Danfoss service provider if you have verified that the PLC or master controller is running and the fieldbus wiring tests good but Alarm 17 continues to appear. Diagnosing internal control board or option card failures requires specialized test equipment and familiarity with Danfoss drive architecture. Also call a professional if you are not trained in industrial fieldbus networks or PLC troubleshooting, as incorrect changes to communication parameters or wiring can create safety hazards or damage other connected devices on the network.
