---
title: "Fanuc 0i-MD Alarm & Fault Codes: Full List + Fixes"
description: "Fanuc 0i-MD alarm and fault codes with meanings, causes, and first-step fixes for servo, spindle, overtravel, and overheat faults on your CNC control."
pubDatetime: 2026-04-22T23:00:00Z
modDatetime: 2026-04-22T23:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
  - industrial
money_part: "Encoder battery"
---

## Fanuc 0i-MD Alarm Codes — What They Mean

The Fanuc 0i-MD is a common machining center control used on vertical mills, horizontal machining centers, and compact CNC machines. Fanuc alarms are numeric and can come from the CNC, PMC, servo system, spindle drive, or ladder logic. The first job is to identify whether the alarm is a program issue, a motion issue, or a hardware issue.

[Jump to Fix](#fix)

## Fanuc 0i-MD Common Alarm Reference

| Alarm | Meaning |
|---|---|
| 000 | General reset / no alarm |
| 100 | Parameter error |
| 300 | Emergency stop |
| 401 | Servo alarm — VRDY off |
| 414 | Digital servo system alarm |
| 424 | Overtravel + direction |
| 430 | Stored stroke limit 1 |
| 500 | Overcurrent in servo amplifier |
| 700 | Spindle alarm |
| 750 | Serial pulse coder fault |
| 910 | SRAM parity error |

## Common Causes by Alarm

- **300 E-stop** — Physical E-stop pressed, broken E-stop chain, or door interlock open.
- **401 / 414 servo alarms** — Servo amplifier not ready, axis overload, encoder issue, or amplifier power supply fault.
- **424 overtravel** — Axis hit travel limit switch or parameterized soft limit.
- **500 servo overcurrent** — Axis jammed, ballscrew binding, or amplifier fault.
- **750 pulse coder** — Encoder cable loose, contaminated connector, or failed encoder battery causing reference loss.

## Step-by-Step Fix {#fix}

1. **Read the exact alarm screen** — Fanuc often gives additional text beyond the number.
2. **Check alarm source** — CNC screen, servo amplifier LEDs, and spindle amplifier LEDs should all be reviewed.
3. **For 300** — Verify all E-stop buttons, door switches, and safety relays are reset.
4. **For 424** — Jog off the limit if mechanically possible, then inspect the limit switch and home reference.
5. **For 750** — Check encoder battery voltage and cable seating before replacing hardware.

## Parts Often Needed

| Part | Notes |
|---|---|
| Encoder battery | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-0i-md-alarm-codes&k=Encoder+battery&tag=errorcodefixes-20) \| Common maintenance item on Fanuc controls |
| Pulse coder cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-0i-md-alarm-codes&k=Pulse+coder+cable&tag=errorcodefixes-20) \| Replace if oil-soaked or damaged |
| Limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-fanuc-0i-md-alarm-codes&tag=errorcodefixes-20) \| For repeated overtravel alarms |
| Servo amplifier | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-0i-md-alarm-codes&k=Servo+amplifier&tag=errorcodefixes-20) \| For persistent 401/500 alarms |
## When to Call a Pro

If the machine shows repeated 910 SRAM or persistent servo amplifier alarms after basic checks, back up parameters immediately and involve a Fanuc service technician or qualified CNC controls specialist.

## Related Articles

- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
- [Fanuc Alarm 3 — Overtravel Minus Hardware Causes & Fix](/posts/fanuc-alarm-3-overtravel/)

## See Also

- [Fanuc Alarm 460 — Spindle Overload](/posts/fanuc-alarm-460/)
- [Fanuc Alarm 500 — Causes & Fix](/posts/fanuc-alarm-500/)
- [Fanuc Alarm 430 — Servo Motor Overheat Fix](/posts/fanuc-alarm-430/)
- [Fanuc Alarm 506 — Servo Following Error Fix](/posts/fanuc-alarm-506/)

## More Fanuc 0I Md Alarm Codes fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| SV0410 | Excess error (stop) — positional deviation while the axis is stopped exceeded the parameter (No. 1829) limit. | Axis mechanically held or dragging, low servo gain, feedback fault, or amplifier not driving the motor while stopped. | Check the axis for mechanical binding and verify the servo amplifier is powered and ready. Confirm the motor holds position; inspect the feedback cable and the excess-error-at-stop parameter before adjusting gains. |
| SV0411 | Excess error (moving) — positional deviation during travel exceeded the parameter (No. 1828) limit. | Axis overload or binding, undersized acceleration, feedback fault, or an underpowered/failing servo amplifier. | Reduce load, check the ballscrew and ways for binding, and confirm the feedback cable is seated. If it recurs only at high feed or rapid, involve controls service before changing motion parameters. |
| SV0417 | Illegal digital servo parameter — a servo setup parameter is out of range or invalid. | Corrupted or wrong motor/servo parameters (motor type, direction, feedback pulse counts), often after a board or battery loss or a bad parameter restore. | Restore servo parameters from your known-good backup. Verify motor form and feedback-pulse parameters match the motor. Do not guess values; use the machine builder's parameter sheet. |
| SV0444 | Inverter/servo amplifier internal cooling fan failure — the amplifier's internal cooling fan has stopped or failed. | Clogged, worn, or seized amplifier cooling fan. | Power down and inspect the amplifier fan for dust and free rotation. Replace the amplifier cooling fan; do not run the drive with a dead fan. |
| SV0445 | Soft disconnection alarm — the digital servo software detected a pulse coder (encoder) disconnection. | Loose or contaminated feedback connector, damaged encoder cable, or encoder fault. | Check and reseat the pulse coder cable at both ends, clean the connector, and inspect for oil intrusion or damage before replacing the encoder. |
| SV0446 | Hard disconnection alarm — hardware detected a disconnected built-in pulse coder. | Broken feedback wiring, failed connector, or failed built-in encoder. | Inspect the encoder cable and connector for breaks. This is a hardware-level detection; if the cable is good, the pulse coder or its interface likely needs service. |
| SV0460 | FSSB disconnect — the fiber-optic serial servo bus (FSSB) lost communication. | FSSB optical fiber unplugged, dirty, or broken; amplifier powered down; or a low-voltage/interface fault. | Check that every servo amplifier on the FSSB line is powered. Reseat and clean the optical fiber connectors along the chain and inspect for kinked or broken fiber. |
| SV0466 | Motor / amplifier combination incorrect — the amplifier's maximum current does not match the motor. | Wrong amplifier fitted, wrong motor parameter set, or mismatched replacement part. | Confirm the amplifier and motor part numbers against the builder's spec and correct the servo parameters. Common after a substituted amplifier or motor. |
| OT0506 | + Over travel (hard) — the positive-direction hardware stroke-limit switch was triggered. | Axis ran into the plus-side limit switch, or a failed/miswired limit switch or dragging cam. | Jog the axis in the minus direction to clear the switch, then inspect the limit switch, wiring, and actuating cam for damage or contamination. |
| OT0507 | - Over travel (hard) — the negative-direction hardware stroke-limit switch was triggered. | Axis ran into the minus-side limit switch, or a failed/miswired limit switch. | Jog the axis in the plus direction to clear the switch, then inspect the limit switch and its wiring. |
| OH0701 | Overheat: fan motor — an abnormality (such as a stoppage) occurred in a control-unit/PCB cooling fan motor. | A control-cabinet/PCB cooling fan stopped or failed during CNC operation. | Power down and check each cooling fan for free rotation and dust buildup. Replace the failed fan motor and clear the cabinet air path. |
| SP1220 | No spindle amp — the serial spindle amplifier is missing or not communicating. | Spindle amplifier powered off, disconnected serial link, or failed amplifier. | Verify the spindle amplifier has power and its serial communication cable to the CNC is connected. Check the amplifier's status LEDs before suspecting the amplifier itself. |
| SP1225 | CRC error (serial spindle) — a communications error occurred on the serial spindle link between the CNC and the spindle amplifier. | Noise, a damaged or loose serial spindle cable, grounding problems, or a failing spindle amplifier. | Reseat and inspect the serial spindle cable, check shielding and grounding, and separate the cable from noise sources before replacing hardware. |
| PS0090 | Reference return incomplete — the zero-return (homing) operation could not be completed normally. | Return started too close to the reference point, speed too slow, grid/one-rotation signal not detected, or a feedback/encoder (or battery) issue. | Jog the axis well away from the reference position and re-run the zero return. If it still fails, check the encoder one-rotation signal and feedback cabling. |


## How to troubleshoot Fanuc 0I Md Alarm Codes

Work a Fanuc 0i-MD alarm from the letter prefix, not just the number. The prefix tells you which subsystem raised it: **PS** program/setting, **SV** servo, **SP** serial spindle, **OT** overtravel, **OH** overheat, **DS** diagnosis, **SR** serial communication. Read the full alarm screen first, since Fanuc appends an axis letter and message text that narrow the fault fast.

Triage in this order:

- **Note whether it clears on reset.** A PS/program or setting alarm that clears with RESET is usually a data or operator issue, not hardware. Servo, spindle, and overheat alarms that will not clear point at the machine side.
- **Look at the amplifiers, not just the screen.** Check the status LEDs and 7-segment displays on the servo and spindle amplifiers. They frequently show a sub-code that pinpoints the failing axis or the specific fault (overcurrent, low DC link, disconnection) more precisely than the CNC alarm alone.
- **Suspect feedback and cabling before parts.** A large share of SV disconnection, excess-error, and reference-return alarms trace to a loose or oil-soaked pulse-coder connector or a chafed cable in the drag chain. Reseat and inspect before condemning an encoder or amplifier.
- **Respect the backup battery.** Fanuc controls keep parameters and absolute position in battery-backed SRAM. A dead or disconnected backup battery causes memory/parity faults and lost reference position. Always back up parameters and the PMC ladder before you change a battery or a board so you can restore a known-good state.

Common failure modes on this control class: servo VRDY/ready faults from an amplifier that lost enable or power, overtravel from a tripped hardware limit switch, overheat from a stopped cabinet or amplifier cooling fan, and reference-return failures after a battery event.

Safety: many of these faults sit behind live 200-600 VDC bus voltages inside the amplifiers. De-energize and let the DC link discharge before opening any drive. Call a Fanuc-qualified controls technician when you see repeated SRAM/parity faults, persistent servo overcurrent or IPM alarms after basic checks, or any fault that requires editing servo/spindle parameters you do not have a backup for.


## Frequently asked questions

### What causes a 401 VRDY OFF servo alarm on a Fanuc 0i-MD?

401 means the servo amplifier's ready (VRDY) signal dropped when the CNC expected it on. Usual causes are an interruption in the E-stop/safety chain, the amplifier losing its enable or main power, a tripped breaker or MCC, or an amplifier fault. Check the E-stop chain and confirm the amplifier has bus power, then read its status LEDs before suspecting the CNC. A companion 701/OH overheat alarm can also drop the drives.

### My Fanuc 0i-MD lost home/reference position after sitting unused. Why?

That points at the encoder backup battery. Fanuc keeps absolute position in battery-backed memory, and a drained or disconnected battery causes reference loss and can trigger APC/pulse-coder alarms (for example a 300-series APC 'need zero return'). Replace the battery with the control powered on if your machine supports it, then re-establish the zero return. Back up parameters first.

### What does a 700 or 701 overheat alarm mean and can I keep running?

700 is cabinet/control-unit overheat and 701 is a PCB cooling-fan fault. Do not keep cutting through them, since heat causes unstable control behavior and shortens component life. Check that cabinet and amplifier fans spin freely, clear dust from filters and heat sinks, and confirm the cabinet door and any A/C or heat exchanger are working. Replace a stopped fan motor before resuming.

### I swapped a servo amplifier or motor and now get alarm 417 or 466. What now?

417 (illegal digital servo parameter) and 466 (motor/amplifier combination incorrect) both mean the servo setup no longer matches the hardware. Restore the servo parameters from your known-good backup and confirm the motor and amplifier part numbers against the machine builder's spec. Do not guess parameter values; use the builder's parameter sheet or Fanuc service.

