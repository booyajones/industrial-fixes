---
title: "Fanuc P/S Alarm — Program and Syntax Error Codes Fix Guide"
author: "Industrial Error Code Fixes"
pubDatetime: 2026-04-26T17:45:00Z
featured: false
draft: false
tags:
  - cnc
  - fanuc
  - machining
description: "Fanuc P/S alarms mean a program or syntax error in the part program. Learn what the P/S number means, how to find the faulted block, and how to fix common syntax errors."
---

## Fanuc P/S Alarm — What It Means

**Fanuc P/S alarms** (Program/Syntax alarms) are the most common alarm type encountered by CNC operators and programmers. A P/S alarm means the Fanuc CNC control has detected something in the part program that it cannot execute — a G or M code it doesn't recognize, a missing required word, a value outside the machine's operating range, or a format the control doesn't support. The machine stops motion immediately at the faulted block.

P/S alarms always include a three-digit number after them (e.g., **P/S ALARM 010**, **P/S ALARM 050**, **P/S ALARM 085**). That number is critical — it identifies the specific type of syntax error and tells you exactly where to look in the program. The alarm display on the MDI panel shows the alarm number, and the cursor in the program editor typically positions itself near the offending block.

P/S alarms appear on all Fanuc control series: 0i, 16i/18i, 21i, 30i/31i/32i, and the newer 0i-F and 30i-B platforms. The alarm numbers and descriptions are consistent across series but a few codes are series-specific — always verify against the alarm list in your control's Operator's Manual.

[Jump to Fix](#fix)

## Common P/S Alarm Numbers and What They Mean

| P/S Number | Meaning |
|-----------|---------|
| P/S 000 | Please turn off power (parameter change requires restart) |
| P/S 001 | TH parity error (program tape/transfer issue) |
| P/S 003 | Too many digits in an address word |
| P/S 005 | No program number, or program format invalid |
| P/S 010 | Improper G code (G code not available on this control) |
| P/S 011 | Feed rate not specified (F word missing in a cutting block) |
| P/S 050 | T code exceeds range |
| P/S 070 | Program memory full |
| P/S 085 | Communication error (MDI or RS-232 data transfer) |
| P/S 086 | DR signal off during DNC operation |
| P/S 101 | Please clear memory |

## Common Causes

- **Missing required address word** — A G01/G02/G03 cutting block is missing the required F (feedrate) word. A block that moves a rotary axis is missing the feed. P/S 011 is the classic "no feedrate" alarm.
- **Unsupported G or M code** — The program uses a G or M code that isn't included in this control's software options. Canned cycles, custom macros, and advanced functions are optional — if the option isn't purchased, the code generates P/S 010.
- **Out-of-range value** — A coordinate value that exceeds the machine's travel (max stroke), a feedrate set to zero, or a spindle speed above the machine maximum. The control refuses to execute out-of-range commands.
- **Decimal point format error** — Fanuc controls can be configured for "decimal point programming" or "no decimal point" mode. A program written for one mode and loaded onto a control in the other mode will generate P/S alarms on every coordinate value.
- **Program memory corruption** — After a power failure, battery fault, or data transfer error, program data in the control's memory can become corrupted, causing P/S alarms in a previously working program.
- **Incorrect canned cycle syntax** — G81–G89 canned cycles require specific syntax including the R plane, Z depth, and Q (for peck drilling). Missing or incorrectly placed arguments generate P/S alarms.

## Step-by-Step Fix {#fix}

1. **Read the full P/S alarm number** — Look at the alarm display on the MDI panel. Note the exact three-digit P/S number. Look up that specific number in your Fanuc Operator's Manual (the alarm list is in the Appendix). The manual description will tell you exactly what type of error the control found.

2. **Locate the faulted block in the program** — Press RESET to clear the alarm, then switch to EDIT mode. Navigate to the program. The cursor should be near the faulted block. If it isn't, use the program's O (operation search) or sequence number to find the last block that ran before the alarm. The fault is almost always in the next block.

3. **Read the faulted block carefully** — Check each word in the block:
   - Is the G code valid for this control and this motion type?
   - Is an F (feedrate) word present if the block involves cutting motion?
   - Are coordinate values reasonable for the machine's stroke?
   - Are decimal points present (or absent) as required by the control's input format?
   - For canned cycles, are all required arguments (R, Z, Q) present and in the correct format?

4. **Fix the program in EDIT mode** — Position the cursor at the bad word. Use the ALTER, INSERT, or DELETE softkeys to correct the error. After editing, verify the surrounding blocks haven't been accidentally modified.

5. **Check the control's decimal point mode** — In MDI mode, look at Parameter 3401, Bit 0 (DPI). If DPI = 1, the control uses decimal point programming (1.0 = 1mm or 1 inch). If DPI = 0, the control uses no-decimal-point input (1 = 0.001mm or 0.0001 inch). A mismatch between program format and control setting causes all coordinate values to be misinterpreted. Consult the parameter manual before changing this — it affects all programs in memory.

6. **If the alarm appears in a previously working program** — First verify no edits were made accidentally. Then check the program memory checksum (if your control supports it). If memory corruption is suspected, delete the program, reload it from the CAM system or DNC, and test.

7. **Reset and dry-run the corrected program** — After corrections, use the SINGLE BLOCK and DRY RUN modes to step through the previously faulted section one block at a time. Confirm the corrected block executes without alarm before returning to full-speed production mode.

## Parts You May Need

| Part | Notes |
|------|-------|
| Fanuc Operator's Manual (your series) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-ps-alarm-program-error&k=fanuc+cnc+operators+manual&tag=errorcodefixes-20) — The alarm list appendix is essential; buy the manual for your specific control series (0i, 16i, 30i) |
| Fanuc Programming Manual | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-ps-alarm-program-error&k=fanuc+cnc+programming+manual&tag=errorcodefixes-20) — Covers correct G/M code syntax, canned cycle formats, and macro B programming |
| Compact flash card (memory backup) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-ps-alarm-program-error&k=fanuc+cnc+compact+flash+card&tag=errorcodefixes-20) — Use to back up all programs after fixes; a CF card backup prevents total loss from memory corruption |

## When to Call a Technician

P/S alarms are programming and format issues, not hardware faults — a qualified CNC programmer or applications engineer should audit the program if the alarm persists after correcting apparent syntax errors. If P/S alarms appear in previously working programs without any edits, check for a failing SRAM battery (the battery that maintains program memory when power is off) or a failing compact flash card. A Fanuc service technician can perform a memory diagnostic and battery replacement.

## Related Articles

- [Fanuc Alarm 414 — Servo Alarm Causes & Fix](/posts/fanuc-alarm-414/)
- [Fanuc Alarm 401 — Servo Ready Off Fix](/posts/fanuc-alarm-401/)
- [Fanuc Alarm 300 — APC Battery Alarm Fix](/posts/fanuc-alarm-300/)
- [Fanuc 0i-MD Alarm Code Guide — Complete Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc Alarm Codes — Complete Diagnostic Guide](/posts/fanuc-alarm-codes/)
