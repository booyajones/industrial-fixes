---
title: "Yaskawa GA800 E14 Fault - Causes & Fix"
description: "E14 (oFA14) means option card connection error at CN5-A. Most common fix: reseat the option card and check for bent pins."
pubDatetime: 2026-06-05T09:51:18Z
modDatetime: 2026-06-05T09:51:18Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA800 E14 Fault — What It Means

The E14 fault (also displayed as oFA14) on a Yaskawa GA800 VFD indicates an Option Card Connection Error at the CN5-A interface. The drive has detected a problem communicating with or sensing the option card installed in that slot. This is not a motor or overload fault. It is a hardware-level issue between the drive's control board and the accessory card plugged into the CN5-A connector.

The fault means the drive cannot establish or maintain proper electrical contact with the option card, which could be a communication module, encoder interface, or other accessory depending on your system configuration. The drive will not operate normally until the connection is restored or the fault condition is cleared.

[Jump to Fix](#fix)

## Common Causes

- **Mis-seated or loose option card** The card is not fully inserted or has worked loose from vibration or handling, breaking the electrical connection at CN5-A.
- **Bent, damaged, or contaminated connector pins** Physical damage or dirt on the CN5-A connector pins prevents proper contact between the drive and the option card.
- **Defective option card** The installed option card itself has failed internally or has a damaged edge connector.
- **Damaged drive control board interface** The CN5-A connection path on the drive's control board is damaged, preventing communication even with a good card.
- **Incorrect or incompatible option card** An option card not designed for the GA800 or not compatible with the firmware version is installed in the CN5-A slot.
- **Loose internal wiring or housing movement** Mechanical shock or improper reassembly has caused the option card mounting area or internal connector to shift out of alignment.

## Step-by-Step Fix {#fix}

1. **Power down the drive and follow lockout/tagout procedures.** Disconnect incoming power, wait for DC bus capacitors to discharge (follow the GA800 manual waiting period), and verify zero voltage before opening the drive enclosure.
2. **Open the drive cover and locate the CN5-A option card slot.** The option card will be a daughter board plugged into a connector on the main control board, consult your GA800 wiring diagram to confirm the CN5-A location for your frame size.
3. **Inspect the option card and connector for visible damage.** Look for bent pins, cracks, corrosion, dust, or foreign material on both the card edge connector and the CN5-A socket on the drive.
4. **Remove and reseat the option card firmly.** Pull the card straight out, inspect both connectors again, then align carefully and press the card fully into the CN5-A connector until it seats completely and any mounting clips or screws are secure.
5. **Restore power and test.** Close the drive cover, restore power, and monitor for the E14 fault. If the fault clears, the issue was a poor connection and reseating solved it.
6. **Swap with a known-good option card if available.** If the fault persists, install a verified working option card of the same type to determine whether the original card or the drive interface is defective.
7. **If the fault follows the card, replace the option card.** If the fault remains with a known-good card installed, the drive's CN5-A interface or control board is damaged and requires service-level repair or control board replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 option card (CN5-A compatible) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e14-fault-code&k=Yaskawa+GA800+option+card+%28CN5-A+compatible%29&tag=errorcodefixes-20) \| Must match the original card type (communication protocol, encoder type, etc.) and be compatible with your GA800 firmware version. |
| GA800 control board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e14-fault-code&k=GA800+control+board+assembly&tag=errorcodefixes-20) \| Required only if the CN5-A interface itself is damaged and reseating or card replacement does not clear the fault. |

## When to Call a Pro

Call a qualified VFD technician or contact Yaskawa technical support if reseating and swapping the option card does not clear the E14 fault. A persistent fault after these steps typically indicates a damaged control board or internal interface that requires factory-level diagnosis and repair. Yaskawa's maintenance guidance is limited to fan and control board replacement, and further internal repairs are outside the scope of field service. Also call a professional if you are not trained in VFD lockout/tagout procedures or if the drive is part of a critical process that requires certified troubleshooting and documentation.
