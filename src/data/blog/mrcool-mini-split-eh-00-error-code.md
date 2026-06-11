---
title: "MRCOOL EH 00 Error Code - Causes & Fix"
description: "EH 00 means an indoor-unit EEPROM parameter error on the control board. Most likely fix: power off 15 minutes, then replace the board."
pubDatetime: 2026-05-31T07:53:12Z
modDatetime: 2026-05-31T07:53:12Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - mrcool
money_part: "MRCOOL indoor control board (PCB)"
---

## MRCOOL EH 00 Error Code — What It Means

EH 00 on your MRCOOL mini split signals an indoor-unit EEPROM parameter error. The indoor control board has detected a problem with its stored operating parameters or the EEPROM chip itself. MRCOOL groups this code (sometimes displayed as E0 or EH00) under faults that point directly to the indoor control board. The EEPROM is a small memory chip on the board that holds calibration and configuration data. When it fails or becomes corrupted, the board cannot run the unit safely and throws this fault.

[Jump to Fix](#fix)

## Common Causes

- **Failed indoor control board or EEPROM chip** The most direct cause is a hardware failure on the indoor PCB itself, which MRCOOL documentation identifies as the primary issue for EH 00.
- **Corrupted board state after a power event** A power surge, brownout, or abrupt shutdown can leave the EEPROM in a corrupted state that persists until the board is fully reset.
- **Loose or damaged wiring at the indoor board** MRCOOL specifically instructs technicians to inspect the indoor control board for loose connectors and damaged terminals that can interfere with EEPROM function.
- **Burn marks or heat damage on the indoor PCB** Visible thermal damage near connectors or the EEPROM chip can corrupt stored parameters and trigger the fault.
- **Incoming power supply voltage abnormality** MRCOOL recommends checking that supply voltage is within the normal range, as under-voltage or over-voltage can destabilize the board and memory.

## Step-by-Step Fix {#fix}

1. **Kill power at the breaker** and leave the unit completely off for 15 minutes, then restore power and check whether the code clears.
2. **Verify supply voltage** with a multimeter at the indoor unit's power terminals if the error returns.
3. **Remove the front panel** of the indoor unit and locate the indoor control board, typically mounted behind the filter area.
4. **Inspect the indoor PCB** closely for loose connectors, damaged terminals, burn marks, or any signs of heat damage.
5. **Reseat all wiring connectors** at the indoor board to make sure secure contact, especially the main power and communication harnesses.
6. **Replace the indoor control board** if voltage is normal and wiring is intact, as MRCOOL identifies the board itself as the likely cause of EH 00.
7. **Call a qualified HVAC technician** if the code persists after board replacement or if you are uncertain about any diagnostic step.

## Parts Often Needed

| Part | Notes |
|------|-------|
| MRCOOL indoor control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-00-error-code&k=MRCOOL+indoor+control+board+%28PCB%29&tag=errorcodefixes-20) \| Primary replacement for EH 00. Match your exact model number and indoor unit serial. |
| Wiring harness connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-mrcool-mini-split-eh-00-error-code&k=Wiring+harness+connectors&tag=errorcodefixes-20) \| If visible damage or melting is present at board terminals. |

## When to Call a Pro

Call a licensed HVAC technician if the 15-minute power reset does not clear the code, if you see burn marks or other damage on the board, or if you are uncomfortable working inside line-voltage equipment. MRCOOL recommends professional service when the indoor control board requires replacement or when diagnosis is uncertain. Technicians have the tools to verify supply voltage safely and can source the correct replacement board for your specific model and serial number.
