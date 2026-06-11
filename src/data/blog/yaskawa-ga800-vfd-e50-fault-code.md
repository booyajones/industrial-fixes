---
title: "Yaskawa GA800 E50 Fault Code - Causes & Fix"
description: "E50 on a Yaskawa GA800 VFD signals an external fault input from an interlock or safety device. The most common fix is locating and clearing the tripped field switch or relay."
pubDatetime: 2026-06-06T11:37:44Z
modDatetime: 2026-06-06T11:37:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
most_likely_cause: "Safety chain or interlock opening"
likelihood: "the most typical field cause"
diy_or_pro: "pro"
money_part: "Replacement interlock relay or safety contact"
---

## Yaskawa GA800 E50 Fault Code — What It Means

The E50 fault code on the Yaskawa GA800 variable frequency drive indicates that an external device has asserted a fault signal into one of the drive's multi-function digital input terminals. This is not an internal drive failure. Instead, the code means that a safety chain, interlock, overload relay, E-stop, or process switch wired into the drive has opened or dropped out, telling the drive to trip and stop operation.

Because the GA800 is configured by the user or integrator, the exact external device causing the fault depends on your application wiring and parameter setup. The drive will hold the E50 fault until the external circuit is restored and the fault is manually cleared. The fault is a deliberate protective mechanism, so the root cause is always found in the field wiring and external equipment, not in the VFD power stage or control electronics.

## Before You Replace Anything

Technicians sometimes replace the VFD control board or the entire drive when E50 appears, but the fault is triggered by an external device. Always trace the wired interlock circuit and verify the state of every switch, relay contact, and field device before ordering drive parts.

[Jump to Fix](#fix)

## Common Causes

- **E-stop or safety interlock opened** An emergency stop button, guard switch, or safety relay chain has opened and is holding the external fault input in the tripped state.
- **Overload relay or motor protection contact tripped** A thermal overload or electronic motor protection relay wired into the fault input has detected an overload condition and opened its normally closed contact.
- **Process limit switch opened** A freeze-stat, pressure switch, airflow proving switch, or other process safety device has detected an out-of-range condition and tripped the fault input.
- **Loose or damaged control input wiring** A wire termination at the drive terminal or at the field device has come loose, corroded, or broken, causing the fault circuit to open intermittently or continuously.
- **Miswired or misconfigured fault input** The drive's multi-function input parameter is mapped to external fault, but the field device is wired in the wrong polarity or logic, or the parameter setup does not match the actual circuit.
- **Faulted external device** A relay, PLC output, or auxiliary contact that is supposed to hold the fault input closed has itself failed or lost power, causing the drive to see a fault condition.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is an E-stop button, guard door, or safety interlock switch visibly open or tripped?</summary>
<div class="dtree-body"><strong>Yes:</strong> Reset or close the safety device, then clear the E50 fault at the drive keypad and attempt a restart. If the fault does not return, the interlock was the cause.<br><strong>No:</strong> Proceed to check the overload relay and other process switches wired into the external fault input circuit.</div>
</details>

<details class="dtree"><summary>Does the overload relay or motor protection contact show a tripped indicator or open state?</summary>
<div class="dtree-body"><strong>Yes:</strong> Allow the overload to cool and reset, verify motor current is within nameplate rating, then clear the drive fault and restart. If it trips again immediately, investigate motor loading or wiring.<br><strong>No:</strong> Move to the next device in the external fault circuit, checking each switch, relay, and PLC output in turn for continuity and proper state.</div>
</details>

<details class="dtree"><summary>With power off and the external fault circuit isolated, does the wiring between the field device and the drive terminal show continuity when the device is closed?</summary>
<div class="dtree-body"><strong>Yes:</strong> The field wiring is intact. The fault is likely caused by the external device itself opening due to a real process or safety condition, or by a parameter mismatch in the drive.<br><strong>No:</strong> Repair or replace the damaged wire, loose termination, or corroded contact in the fault input circuit, then retest.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Record the fault and drive state.** Write down the exact fault code (E50), the drive model and serial number, and note what the machine was doing when the fault occurred. Check the drive display for any additional alarm history.
2. **Verify which input is mapped to external fault.** Review the GA800 parameter setup (consult your commissioning documentation or the drive's uploaded parameters) to identify which multi-function digital input terminal is configured as the external fault input.
3. **Inspect the external fault circuit at the field devices first.** Walk through the elementary diagram and physically check every E-stop, overload relay, guard switch, pressure switch, freeze-stat, and interlock contact wired into that input. Look for tripped indicators, open contacts, and loose wire terminations.
4. **Check the input state at the drive terminal.** With a multimeter, measure the voltage or continuity at the drive's external fault input terminal while the fault is active. Compare the measured state to the expected logic (normally closed or normally open) defined in the drive parameters.
5. **Isolate and test each external device.** Temporarily jumper or bypass one device at a time (only if safe to do so and with proper lockout/tagout) to determine which component is causing the input to open. Never bypass safety interlocks during normal operation.
6. **Remove the external cause and clear the fault.** Once you have identified and corrected the tripped relay, open switch, or broken wire, restore the circuit to its normal state. Press the drive's reset button or cycle control power to clear the E50 fault.
7. **Verify the fix with a test run.** Restart the drive and confirm that the external fault input remains in the healthy state throughout normal operation. Monitor the input during several start/stop cycles to make sure the fault does not return.
8. **If the fault persists with a verified healthy field circuit, inspect the drive control board and wiring.** Check for physical damage, loose terminal screws, or corrosion at the input terminals. If no field cause is found and the drive repeatedly trips E50, contact Yaskawa technical support with your drive model, serial number, parameter backup, and a description of the application.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Replacement interlock relay or safety contact | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e50-fault-code&k=Replacement+interlock+relay+or+safety+contact&tag=errorcodefixes-20) \| Only if testing proves the existing relay coil or contact is defective and cannot close the fault circuit. |
| GA800 control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e50-fault-code&k=GA800+control+board&tag=errorcodefixes-20) \| Rarely needed for E50. Only replace if the external circuit is verified healthy and the input terminal itself is proven faulty through continuity and voltage testing. |

## When to Call a Pro

Call a qualified electrician or controls technician immediately if you are not trained in industrial electrical troubleshooting, if the VFD is part of a machine with moving hazards or high-voltage circuits, or if you cannot safely access the field wiring and interlock devices. A professional should handle all work involving lockout/tagout, multi-point safety chains, PLC-controlled interlocks, and any situation where bypassing a safety device would create a hazard. If you have traced the external fault circuit and found no open devices or broken wires, the problem may involve parameter configuration or a control board input failure, both of which require a technician familiar with Yaskawa drives and the specific machine application.

**Rough cost:** A pro service call runs about $150-400 depending on the external device requiring repair or replacement.
