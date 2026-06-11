---
title: "Yaskawa GA800 E22 Fault Code - Causes & Fix"
description: "E22 is not a standard Yaskawa GA800 fault code. Learn how to verify the actual code, reset the drive, and contact support with the right info."
pubDatetime: 2026-05-30T12:32:48Z
modDatetime: 2026-05-30T12:32:48Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "GA800 control board"
---

## Yaskawa GA800 E22 Fault Code — What It Means

E22 does not appear in Yaskawa's published GA800 fault code documentation. If your keypad displays E22, it may be a misread code, a custom alarm configured by the installer, or a code from a different Yaskawa drive family. The GA800 uses alphanumeric fault codes like E.xx or Fxx, and many involve option modules, communication boards, or encoder feedback issues. Before troubleshooting, confirm the exact code displayed on the keypad and check your model's full fault list in the manual.

Because this code is not standard, you cannot safely assume its cause without verifying the display and consulting Yaskawa technical support. The drive may still require a reset after clearing the underlying condition, but identifying the true fault is the first step.

[Jump to Fix](#fix)

## Common Causes

- **Misread or transposed fault code** The actual code may be E.22, 22, F22, or a similar alphanumeric combination not matching E22.
- **Custom alarm programmed by integrator** Some installers configure user-defined alarms that do not appear in Yaskawa's standard fault table.
- **Code from a different Yaskawa drive series** E22 may belong to a V1000, A1000, or other Yaskawa model installed nearby or documented in mixed manuals.
- **Display or keypad malfunction** A failing keypad or corrupted display can show incorrect fault codes that do not match the drive's internal log.

## Step-by-Step Fix {#fix}

1. **Write down the exact code** as it appears on the keypad, including all digits, letters, decimal points, and any accompanying text or symbols.
2. **Record your drive model and serial number** from the nameplate on the front or side of the unit, along with any option cards installed.
3. **Check the drive's parameter monitor** by navigating to the fault history menu (consult your keypad manual) to see if the internal log shows a different code.
4. **Compare the code** to the fault table in your GA800 manual or download the latest version from Yaskawa's website for your specific model.
5. **Attempt a fault reset** by pressing the RESET button on the keypad after removing power or clearing the condition if you identify a match.
6. **Contact Yaskawa technical support** with your model number, serial number, the exact fault code, a description of when it occurs, your application type, and how long the drive has been in service.
7. **Inspect option modules and control boards** if support confirms the code relates to feedback or communication hardware, and replace only the components they specify.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e22-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Only if Yaskawa support confirms board-level failure and provides the exact part number for your model. |
| GA800 cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e22-fault-code&k=GA800+cooling+fan&tag=errorcodefixes-20) \| User-replaceable component covered in the maintenance manual if overheating is suspected. |

## When to Call a Pro

Call a qualified drive technician or contact Yaskawa technical support immediately if you cannot find E22 in your manual, if the code reappears after reset, or if the drive will not clear the fault. The GA800 maintenance documentation explicitly states that repairs beyond fan and control board replacement are outside the scope of field service. Do not attempt to modify parameters, swap boards, or bypass interlocks without manufacturer guidance, as this can damage the drive or create unsafe motor operation.

## See Also

- [Yaskawa V1000 Complete Fault Code Guide — All Faults and Fixes](/posts/yaskawa-v1000-complete-guide/)
- [Yaskawa GA800 E16 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e16-fault-code/)
- [Yaskawa GA800 E17 Fault - Causes & Fix](/posts/yaskawa-ga800-e17-fault-code/)
- [Yaskawa GA800 E11 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e11-fault-code/)
