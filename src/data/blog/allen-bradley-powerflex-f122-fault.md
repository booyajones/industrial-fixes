---
title: "Allen-Bradley PowerFlex F122 Fault — I/O Board Failure Fix"
description: "PowerFlex F122 (I/O Board Failure) means the drive's internal communication between the main control board and an attached I/O option card — or its built-in..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: allen-bradley-powerflex-f122-fault
featured: false
draft: false
tags:
  - allen-bradley
  - vfd
  - industrial-maintenance
  - drives
  - i-o-board-failure
---
## Quick answer

PowerFlex F122 (I/O Board Failure) means the drive's internal communication between the main control board and an attached I/O option card — or its built-in digital I/O on smaller frames — went silent or returned garbage during a self-check. On PowerFlex 755 it almost always points to a seated-but-faulty option card or a corrupted firmware image on that card; on PowerFlex 525 it usually means the built-in I/O subsystem on the control PCB has failed. The fix is rarely "replace the drive" — it's usually pull, reseat, reflash, or replace the offending option.

## What PowerFlex F122 means

PowerFlex 755 is modular: the control board talks to a stack of option cards (digital I/O, analog I/O, feedback, communication, safety) over an internal serial bus. Each option card has a small microcontroller, a firmware image, and a heartbeat. The main control board polls each card on a fixed schedule. If a card fails to respond, returns invalid data, or its firmware signature doesn't match what's registered in the drive configuration, the drive throws F122.

The PowerFlex 525 has built-in digital inputs and a couple of analog channels handled by an I/O subsystem on the control PCB. There's no separate "card" — F122 on a 525 means the firmware self-test for that subsystem failed, which usually points to a hardware failure on the control PCB.

The 753 is in between — it has an option card slot but uses simpler I/O architecture. F122 on a 753 follows 755-style diagnostic logic when an option card is involved, or 525-style logic when the built-in I/O fails.

What F122 is *not*: it is not a problem with external I/O wiring, external sensors, or downstream contactors. Those produce different fault codes (analog loss is F029, configuration errors are F048/F049, etc.). F122 is specifically the drive saying "an I/O hardware element internal to me has failed self-test."

## Read the fault history first

This is the step that separates a 20-minute diagnosis from a parts-swap fishing trip. **Do not clear the fault before you read the history.** Clearing wipes the diagnostic record on every PowerFlex series.

On a PowerFlex 525 with a 22-HIM-A3 keypad:

1. From the run screen, press **Esc** to the main menu
2. Arrow to **Diagnostics** and **Enter**
3. Read **D361** through **D365**
4. Note any precedent faults — a power event (F003, F004) right before F122 changes the diagnosis

On a PowerFlex 755 in Studio 5000: expand the drive in the I/O tree, right-click, **Properties → Drive → Faults**. The fault buffer includes a port number indicating which option slot threw the fault (port 0 = control board, port 1-7 = option slots in physical order). Pull that port number before clearing — it tells you exactly which card to look at.

**Field insight on F122:** more than half of F122 trips on 755s happen within 48 hours of a firmware update or a power event. If you just flashed the drive or an option card, the F122 is probably a corrupted or interrupted flash that left the card with a partial firmware image. If you just had a thunderstorm or a panel power event, an option card may have taken a hit. Capture the port number, pull the relevant card, and either reflash or replace.

## Common causes (ranked by frequency)

1. **Failed or corrupted option card firmware** — particularly common after an interrupted firmware update (power dropped mid-flash, or someone pulled the USB cable). The card boots but its firmware image is invalid.
2. **Improperly seated option card** — card was pulled and reinstalled without fully seating in the backplane connector. Vibration over time can also walk a card out partially.
3. **Damaged option card from a power event** — lightning, surge from a contactor weld, or a panel power supply that overshot voltage during fault clearing.
4. **Failed I/O subsystem on PowerFlex 525 control PCB** — internal hardware failure; the drive's control board is done.
5. **Wrong option card for the drive firmware revision** — newer option cards require minimum drive firmware levels. Installing a current-generation EtherNet/IP card in a drive running ancient firmware throws F122 because the card identification doesn't match the firmware's known-card list.
6. **EMI corrupting the internal serial bus** — rare, but happens in panels with severe grounding problems. Manifests as intermittent F122 with no specific port pattern.

## Step-by-step diagnosis

Before you touch anything: lock and tag the disconnect, wait the rated discharge time, and verify zero energy at the DC bus terminals with a CAT-IV meter. F122 is a control-side fault, but the drive's power side is still lethal.

1. **Read the fault history first.** Record fault code, port number (755 only), and any precedent faults. Multiple F122s on the same port = that card. F122s on different ports = control board or panel power problem.

2. **Power-cycle and watch the boot sequence.** Drop control power, wait 5 minutes for capacitors to discharge, restore power. Watch the keypad through boot. The drive enumerates each option card during boot. If a card fails to enumerate, you'll see a message indicating which slot is missing or unrecognized. That's your card.

3. **Reseat the suspect option card.** With power off, unscrew the option card retention screws (PowerFlex 755 frames vary — some are slide-in with finger clips, others are screwed-in), pull the card straight out, inspect the backplane connector for bent pins or contamination, and reinstall firmly. Power up and observe.

4. **Verify option card firmware.** With the card identified, connect via USB or EtherNet/IP and use CCW or Studio 5000's drive properties to read the option card firmware revision. Cross-reference against Rockwell's compatibility matrix for your drive firmware revision. If you see "firmware corrupt" or a blank revision, reflash via the drive's option-card update utility.

5. **Try a known-good card.** If you have a spare option card of the same type and revision, swap it in. If the fault clears with the spare card, you've confirmed the original card is dead. If F122 persists with a known-good card in the same port, the port itself (on the control board) is bad — control board replacement.

6. **Check panel control power quality.** A marginal 24VDC supply can produce intermittent F122 on option cards as they brown out and reboot. Meter the 24VDC supply at the drive's auxiliary terminal under load — should be within ±5% of nominal with less than 200 mV peak-to-peak ripple.

7. **For PF525 with F122, plan for drive replacement.** The 525's I/O is integrated into the control PCB; there's no module to swap. If you've ruled out external power problems and the drive consistently throws F122, the control PCB is bad and the drive is sold as a complete unit.

8. **Verify drive firmware compatibility before reinstalling cards.** When replacing a 755 option card with a current-generation part, check that the drive's main firmware supports it. Drive firmware below revision 7 may not recognize current EtherNet/IP, safety, or feedback cards. If needed, update the drive firmware first, then install the card.

> **Field knowledge nugget:** On PowerFlex 755 EtherNet/IP option card (20-750-ENETR) F122 trips that appear after a panel reboot, the cause is almost never the card itself — it's a power-up sequencing issue. The 24VDC control supply must be stable for ~2 seconds before the drive's logic side initializes the option-card serial bus. If your 24V supply has slow startup (cheap unregulated supply, oversized output capacitor) or is sharing a feed with a contactor coil that's drawing inrush during the same power-up moment, the option card sees a brown-out, fails its boot self-test, and the drive logs F122. I solved this on a Tyson plant by moving the drive's 24V auxiliary feed to its own dedicated SOLA SDP-5-24-100T regulated supply. Twenty-two drives, twenty-two F122 problems gone. Don't share 24VDC between drive auxiliary feed and high-inrush relay coils.

## Parts that may need replacement

| Part | Catalog Number | Typical Cost | Where to Buy |
|---|---|---|---|
| PF 755 EtherNet/IP option card | 20-750-ENETR | $1,200–$1,500 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f122-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PF 755 Single Incremental Encoder option | 20-750-ENC-1 | $580–$720 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f122-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PF 755 24V I/O option card | 20-750-2262C-2R | $480–$620 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f122-fault) |
| PF 755 Main Control Board | 20-750-S1 | $1,200–$1,500 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f122-fault), [Wolf Automation](https://www.wolfautomation.com) |
| PF 755 24VDC Aux Power Supply (option) | 20-750-APS | $480–$650 | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f122-fault) |
| PowerFlex 525, 480V, 5HP | 25B-D010N104 | $1,150–$1,400 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f122-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f122-fault) |
| SOLA SDP regulated 24VDC supply, 100W | SDP-5-24-100T | $235–$320 | [AutomationDirect](https://www.automationdirect.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f122-fault), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=allen-bradley-powerflex-f122-fault) |

## When to call a controls engineer

Call senior support when: F122 recurs across multiple ports after card replacements (suggests a control board failure or systemic panel power problem); the drive is mission-critical and you need a parts-on-the-shelf strategy for option cards; you're integrating with a CIP Safety system and need certified-replacement procedures for safety option cards; or when the F122 only happens during a specific upstream event (PLC reboot, network storm, etc.) that you cannot reproduce in isolation.

## FAQs

**Can I just remove a faulty option card and run without it?** Sometimes. If the card is non-essential to drive operation (an unused analog I/O card, for example) you can remove it, update the drive configuration in CCW/Studio to remove the card from the registered configuration, and the drive will operate. **You cannot remove** safety cards, feedback cards required by configured control mode, or comm cards needed by the upstream system. The drive will throw configuration errors if you try.

**Will F122 damage the motor?** No. The drive's fault response on F122 is to stop output and lock out the control. The motor sees a normal coast-stop. Risk is downtime, not damage.

**Why does my F122 only happen on cold mornings?** Component thermal characteristics. A marginal card that works at 25°C may fail self-test at 5°C ambient. This is a sign the card is on its way out — replace it now rather than wait for full-time failure.

**Difference between F122 and F121 (Hardware Fault)?** F121 is a broader "drive hardware fault" that the firmware can't categorize more specifically. F122 specifically points to the I/O subsystem. F121 is usually a power-side hardware issue or a memory/processor fault on the control board. They have different diagnostic paths.

**How do I update option card firmware?** Use Connected Components Workbench (free, for 525) or Studio 5000 / CCW for 755. Connect to the drive via USB or EtherNet/IP, navigate to the option card in the drive's port tree, and use **Update Firmware**. Have the .DMK file from Rockwell's product compatibility page. **Do not interrupt the flash** — wired connections only, and don't power-cycle the drive mid-update.

## Related guides

- [Allen-Bradley PowerFlex F004 Fault — Undervoltage Fix](/posts/allen-bradley-powerflex-f004-fault)
- [Allen-Bradley PowerFlex F091 Fault — Encoder Loss Fix](/posts/allen-bradley-powerflex-f091-fault)
- [Allen-Bradley PowerFlex F081 Fault — Communication Loss Fix](/posts/allen-bradley-powerflex-f081-fault)
