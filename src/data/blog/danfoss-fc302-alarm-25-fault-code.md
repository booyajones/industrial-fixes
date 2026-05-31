---
title: "Danfoss FC302 Alarm 25 - Causes & Fix"
description: "Alarm 25 on a Danfoss FC302 means brake resistor short circuit. Learn what it means, common causes, diagnostic steps, and parts."
pubDatetime: 2026-05-29T09:45:31Z
modDatetime: 2026-05-29T09:45:31Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - vfd
  - danfoss
---

## Danfoss FC302 Alarm 25 — What It Means

Alarm 25 on a Danfoss VLT AutomationDrive FC 302 indicates that the drive has detected a short circuit in the brake resistor circuit during operation. When this fault occurs, the drive disables the brake function to protect itself but continues to run. The brake function remains disabled until you clear the alarm and fix the underlying short circuit condition.

[Jump to Fix](#fix)

## Common Causes

- **Failed brake resistor with internal short** The brake resistor itself has developed an internal short circuit and no longer presents the correct resistance.
- **Shorted or damaged brake wiring** Cables between the drive and brake resistor have insulation damage, chafing, or conductor-to-conductor faults.
- **Incorrect wiring or loose connection fault** The braking circuit is wired incorrectly or loose conductors have contacted each other and caused a short.
- **Overheated or physically damaged resistor terminals** The resistor terminal block or connection points show signs of overheating or physical damage that created a short path.
- **Drive-side brake chopper or circuit issue** If the resistor and wiring test good, the internal braking circuit in the drive may have a fault, though this is less common.

## Step-by-Step Fix {#fix}

1. Remove power to the drive and lock out the supply before working on the braking circuit.
2. Inspect the brake resistor and all associated wiring for physical damage, overheating, chafing, burned insulation, or shorted terminals.
3. Disconnect the brake resistor leads from the drive and measure the resistor with a multimeter to check for a short circuit. Replace the resistor if it shows a dead short or reads far below its rated resistance.
4. Test the brake cable from the drive to the resistor for continuity to ground and conductor-to-conductor shorts. Repair or replace any damaged wiring.
5. Verify the brake circuit is wired correctly according to the drive manual and that parameter 2-15 Brake Check is configured properly for your brake monitoring setup.
6. Restore power and observe the drive. If the alarm clears, run a test cycle. If Alarm 25 persists with a known-good resistor and wiring, the internal braking circuit in the drive needs evaluation by qualified drive service personnel.
7. Document the resistor resistance values and cable test results in your maintenance log for future reference.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Brake resistor (Danfoss compatible, match your drive's rating) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-25-fault-code&k=Brake+resistor+%28Danfoss+compatible%2C+match+your+drive%27s+rating%29&tag=errorcodefixes-20) \| Primary replacement when the resistor tests shorted. Consult your FC 302 model documentation for the correct resistance and wattage rating. |
| Brake circuit wiring and terminals | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-25-fault-code&k=Brake+circuit+wiring+and+terminals&tag=errorcodefixes-20) \| Replace if insulation is damaged, conductors are shorted, or terminals show overheating or corrosion. |

## When to Call a Pro

Call a qualified VFD technician or Danfoss-certified service provider if the alarm persists after you have replaced the brake resistor and verified all wiring is intact and correctly installed. Internal drive faults in the brake chopper circuit require specialized diagnostic tools and knowledge of the FC 302 hardware. Also call a pro if you are not trained in lockout/tagout procedures or if your facility requires certified personnel for all VFD work.
