---
title: "Schneider Altivar Fault CFF — Causes & Fix"
description: "What Schneider Altivar fault CFF means, why incorrect configuration triggers, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - schneider
---

## Schneider Altivar Fault CFF — What It Means

Schneider Altivar fault **CFF** (Configuration Fault) indicates an **incorrect configuration** was detected — the drive found a mismatch or incompatibility between the stored configuration data and the drive's current hardware or software. CFF is common on Altivar 12, 21, 31, 61, and 71 series drives and typically appears after a firmware update, parameter restore, or option card change that results in conflicting or incomplete parameter data. The drive refuses to run until the configuration is resolved.

[Jump to Fix](#fix)

## Common Causes

- **Parameter restore from an incompatible source** — Uploading a parameter file from a different drive model or firmware version causes CFF because some parameters don't exist or have different valid ranges.
- **Option card replacement or addition** — Installing or removing an I/O expansion card, fieldbus module, or encoder card changes the drive's hardware topology; the stored configuration no longer matches.
- **Firmware update/downgrade** — Updating or rolling back firmware can introduce configuration incompatibilities if the parameter database structure changed.
- **Corrupted parameter memory** — Power loss during a parameter save or write operation can corrupt the drive's EEPROM parameter storage.

## Step-by-Step Fix {#fix}

1. **Record the fault in the drive menu** — Use the keypad or SoMove software to view the active fault. Confirm CFF is the active fault and check whether any sub-fault code is displayed.
2. **Perform a factory reset** — The most reliable fix: navigate to the Factory Settings menu and restore the drive to factory defaults. This clears all parameter conflicts. Note: you must reprogram the drive after a factory reset.
   - Altivar 31/61/71: Go to `[Full]` menu → `[FCS]` → Set to `[InI]` → Confirm.
   - Altivar 12: Hold Mode + Down buttons simultaneously on startup.
3. **Reconfigure drive parameters** — After the factory reset, re-enter all application parameters: motor nameplate data (voltage, current, frequency, speed), acceleration/deceleration ramps, I/O assignments, and protection settings.
4. **Check option cards** — If the CFF appeared after installing or removing a card, reseat the card firmly. If replacing the card type, a factory reset followed by full reconfiguration is required.
5. **Update SoMove/firmware** — If using SoMove, ensure the SoMove version supports the drive's firmware version. Download the latest configuration file template for your drive model.
6. **Save and test** — After reconfiguration, save parameters to the drive (and optionally back up to a laptop via SoMove). Run the drive at low speed first to confirm normal operation.

## Parts Often Needed

| Part | Notes |
|------|-------|
| No hardware typically needed | [Amazon](https://www.amazon.com/s?k=No+hardware+typically+needed&tag=errorcodefixes-20) \| CFF is almost always a configuration/software issue |
| Option card | [Amazon](https://www.amazon.com/s?k=Option+card&tag=errorcodefixes-20) \| Only if the installed card is damaged or wrong type |
## When to Call a Pro

If CFF persists after a factory reset, the drive's internal parameter EEPROM may be corrupted. Schneider Electric's repair centers can reflash the drive firmware and restore the parameter memory. Contact Schneider service if factory reset doesn't resolve the fault.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
