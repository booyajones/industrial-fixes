---
title: "Siemens G120 F01044 - Causes & Fix"
description: "F01044 means the Control Unit cannot load descriptive data from memory. Most common fix: power cycle, reseat memory card, or replace CU."
pubDatetime: 2026-05-31T11:18:13Z
modDatetime: 2026-05-31T11:18:13Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
---

## Siemens G120 F01044 — What It Means

F01044 on a Siemens SINAMICS G120 means the Control Unit detected an error while loading descriptive data stored in non-volatile memory. Siemens fault documentation identifies this as either "CU: Descriptive data error" or "Loading memory data card defective," depending on the fault table version. Both descriptions point to the same root problem: the Control Unit cannot correctly read or validate its stored configuration data. This is a memory or internal data fault, not a motor or power circuit issue.

[Jump to Fix](#fix)

## Common Causes

- **Corrupted non-volatile memory data** The Control Unit's internal memory has become corrupted or inconsistent, preventing it from loading descriptive data at startup.
- **Defective or poorly seated memory data card** If the drive uses a removable memory or data card, the card may be damaged, improperly seated, or have contaminated contacts.
- **Incomplete parameter transfer or power loss during commissioning** A parameter upload, firmware change, or unexpected power interruption can leave descriptive data in an unreadable state.
- **Control Unit hardware fault** The Control Unit itself may have failed if the fault returns after power cycling, reseating cards, and reloading parameters.

## Step-by-Step Fix {#fix}

1. **Record the fault buffer** and current drive configuration using the BOP or commissioning software before making any changes.
2. **Power-cycle the drive completely** by turning off all supply power, waiting 30 seconds, then powering back on to see if the fault clears after a full restart.
3. **Inspect and reseat the memory data card** if your G120 uses a removable storage card. Remove it, check for damage or contamination on the contacts, firmly reseat it, and re-test.
4. **Reload drive parameters** from a known-good backup file or recommission the drive from scratch if stored data is corrupt. Use Siemens Starter or SINAMICS G120 Smart Access software to upload a clean configuration.
5. **Update the Control Unit firmware** if the installed version is outdated or known to have memory stability issues. Consult Siemens documentation for your CU model and compatible firmware revisions.
6. **Replace the Control Unit** if the fault persists after power cycling, reseating or replacing the memory card, and restoring parameters. The CU cannot reliably load its own descriptive data and must be replaced with a unit matching your G120 hardware family and firmware compatibility.
7. **Clear the fault and monitor** after any corrective action. Check the fault buffer again after several hours of operation to confirm the issue is resolved.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01044-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Match the exact CU variant and firmware revision installed in your drive. Required when internal memory or hardware fault persists. |
| Siemens Memory Data Card (for G120) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-vfd-f01044-fault-code&k=Siemens+Memory+Data+Card+%28for+G120%29&tag=errorcodefixes-20) \| If your drive uses a removable memory or parameter card and the card is damaged or defective. Verify card compatibility with your CU model. |

## When to Call a Pro

Call a qualified Siemens technician or drive specialist if the fault returns after power cycling and reseating the memory card, if you do not have parameter backups and need to recommission the drive, or if you are unsure which Control Unit or firmware version is installed. Replacing a Control Unit or reloading drive parameters requires knowledge of the driven equipment and motor parameters to avoid commissioning errors. If the drive is part of a networked or safety-rated system, always involve a professional to maintain system integrity and compliance.
