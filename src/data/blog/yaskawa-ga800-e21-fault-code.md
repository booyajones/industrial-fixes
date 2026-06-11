---
title: "Yaskawa GA800 E21 Fault - Causes & Fix"
description: "E21 on the Yaskawa GA800 signals a Z pulse correction error in the encoder feedback loop. Fix wiring, encoder, or feedback circuit issues."
pubDatetime: 2026-05-30T12:32:17Z
modDatetime: 2026-05-30T12:32:17Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Encoder feedback cable"
---

## Yaskawa GA800 E21 Fault — What It Means

The E21 fault on a Yaskawa GA800 drive indicates a Z pulse correction error. The drive is not receiving a valid encoder Z-index pulse that aligns with the expected motor position feedback. This means the feedback system cannot correctly synchronize the encoder's index pulse with the drive's internal position reference.

This is not a motor overload or input power problem. It is a signal integrity issue specific to the encoder feedback circuit. The drive detects that the Z pulse relationship is incorrect or missing, which prevents proper closed-loop position or speed control.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect motor wiring** Power leads to the motor are miswired, swapped, or loosely terminated at the drive or motor junction box.
- **Incorrect encoder wiring** Encoder signal wires are connected to the wrong terminals, reversed polarity, or not seated fully in the drive's feedback connector.
- **Damaged encoder cable** The encoder cable has internal breaks, shield damage, or contamination that corrupts the Z pulse signal before it reaches the drive.
- **Faulty encoder** The motor's encoder has internal wear, dirt on the code disk, or electronic failure that prevents it from generating a clean Z pulse.
- **Drive feedback circuit fault** The encoder input circuit on the drive control board has failed and cannot process the Z pulse even when wiring and encoder are correct.

## Step-by-Step Fix {#fix}

1. Verify the fault code and drive model by reading the keypad display and checking the nameplate to confirm you have a GA800 and that E21 is the active alarm.
2. Inspect motor power wiring at both the drive output terminals and motor connection box, checking for correct phase sequence, tight connections, and no visible damage or burns.
3. Inspect encoder cable and connections at the motor encoder connector and drive feedback input, ensuring pins are straight, fully inserted, cable shield is intact, and no oil or moisture is present.
4. Compare all wiring to the GA800 installation manual wiring diagram for your specific encoder type and motor feedback configuration, correcting any discrepancies in terminal assignment or shield grounding.
5. Isolate the fault source by swapping the encoder cable with a known-good spare if available, or temporarily connecting a different motor and encoder assembly to see if the E21 fault follows the hardware or stays with the drive.
6. Test the encoder signal integrity by checking the A, B, and Z pulse outputs with an oscilloscope if you have access, looking for clean square waves and a single Z pulse per motor revolution (consult your encoder datasheet for expected voltage levels).
7. Contact Yaskawa technical support with the drive serial number, exact model code, application details, and results of your wiring and isolation checks if the fault persists after confirming wiring and trying a cable swap.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Encoder feedback cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e21-fault-code&k=Encoder+feedback+cable&tag=errorcodefixes-20) \| Match the connector type and length to your motor encoder and drive model. |
| Motor encoder assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e21-fault-code&k=Motor+encoder+assembly&tag=errorcodefixes-20) \| Order by motor model and encoder resolution, usually factory-matched to the original motor. |
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-e21-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Field-replaceable part for drive feedback circuit failures, contact Yaskawa for the exact board revision for your drive serial number. |

## When to Call a Pro

Call a qualified drive technician or Yaskawa service partner if the E21 fault remains after you have verified all wiring, tried a known-good encoder cable, and ruled out obvious mechanical or connection problems. Encoder signal troubleshooting with an oscilloscope and control board replacement both require experience with feedback systems and electrostatic-safe handling. If your application is mission-critical or you do not have a spare encoder or cable to isolate the fault, bring in a pro before you risk damaging good components with trial-and-error swaps.

## See Also

- [Yaskawa GA800 E26 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e26-fault-code/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA800 E09 Fault - Causes & Fix](/posts/yaskawa-ga800-e09-fault-code/)
- [Yaskawa GA800 E22 Fault Code - Causes & Fix](/posts/yaskawa-ga800-e22-fault-code/)
