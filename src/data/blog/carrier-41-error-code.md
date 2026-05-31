---
title: "Carrier 41 Error Code — Blower Motor Fault Fix"
author: "Marcus Webb"
pubDatetime: 2024-03-22T08:00:00Z
modDatetime: 2024-03-22T08:00:00Z
slug: carrier-41-error-code
featured: false
draft: false
tags:
  - hvac
  - carrier
  - furnace
  - blower-motor
description: "Carrier error code 41 means the blower motor is not operating correctly. This guide covers diagnosis and fixes for the ECM blower motor fault on Carrier gas furnaces."
---

## Error Code: Carrier 41

**What it means:** Code 41 is a blower motor fault — the control board is not detecting proper operation from the ECM (electronically commutated motor) blower. On most Carrier furnaces with variable-speed ECM motors, the board monitors a feedback signal from the motor module. When that signal is absent or out of range, the board locks out with Code 41. The furnace will shut down to prevent overheating and potential heat exchanger damage.

## Common Causes

- **Failed ECM motor module** — The module attached to the back of the motor is the most common failure point. It controls motor speed via PWM signals from the board. Module failures are common on motors 7–12 years old, especially in humid environments.
- **Open or shorted motor winding** — A motor winding failure prevents the module from spinning the rotor. Check winding resistance with a multimeter.
- **Faulty control board** — The furnace board sends a variable-speed command signal to the ECM module. If the board is not outputting that signal correctly, the motor will not respond.
- **Loose or corroded motor connector** — The 5-pin or 16-pin ECM connector at the motor module is a common failure point. Corrosion or a loose connection breaks the communication loop.
- **Incorrect motor speed profile stored** — On some Carrier systems, the speed profile is stored in the module. A power surge or failed previous motor can leave the module with a corrupt profile.

## Diagnosis Steps

1. Power off the furnace at the disconnect. Wait 60 seconds for the ECM module capacitors to discharge before touching connectors.
2. Locate the ECM blower motor in the bottom section of the air handler. Inspect the large rectangular module bolted to the motor end.
3. Check all motor connectors — unplug, inspect for corrosion, moisture, or bent pins. Reconnect firmly and restore power. If the fault clears, the connector was the problem.
4. At the motor module, measure the 120V or 240V AC supply voltage while the furnace is calling for heating. If power is present at the module but the motor doesn't run, the module or motor is failed.
5. Remove the motor from the blower housing. Use a multimeter on resistance mode to measure across each winding set. Open windings (OL reading) confirm motor winding failure.

## Fix

If the connectors are clean and seated, the fault is almost always the ECM module itself — not the motor. The module is sold separately from the motor and is significantly cheaper. Carrier, Bryant, and Payne furnaces use modules from Regal Beloit (formerly A.O. Smith) and GE. Match the module part number printed on the module label exactly — ECM modules are not interchangeable across motor frame sizes.

To replace the module: remove the two screws holding it to the motor end cap, unplug the two connectors, swap the replacement module, and reconnect. The motor itself does not need to be removed from the blower housing to replace the module.

If the motor winding has failed (open OL reading on any winding), replace the full motor assembly. Order by the motor's HP, RPM, frame size, and rotation direction — all printed on the motor nameplate.

After replacement, restore power and observe the blower operation through a full heating cycle. The Code 41 should clear on the first successful cycle.

## Parts

| Part | Where to Buy |
|------|-------------|
| [ECM motor module (match part number)](https://www.amazon.com/s?ascsubtag=ecf-carrier-41-error-code&k=ECM+motor+module+%28match+part+number%29&tag=errorcodefixes-20) | RepairClinic, Grainger |
| [ECM blower motor assembly](https://www.amazon.com/s?ascsubtag=ecf-carrier-41-error-code&k=ECM+blower+motor+assembly&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Motor control board](https://www.amazon.com/s?k=Motor+control+board&tag=errorcodefixes-20) | SupplyHouse, Grainger |

## When to Call a Technician

Diagnosing an ECM motor correctly requires understanding the difference between the motor and module — many techs replace the whole motor when only the module is failed. If you're not comfortable with electrical diagnosis or if this is a larger commercial system, have a licensed HVAC technician handle it. The repair itself (once diagnosed) is straightforward for a capable DIYer.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier Error Code 65 — Inducer Motor Fault](/posts/carrier-65-error-code/)
- [Carrier 31 Error Code — Pressure Switch Fix](/posts/carrier-31-error-code/)
- [Carrier 54 Error Code — Soft Lockout: Low Pressure Switch Open](/posts/carrier-54-error-code/)
- [Carrier 40MAQ / 40MVC Mini Split Error Codes — Causes & Fix](/posts/carrier-40maq-error-codes/)
