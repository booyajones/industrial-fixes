---
title: "Haas Alarm 120-129 — Automatic Tool Changer (ATC) Fault Fix Guide"
author: "Dana Kowalski"
pubDatetime: 2026-04-26T17:45:00Z
featured: false
draft: false
tags:
  - cnc
  - haas
  - machining
description: "Haas Alarm 120-129 ATC fault codes explained — what each ATC alarm means, how to safely recover, diagnose proximity switches and air pressure, and fix tool changer faults."
---

## Haas Alarm 120-129 — ATC Faults

The **120-series alarms** on Haas machining centers (VF-series, UMC, Mini-Mills, and EC horizontal centers) all indicate **Automatic Tool Changer (ATC) failures**. These alarms stop program execution immediately because an unresolved ATC fault — particularly one where the tool changer arm is mid-stroke — poses a crash risk to the spindle, workpiece, and machine structure. Among all CNC alarms, ATC faults cause the most unplanned downtime in production environments because they require careful manual recovery before the machine can resume operation.

Key alarms in this range include:

| Alarm | Description |
|-------|-------------|
| 120 | ATC fault — general (arm did not complete cycle) |
| 121 | Carousel fault — pocket position not confirmed |
| 122 | ATC arm not at home position |
| 123 | ATC arm fault — mid-stroke timeout |
| 124 | Tool not clamped |
| 125 | Carousel motion timeout |
| 126 | ATC motor overload |
| 127 | Tool in spindle not confirmed |
| 128 | Pocket not at spindle |
| 129 | ATC general fault |

[Jump to Fix](#fix)

## Common Causes

- **Proximity switch misalignment or failure** — The ATC arm and carousel positions are monitored by inductive proximity sensors. If a sensor shifts slightly (from vibration or a service bump) or fails, the control cannot confirm position and faults. This is the most common hardware cause of 120-series alarms.
- **Low air pressure** — Haas tool changers use pneumatic cylinders for the tool clamp/unclamp mechanism and (on some models) arm motion assist. Insufficient air pressure — below 85 PSI — prevents the cylinder from completing its stroke within the timeout period.
- **Tool obstruction or jam** — A tool that has slipped in its retention knob, a chip packed into a tool pocket, or a damaged tool holder that won't seat correctly can physically stop the carousel or arm mid-motion.
- **ATC drive motor or brake issue** — The ATC arm rotates via a dedicated gearmotor with an integral brake. A failed motor winding, seized bearing, or stuck brake prevents the arm from completing its rotation cycle.
- **Lubrication failure** — The ATC carousel and arm drive require periodic lubrication. Dry bearings and gears increase friction, causing motion timeouts that generate 120-series alarms.
- **Retention knob failure** — A loose or failed retention knob allows the tool holder to sit low in the spindle taper, causing the "tool in spindle" sensor to fault when the ATC arm tries to engage.

## Step-by-Step Fix {#fix}

**Critical safety step first:** Do NOT power-cycle the machine while the ATC arm is mid-stroke. Doing so may lose the control's memory of the arm position and make recovery significantly harder. Leave the machine powered, in alarm state, and assess the arm position visually before touching anything.

1. **Visually confirm the ATC arm position** — Look through the ATC door window (do not open the door with the arm in an unknown position). Note exactly where the arm is: at home (parked), mid-stroke (between home and spindle), or at the spindle. This determines your recovery path.

2. **Use the ATC RECOVERY menu** — On the Haas control, navigate to:
   - **VF-series with classic Haas control:** Press PARAM/DGNOS > DGNOS tab, look for ATC-related diagnostic pages
   - **Next Generation Control (NGC):** Press the ATC RECOVER button (or navigate through the recovery wizard on the touchscreen)
   Follow the on-screen prompts to manually step the arm through its cycle to the home position. Never force motion faster than the recovery routine allows.

3. **Check all tool pockets for jams** — After recovering the arm to home, rotate the carousel manually (in Recovery mode) and inspect each pocket. Look for:
   - Tools that have rotated out of position (low in the pocket, tilted)
   - Chips or swarf packed around tool holders
   - A damaged retention knob that is pulling the tool holder out of the pocket

4. **Inspect the ATC proximity switches** — Each critical ATC position has a proximity sensor with an LED indicator. Locate the sensors (typically visible through the ATC access panel on the side or back of the column). With the arm at known home position, all "home" position sensors should show LED ON. A sensor whose LED state doesn't match the arm's physical position has either failed or shifted.

5. **Verify air pressure** — Check the machine's main air pressure gauge (at the regulator, usually on the back of the machine). Haas requires **85–100 PSI** at the machine inlet. Open the ATC service panel and check if there is a dedicated ATC air regulator — it may have a separate setting. Low air causes incomplete clamp/unclamp cycles, generating Alarms 124 and 127.

6. **Inspect retention knobs** — Remove each tool from the ATC and check its retention knob by hand. The knob should thread smoothly into the tool holder and feel tight. A retention knob that spins loose, strips, or is visibly deformed needs replacement before the tool is returned to service.

7. **Reset and test with a simple program** — After resolving the mechanical issue, perform a full ATC cycle test: load all tools in MDI mode using T## M6 commands for each pocket position. Confirm each tool change completes without alarm before returning to production.

## Parts You May Need

| Part | Notes |
|------|-------|
| ATC proximity switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-120-atc-fault&k=haas+atc+proximity+switch+sensor&tag=errorcodefixes-20) — Verify sensor thread size and sensing distance from Haas parts list; prox sensors are model-specific |
| CAT40 retention knob | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-120-atc-fault&k=CAT40+retention+knob+pull+stud&tag=errorcodefixes-20) — Replace if loose, stripped, or damaged; buy in bulk as they wear with repeated tool changes |
| CAT50 retention knob | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-120-atc-fault&k=CAT50+retention+knob+pull+stud&tag=errorcodefixes-20) — For larger VF-series machines; confirm spindle taper size on your model |
| ATC grease / lubricant | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-120-atc-fault&k=haas+atc+grease+lubricant&tag=errorcodefixes-20) — Use Haas-specified grease on arm pivot and carousel drive gear; dry gears cause motion timeouts |

## When to Call a Technician

If the ATC arm is mid-stroke and the recovery menu cannot complete the arm's cycle, do not attempt to force the mechanism manually. Call Haas Factory Outlet (HFO) service — a forced recovery attempt can bend the arm, strip the gear drive, or damage the spindle, converting a $300 sensor fault into a $15,000 mechanical repair. Additionally, ATC motor and brake replacement requires removal of the ATC assembly and precise alignment during reinstallation — this is HFO service work.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 134 — Spindle Drive Fault Fix](/posts/haas-alarm-134-spindle-drive/)
- [Haas CNC Alarm Codes — Complete Reference Guide](/posts/haas-alarm-codes/)

## See Also

- [Haas VF-4 Common Alarms Guide — What They Mean and How to Fix Them](/posts/haas-vf4-common-alarms/)
- [Haas SL-20 Lathe Common Alarms — What They Mean and How to Fix Them](/posts/haas-sl-20-lathe-alarms/)
- [Haas Alarm 103 Overheating — CNC Machine Thermal Fault Diagnosis and Fix](/posts/haas-alarm-103-overheating/)
- [Haas Alarm 113 — Spindle Encoder Fault Causes & Fix](/posts/haas-alarm-113/)
