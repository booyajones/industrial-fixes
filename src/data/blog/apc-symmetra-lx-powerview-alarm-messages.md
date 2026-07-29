---
title: "APC Symmetra LX PowerView Alarm Messages: Complete Verified Troubleshooting Reference"
description: "Every PowerView display message on the APC Symmetra LX (4-16 kVA) from official APC Operations Manual 990-1546: start-up warnings, module failures, threshold alarms, bypass and general fault messages, each with APC's own corrective action."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: apc-symmetra-lx-powerview-alarm-messages
featured: false
draft: false
tags:
  - apc
  - ups
  - power-quality
  - electrical
most_likely_cause: "Tripped input circuit breaker. APC's own service instructions call a tripped circuit breaker the most common UPS problem."
money_part: "Symmetra LX battery module"
free_checks:
  - "Scroll through every active PowerView message, not just the first one. APC says multiple messages can be active at once and must be read together"
  - "Check the UPS input circuit breaker and the System Enable switch before replacing any module"
  - "Open Logging > View Log on the PowerView to read the last 64 events and see what happened right before the alarm"
---

## Symmetra LX PowerView Messages: What They Mean

The APC Symmetra LX is a modular UPS, published in 200/208/230 V versions from 4 to 16 kVA, in rack-mount, tower, and Extended Run configurations. Everything the UPS wants to tell you comes through the PowerView display on the front of the frame: an alphanumeric LCD with navigation keys, status indicators, and an audible alarm.

The complete list of PowerView messages lives in Chapter 4 ("Messages") of APC's **Symmetra LX Operations Manual, document 990-1546, English, January 2004**. Every message, meaning, and corrective action on this page is taken from that chapter. The manual groups messages into six categories (Start-Up, General Status, Module Failure, Threshold Alarm, Bypass, and General Fault) and this page keeps that structure so you can cross-check against the original PDF.

One rule from the manual before you diagnose anything: **more than one of these messages may occur at one time.** APC explicitly instructs you to review all of the displayed messages for a better understanding of the system condition. A "UPS Fault" message, for example, always appears alongside a "Bad Power Module" message, and reading only one of the pair sends you down the wrong path.

## Status Indicators and the Display

The four PowerView status indicators frame every message you read.

| Indicator | Color | Status (per 990-1546) |
|---|---|---|
| LOAD ON | Green | The UPS is supplying power to the load. It may be operating in any one of these modes: On-Line, On-Battery, Command-Bypass, or Maintenance |
| ON BATT | Yellow | A mains power failure has occurred, and the battery modules are supplying power to the load equipment |
| BYPASS | Yellow | Power to the load is being supplied directly by the mains power source. The UPS is removed from the circuit |
| FAULT | Red | The UPS has detected an internal fault condition. An alarm message will appear on the PowerView display |

The manual also documents a display-level key combination: pressing **ESC + Help (?) + ENTER** simultaneously for about one second resets the PowerView RM interface, confirmed by two short beeps. (Holding the same three keys for about three seconds instead puts the interface into programming mode for installing new language program files, so keep the press short.)

## Start-Up Messages

These appear when you power up or issue the Pwr ON command.

| Message | Meaning | Corrective action (per APC) |
|---|---|---|
| #Pwr modules changed since last ON. | At least one power module has been added or removed since the last Pwr ON command | No corrective action necessary. Proceed with the startup |
| #Batteries changed since last ON. | At least one battery module has been added or removed since the last Pwr ON command | No corrective action necessary. Proceed with the startup |
| No Redundant Intelligence Module (IM). | There is no redundant intelligence module installed and working | Proceed with the startup, or abort and install a new IM. Note: without two functioning IMs there is no redundancy in the event of an IM failure |
| Batt capacity less than Return Batt Cap. | Battery capacity is less than the user-specified minimum required to turn on the load | Option 1: abort the startup and allow batteries to recharge. Option 2: continue startup with less than minimum battery capacity |
| Input Freq outside configured range. | Input frequency is outside the configured range. Output will not synchronize with the input, normal bypass is not available, and the system will start on-battery | Improve the frequency of the incoming voltage; widen the acceptable range (Startup > Setup > OutputFreq); or proceed knowing normal bypass is unavailable |
| AC adequate for UPS but not for bypass. | The UPS will function on-line with this input voltage, but if bypass were required the input voltage is not adequate to power the load equipment | Improve the incoming voltage, or proceed with startup knowing normal bypass is not available |
| Low/No AC input, startup on battery. | Input voltage is not adequate to start the UPS. If startup proceeds, the UPS will function from battery | Abort startup until acceptable input voltage is present, or proceed and accept that the battery will discharge |

## Module Failure Messages

The Symmetra LX is modular by design. Battery modules, power modules, and intelligence modules each report failures individually. APC's corrective action for all four messages below is the same: refer to installing modules in the **Physical Installation or Service Manual**. Note that the operations manual deliberately does not contain the replacement procedure.

| Message | Meaning |
|---|---|
| Bad Battery Module. | A battery module failed and requires replacement |
| Bad Power Module. | A power module failed and requires replacement |
| Intelligence Module is installed and failed. | The intelligence module in the lower IM slot has failed |
| Redundant Intelligence Module is installed and failed. | The intelligence module in the upper IM slot has failed |

## Threshold Alarm Messages

These are user-configurable alarms, not hardware failures. The load is still supported. The UPS is warning you that headroom you asked it to protect is gone.

| Message | Meaning | Corrective action (per APC) |
|---|---|---|
| Load is above kVA alarm threshold. | The load has exceeded the user-specified load alarm threshold | Reduce the load, or use the PowerView to raise the alarm threshold |
| Redundancy has been lost. | The UPS no longer detects redundant power modules. Either power module(s) failed or the load increased | Install additional power modules; decrease the load; or disable the alarm by setting redundancy to zero (Startup > Setup > Alarms > Redundancy > Zero) |
| Redundancy is below alarm threshold. | Actual power-module redundancy fell below the user-specified redundancy alarm threshold. Either module(s) failed or the load increased | Install additional power modules; decrease the load; or use the PowerView to decrease the redundancy alarm threshold (Startup > Setup > Alarms > Redundancy) |
| Runtime is below alarm threshold. | Predicted runtime is lower than the user-specified minimum runtime alarm threshold. Either battery capacity decreased or the load increased | Allow the battery modules to recharge; increase the number of battery modules; decrease the load; or decrease the minimum runtime alarm threshold (Startup > Setup > Alarms > Runtime) |

The configurable ranges under Setup > Alarms are: **Redundancy** 0 (default), 1, or 2; **Load** Never (default), or 1 through 10 or 12 kVA, with the upper value limited by the maximum power of the UPS; **Runtime** 0:0 (default), 5m, 10m, 15m, 30m, 45m, then 1h through 8h.

## Bypass Messages

| Message | Meaning | Corrective action (per APC) |
|---|---|---|
| Bypass is not in range (either freq or voltage). | Frequency and/or voltage are out of acceptable range for bypass. Occurs while the UPS is online and indicates bypass may not be available if required; the system may start on-battery | Decrease the sensitivity to input frequency (Startup > Setup > OutputFreq), or correct the input voltage and/or frequency |
| Bypass contactor stuck in bypass position. | The UPS is positioned in the bypass position and cannot go on-line | Call your contract service provider or APC Technical Support |
| Bypass contactor stuck in on-line position. | The UPS is positioned in the on-line position and cannot go to bypass | Call your contract service provider or APC Technical Support |
| UPS in bypass due to internal fault. | The UPS has transferred to bypass mode because a fault has occurred | Call your contract service provider or APC Technical Support |
| UPS in bypass due to overload. | The load exceeded the system power capacity and the UPS has switched to bypass mode | Decrease the load, or add power modules to the system |
| System is in Maintenance Bypass. | The UPS is in bypass because the maintenance bypass switch is in the On position | No corrective action necessary |

## General Fault Messages

| Message | Meaning | Corrective action (per APC) |
|---|---|---|
| On Battery. | The UPS is in on-battery mode and the battery modules are being discharged | No action necessary, but runtime is limited in duration. Prepare to shut down the UPS and the load equipment, or restore incoming voltage |
| Need Bat Replacement. | One or more battery modules are in need of replacement | Refer to module replacement procedure |
| UPS Fault. | A fault occurred in a power module. This message always occurs when there is a bad power module failure message | Call your contract service provider or APC Technical Support |
| Shutdown or unable to transfer to Batt due to overload. | The UPS shut down because an overload occurred and bypass is not available | Reduce the load, add power modules, or replace failed power modules to eliminate the overload. If bypass is unavailable because of a power failure, wait for power to be restored; if it is a utility problem, have it corrected |
| Load Shutdown from Bypass. Input Freq/Volts outside limits. | The UPS shut the load down while on bypass because input power went out of acceptable range | Correct the input voltage problem |
| Fault, Battery Charger Failure. | The battery charger in one or more power module(s) failed | Refer to module replacement procedure |
| Fault, Bypass Relay Malfunction. | The bypass relay has malfunctioned | Call your contract service provider or APC Technical Support |
| Fault, Internal Temp exceeded normal limits. | The temperature of one or more battery modules is too hot | Replace the overheated module. Refer to module replacement procedure |
| Input circuit breaker tripped open. | The UPS input circuit breaker tripped open. Input voltage is disconnected to the UPS | If this occurs together with an overload condition, decrease the load and reset the breaker. If no overload exists, reset the breaker; if it trips open again, call your contract service provider or APC Technical Support |
| System level fan failed. | A cooling fan in the UPS frame failed | Call your contract service provider or APC Technical Support |
| The Redundant Intelligence Module (IM) is in control. | The IM in the lower slot failed or is not installed; the upper-slot IM is managing all activity | Replace the intelligence module. Refer to module replacement procedure |
| IIC inter-module communications failed. | Communications between the MIM and at least one other module failed | Call your contract service provider or APC Technical Support |

## General Status Messages (Informational)

These log configuration changes and recoveries. APC lists **no corrective action necessary** for all of them.

- **# of batteries increased. / # of batteries decreased.** At least one battery module was added to, or removed from, the system
- **# of Pwr Modules increased.** At least one power module was added
- **Intelligence Module inserted. / removed.** An IM was installed in, or removed from, the lower IM slot
- **Redundant Intelligence Module inserted. / removed.** An IM was installed in, or removed from, the upper IM slot
- **# of External Battery Cabinets increased. / decreased.** An external battery cabinet was connected to, or disconnected from, the frame
- **Redundancy Restored.** Power-module redundancy loss occurred and was restored, either because additional modules were installed or the load was reduced
- **Load is No Longer above Alarm Threshold.** The load exceeded the threshold and the situation has been corrected, either because the load decreased or the threshold was increased
- **Min Runtime restored.** System runtime dropped below the configured minimum and was restored: battery modules were added or recharged, the load was reduced, or the threshold was raised

## How to Troubleshoot a Symmetra LX Alarm

1. **Read every active message.** Scroll the display and note all of them. APC's own instruction is to review all displayed messages together for a better understanding of the system condition.
2. **Check breakers first.** APC's service instructions in Chapter 5 (Maintenance) put it bluntly: "A tripped circuit breaker is the most common UPS problem!" Verify the input circuit breaker and the System Enable switch. The startup procedure also requires that, for hardwired loads, each output circuit breaker in the distribution panels is ON, and for plugged loads, each UPS PDU output circuit breaker is ON.
3. **Pull the event history.** Logging > View Log holds the most recent 64 events; point to an entry and press ENTER for more information. Logging > View Statistics records the total number of transfers to battery, low battery events, faults, and on-battery runtime events. The sequence of events immediately before the alarm usually separates a utility problem from a module problem. You can include or exclude event types under Configure Logging (Power Events, UPS Control, UPS Faults, User Activity, Measure UPS Events).
4. **Use the Diagnostics menu.** Diagnostics > Fault and Diagnostics displays the current system fault and diagnostic information about that fault. There are dedicated status screens for the (Main) Intelligence Module, Redundant Intelligence Module, Power Modules, and Batteries, so you can identify exactly which module raised the flag before you touch anything.
5. **Run a self test.** Control > Do Self Test initiates system self-testing and diagnostics, and displays an error message when a problem is detected. Automatic self tests are configurable under Setup > Other > Self Test: At Power On, 7 days, 14 days (the default), or Disabled.
6. **Recalibrate runtime only when it is safe to.** Control > Start Runtime Cal delivers load output power from the battery source and **discharges the battery to 25% of capacity**, and battery capacity must be at 100% to execute the test. It genuinely runs your batteries down, so do not start one when utility power is unstable.

## When to Stop and Call a Qualified Technician

The Symmetra LX's serviceable parts are its modules: battery modules, power modules, and intelligence modules. Even for those, the operations manual does not contain the procedure. It refers you to the **Physical Installation or Service Manual** for installing modules, which is the manufacturer telling you the step needs its own documented process.

Everything else is explicitly a **"Call your contract service provider or APC Technical Support"** item in APC's own message table. Concretely, stop and call for service when you see:

- **Bypass contactor stuck** in either the bypass or the on-line position
- **UPS in bypass due to internal fault**
- **Fault, Bypass Relay Malfunction**
- **System level fan failed**
- **IIC inter-module communications failed**
- **UPS Fault**
- **Input circuit breaker tripped open** that trips again after one reset with no overload present

Treat this as live high-voltage work, because it is: the Symmetra LX is a 200/208/230 V system with high-energy battery modules, and the output voltage is configurable to 200, 208 or 240 V (US/Japan) or 220, 230 or 240 V (international). Do not open the frame. Do not use the maintenance bypass switch as an improvised fix for a fault condition either: the manual defines bypass as delivering power directly from the utility source to the load with the UPS removed from the circuit, which means your load is running with no battery protection and no conditioning at all while it is there.

## Frequently Asked Questions

### Why did my Symmetra LX start on battery even though utility power is present?

Check for "Input Freq outside configured range" or "Low/No AC input, startup on battery" at startup, or "Bypass is not in range" while running. The UPS output phase locks to the input only within the configured window, set at Setup > Output Frequency: 50 ±3 Hz, 50 ±0.1 Hz, 60 ±3 Hz, 60 ±0.1 Hz, or Full range tracking. If your source drifts outside that window (a generator is the classic case), the output will not synchronize with the input, normal bypass is not available, and the system starts on-battery. Widen the acceptance window or fix the source frequency.

### What does "UPS Fault" actually mean, and can I clear it myself?

Per the manual, "UPS Fault" means a fault occurred in a power module, and it always occurs together with a bad power module failure message. The corrective action APC lists is to call your contract service provider or APC Technical Support. Identify the failed module first via Diagnostics > Power Modules so you know exactly what to report.

### "Redundancy has been lost." Is my load in danger?

Not immediately. The message means the UPS no longer detects redundant power modules, because either module(s) failed or the load increased. Your load is still supported, but a further power-module failure now has no spare to fall back on. APC's options are to install additional power modules, decrease the load, or, if you knowingly run without redundancy, disable the alarm by setting redundancy to zero (Startup > Setup > Alarms > Redundancy > Zero).

### How do I see what happened before the alarm?

Logging > View Log stores the most recent 64 events; point to an entry and press ENTER for more information on that event. Logging > View Statistics records the total number of transfers to battery, low battery events, faults, and on-battery runtime events.

### The display is frozen or garbled. Is the UPS down?

Not necessarily. Per the manual, pressing ESC + Help + ENTER simultaneously for about one second resets the PowerView RM interface, confirmed by two short beeps. The green LOAD ON indicator tells you whether the UPS is supplying power to the load regardless of what the LCD is showing. If the display stays dead after a reset, treat it as a service call rather than pulling modules on a live system.

## Sources

- APC Symmetra LX Operations Manual, 200/208/230 V, 4-16 kVA (APC document 990-1546, English, January 2004). Chapter 4 "Messages" is the source for every message, meaning, and corrective action on this page; Chapter 3 for the menu commands and configurable ranges; Chapter 5 for the service instructions: https://unitedpowerups.com/wp-content/uploads/2017/03/SymmetraLX_UsersManual-1.pdf
