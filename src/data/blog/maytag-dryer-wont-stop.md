---
title: "Maytag Dryer Won't Stop - Causes & Fix"
description: "Usually a stuck start button or faulty user interface board sending continuous run signals. Reset power and inspect console buttons first."
pubDatetime: 2026-06-09T13:06:30Z
modDatetime: 2026-06-09T13:06:30Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - dryer
  - maytag
  - symptom
---

## Maytag Dryer Won't Stop — What's Happening

When a Maytag dryer won't stop running, the drum keeps tumbling or the cycle display stays lit even after the timer should have ended or you've pressed cancel. This is a symptom, not a specific error code, though you may see code F02 (keypad/user interface fault) on some models. The issue usually means the control is receiving a continuous run signal from a stuck button, a shorted keypad membrane, or a relay on the main control board that has welded closed and won't drop out.

Unlike thermal or airflow codes such as AF/F4E3, a "won't stop" complaint points to the control inputs or board logic rather than sensors or venting. Depending on the model, the drum may keep spinning, the heater may stay on, or just the display may be stuck in cycle mode while the drum has stopped. The root cause is almost always electrical: a stuck physical button, a failed user interface board, a main control board relay fault, or less commonly a door-switch circuit problem that prevents the control from recognizing the cycle should end.

[Jump to Fix](#fix)

## Most Likely Causes

- **Stuck start or cancel button** A physically jammed or sticky button on the console sends a constant signal to the control, preventing the cycle from ending or restarting the dryer immediately after stop.
- **Failed user interface board or keypad membrane** A shorted touchpad membrane or failed UI circuit generates false button-press inputs, triggering F02 codes or causing the control to see continuous start commands.
- **Main control board relay stuck closed** A relay on the main control that drives the motor or heater can weld shut due to arcing, keeping power applied even when the cycle logic says stop.
- **Wiring harness or connector fault between UI and main control** Loose pins, corrosion, or heat damage in the ribbon cable or plug between the user interface and main board can create shorts or intermittent signals that mimic stuck buttons.
- **Door switch or door-switch circuit fault** If the control does not correctly sense the door open/closed status, cycle logic may fail to terminate or the dryer may restart immediately after you think you've stopped it.

## How to Diagnose and Fix {#fix}

1. Verify whether the drum is still spinning, the heater is still on, or only the display/cycle timer appears stuck so you know which circuits to focus on.
2. Perform a hard reset by pressing the control-panel reset sequence (if available), then unplug the dryer or flip the breaker for three minutes and restore power to clear transient faults.
3. Inspect each button on the console by pressing and releasing every key to check for physical sticking or unresponsive feel that indicates a jammed button or torn membrane.
4. Enter the built-in diagnostics mode (if your model supports it) to retrieve and document any stored fault codes, particularly F02, before clearing them.
5. Check all wiring connectors at the back of the user interface and on the main control board for loose pins, corrosion, discoloration from heat, or pushed-out terminals.
6. Test the door switch by manually operating the door latch and listening for a click, or use a multimeter to confirm the switch opens and closes circuit as the door moves.
7. If all inputs and wiring test good and the symptom returns immediately after reset, replace the user interface board first (for F02 or button-related faults) or the main control board if the relay or cycle logic is at fault.
8. After replacing the suspect board, run a short test cycle and press cancel mid-cycle to confirm the dryer stops promptly and does not restart on its own.

## Parts You Might Need

| Part | Notes |
|------|-------|
| User interface control board (console/keypad assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-dryer-wont-stop&k=User+interface+control+board+%28console%2Fkeypad+assembly%29&tag=errorcodefixes-20) \| Includes the touchpad membrane and button contacts that send cycle commands to the main control. |
| Main electronic control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-dryer-wont-stop&k=Main+electronic+control+board&tag=errorcodefixes-20) \| Houses the relays and logic that energize motor and heater circuits; replace if relay is stuck or UI replacement does not fix symptom. |
| Door switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-dryer-wont-stop&k=Door+switch&tag=errorcodefixes-20) \| Confirms door closed status to the control; test before replacing boards if symptom is tied to door open/close behavior. |
| Wiring harness or ribbon cable (UI to main control) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-maytag-dryer-wont-stop&k=Wiring+harness+or+ribbon+cable+%28UI+to+main+control%29&tag=errorcodefixes-20) \| Connector assembly between console and main board; inspect for damaged pins or order if physical damage is visible. |

## Related Error Codes

If your appliance also shows a code on the display, these match this problem:

- [Maytag Dryer Err error code](/posts/maytag-dryer-err-error-code/)
- [Maytag Dryer F01 error code](/posts/maytag-dryer-f01-error-code/)
- [Maytag Dryer F02 error code](/posts/maytag-dryer-f02-error-code/)
- [Maytag Dryer F1E1 error code](/posts/maytag-dryer-f1e1-error-code/)
- [Maytag Dryer F1E3 error code](/posts/maytag-dryer-f1e3-error-code/)
- [Maytag Dryer F1E4 error code](/posts/maytag-dryer-f1e4-error-code/)
- [Maytag Dryer F1E5 error code](/posts/maytag-dryer-f1e5-error-code/)
- [Maytag Dryer F20 error code](/posts/maytag-dryer-f20-error-code/)
- [Maytag Dryer F22 error code](/posts/maytag-dryer-f22-error-code/)
- [Maytag Dryer F23 error code](/posts/maytag-dryer-f23-error-code/)
- [Maytag Dryer F24 error code](/posts/maytag-dryer-f24-error-code/)
- [Maytag Dryer F25 error code](/posts/maytag-dryer-f25-error-code/)

## When to Call a Pro

If you are uncomfortable working with live 240-volt circuits (on electric models) or if diagnostics point to the main control board, call a qualified appliance technician. Board-level faults require confident multimeter work and proper part matching by model number. If the dryer has F02 or other stored codes that return immediately after every reset, or if you have already replaced the user interface and the symptom persists, professional diagnosis of the main control and all wiring harnesses will save you from replacing the wrong part twice.
