---
title: "Carrier 42 Error Code — Causes & Fix"
description: "What Carrier error code 42 means, why the inducer motor faults, and how to fix it step by step."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - carrier
---

## Carrier 42 Error Code — What It Means

Carrier code 42 is an **inducer motor fault** — the control board fired the inducer but didn't see the expected speed feedback or pressure switch closure within the startup window. The inducer (draft motor) must pull combustion gases before ignition begins; if it fails to prove airflow, the board locks out to prevent unsafe combustion. You'll see 4 long flashes followed by 2 short flashes on the status LED.

[Jump to Fix](#fix)

## Common Causes

- **Failed inducer motor** — Bearings seize or windings burn out, motor doesn't reach operating speed; most common cause on units over 10 years old.
- **Blocked flue or condensate** — Partially blocked exhaust vent or condensate line creates back pressure that prevents the pressure switch from closing even when the motor runs.
- **Faulty draft pressure switch** — The hose, port, or diaphragm on the pressure switch fails; motor runs fine but switch never proves.
- **Defective control board** — Board doesn't send proper voltage to the inducer or misreads the tach signal.

## Step-by-Step Fix {#fix}

1. **Check the flue and intake pipes** — Inspect both PVC pipes (on 90%+ units) or the metal flue collar for blockages: bird nests, ice, debris. Clear any obstruction.
2. **Listen to the inducer on call for heat** — Motor should spin up before the ignitor glows. If silent, check 120V at the inducer connector with a multimeter; present voltage + no spin = bad motor.
3. **Inspect the pressure switch hose** — Remove the small rubber hose between the inducer housing and pressure switch. Look for cracks, kinks, or condensate pooling. Blow it clear with compressed air.
4. **Test the pressure switch** — With the inducer running, use a manometer or jumper the switch terminals momentarily. If jumping clears the fault, replace the switch.
5. **Reset the system** — Cut power at the disconnect for 30 seconds, restore, and call for heat. Confirm LED shows solid green or normal flash pattern.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Inducer motor assembly](https://www.amazon.com/s?k=Inducer%20motor%20assembly&tag=errorcodefixe-20) | Match HP and RPM to model; Carrier OEM or aftermarket (Fasco, Rotom) |
| [Draft pressure switch](https://www.amazon.com/s?k=Draft%20pressure%20switch&tag=errorcodefixe-20) | Single or dual-port; verify cracking pressure spec on the label |
| [Pressure switch hose](https://www.amazon.com/s?k=Pressure%20switch%20hose&tag=errorcodefixe-20) | Standard 3/16" or 1/4" silicone tubing |

## When to Call a Pro

If the flue is clear, the switch tests good, and the motor runs but the fault persists, the control board may have a failed tach input circuit. Board replacement requires verifying compatibility and should be done by a licensed technician on systems still under warranty.
