---
title: "Danfoss FC302 Alarm 38 - Causes & Fix"
description: "Danfoss FC302 Alarm 38 means internal fault, usually a communication error between control and power cards. Reset steps inside."
pubDatetime: 2026-05-30T12:20:39Z
modDatetime: 2026-05-30T12:20:39Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control Card"
---

## Danfoss FC302 Alarm 38 — What It Means

Alarm 38 on the Danfoss VLT FC302 indicates an internal fault. This is not a single field-replaceable failure but a broad category that requires further diagnosis. The drive will display a subcode to help narrow down the problem. According to Danfoss technical support, the most common cause of Alarm 38 is a communication error between the control card and the power card inside the drive. The fault can appear after a disturbance, maintenance work, or component failure that interrupts the internal signal path between these boards.

[Jump to Fix](#fix)

## Common Causes

- **Communication failure between control card and power card** This is the specific internal fault Danfoss identifies for Alarm 38 in its support documentation.
- **Loose or disconnected internal connectors** Vibration, maintenance, or installation errors can unseat the ribbon cables or connectors linking the control and power boards.
- **Failed control card** Electronic component failure on the control card can stop it from communicating with the power section.
- **Failed power card** A fault on the power card can prevent it from responding to control signals or reporting status back to the control board.
- **Improperly seated or incompatible option card** If an option card is installed, poor contact or board-level incompatibility after a replacement can trigger internal fault alarms.
- **Electrical surge or disturbance** Transient voltage events can damage internal electronics and disrupt board-to-board communication paths.

## Step-by-Step Fix {#fix}

1. **Cycle power** by switching off the drive, waiting 30 seconds, and powering it back on to attempt a reset as Danfoss recommends.
2. **Note the displayed subcode** or any additional numbers shown with Alarm 38 and write them down for reference.
3. **Power down completely** and lock out the drive, then open the enclosure to access the internal boards.
4. **Inspect and reseat all internal connections**, paying special attention to the ribbon cables and connectors between the control card and power card, and check that any installed option cards are firmly seated.
5. **Look for physical damage** such as burn marks, corrosion, or loose solder joints on the control card, power card, and interconnects.
6. **Power up and test** the drive after reseating connections to see if the fault clears.
7. **Contact Danfoss technical support** with your drive model, serial number, and subcode if the alarm persists, because the exact internal fault code determines which board requires replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control Card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-38-fault-code&k=Danfoss+FC302+Control+Card&tag=errorcodefixes-20) \| Required if diagnostics or Danfoss support confirm control-side communication failure. |
| Danfoss FC302 Power Card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-38-fault-code&k=Danfoss+FC302+Power+Card&tag=errorcodefixes-20) \| Needed when the power section is not responding to the control board. |
| Internal Ribbon Cable or Connector Kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-38-fault-code&k=Internal+Ribbon+Cable+or+Connector+Kit&tag=errorcodefixes-20) \| Use if visual inspection shows damaged or broken interconnects between boards. |

## When to Call a Pro

Call a qualified VFD technician or contact Danfoss technical support if cycling power and reseating internal connections does not clear Alarm 38. Internal board diagnosis requires knowledge of the specific subcode, access to internal schematics, and safe handling of live power electronics. If you are not trained to open and service the drive or lack the tools to isolate board-level faults, professional repair or factory service is the safest route. Danfoss support can guide board replacement based on the exact fault code displayed.

## See Also

- [Danfoss FC302 ALARM 30 - Causes & Fix](/posts/danfoss-fc302-alarm-30-fault-code/)
- [Danfoss FC302 ALARM 31 - Causes & Fix](/posts/danfoss-fc302-alarm-31-fault-code/)
- [Danfoss FC102 VLT HVAC Drive Fault Codes — Complete Diagnostic Reference](/posts/danfoss-fc102-fault-codes/)
- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
