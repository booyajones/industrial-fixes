---
title: "Fanuc Alarm 1 Overtravel — Causes & Fix"
description: "What Fanuc alarm 1 overtravel minus means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - fanuc
money_part: "Hardware overtravel limit switch"
---

## Fanuc Alarm 1 Overtravel — What It Means

Fanuc alarm 1 (OT0001: OVER TRAVEL: -X, or the corresponding axis) is a hardware overtravel alarm indicating that an axis has physically hit the minus-direction hardware overtravel limit switch. This is a positive limit detection — an actual mechanical switch mounted at the end of the axis travel has opened, telling the CNC that the axis has exceeded the physical travel boundary in the negative direction. The CNC removes servo power from the axis and requires an operator reset with the axis jogged away from the limit switch before normal operation can resume.

[Jump to Fix](#fix)

## Common Causes

- **Axis jogged or commanded past machine travel limits** — An operator jogged the axis in the minus direction without watching position, or a part program commanded a position outside the machine's soft and hard travel limits.
- **Incorrect work offset or fixture offset** — A G54–G59 work coordinate offset combined with a tool path puts the commanded position outside the physical travel range, driving the axis into the hardware limit.
- **Soft limits not configured** — If the CNC's software travel limits (parameters 1320/1321 on Fanuc 0i/18i series) are not set, the machine has no software barrier before the hardware overtravel switch, making it easier to hit the physical limit.
- **Overtravel switch mechanical fault** — The limit switch bracket is loose, the switch was moved, or the switch contacts are damaged and producing a false overtravel signal at mid-travel.

## Step-by-Step Fix {#fix}

1. **Enter the overtravel release mode** — On Fanuc CNC, hold the OT RELEASE key (or the machine-specific equivalent) while switching to JOG mode. The alarm must be in reset state (MDI key switch to appropriate position depending on machine builder).
2. **Jog the axis in the positive direction** — While holding the OT release button, jog the affected axis in the + direction (away from the minus hardware limit). Move until the switch is no longer actuated — typically a few millimeters to a few centimeters.
3. **Release the OT release key and clear the alarm** — Once the axis is clear of the switch, release the OT key, press RESET to clear the alarm, and confirm the axis is back in the valid travel range.
4. **Check work offsets and tool length offsets** — Navigate to the offset page and review the G54–G59 work offsets and tool length offsets. Identify whether any combination of offsets plus commanded position drove the axis to the limit.
5. **Verify and set soft travel limits** — In the parameter screen (PWE=1 required), check parameters 1320 and 1321 for each axis. Set the soft limits to leave a safe margin (typically 5–10mm) before the hardware overtravel switch.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Hardware overtravel limit switch | [Amazon](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-fanuc-alarm-1-overtravel&tag=errorcodefixes-20) \| Replace if switch is damaged or producing false signals |
| Switch mounting bracket | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-fanuc-alarm-1-overtravel&k=Switch+mounting+bracket&tag=errorcodefixes-20) \| Replace if bracket is bent and mis-positioning the switch |
## When to Call a Pro

If the axis hits the overtravel switch during normal operation with correct offsets and the soft limits are set, the servo system may be following position errors that exceed the tolerance — a servo gain or mechanical problem requiring a Fanuc service engineer to diagnose.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
- [Fanuc Alarm 3 — Overtravel Minus Hardware Causes & Fix](/posts/fanuc-alarm-3-overtravel/)

## See Also

- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 401 — Servo Axis Overload Fix](/posts/fanuc-alarm-401/)
- [Fanuc Alarm 430 — Servo Motor Overheat Fix](/posts/fanuc-alarm-430/)
- [Fanuc Alarm 500 — Causes & Fix](/posts/fanuc-alarm-500/)
