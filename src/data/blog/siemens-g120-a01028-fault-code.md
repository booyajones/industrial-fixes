---
title: "Siemens G120 A01028 - Causes & Fix"
description: "Siemens G120 A01028 is a configuration error alarm caused by parameter and hardware mismatch. Learn causes, diagnostic steps, and parts."
pubDatetime: 2026-05-27T10:42:12Z
modDatetime: 2026-05-27T10:42:12Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Control Unit (CU)"
most_likely_cause: "Wrong device type selected in TIA Portal or Startdrive"
---

## What this code means
The A01028 alarm on a Siemens SINAMICS G120 is a configuration error, not a hardware trip fault. Siemens describes it as a parameterization mismatch where the downloaded settings were generated for a different module type or order number (MLFB) than the one physically installed in the drive. The alarm text reads: "The loaded settings are not compatible with the inverter." This means the drive's actual hardware does not match the stored configuration, typically because the wrong device type was selected in the project or parameters were restored from another drive with a different MLFB. The alarm does not indicate a direct hardware failure but rather a commissioning or configuration error that prevents the drive from accepting the parameter set.

## Common Causes

- **Wrong device type selected in TIA Portal or Startdrive** The project was configured for a different G120 hardware variant than the one physically installed, so the downloaded parameter set does not match the actual drive model.
- **Control Unit and Power Module mismatch** The Control Unit or Power Module was replaced without updating the commissioning data, or the stored configuration references hardware that is no longer present.
- **Parameters restored from a different drive** A parameter backup from another G120 with a different MLFB or order number was downloaded to this drive, creating an incompatibility between the stored settings and the installed hardware.
- **Firmware or data compatibility issue** The drive firmware was updated or hardware was changed without revalidating the configuration, resulting in a mismatch between the parameter set and the current hardware state.
- **Non-volatile parameter save failed or corrupted** The drive's stored configuration became corrupted or was not saved correctly after the last commissioning, causing the alarm to appear on startup.

## Step-by-Step Fix {#fix}

1. **Verify the exact drive nameplate and MLFB numbers** on both the Control Unit and Power Module, then compare them to the hardware configuration in your TIA Portal or Startdrive project to confirm they match.
2. **Check the drive's alarm buffer and diagnostics** to confirm A01028 is the active issue and that no separate hardware faults are present that could complicate troubleshooting.
3. **Correct the project hardware configuration** in TIA Portal or Startdrive to match the installed drive hardware, then download the corrected parameter set to the drive.
4. **Save parameters non-volatilely** by setting parameter p0971 to 1, which Siemens specifically recommends to clear the alarm after correcting the mismatch.
5. **Power cycle the drive** by switching off mains power, waiting 30 seconds, and powering back on to allow the drive to reload the corrected configuration.
6. **Re-commission the drive** if the alarm returns after correction, following Siemens' recommended startup procedure for your specific G120 model rather than forcing the old parameter set.
7. **Replace the Control Unit or inverter** only if the alarm persists after verifying correct hardware configuration and re-commissioning, as this indicates a hardware issue preventing parameter acceptance.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a01028-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Match the exact MLFB to your Power Module. Replace if re-commissioning does not clear the alarm after correct configuration. |
| Siemens G120 Power Module (PM) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-a01028-fault-code&k=Siemens+G120+Power+Module+%28PM%29&tag=errorcodefixes-20) \| Verify the MLFB matches your Control Unit and project configuration. Required if the installed module type is incompatible with your system. |

## When to Call a Pro

Call a qualified technician or Siemens service partner if you do not have access to TIA Portal or Startdrive to verify and correct the hardware configuration in your project. Also reach out if the alarm persists after you have confirmed matching MLFB numbers, re-commissioned the drive, and power cycled it. Configuration errors can sometimes mask deeper issues with Control Unit memory or firmware compatibility that require specialized diagnostic tools and factory support. If you are unsure how to safely power down the drive or lack training on Siemens parameter management, professional assistance will prevent accidental data loss or further configuration problems.
