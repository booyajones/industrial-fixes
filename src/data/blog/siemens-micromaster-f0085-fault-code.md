---
title: "Siemens Micromaster F0085 - Causes & Fix"
description: "F0085 on Siemens Micromaster means external fault input trip. Learn real-world causes and how to trace and repair the external interlock chain."
pubDatetime: 2026-05-29T09:38:03Z
modDatetime: 2026-05-29T09:38:03Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "E-stop switch or safety interlock switch"
most_likely_cause: "Open or tripped external interlock chain"
---

## What this code means
F0085 on a Siemens Micromaster 420 or 440 drive means the inverter has received a fault signal from an external source, not an internal power stage failure. The drive is responding to a digital input or interlock circuit that has commanded a trip. This fault indicates the problem is usually outside the drive itself, in the wiring, safety devices, or control logic feeding the configured external fault terminal. The inverter is working correctly by stopping the motor when it sees the external permissive chain open or a safety device activate.

## Common Causes

- **Open or tripped external interlock chain** The series permissive circuit wired to the drive's external fault input is open due to a safety device, E-stop, or PLC interlock being active.
- **Safety device opened** An E-stop switch, door switch, pressure switch, thermal switch, or overload relay auxiliary contact in the fault chain has tripped or opened.
- **Miswired digital input or wrong parameterization** A control terminal is configured to generate external fault but is held active by design error, noise, or incorrect parameter assignment.
- **Loose, broken, or damaged control wiring** Field wiring to the external fault input circuit has become disconnected, corroded, or physically damaged.
- **Fault from another device in the permissive chain** A remote BMS controller, PLC, or networked safety device has issued a stop command through the interlock circuit.

## Step-by-Step Fix {#fix}

1. **Verify the drive model and parameter set** to identify which control terminal is assigned to the external fault input, then confirm the fault is active on the keypad or diagnostics display.
2. **Inspect the external fault input circuit** at the drive's control terminals and trace the wiring back through the entire interlock chain, including E-stops, door switches, pressure switches, and any PLC or overload relay contacts.
3. **Measure the input state at the terminal** using a multimeter and compare the voltage or logic level to what the installation expects for a run-enable or permissive-closed condition.
4. **Temporarily isolate the external fault circuit** only if the machine is safe to test, then observe whether the fault clears. If it does, the problem is in the external chain, not the inverter.
5. **Repair the external device or wiring** by tightening loose terminal connections, replacing broken or corroded conductors, restoring failed switch contacts, or correcting PLC interlock logic.
6. **Check parameter settings** and remove any incorrect assignment of a digital input to external fault if that function is not intended for your application.
7. **Reset the fault** using the keypad or control command after the external cause is corrected, then test run the drive under normal load.

## Parts Often Needed

| Part | Notes |
|------|-------|
| E-stop switch or safety interlock switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0085-fault-code&k=E-stop+switch+or+safety+interlock+switch&tag=errorcodefixes-20) \| Replace if the contact is failed open, stuck, or mechanically damaged in the permissive chain. |
| Pressure switch, airflow switch, or temperature switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0085-fault-code&k=Pressure+switch%2C+airflow+switch%2C+or+temperature+switch&tag=errorcodefixes-20) \| Replace if the switch is tripping incorrectly or has failed contacts feeding the external fault input. |
| Control wiring harness or terminal block | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0085-fault-code&k=Control+wiring+harness+or+terminal+block&tag=errorcodefixes-20) \| Replace damaged, corroded, or broken field wiring and terminals in the external fault circuit. |
| Overload relay auxiliary contact or permissive relay | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-micromaster-f0085-fault-code&k=Overload+relay+auxiliary+contact+or+permissive+relay&tag=errorcodefixes-20) \| Replace if the auxiliary contact or interlock relay is stuck open or has failed in the safety chain. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not trained to work safely with industrial control wiring, if the interlock chain is complex or involves PLC logic you cannot access, or if isolating the external fault circuit does not clear the code and you suspect drive control board damage. Also call for help if the safety devices are part of a certified machine guarding system that requires documented repair and re-commissioning, or if the fault persists after all external devices and wiring have been verified and the drive may need factory service or replacement of its digital input circuitry.
