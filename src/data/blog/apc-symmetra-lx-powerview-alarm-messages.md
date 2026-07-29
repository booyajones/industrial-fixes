---
title: "APC Symmetra LX PowerView Alarm Messages: Complete Verified Troubleshooting Reference"
description: "Every PowerView display message on the APC Symmetra LX (4-16 kVA) from official manual 990-1546: startup warnings, module failures, threshold alarms, bypass and fault messages, with APC's corrective action for each."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: apc-symmetra-lx-powerview-alarm-messages
featured: false
draft: true
tags:
  - apc
  - ups
  - power-quality
  - electrical
most_likely_cause: "Tripped input circuit breaker — APC's own service chapter calls a tripped circuit breaker the most common UPS problem"
money_part: "Symmetra LX battery module"
free_checks:
  - "Scroll through every active PowerView message, not just the first one — APC says multiple messages can be active at once and together they describe one system condition"
  - "Check the UPS input circuit breaker and the System Enable switch before replacing any module"
  - "Open Logging > View Log on the PowerView to read the last 64 events and see what happened right before the alarm"
---

## Symmetra LX PowerView Messages — What They Mean

The APC Symmetra LX is a modular, N+1-capable UPS built in 200/208/230 V versions from 4 to 16 kVA, in rack-mount, tower, and Extended Run configurations. Everything the UPS wants to tell you comes through the PowerView display on the front of the frame: an alphanumeric LCD with navigation keys, four status LEDs, and an audible alarm.

The complete list of PowerView messages lives in Chapter 4 ("Messages") of APC's official Symmetra LX User's Manual, document 990-1546 (January 2004). That chapter is the authoritative reference for this UPS family, and every message, meaning, and corrective action below is taken directly from it. The manual groups messages into six categories — Start-Up, General Status, Module Failure, Threshold Alarm, Bypass, and General Fault — and this page keeps that structure so you can cross-check against the original PDF.

One rule from the manual before you diagnose anything: **more than one message can be active at the same time.** APC explicitly tells you to review all of the displayed messages together for a full picture of the system condition. A "UPS Fault" message, for example, always appears alongside a "Bad Power Module" message — reading only one of the pair sends you down the wrong path.

## Status LEDs and the Display

The four PowerView status indicators frame every message you read:

| Indicator | Color | Meaning |
|---|---|---|
| LOAD ON | Green | The UPS is supplying power to the load, in any of these modes: On-Line, On-Battery, Command-Bypass, or Maintenance |
| ON BATT | Yellow | Mains power failed; battery modules are supplying the load |
| BYPASS | Yellow | The load is being fed directly from mains; the UPS is removed from the circuit |
| FAULT | Red | The UPS detected an internal fault; an alarm message will appear on the PowerView display |

If the display itself is unresponsive, pressing ESC + Help (?) + ENTER simultaneously for about one second resets the PowerView interface (you'll hear two short beeps). This resets the display module only — it is not a UPS reset and does not clear the underlying condition.

## Start-Up Messages

These appear when you power up or issue the Pwr ON command.

| Message | Meaning | Corrective action (per APC) |
|---|---|---|
| #Pwr modules changed since last ON. | At least one power module was added or removed since the last Pwr ON command | None needed — proceed with startup |
| #Batteries changed since last ON. | At least one battery module was added or removed since the last Pwr ON command | None needed — proceed with startup |
| No Redundant Intelligence Module (IM). | No redundant intelligence module is installed and working | Proceed, or abort and install a new IM. Note: without two functioning IMs there is no redundancy if an IM fails |
| Batt capacity less than Return Batt Cap. | Battery capacity is below the user-specified minimum required to turn on the load | Option 1: abort startup and let batteries recharge. Option 2: continue startup with less than minimum capacity |
| Input Freq outside configured range. | Input frequency is outside the configured range; output will not synchronize to input, normal bypass is not available, and the system will start on-battery | Improve the incoming frequency, widen the acceptable range (Startup > Setup > OutputFreq), or proceed knowing bypass is unavailable |
| AC adequate for UPS but not for bypass. | The UPS can run on-line from this input voltage, but if bypass were needed the input is not adequate to carry the load | Improve the incoming voltage, or proceed with bypass unavailable |
| Low/No AC input, startup on battery. | Input voltage is not adequate to start the UPS; if you proceed, it runs from battery | Abort until acceptable input voltage is present, or proceed and accept the battery discharge |

## Module Failure Messages

The Symmetra LX is modular by design — battery modules, power modules, and intelligence modules each report failures individually, and the frame logs insertions and removals as routine status events.

| Message | Meaning | Corrective action (per APC) |
|---|---|---|
| Bad Battery Module. | A battery module failed and requires replacement | Replace it — follow the module replacement procedure in the Physical Installation or Service Manual |
| Bad Power Module. | A power module failed and requires replacement | Replace it per the same module replacement procedure |
| Intelligence Module is installed and failed. | The intelligence module in the lower IM slot has failed | Replace per the module replacement procedure |
| Redundant Intelligence Module is installed and failed. | The intelligence module in the upper IM slot has failed | Replace per the module replacement procedure |

## Threshold Alarm Messages

These are user-configurable alarms, not hardware failures. The load is still supported — the UPS is warning you that headroom you asked it to protect is gone.

| Message | Meaning | Corrective action (per APC) |
|---|---|---|
| Load is above kVA alarm threshold. | The load exceeded the user-specified load alarm threshold | Reduce the load, or raise the threshold from the PowerView |
| Redundancy has been lost. | The UPS no longer detects redundant power modules — either module(s) failed or the load increased | Install additional power modules, decrease the load, or disable the alarm by setting redundancy to zero (Startup > Setup > Alarms > Redundancy > Zero) |
| Redundancy is below alarm threshold. | Actual power-module redundancy fell below the user-specified redundancy alarm threshold | Install additional power modules, decrease the load, or lower the threshold (Startup > Setup > Alarms > Redundancy) |
| Runtime is below alarm threshold. | Predicted runtime is lower than the user-specified minimum — battery capacity decreased or the load increased | Let batteries recharge, add battery modules, decrease the load, or lower the threshold (Startup > Setup > Alarms > Runtime) |

The configurable ranges (Setup > Alarms) are: redundancy alarm 0 (default), 1, or 2 spare power modules; load alarm Never (default) or 1–10 or 12 kVA, capped by the frame's maximum power; runtime alarm from 0:0 (default) up to 8 hours.

## Bypass Messages

| Message | Meaning | Corrective action (per APC) |
|---|---|---|
| Bypass is not in range (either freq or voltage). | Input frequency and/or voltage are outside the acceptable range for bypass while the UPS is online — bypass may not be available if needed, and the system may start on-battery | Decrease sensitivity to input frequency (Startup > Setup > OutputFreq), or correct the input voltage/frequency |
| Bypass contactor stuck in bypass position. | The UPS is stuck in the bypass position and cannot go on-line | Call your contract service provider or APC Technical Support |
| Bypass contactor stuck in on-line position. | The UPS is stuck in the on-line position and cannot transfer to bypass | Call your contract service provider or APC Technical Support |
| UPS in bypass due to internal fault. | A fault occurred and the UPS transferred itself to bypass | Investigate the accompanying fault messages; internal faults are a service call |
| UPS in bypass due to overload. | The load exceeded the system power capacity and the UPS switched to bypass | Decrease the load, or add power modules to the system |
| System is in Maintenance Bypass. | The maintenance bypass switch is in the On position | None — this is the expected state during maintenance bypass |

## General Fault Messages

| Message | Meaning | Corrective action (per APC) |
|---|---|---|
| On Battery. | The UPS is in on-battery mode and battery modules are discharging | No action required, but runtime is limited — prepare to shut down the UPS and load, or restore incoming voltage |
| Need Bat Replacement. | One or more battery modules need replacement | Follow the module replacement procedure |
| UPS Fault. | A fault occurred in a power module. This message always appears together with a Bad Power Module failure message | Call your contract service provider or APC Technical Support |
| Shutdown or unable to transfer to Batt due to overload. | The UPS shut down because an overload occurred and bypass is not available | Reduce the load, add power modules, or replace failed power modules to eliminate the overload. If bypass is unavailable because of a power failure, wait for power to return; if it's a utility problem, have it corrected |
| Load Shutdown from Bypass. Input Freq/Volts outside limits. | While on bypass, input power went out of acceptable range and the UPS shut the load down | Correct the input voltage problem |
| Fault, Battery Charger Failure. | The battery charger in one or more power modules failed | Replace the affected power module(s) per the module replacement procedure |
| Fault, Bypass Relay Malfunction. | The bypass relay has malfunctioned | Call your contract service provider or APC Technical Support |
| Fault, Internal Temp exceeded normal limits. | One or more battery modules are too hot | Replace the overheated module per the module replacement procedure |
| Input circuit breaker tripped open. | The UPS input circuit breaker tripped; input voltage is disconnected from the UPS | If there's a concurrent overload condition, decrease the load and reset the breaker. If there's no overload, reset the breaker — and if it trips again, call your service provider or APC Technical Support |
| System level fan failed. | A cooling fan in the UPS frame failed | Call your contract service provider or APC Technical Support |
| The Redundant Intelligence Module (IM) is in control. | The lower-slot intelligence module failed or is not installed; the upper-slot IM is managing all activity | Replace the intelligence module per the module replacement procedure |
| IIC inter-module communications failed. | Communications between the MIM and at least one other module failed | Call your contract service provider or APC Technical Support |

## General Status Messages (Informational)

These log configuration changes and recoveries. APC lists no corrective action for any of them:

- **# of batteries increased. / # of batteries decreased.** — a battery module was added to or removed from the system
- **# of Pwr Modules increased.** — a power module was added
- **Intelligence Module inserted. / removed.** — an IM was installed in or removed from the lower IM slot
- **Redundant Intelligence Module inserted. / removed.** — an IM was installed in or removed from the upper IM slot
- **# of External Battery Cabinets increased. / decreased.** — an external battery cabinet was connected to or disconnected from the frame
- **Redundancy Restored.** — power-module redundancy was lost and has been restored, either because modules were installed or the load dropped
- **Load is No Longer above Alarm Threshold.** — the load fell back below the alarm threshold (or the threshold was raised)
- **Min Runtime restored.** — runtime dropped below the configured minimum and recovered: battery modules were added or recharged, the load was reduced, or the threshold was raised

## How to Troubleshoot a Symmetra LX Alarm

1. **Read every active message.** Scroll the display and note all of them — the combination identifies the condition better than any single message.
2. **Check breakers first.** APC's own service chapter says a tripped circuit breaker is the most common UPS problem. Verify the input circuit breaker, the System Enable switch, and (for hardwired or PDU loads) the output distribution breakers before condemning hardware.
3. **Pull the event history.** Logging > View Log holds the most recent 64 events; select an entry and press ENTER for detail. Logging > View Statistics shows lifetime counts of transfers to battery, low-battery events, faults, and on-battery runtime. The sequence of events immediately before the alarm usually separates a utility problem from a module problem.
4. **Use the Diagnostics menu.** Diagnostics > Fault and Diagnostics shows the current system fault with diagnostic detail, and there are dedicated status screens for the intelligence module, redundant IM, power modules, and batteries — so you can identify exactly which module raised the flag before you touch anything.
5. **Run a self test.** Control > Do Self Test runs the built-in diagnostics and displays an error message if a problem is found. You can also schedule automatic self tests under Setup > Other > Self Test (At Power On, every 7 days, every 14 days — the default — or Disabled).
6. **Recalibrate runtime if predictions look wrong.** Control > Start Runtime Cal delivers load power from the battery and discharges to 25% capacity to rebuild an accurate runtime estimate. Battery capacity must be at 100% to start it, and it genuinely discharges your batteries — don't run it when utility power is shaky.

## When to Stop and Call a Qualified Technician

The Symmetra LX's user-serviceable parts are its modules: battery modules, power modules, and intelligence modules, each with a documented replacement procedure in APC's Physical Installation or Service Manual. Everything else — bypass contactor, bypass relay, frame-level fans, inter-module (IIC) communications, and any internal fault — is explicitly a "call your contract service provider or APC Technical Support" item in the official message table, and for good reason: this is a 200/208/230 V system backed by high-energy battery strings, and the frame internals are not designed for field repair.

Concretely, stop and call for service when you see: **Bypass contactor stuck** (either position), **Fault, Bypass Relay Malfunction**, **System level fan failed**, **IIC inter-module communications failed**, **UPS Fault**, or an **input circuit breaker that trips again after one reset**. Do not open the frame, and do not operate the maintenance bypass switch as an improvised fix for a fault condition — the bypass procedures in the manual assume a working system and a deliberate maintenance plan, and on bypass your load has no battery protection at all.

## Frequently Asked Questions

### Why did my Symmetra LX start on battery even though utility power is present?

Check for "Input Freq outside configured range" or "Low/No AC input, startup on battery" at startup, or "Bypass is not in range" while running. The UPS phase-locks its output to the input only within the configured window (Setup > Output Frequency: 50 ±3 Hz, 50 ±0.1 Hz, 60 ±3 Hz, 60 ±0.1 Hz, or full-range tracking). If your source — a generator is the classic case — drifts outside that window, the UPS refuses to sync, bypass becomes unavailable, and it will carry the load on battery. Widen the acceptance window or fix the source frequency.

### What does "UPS Fault" actually mean, and can I clear it myself?

Per the manual, "UPS Fault" means a fault occurred in a power module, and it always appears together with a "Bad Power Module" message. The corrective action APC lists is to call your contract service provider or APC Technical Support. Identify the failed module first via Diagnostics > Power Modules so you know exactly what to report.

### "Redundancy has been lost" — is my load in danger?

Not immediately. The message means the UPS no longer detects spare (redundant) power modules — either a module failed or the load grew into the headroom. Your load is still supported, but a single further power-module failure now has no spare to fail over to. Fix it by installing additional power modules or decreasing the load; if you knowingly run without redundancy, you can set the redundancy alarm to zero (Startup > Setup > Alarms > Redundancy > Zero) so it stops alarming.

### How do I see what happened before the alarm?

Logging > View Log stores the most recent 64 events; highlight one and press ENTER for details. Logging > View Statistics keeps running totals of transfers to battery, low-battery events, faults, and on-battery runtime. You can configure which event classes get logged (Power Events, UPS Control, UPS Faults, User Activity, Measure UPS Events) under Configure Logging.

### The display is frozen or garbled — is the UPS down?

Not necessarily. The PowerView interface can be reset independently of the UPS by pressing ESC + Help + ENTER together for about one second (two short beeps confirm). The green LOAD ON LED tells you whether the load is being fed regardless of what the LCD shows. If the display stays dead after a reset, treat it as a service call rather than pulling modules on a live system.

## Sources

- APC Symmetra LX User's Manual, 200/208/230 V, 4–16 kVA (APC document 990-1546, January 2004) — Chapter 4 "Messages" is the source for every message, meaning, and corrective action on this page: https://unitedpowerups.com/wp-content/uploads/2017/03/SymmetraLX_UsersManual-1.pdf
