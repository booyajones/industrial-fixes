---
title: "APC Back-UPS Pro F02 Error (On-Battery Output Short): Causes and the Two Fixes That Work"
description: "APC Back-UPS Pro F02 means the UPS detected an output short while on battery. Unplug every load from the Battery Backup outlets and reconnect one at a time, or reseat the battery connector if F02 appears at power-on."
slug: apc-back-ups-pro-f02-error-code
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - apc
  - ups
  - power-systems
most_likely_cause: "Shorted or faulty device or cable plugged into a Battery Backup outlet"
free_checks:
  - "Turn the UPS off, unplug every device from the Battery Backup outlets, then turn it back on with no load. If F02 is gone, a connected device or cable caused it."
  - "Reconnect loads one at a time until the fault returns. The last device you reconnected is the culprit."
  - "If F02 appears the moment you switch the unit on, open the battery compartment, reseat the battery connector firmly, and retry."
  - "Still faulting at power-on? Retry once with the UPS unplugged from the wall outlet before contacting APC support."
---

## What this code means

APC Back-UPS Pro units (the BR series) report detected system errors as F-codes, F01 through F09, on the front display. F02 is "On-Battery Output Short": while the UPS was running on battery power, it detected a short circuit on its output and shut the output down to protect itself and the rest of your connected equipment.

The definition comes directly from APC's official manuals. Document 990-91253B (Back-UPS Pro BR650MI, BR900MI, BR1300MI, BR1600MI) and document 990-3889B (Back-UPS Pro BR1200GI/BR1500GI, 230 V) both carry the same F01-F09 System Faults table, and both list F02 as an on-battery output short.

What makes F02 different from the other F-codes is that it has two distinct, separately documented failure modes:

1. **A genuine output short while on battery.** Something plugged into the Battery Backup outlets, either the device itself or its power cable, is shorted or faulty. This is the classic case, and the manual gives an exact isolation procedure.
2. **F02 shown immediately at power-on.** Schneider Electric's official FAQ FAQ000273815 states that an F02 (or F04) displayed when turning the unit on commonly means the internal battery is not correctly connected.

Most advice you will find on forums assumes only the first case, which is why "unplug everything" sometimes fails to help and people end up replacing a UPS that only needed its battery connector reseated. Work out which scenario you are in first, then apply the matching fix.

## Which scenario are you in?

- **F02 tripped during a power outage, during a self-test, or at the moment the UPS transferred to battery.** Treat it as a real output short on a connected load. Go to Fix 1.
- **F02 appears the instant you switch the unit on**, especially on a brand-new unit, after a battery replacement, or after the UPS was moved or shipped. Suspect the battery connection. Go to Fix 2.

If you are not sure, run Fix 1 first. It costs nothing, takes ten minutes, and rules out the load side completely.

## Fix 1: Find the shorted device (the official isolation sequence)

This is the corrective action straight from APC manual 990-91253B:

1. **Turn the UPS off.**
2. **Disconnect ALL equipment from the Battery Backup outlets.** Everything: computers, monitors, network gear, chargers, and any power strips. The fault is a short on the UPS output, so the output must start empty.
3. **Turn the UPS on.** With no load connected, a healthy unit should start without the fault.
4. **Reconnect one item at a time.** After each device, confirm the UPS is still running normally before adding the next. When F02 returns, the last device you reconnected (or its cable) is the offending load.

Practical notes from the bench:

- **Suspect the cable as much as the device.** A crushed or pinched IEC cord, a cord run under a desk foot or chair wheel, or insulation chafed against a sharp edge can short line to neutral without the device itself being dead. Inspect each cord as you reconnect it.
- **Remove power strips from the test entirely.** A surge strip or daisy-chained power strip plugged into a Battery Backup outlet adds a whole extra set of cords and contacts to the fault path. Test devices plugged directly into the UPS first.
- **A failed power supply is the most common offender.** If one specific device reliably brings F02 back, its internal supply has likely failed short. Do not keep re-plugging it into the UPS to confirm; have the device repaired or replaced.
- **Test only on the Battery Backup outlets.** The isolation procedure concerns the battery-backed output, which is what the inverter drives when the unit is on battery. Keep the test clean by changing one variable at a time.

Once you have identified the offending device, the UPS itself normally needs nothing: clear the fault by power-cycling the unit with the bad load removed, then reconnect the known-good equipment.

## Fix 2: Reseat the battery connection (F02 at power-on)

Per Schneider Electric FAQ FAQ000273815, F02 or F04 displayed when turning on a Back-UPS commonly means the battery is not correctly connected. The published sequence:

1. **Turn the unit off and unplug it from the wall** before opening the battery compartment.
2. **Open the battery compartment and reseat the battery connector.** Disconnect it fully, inspect for bent or recessed pins and loose terminal fittings, and push it back together until firmly seated.
3. **Retry.** Plug the unit back in and turn it on.
4. **If the fault persists, retry once with the unit unplugged from the wall.** The FAQ specifically includes this step: attempt the power-on with no AC input.
5. **If F02 still shows, contact APC support.** At that point the fault is not something the published procedure can clear.

This scenario is common on units that were just shipped, just had a battery swap, or were moved: a connector that looks plugged in but is not fully home is enough to trigger the fault at start-up.

If during this check you find a damaged connector or a battery at end of life, use the APC-specified replacement cartridge for your model. Per the official manuals, the BR1200GI/BR1500GI use the APCRBC124 cartridge, and the BR650MI/BR900MI/BR1300MI/BR1600MI range uses APCRBC110, APCRBC164, APCRBC165, or APCRBC166 depending on model. Match the RBC number to your exact model from the manual before ordering, since the connector and form factor differ across the range.

One important caution: F02 is not a "replace battery" code. Do not buy a battery to chase this fault unless the connector or cartridge is visibly damaged or the battery has separately failed. The two documented fixes are load isolation and connector reseating.

## F02 vs F04: do not mix them up

| Code | Fault name (per APC manuals) | What it means | Your first move |
| --- | --- | --- | --- |
| F02 | On-Battery Output Short | Short circuit detected on the output while the UPS was on battery | Fix 1 (isolate the load). If shown at power-on, Fix 2 (reseat battery). |
| F04 | Clamp Short | Internal fault | If shown at power-on, reseat the battery connector once per FAQ000273815. Otherwise not user-correctable; contact APC Technical Support. |

F02 and F04 travel together in Schneider's FAQ because both can appear at power-on with a poorly seated battery. The difference is what happens when the battery checks out: F02 still has a legitimate user-side fix (a shorted load), while F04 is an internal fault with no published field repair.

For context, the Back-UPS Pro manuals list nine detected system errors, F01 through F09. Manual 990-91253B labels F05 as "Charge Status," F08 as "Fan Condition" (BR1600MI only), and F09 as "Internal Error." F02 is the only code in the table that you fix by unplugging your own equipment; most of the rest point at the unit itself.

## When to stop and contact support

Stop troubleshooting and contact APC Technical Support when:

- **F02 persists with nothing connected to the Battery Backup outlets and the battery reseated.** You have exhausted both published fixes; the fault is internal.
- **F02 persists even with the unit unplugged from the wall**, per the FAQ sequence. That is the FAQ's explicit trigger for contacting support.
- **You see or smell any evidence of damage**: a burnt smell, discolored or melted outlet faces, or a hot chassis. Take the unit out of service.

Do not open the chassis beyond the battery compartment. A UPS contains capacitors that can hold a charge even when the unit is unplugged, and the battery itself can deliver very high short-circuit current across a dropped tool or ring. There are no user-serviceable parts past the battery door; internal repair belongs with APC or a qualified electronics technician.

## Frequently asked questions

### Does F02 mean my APC battery is bad?

Not by definition. F02 is an output short fault, not a battery health warning. The battery becomes relevant only in the power-on scenario: per Schneider FAQ FAQ000273815, F02 shown when switching the unit on commonly means the battery is not correctly connected, which a firm reseat of the connector fixes. If your unit is separately indicating a battery replacement condition, handle that on its own terms with the correct RBC cartridge for your model.

### Can a single plugged-in device really cause F02?

Yes, and it is the most common cause. A shorted device or a damaged power cable on the Battery Backup outlets is exactly what the fault detects. That is why the official corrective action is to disconnect all equipment, power the UPS back on, and reconnect one item at a time until the fault reappears. The last item reconnected is your fault source.

### Why does F02 only show up when the power goes out?

Because the fault condition is defined as a short detected while on battery. In normal operation your equipment may sit on utility power, but during an outage or transfer the UPS inverter drives the output directly and detects the short on the battery-backed outlets. A marginal or shorted load can therefore hide until the exact moment you need the UPS, which is the worst time to discover it. If you have had one F02 event, run the isolation procedure now rather than waiting for the next outage to repeat it.

### I unplugged everything and reseated the battery, but F02 is still there. Now what?

Follow the FAQ's final steps: retry the power-on once with the unit unplugged from the wall outlet, and if the fault persists, contact APC Technical Support. At that point neither documented failure mode applies, the fault is internal, and there is no published user repair. Do not open the unit beyond the battery compartment to hunt for it.

## Sources

- APC Back-UPS Pro BR650MI/BR900MI/BR1300MI/BR1600MI User Manual (APC doc EN 990-91253B): https://www.battery-direct.fr/Datenblaetter/apc-back-ups-pro-manual.pdf
- APC Back-UPS Pro BR1200GI/BR1500GI 230V Installation and Operation Manual (APC doc EN 990-3889B, 09/2019): https://media.distributordatasolutions.com/apc/2020q3/documents/885d73f3aac6f5c1965eb953b67ed231734fdf01.pdf
- Schneider Electric FAQ FAQ000273815, "F02 or F04 Error Code When Turning on Back-UPS": https://www.se.com/us/en/faqs/FAQ000273815/
