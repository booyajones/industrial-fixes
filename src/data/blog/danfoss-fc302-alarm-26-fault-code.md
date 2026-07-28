---
title: "Danfoss FC302 ALARM 26 - Causes & Fix"
description: "ALARM 26 on Danfoss FC302 means brake resistor power limit exceeded. Learn causes, diagnostic steps, and fixes for this VFD fault."
pubDatetime: 2026-05-29T09:46:07Z
modDatetime: 2026-05-29T09:46:07Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss brake resistor"
most_likely_cause: "Brake resistor undersized for the application"
---

## What this code means
ALARM 26 on the Danfoss VLT AutomationDrive FC 302 (and FC 301) indicates brake resistor power limit or brake overload. The drive continuously calculates the braking power being dissipated in the brake resistor using a mean value over the last 120 seconds of run time, based on DC-link voltage and the brake resistor value you entered in parameter 2-16 AC Brake Max. Current. The alarm activates when dissipated braking power exceeds 90% of the configured brake resistor power limit. If parameter 2-13 Brake Power Monitoring is set to trip, the drive will shut down when braking power reaches 100% of the limit.

This fault does not mean the brake resistor has failed electrically in most cases. It means the resistor is being asked to dissipate more thermal energy than it can handle safely over time. The drive is protecting the resistor (and itself) from thermal damage by warning you or tripping before the resistor overheats or burns out.

## Common Causes

- **Brake resistor undersized for the application** The installed resistor does not have enough power or thermal capacity for the actual deceleration energy or duty cycle your machine demands.
- **Excessive braking energy from short deceleration ramps** Very short ramp-down times or frequent stop/start cycling force the resistor to absorb energy faster than it can dissipate heat.
- **Incorrect brake resistor parameter settings** The drive's brake current or resistor data (especially parameter 2-16) does not match the actual installed resistor, causing false or premature alarm calculation.
- **Brake resistor wiring fault or poor connection** Loose terminals, broken leads, or heat-damaged wiring prevent effective energy dissipation or cause abnormal measurement by the drive.
- **Application demands exceed hardware rating** The machine is commanded to brake too hard or too often for the brake resistor installed, regardless of resistor condition.

## Step-by-Step Fix {#fix}

1. Confirm the fault code is ALARM 26 and not a different brake alarm such as Alarm 27 (Brake IGBT fault) by checking the drive display or event log.
2. Check parameter 2-13 Brake Power Monitoring to see if it is set to warning or trip, and review parameter 2-16 AC Brake Max. Current to verify it matches your installed brake resistor's specifications.
3. Inspect the brake resistor assembly and all wiring for loose or corroded terminals, heat discoloration, charring, broken leads, or physical damage to the resistor body.
4. Measure the resistance of the brake resistor with a multimeter (drive powered off and resistor disconnected) and compare it to the nameplate or datasheet value to confirm the resistor is not open or shorted.
5. Review your application duty cycle and deceleration ramp settings (parameter group 3-4x) to determine if braking demand is excessive, and lengthen deceleration ramps if the process allows.
6. Correct the brake resistor parameter data in the drive if the installed resistor does not match what the drive expects, or replace the resistor with a correctly sized unit if it is undersized or damaged.
7. Clear the alarm, test the machine under normal operating conditions, and monitor parameter readouts or alarm history to verify braking power stays below 90% of the limit during typical cycles.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss brake resistor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-26-fault-code&k=Danfoss+brake+resistor&tag=errorcodefixes-20) \| Match frame size and power rating to your FC 302 model and application duty cycle (consult Danfoss sizing tables or your original installation documentation). |
| Brake resistor terminals and connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-alarm-26-fault-code&k=Brake+resistor+terminals+and+connectors&tag=errorcodefixes-20) \| Replace if heat-damaged, corroded, or loose after inspection. |

## When to Call a Pro

Call a qualified technician or Danfoss service partner if the alarm persists after you have verified correct resistor sizing, wiring integrity, and parameter settings. If the brake resistor tests good and the application duty cycle is within normal limits but the drive continues to trip, the internal brake chopper circuit or brake monitoring path may be faulty and will require drive-level diagnostics or hardware replacement. Also call a professional if you are unsure how to safely measure DC-link components, interpret drive parameters, or size a replacement brake resistor for your specific load and deceleration profile.
