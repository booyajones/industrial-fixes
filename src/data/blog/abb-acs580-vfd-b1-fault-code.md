---
title: "ABB ACS580 B1 Fault Code - Causes & Fix"
description: "B1 on an ABB ACS580 is an auxiliary subcode, not a standalone fault. Check the full fault number displayed with it to diagnose."
pubDatetime: 2026-05-31T11:10:08Z
modDatetime: 2026-05-31T11:10:08Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
---

## ABB ACS580 B1 Fault Code — What It Means

On ABB ACS580 drives, B1 is not a fault code by itself. It is an auxiliary code or subcode that appears alongside a main fault number. The ACS580 fault documentation shows that the second number of the code indicates the specific problem branch within a fault family. Without the full fault code displayed on the keypad or event history, you cannot identify the root cause. ABB's troubleshooting guide explicitly states to check the auxiliary code together with the primary fault number to determine the exact issue.

B1 identifies a specific path or subtype of the main fault, so the meaning changes depending on which fault family it is attached to. Always read the complete fault string from the drive display before attempting any repair. The fault list in the ACS580 manual will give you the precise corrective action once you have both the primary fault code and the B1 auxiliary code together.

[Jump to Fix](#fix)

## Common Causes

- **Loose or missing power supply connections** Poor input wiring, loose terminals, or a blown fuse can trigger multiple fault families that use auxiliary codes like B1.
- **Motor cable or motor wiring fault** Short circuit, earth fault, incorrect phasing, or star-delta connection errors in the motor circuit produce faults with subcodes.
- **Overtemperature or blocked airflow** Dirty heatsink fins, failed auxiliary fan, or high ambient temperature force the drive into thermal protection modes with auxiliary identifiers.
- **Parameter or configuration mismatch** Startup data that does not match the motor nameplate or incorrect settings after a service event can cause faults with subcodes.
- **STO safety circuit open or misconfigured** Both safety input channels must be closed for the drive to run, and STO wiring or jumper issues appear with auxiliary fault codes.

## Step-by-Step Fix {#fix}

1. **Read the full fault code** from the keypad or event history menu and write down both the primary fault number and the B1 auxiliary code.
2. **Look up the fault family** in the ABB ACS580 fault list using the complete code, then follow the manufacturer corrective actions for that specific fault.
3. **Inspect input power terminals** for loose connections, verify all three phases are present, and check for blown fuses or phase imbalance at the supply.
4. **Check motor and output wiring** for damaged insulation, loose connections, correct phasing, and verify no contactors are interrupting the motor circuit.
5. **Verify cooling and airflow** by cleaning heatsink fins, confirming the auxiliary fan runs, and checking that ambient temperature is within the drive's rated range.
6. **Review parameter settings** if the fault appeared after service or motor replacement, and confirm motor nameplate data matches the startup parameters in the drive.
7. **Reset the fault** only after correcting the root cause, and cycle power to the control unit if the fault returns immediately after reset.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 input fuse kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-b1-fault-code&k=ABB+ACS580+input+fuse+kit&tag=errorcodefixes-20) \| Match fuse rating and type to your drive frame size and input voltage per the ACS580 installation manual. |
| ABB ACS580 control board (CTRL) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-b1-fault-code&k=ABB+ACS580+control+board+%28CTRL%29&tag=errorcodefixes-20) \| Order by drive frame and firmware revision if parameter corruption or STO logic issues persist after all wiring checks. |
| ABB ACS580 heatsink cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-b1-fault-code&k=ABB+ACS580+heatsink+cooling+fan&tag=errorcodefixes-20) \| Replacement fan for drives with auxiliary cooling, verify voltage and connector type for your frame. |

## When to Call a Pro

Call a qualified electrician or ABB service partner if you cannot identify the full fault code, if the fault returns after you have corrected wiring and parameter issues, or if you are unfamiliar with three-phase power and motor circuits. STO safety circuit faults and repeated thermal trips often indicate deeper issues that require load testing, insulation testing, and firmware diagnostics. ABB recommends contacting their support if faults persist after following the corrective actions in the manual, especially if the drive was recently installed or serviced.
