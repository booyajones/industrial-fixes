---
title: "Yaskawa GA800 A.112 Alarm - Causes & Fix"
description: "A.112 on a Yaskawa GA800 is an alarm for missing or invalid run/reference input. Most often the command source is set wrong on the keypad."
pubDatetime: 2026-06-08T11:05:21Z
modDatetime: 2026-06-08T11:05:21Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Wrong run-command or speed-reference source selected in the drive parameters"
likelihood: "the most common cause"
diy_or_pro: "pro"
money_part: "External speed reference device or potentiometer"
---

## Yaskawa GA800 A.112 Alarm — What It Means

The A.112 code on the Yaskawa GA800 is an alarm condition, not a hard fault that shuts down the drive completely. It means the drive is not receiving a valid run command or speed reference from the source you have selected in the parameters. The GA800 separates alarms from faults, and alarms display on the keypad as warnings that something in the control path is not configured or wired correctly.

In practical terms, the motor will not respond because the drive does not see the input signal it expects. The alarm typically appears when the command source (keypad, terminals, or network) does not match the wiring, when the reference signal lands on the wrong terminal for the type selected, or when a DIP switch on the control board does not match the configuration. Fixing it requires verifying that the source selection, wiring, and board settings all agree.

## Before You Replace Anything

Technicians sometimes replace the control board or analog input card when the real issue is simply a parameter mismatch or a wire landed on A1 instead of A2. Always verify the command-source parameters and terminal wiring against the connection diagram before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Wrong speed-reference source selected (~35%)** The drive parameter for frequency reference (keypad, analog voltage, analog current, or network) does not match the actual source feeding the signal.
- **Wrong run-command source selected (~30%)** The drive parameter for run command (keypad, digital input terminals, or network) does not match the device sending the start signal.
- **Reference wiring on wrong terminals (~15%)** A voltage reference signal is landed on A2 instead of A1, or a current reference is on A1 instead of A2, or the common wire is missing from AC.
- **DIP switch mismatch on control board (~10%)** The control board DIP switches do not match the analog input type (voltage or current) configured in the parameters.
- **Open or loose control wiring (~7%)** A wire in the analog reference circuit or run-command circuit is disconnected, broken, or making intermittent contact at a terminal.
- **Configuration not reinitialized after setup change (~3%)** After a factory reset or parameter change, the drive was not stepped through the initial setup wizard to match the new wiring.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the motor run when you press the RUN key on the keypad?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive itself is working and the problem is in the external command or reference wiring. Check which source is selected in the parameters and verify the terminal connections for that source.<br><strong>No:</strong> The drive may be set to expect a run command from terminals or network instead of the keypad. Check the run-command source parameter and switch it to keypad to test.</div>
</details>

<details class="dtree"><summary>Is the reference signal a 0–10 V analog voltage?</summary>
<div class="dtree-body"><strong>Yes:</strong> The signal wire must land on terminal A1 and the common on AC. Verify the drive parameter for frequency reference is set to analog voltage input.<br><strong>No:</strong> If it is a 4–20 mA current signal, the wire must land on A2 and common on AC, and the parameter must be set to analog current. Check the DIP switches on the control board to match.</div>
</details>

<details class="dtree"><summary>Have you recently changed parameters or reset the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Run the initial setup wizard from the keypad menu to reinitialize the configuration and confirm the command and reference sources match your wiring.<br><strong>No:</strong> Verify the control board DIP switches match the analog input type, then inspect every terminal connection in the reference and run-command circuit for loose or mislanded wires.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Read the keypad carefully** and confirm the displayed code is A.112 and that it is shown as an alarm, not a fault. Alarms on the GA800 warn of a setup or wiring issue without fully shutting down the drive.
2. **Check the command source parameter** in the drive menu. If the motor should start from the keypad, set the run-command source to keypad and press RUN to test. If it should start from terminals, verify which digital input is configured for the run command.
3. **Check the frequency-reference source parameter** and confirm it matches your wiring. If you are sending 0–10 V, the parameter must be set to analog voltage input. If you are sending 4–20 mA, it must be set to analog current input.
4. **Verify the reference wiring against the terminal diagram** in the GA800 manual. For voltage reference, the signal wire lands on A1 and common on AC. For current reference, the signal wire lands on A2 and common on AC.
5. **Inspect the DIP switches on the control board** inside the drive. Consult your model's manual for the correct switch positions for voltage or current analog input, and set them to match the parameter configuration.
6. **Test the motor again** after each correction. Press RUN on the keypad if that is your selected source, or apply the run command from your external control if terminals or network are selected.
7. **If the alarm persists**, run the initial setup wizard from the keypad menu to reinitialize the drive configuration. Step through each screen and confirm the command and reference selections match your actual wiring and application.
8. **If still unresolved**, record the drive model number, serial number, displayed alarm code, and a description of your control wiring. Contact Yaskawa technical support or your distributor with this information for application-specific troubleshooting.

## Parts Often Needed

| Part | Notes |
|------|-------|
| External speed reference device or potentiometer | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-112-fault-code&k=External+speed+reference+device+or+potentiometer&tag=errorcodefixes-20) \| If the analog voltage or current source feeding A1 or A2 is faulty or does not match the drive's input range. |
| Control terminal wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-a-112-fault-code&k=Control+terminal+wiring+harness&tag=errorcodefixes-20) \| Repair or replace damaged or mislanded wiring between the external control devices and terminals A1, A2, AC, and the run-command inputs. |

## When to Call a Pro

Call a qualified industrial electrician or drive technician if you are not familiar with VFD parameter programming, control wiring, or the use of a multimeter to measure analog signals. The GA800 requires careful matching of parameters, terminal wiring, and control board settings, and incorrect configuration can prevent the motor from running or cause unsafe operation. A technician will verify the command and reference sources, check the wiring against the connection diagram, confirm the DIP switch settings, and test the analog input circuit with proper instrumentation. If the drive or control board is damaged, the technician can also coordinate replacement parts and programming with Yaskawa or an authorized distributor.

**Rough cost:** A pro service call runs about $150–400.
