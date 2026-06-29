---
title: "Yaskawa GA800 F022 - Causes & Fix"
description: "F022 means external fault signal from option board or control input. Most often caused by missing safety jumper or PLC fault signal."
pubDatetime: 2026-06-27T11:41:36Z
modDatetime: 2026-06-27T11:41:36Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Yaskawa GA800 option board (bUS Ethernet, PID, analog)"
most_likely_cause: "Missing or open safety terminal jumper (Safe Torque Off inputs)"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect terminals M3 and M4 for a closed jumper connection if Safe Torque Off is not in use"
  - "Check the drive fault log to see which option board or terminal triggered the fault"
  - "Verify PLC or safety relay outputs are in the 'run' state and not sending a fault signal"
part_price: "$80-200 for option board, $150-300 for main control board"
no_buy_pct: "60%"
---

## Yaskawa GA800 F022 — What It Means

The F022 fault on a Yaskawa GA800 VFD indicates an External Fault or Option Board External Fault. This means the drive has received a fault logic signal from an installed option board (such as a communication module, PID controller card, or analog input module) or from a dedicated external fault input terminal. When this signal is active, the drive halts operation immediately to protect the system.

The fault does not originate inside the drive itself. Instead, it comes from external control logic like a PLC, safety relay, encoder feedback instability, or a missing jumper on safety terminals. The drive is simply reporting that something connected to it has commanded a shutdown. You need to identify which external device or terminal is sending the fault signal before the drive will run again.

## Before You Replace Anything

Technicians often replace the main control board or option board first. Check the fault log and PLC/safety relay states before swapping any boards, most F022 faults trace to wiring, jumpers, or upstream control logic.

[Jump to Fix](#fix)

## Common Causes

- **Missing safety terminal jumper (~35%)** Safe Torque Off inputs on terminals M3/M4 require a closed jumper connection (near 0Ω continuity) to operate, and the drive will not run if this is open.
- **External PLC or safety relay fault signal (~30%)** A PLC, safety relay, or PID controller has sent a logic fault signal to the drive's option board or external fault terminal, halting operation.
- **PID feedback instability (~15%)** In PID control applications, rapid oscillation of the reference or feedback can trigger an external fault condition if the control logic is configured to monitor for steady-state errors.
- **Loose or damaged communication cable (~10%)** Missing or broken Ethernet/RJ45 cables or poor connections on the option board can cause bUS errors that route to an external fault condition.
- **Mechanical load issues triggering torque spikes (~7%)** A stiff gearbox, loose encoder coupling, or binding motor load can cause torque reference spikes that the external control logic interprets as a fault.
- **Motor or cable ground fault (~3%)** Motor or lead ground faults often trigger external fault logic in the control circuit before the drive reports an internal fault.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are terminals M3 and M4 jumpered together (if Safe Torque Off is not used)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The safety circuit is closed, move on to check external control devices.<br><strong>No:</strong> Install a jumper wire across M3 and M4, reset the fault, and try to run the drive.</div>
</details>

<details class="dtree"><summary>Does the drive fault log or modified parameters menu identify a specific option board or terminal?</summary>
<div class="dtree-body"><strong>Yes:</strong> Focus troubleshooting on that board or input, inspect its wiring and control signal source.<br><strong>No:</strong> Perform a full inspection of all option boards, PLC outputs, and safety relay states.</div>
</details>

<details class="dtree"><summary>Is a PLC or safety relay connected to the drive, and is it energized in the 'run' state?</summary>
<div class="dtree-body"><strong>Yes:</strong> The external logic appears healthy, check for intermittent wiring or encoder feedback problems.<br><strong>No:</strong> Verify the PLC or relay is powered and programmed to allow the drive to run, or bypass it temporarily for testing.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Access the fault log** on the drive keypad or via the drive software to identify which option board or terminal triggered the F022 external fault.
2. **Inspect safety terminals M3 and M4** and verify a jumper wire is installed across them if Safe Torque Off is not in use, the jumper must show near 0Ω continuity.
3. **Check external control devices** including PLCs, safety relays, and PID controllers to confirm they are powered and not sending a fault logic signal to the drive.
4. **Inspect communication and feedback wiring** on all option boards, look for loose RJ45 cables, damaged encoder tethers, or missing ground connections.
5. **Perform a megger test** on the motor and motor leads to rule out ground faults that might trigger external fault logic in the control circuit.
6. **Monitor PID reference and feedback** if the drive is in PID control mode, watch for rapid oscillation or steady-state errors that might trip the external fault condition.
7. **Re-autotune motor parameters** if an encoder was recently replaced or if mechanical couplings were serviced, and verify all encoder couplings are tight and secure.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Yaskawa GA800 option board (bUS Ethernet, PID, analog) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f022-fault-code&k=Yaskawa+GA800+option+board+%28bUS+Ethernet%2C+PID%2C+analog%29&tag=errorcodefixes-20) \| Match the exact part number for your installed communication or control module, consult your drive documentation. |
| Yaskawa GA800 main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f022-fault-code&k=Yaskawa+GA800+main+control+board&tag=errorcodefixes-20) \| Only replace if the fault is internal to the drive logic after ruling out all external sources, Yaskawa supports control board replacement. |
| Safety terminal jumper wire (M3/M4) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-f022-fault-code&k=Safety+terminal+jumper+wire+%28M3%2FM4%29&tag=errorcodefixes-20) \| Short wire rated for 24V logic, 18-22 AWG, make sure near 0Ω resistance when installed. |

## When to Call a Pro

Call a qualified electrician or automation technician if you are not familiar with VFD wiring, PLC programming, or high-voltage industrial equipment. The F022 fault often involves tracing control logic across multiple devices (PLCs, safety relays, option boards) and interpreting drive parameter settings. If the fault persists after checking jumpers and external control states, a technician will need to analyze the fault log, perform electrical testing on motor leads, and potentially reprogram or replace option boards. Any work involving the main control board, encoder coupling, or motor megger testing requires proper lockout/tagout procedures and experience with three-phase power systems.

**Rough cost:** A pro service call runs about $150-400 depending on source and labor.
