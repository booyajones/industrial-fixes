---
title: "Siemens G120 A01590 Fault Code - Causes & Fix"
description: "A01590 is not a standard Siemens G120 code. Learn how to read the actual fault buffer, troubleshoot unknown alarms, and clear errors."
pubDatetime: 2026-05-27T10:47:30Z
modDatetime: 2026-05-27T10:47:30Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens BOP-2 Basic Operator Panel"
most_likely_cause: "Misread or partial fault code"
---

## Siemens G120 A01590 Fault Code — What It Means

A01590 does not appear in published Siemens SINAMICS G120 fault and alarm code lists. Siemens uses five-digit codes like F01001 or A01251, and the A01590 identifier may be a transcription error, a code from another drive family, or an internal diagnostic value not listed in standard manuals. The G120 stores fault and alarm history in diagnostic buffers accessible through parameters r0945, r0947, and r0949. Reading these parameters directly from the drive will show the actual fault number and detailed cause.

If you see A01590 on your display or operator panel, verify the exact text and check whether the drive is a G120, G120C, G120D, or another SINAMICS model. Some codes are device-specific or firmware-version-specific. Siemens documentation instructs technicians to consult the diagnostic buffer and cross-reference the code in the drive's list manual rather than relying on partial or misread numbers.

[Jump to Fix](#fix)

## Common Causes

- **Misread or partial fault code** The display may show only part of a longer code, or the number was copied incorrectly during troubleshooting.
- **Code from a different Siemens drive family** A01590 may belong to a SINAMICS S120, SIMOVERT, or other product line that uses a different code structure.
- **Internal diagnostic value** Some parameter values are reserved for Siemens service use and do not appear in customer-facing fault lists.
- **Firmware or software mismatch** Outdated or mismatched firmware can generate unlisted codes or display errors that do not correspond to published tables.
- **Communication or display error** A corrupted BOP-2 or IOP panel readout can show garbled codes that do not exist in the drive's memory.

## Step-by-Step Fix {#fix}

1. Verify the exact code on the drive display or operator panel and write down the complete number, including any leading letters or decimal points.
2. Access parameter r0945 on the keypad or through STARTER software to read the fault buffer and confirm the actual stored fault or alarm number.
3. Cross-reference the code from r0945 in the Siemens G120 list manual for your firmware version, available on the Siemens support portal or supplied with your drive documentation.
4. Check the drive nameplate and model number to confirm you have a G120, G120C, G120D, or other variant, since fault codes differ between families.
5. Perform a POWER ON reset by switching off mains supply, waiting thirty seconds, then switching on again, if the manual indicates the code is clearable by reset.
6. Update drive firmware through STARTER software if the code does not appear in your current list manual and a newer firmware version is available.
7. Contact Siemens technical support with the r0947 and r0949 parameter values, drive serial number, and firmware version if the code remains unlisted or the fault persists after reset.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens BOP-2 Basic Operator Panel | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a01590-fault-code&k=Siemens+BOP-2+Basic+Operator+Panel&tag=errorcodefixes-20) \| Replacement keypad if display is corrupted or unreadable. |
| Siemens G120 Control Unit CU240 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a01590-fault-code&k=Siemens+G120+Control+Unit+CU240&tag=errorcodefixes-20) \| Match your drive frame size and firmware if the control unit is faulty or code persists after all other checks. |

## When to Call a Pro

Call a qualified technician or Siemens-certified service partner if you cannot locate the fault code in your drive's list manual after reading the diagnostic buffer, if the drive continues to trip after a POWER ON reset and all wiring checks are complete, or if Siemens support confirms the code requires internal diagnostics or hardware replacement. Professional help is also necessary if you lack STARTER software access, cannot update firmware safely, or if the drive is part of a networked system where incorrect troubleshooting may affect other machines.

## See Also

- [Siemens SINAMICS G120X Fault Codes: Complete Guide](/posts/siemens-g120x-fault-codes/)
- [Siemens VFD F0002 Fault - Overvoltage: What It Means and How to Fix It](/posts/siemens-vfd-f0002-fault/)
- [Siemens G120 F01040 - Causes & Fix](/posts/siemens-g120-f01040-fault-code/)
- [Siemens Cerberus/MXL Fire Alarm Fault Codes — Troubleshooting Guide](/posts/siemens-fire-alarm-fault-codes/)
