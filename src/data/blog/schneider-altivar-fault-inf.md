---
title: "Schneider Altivar Fault INF — Causes & Fix"
description: "What Schneider Altivar VFD fault code INF means, why an internal fault occurs, and how to recover the drive."
pubDatetime: 2026-04-22T11:00:00Z
modDatetime: 2026-04-22T11:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - schneider
---

## Schneider Altivar Fault INF — What It Means

INF on a Schneider Electric Altivar drive (ATV312, ATV320, ATV630, ATV930 series) indicates an internal fault. The drive's self-diagnostic system detected an internal error that it cannot attribute to an external cause — this may be a memory error, a communication fault between internal boards, or a hardware failure in the power or control stage. The drive stops and locks out. INF is a serious fault that typically requires more than a simple reset to resolve.

[Jump to Fix](#fix)

## Common Causes

- **EEPROM or memory error** — Corrupted internal memory from a power interruption during a write operation or from EEPROM end-of-life.
- **Communication error between control and power cards** — On larger Altivar drives with separate control and power boards, a failure in the inter-board communication bus triggers INF.
- **Power supply fault within the drive** — An internal switched-mode power supply feeding the control electronics has failed or is producing out-of-spec voltage.
- **Firmware fault or version mismatch** — A firmware update that did not complete correctly, or a control card that does not match the firmware version expected by the drive.

## Step-by-Step Fix {#fix}

1. **Power cycle the drive completely** — Remove input power for at least 2 minutes (allow DC bus to fully discharge) and restore. Some INF faults caused by transient memory errors will clear on a full power cycle.
2. **Attempt a factory reset** — Access the drive menu and navigate to the Reset to factory defaults option (typically under Settings or Factory Reset). This re-initializes EEPROM. Note: this will clear all parameter changes; record parameters first if possible.
3. **Check the fault history** — Review the fault history log on the keypad. If INF appears alongside other faults (UV, OHF), the root cause may be power supply related.
4. **Inspect internal connections** — On larger Altivar models, open the drive cover and check the ribbon cable and harness connections between the control card and power stage. Re-seat any loose connectors.
5. **Check the 24V internal power supply** — On drives with accessible test points, verify the internal 24V DC supply is within specification. An out-of-spec supply will cause control card resets and INF faults.
6. **Update or reinstall firmware** — If the fault is firmware-related, use the Altivar DTM or SoMove software to reflash the drive firmware to the correct version.
7. **Replace the control card** — If the above steps do not clear INF, the control board has a hardware fault and must be replaced.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Altivar control card / board | [Amazon](https://www.amazon.com/s?k=Altivar+control+card+%2F+board&tag=errorcodefixes-20) \| Order by drive model and firmware version |
| Internal power supply board | [Amazon](https://www.amazon.com/s?k=Internal+power+supply+board&tag=errorcodefixes-20) \| Replace if 24V supply is confirmed out of specification |
| Communication ribbon cable | [Amazon](https://www.amazon.com/s?k=Communication+ribbon+cable&tag=errorcodefixes-20) \| Replace if damaged between control and power cards |
## When to Call a Pro

INF is rarely field-repairable beyond a factory reset. If power cycling and parameter initialization do not clear the fault, contact a Schneider Electric-authorized drive service center for control card replacement and firmware verification.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)
