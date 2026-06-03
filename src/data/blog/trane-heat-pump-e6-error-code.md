---
title: "Trane E6 Error Code - Causes & Fix"
description: "E6 means phase reversal or phase loss at power-up. Check incoming power phasing, then inspect 1T2 and 1T12 transformer wiring."
pubDatetime: 2026-05-31T14:52:25Z
modDatetime: 2026-05-31T14:52:25Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - hvac
  - mini-split
  - trane
---

## Trane E6 Error Code — What It Means

The E6 error on Trane heat pumps with UCM control boards indicates a phase reversal or phase loss fault detected during the first two seconds of power-up. The UCM controller is sensing incorrect phase sequence or missing voltage on the incoming low-voltage supply, which prevents safe operation. This is not a communication error. It is a power supply integrity check that protects the compressor and electronics from damage due to incorrect electrical phasing or unstable power at startup.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect phase sequence on incoming supply** The three-phase power legs are connected in the wrong order, causing the UCM to detect reversed rotation potential.
- **Phase loss or open leg during startup** One of the power supply phases is missing or intermittent at the moment the UCM powers up and runs its diagnostic.
- **Transformer 1T2 wiring or polarity error** The 1T2 transformer leads are reversed or miswired, causing the low-voltage signal to the UCM to read as incorrect phasing.
- **Transformer 1T12 wiring or polarity error** The 1T12 transformer connections are wrong, sending a phase-reversed or incomplete signal to the control board.
- **Low-voltage power problem to the UCM** Voltage sag, loose connections, or insufficient supply during startup prevent the UCM from correctly sensing phase sequence.
- **UCM software revision mismatch or fault handling difference** Older revision D boards may allow the unit to run while flashing E6, while revision E requires a full power disconnect to reset.

## Step-by-Step Fix {#fix}

1. **Confirm the E6 code** appears at startup on a Trane heat pump with a UCM control board and note the UCM revision letter (D or E) if visible.
2. **Perform the Power Supply Checkout Procedure** in your unit's service manual to verify correct incoming line voltage, phase sequence, and that no phase is open or missing.
3. **Inspect transformer 1T2 wiring** and verify polarity matches the wiring diagram on the unit label, correcting any reversed leads or loose connections.
4. **Inspect transformer 1T12 wiring** and verify polarity and connections match the factory diagram, correcting any errors.
5. **Remove all power** to the unit by opening the disconnect or breaker for at least 30 seconds to clear the fault lockout (required for revision E UCMs).
6. **Restore power** and observe startup. If E6 reappears, recheck phase sequence at the main supply with a phase rotation meter.
7. **Disable the diagnostic** (only if authorized and on revision E boards) by setting switch SW3-5 to ON if a persistent nuisance fault is confirmed and approved by engineering or the customer.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Trane UCM control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-heat-pump-e6-error-code&k=Trane+UCM+control+board&tag=errorcodefixes-20) \| Replacement if board fails to clear E6 after wiring and power supply are verified correct. |
| 1T2 transformer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-heat-pump-e6-error-code&k=1T2+transformer&tag=errorcodefixes-20) \| Replacement if internal winding failure or short is found during testing. |
| 1T12 transformer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-trane-heat-pump-e6-error-code&k=1T12+transformer&tag=errorcodefixes-20) \| Replacement if polarity cannot be corrected or transformer shows signs of failure. |

## When to Call a Pro

Call a licensed HVAC technician if you see the E6 code. This fault involves three-phase power diagnostics, transformer polarity checks, and control board revision-specific reset procedures that require test equipment and electrical training. Incorrect work on phase wiring can damage the compressor, void warranties, or create safety hazards. A technician will use a phase rotation meter, follow the factory Power Supply Checkout Procedure, and determine whether the fault is in the supply, transformers, or the UCM itself.
