---
title: "Yaskawa GA800 E13 Error - Causes & Fix"
description: "E13 on a Yaskawa GA800 VFD is a parameter configuration error. Check recent parameter changes and restore valid settings to clear the code."
pubDatetime: 2026-06-05T09:50:42Z
modDatetime: 2026-06-05T09:50:42Z
author: "James Rutherford"
featured: false
draft: true
tags:
  - vfd
  - yaskawa
---

## Yaskawa GA800 E13 Error — What It Means

E13 on the Yaskawa GA800 variable frequency drive is not a hardware fault code. It is a parameter-related error that points to an invalid or unsupported setting in the drive's configuration. The exact meaning can vary depending on installed option cards and control setup, so check the drive's display text and consult the GA800 technical manual for your specific model.

This error typically appears after commissioning, parameter changes, or initialization work when a parameter value falls outside the allowed range or conflicts with the current control mode. The drive will not run until the configuration issue is corrected and the error is cleared by a power cycle or reinitialization.

[Jump to Fix](#fix)

## Common Causes

- **Parameter value out of range** A recently changed parameter was set to a value not permitted by the GA800 for the current drive rating or configuration.
- **Incorrect control mode or I/O setup** The terminal assignment or control method selected conflicts with other drive settings or hardware wiring.
- **Mismatched option card or network configuration** Communications or safety option board settings do not match the installed hardware or network type.
- **Incomplete initialization after major change** The drive was not properly reinitialized after changing fundamental setup items, leaving it in an invalid state.

## Step-by-Step Fix {#fix}

1. Read the full error message from the keypad or operator display and write down the text and any associated parameter numbers shown.
2. Review recent parameter changes in the drive and compare each value against the allowable range listed in the GA800 parameter table for your drive model and capacity.
3. Check control method, terminal assignment, and option-card DIP-switch or parameter settings if the error appeared after commissioning, wiring work, or option installation.
4. Correct any out-of-range or conflicting parameter by navigating to that parameter number on the keypad and entering a valid value from the manual.
5. Power cycle the drive by turning off the control power supply or AC input breaker, waiting 30 seconds, then restoring power to confirm the error clears.
6. If the error persists with all parameters confirmed correct, perform a factory reset using parameter A1-03 (only if the application allows loss of custom settings), then re-enter your basic setup values.
7. Inspect and reseat any option cards or control-board connectors if the error returns after all settings are verified, and contact Yaskawa support if the problem continues.

## Parts Often Needed

| Part | Notes |
|------|-------|
| GA800 option card (communications, I/O, or safety) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e13-fault-code&k=GA800+option+card+%28communications%2C+I%2FO%2C+or+safety%29&tag=errorcodefixes-20) \| Only if the error is traced to a failed or unseated expansion module. |
| GA800 control board assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e13-fault-code&k=GA800+control+board+assembly&tag=errorcodefixes-20) \| Required only if repeated non-configuration errors occur after all settings are corrected and option cards are verified. |

## When to Call a Pro

Call a qualified Yaskawa technician or controls integrator if you cannot identify which parameter is triggering E13, if the error returns immediately after correction and power cycle, or if the drive was recently installed and you are unfamiliar with VFD commissioning procedures. Also contact Yaskawa technical support if the error appears alongside other fault codes or if the keypad becomes unresponsive, since control-board or option-card hardware failure may require factory repair or replacement beyond typical field service scope.
