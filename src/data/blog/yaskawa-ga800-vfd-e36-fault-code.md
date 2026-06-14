---
title: "Yaskawa GA800 E36 Fault - Causes & Fix"
description: "E36 on a Yaskawa GA800 VFD means the Safe Torque Off circuit is open or not satisfied. Most often, check the STO jumper or safety relay."
pubDatetime: 2026-06-05T10:04:59Z
modDatetime: 2026-06-05T10:04:59Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Safety relay"
most_likely_cause: "Missing or loose STO jumper"
---

## Yaskawa GA800 E36 Fault — What It Means

The E36 fault on a Yaskawa GA800 variable frequency drive indicates that the Safe Torque Off (STO) input circuit is open or the drive is being held in a safety-off state. The GA800 will not produce torque unless the STO circuit is properly satisfied through the dedicated STO input terminals. This is not a motor overload or power stage failure. It is a safety-chain fault.

In applications where the drive is configured to use an external safety chain (E-stop, guard door switches, or safety relays), the fault means that chain is open or the safety device has tripped. In stand-alone installations where no external safety system is used, the fault typically means the required jumper or bridge between the STO terminals is missing or has come loose. The drive is designed to stay locked out until the STO circuit shows a valid closed condition.

[Jump to Fix](#fix)

## Common Causes

- **Missing or loose STO jumper** When the drive runs without an external safety chain, the STO terminals require a jumper or bridge, and if it is not installed or has worked loose, the drive will fault.
- **Safety relay output open or not reset** The safety relay feeding the STO circuit may have tripped or failed to close after an E-stop or guard event, leaving the STO loop open.
- **Broken or miswired STO circuit wiring** Conductors between the safety device and the GA800 STO terminals may be broken, landed on the wrong terminal block, or poorly terminated.
- **Upstream safety device trip** An E-stop button, safety light curtain, guard door switch, or other safety interlock in the chain may be open or in a fault state.
- **Incorrect terminal function parameters** The GA800 terminal assignments may not be configured correctly for the intended STO input and output functions.
- **Failed safety relay contacts** The mechanical contacts inside the safety relay that close the STO loop may have failed open or become intermittent.

## Step-by-Step Fix {#fix}

1. **Verify the machine is safe** and de-energize surrounding equipment before working on the safety circuit or STO wiring.
2. **Check the drive fault display** to confirm E36 is the active fault and note the fault history for any pattern or repeated trips.
3. **Inspect the STO terminal wiring** at the GA800 terminal block for loose connections, missing jumpers, broken wires, or incorrect landing points.
4. **Verify the state of the safety relay** or safety chain and confirm that any E-stop or guard door switches have been reset and their outputs are closed.
5. **Review the terminal function parameters** in the GA800 to confirm the STO input and any safety-related output assignments match the wiring and application design.
6. **Restore the STO loop** by reseating terminals, repairing open conductors, replacing failed relay contacts, or installing the jumper if the drive is meant to run without an external safety system.
7. **Clear the fault and command a run** only after confirming the STO circuit is stable and closed, and escalate to Yaskawa support with model, serial, and fault history if the fault persists with a known-good circuit.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Safety relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e36-fault-code&k=Safety+relay&tag=errorcodefixes-20) \| If external relay contacts feeding the STO circuit are found failed open or intermittent. |
| STO terminal jumper or bridge wire | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e36-fault-code&k=STO+terminal+jumper+or+bridge+wire&tag=errorcodefixes-20) \| For stand-alone installations not using an external safety chain, if the original jumper is missing or damaged. |
| Terminal block or connector | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-ga800-vfd-e36-fault-code&k=Terminal+block+or+connector&tag=errorcodefixes-20) \| If STO terminal connections are loose, corroded, or damaged and cannot be reliably re-landed. |

## When to Call a Pro

Call a qualified industrial electrician or Yaskawa-certified technician if you are not trained in safety-circuit troubleshooting, if the STO wiring diagram is unclear or unavailable, or if the fault continues after verifying that the STO loop is intact and the safety devices are reset. Safety circuits are critical to machine and personnel protection, and incorrect changes can create serious hazards. Also call for support if the drive requires parameter changes you are not authorized to make or if the fault persists with a confirmed good external circuit, as internal drive diagnostics or replacement may be needed.
