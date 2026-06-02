---
title: "LG Dryer E00 Error Code - Causes & Fix"
description: "E00 means the display board can't read software from the main control board. Power-cycle the dryer for 60 seconds first."
pubDatetime: 2026-05-31T03:33:00Z
modDatetime: 2026-05-31T03:33:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - appliance
  - dryer
  - lg
---

## LG Dryer E00 Error Code — What It Means

The E00 error on an LG dryer signals a control and communication fault between the display PCB and the main PCB. According to LG, the display board cannot read the software from the main control board. This is not a mechanical problem like a clogged vent or faulty thermistor. It is an electronics issue involving the control boards and their communication link.

In technical terms, the error points to an EEPROM operation abnormality or a firmware/memory problem on the main board. The display board tries to load the dryer's program from the main board and fails. Most of the time this is a transient software glitch that clears with a power reset, but if it returns the fault is usually a failed main PCB, a defective display PCB, or a loose connection between the two boards.

[Jump to Fix](#fix)

## Common Causes

- **Transient control lockup or software glitch** A power event or brief surge can cause the control boards to lock up, preventing normal communication until the system is fully reset.
- **Failed or corrupted main PCB software or memory** The main control board's EEPROM or firmware may have failed or become corrupted, so the display board cannot read the operating program.
- **Communication problem between boards** A loose connector, damaged wire, or poor contact in the harness linking the display PCB to the main PCB can block the data transfer.
- **Defective main control board** The main PCB itself may have failed due to component wear, heat damage, or electrical stress, making it unable to send valid software to the display.
- **Defective display board** Less commonly, the display PCB itself may be faulty and unable to read data even when the main board is sending it correctly.

## Step-by-Step Fix {#fix}

1. **Unplug the dryer or trip the circuit breaker** and leave the power off for at least 60 seconds to allow the control boards to fully discharge and reset.
2. **Hold the START/PAUSE button for 5 seconds** while the power is still off, then release it (LG recommends this step on some models to help clear certain error-reset procedures).
3. **Restore power** by plugging the dryer back in or switching the breaker on, then run a test cycle to see if the E00 code clears.
4. **If the code returns immediately**, unplug the dryer again and remove the top or rear panel to access the control boards and their wiring harness.
5. **Inspect the connectors** between the display PCB and main PCB for looseness, corrosion, burn marks, or damaged pins, and reseat any connectors that appear loose.
6. **Check the main PCB and display PCB** for visible damage such as scorched components, swollen capacitors, or cracked solder joints on the board surface.
7. **Replace the main control board** if no harness fault is found and the error persists, since failed main-board software or memory is the most common cause of E00 after reset fails.
8. **If replacing the main PCB does not resolve the code**, replace the display PCB as a secondary measure, since a faulty display board can also prevent successful communication.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Main control board (main PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-dryer-e00-error-code&k=Main+control+board+%28main+PCB%29&tag=errorcodefixes-20) \| Match your dryer's model number exactly. This is the most common replacement for persistent E00 errors. |
| Display board (user interface PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-dryer-e00-error-code&k=Display+board+%28user+interface+PCB%29&tag=errorcodefixes-20) \| Order the correct part for your model. Replace if the main board does not fix the error or if the display shows visible damage. |
| Wiring harness (board-to-board connector) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-dryer-e00-error-code&k=Wiring+harness+%28board-to-board+connector%29&tag=errorcodefixes-20) \| Only needed if inspection reveals physical damage to the harness or connectors between the two control boards. |

## When to Call a Pro

Call a professional if the power reset does not clear the code or if you are not comfortable working inside the dryer's control cabinet. Board-level diagnosis requires access to live 240 V circuits, and misidentifying the failed board can lead to unnecessary parts cost. A qualified technician can test the communication link between boards, verify connector integrity, and confirm which PCB has failed before ordering parts. If your dryer is still under warranty, contact LG or an authorized service center before attempting any board replacement yourself.
