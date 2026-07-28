---
title: "Siemens G120 F01600 - Causes & Fix"
description: "Siemens G120 F01600 means Safety Integrated STOP A initiated. Learn the real causes, diagnostic steps, and parts for this safety fault."
pubDatetime: 2026-05-27T10:48:07Z
modDatetime: 2026-05-27T10:48:07Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Safety relay or STO interface module"
most_likely_cause: "Forced checking procedure of the safety shutdown path unsuccessful"
---

## What this code means
F01600 on a Siemens SINAMICS G120 means the drive's Safety Integrated function has initiated STOP A. This is a safety-related stop event triggered by the safety processor, not a generic power-stage or motor fault. The drive detects a condition in the safety chain and commands a safe stop to protect personnel and equipment.

This fault is part of the Safety Integrated architecture and points to a problem in the safe-stop logic, monitoring channels, or safety input wiring. It is not caused by typical motor overload, encoder failure, or power module issues. The fault value stored in parameter r0949 tells you which specific safety condition triggered the stop.

## Common Causes

- **Forced checking procedure of the safety shutdown path unsuccessful** The drive's internal test of the safety shutdown path failed, preventing the safety logic from confirming the STO circuit works correctly.
- **Monitoring channel defect (F01611 present or recent)** A fault in one of the safety monitoring channels triggers STOP A as a subsequent protective response.
- **Stop request from processor 2** The safety processor issued a stop command due to an internal logic condition or external safety input state.
- **Pulses suppressed although STO not selected and no internal STOP A present** The drive detected pulse suppression without a valid STO signal or internal stop command, indicating a configuration or wiring error.
- **STO or safety input wiring open or miswired** The Safe Torque Off circuit or safety relay contacts are not closed or are incorrectly connected, breaking the safety chain.
- **Upstream safety controller or interlock device commanding stop** An external safety PLC, safety relay, or emergency stop circuit is sending a stop signal to the drive's safety inputs.

## Step-by-Step Fix {#fix}

1. {'lead': 'Read the fault value in parameter r0949', 'text': 'and record it to identify the specific trigger path for the STOP A event.'}
2. {'lead': 'If r0949 equals 0', 'text': ', investigate the stop request from processor 2 by checking the safety logic configuration and any external safety controller signals.'}
3. {'lead': 'If r0949 equals 1005', 'text': ', select Safe Torque Off (close the STO circuit) and then de-select it (open and re-close) to reset the safety path.'}
4. {'lead': 'If r0949 equals 9999', 'text': ', perform diagnostics for fault F01611 by checking the safety monitoring channels and their wiring for defects or failures.'}
5. {'lead': 'Inspect the STO input terminals and safety relay contacts', 'text': 'for loose connections, open circuits, or incorrect wiring, and verify continuity through the entire safety chain.'}
6. {'lead': 'Check any upstream safety devices', 'text': 'such as emergency stop buttons, safety interlocks, or safety PLCs to confirm they are not commanding a stop.'}
7. {'lead': 'Clear the fault and re-enable the drive', 'text': 'only after you have verified and corrected the safety condition, then test the safety circuit function before returning to normal operation.'}

## Parts Often Needed

| Part | Notes |
|------|-------|
| Safety relay or STO interface module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01600-fault-code&k=Safety+relay+or+STO+interface+module&tag=errorcodefixes-20) \| If the existing safety relay or STO wiring interface is defective or miswired, replace or repair according to your system's safety circuit design. |
| Control Unit (CU) with Safety Integrated | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01600-fault-code&k=Control+Unit+%28CU%29+with+Safety+Integrated&tag=errorcodefixes-20) \| If diagnostics confirm a failed safety processor or monitoring channel inside the CU, consult Siemens service for Control Unit replacement or repair. |

## When to Call a Pro

Call a qualified technician or Siemens service if you cannot identify the fault value in r0949, if F01611 reappears after clearing, or if you are unfamiliar with Safety Integrated commissioning and diagnostics. Safety-related faults require knowledge of functional safety standards and the specific safety configuration of your system. Do not bypass or disable safety functions to clear this fault. If the safety chain is complex or involves a safety PLC or third-party safety controller, bring in a controls specialist to trace the stop signal and verify compliance with your safety design.
