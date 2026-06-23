---
title: "ABB ACS580 A3A1 Fault - Causes & Fix"
description: "A3A1 means DC link overvoltage while the drive is stopped. Most often caused by incorrect supply voltage setting in parameter 95.01."
pubDatetime: 2026-06-21T10:35:01Z
modDatetime: 2026-06-21T10:35:01Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS580 brake chopper module"
most_likely_cause: "Incorrect supply voltage parameter setting"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check parameter 95.01 (Supply voltage) on the keypad and compare it to your actual incoming line voltage"
  - "Measure the AC line voltage at L1, L2, L3 with a multimeter to verify it matches the drive rating"
  - "Inspect the motor cable and supply line for power factor correction capacitors or surge absorbers"
no_buy_pct: "80%"
---

## ABB ACS580 A3A1 Fault — What It Means

The A3A1 fault on an ABB ACS580 indicates DC link overvoltage in the intermediate circuit while the drive is stopped. The drive has detected that the DC bus voltage exceeds the maximum safe threshold when it is not running. This is different from overvoltage faults that occur during deceleration or under load. If the supply voltage parameter is set incorrectly, the motor may rush uncontrollably on startup, or the brake chopper and resistor may be overloaded. The fault protects the drive from damage but signals a mismatch between expected and actual conditions.

## Before You Replace Anything

Technicians sometimes replace the brake chopper or capacitor bank first. Check parameter 95.01 and measure actual incoming line voltage with a multimeter before ordering any internal parts.

[Jump to Fix](#fix)

## Common Causes

- **Incorrect supply voltage parameter (~50%)** Parameter 95.01 is set higher than the actual incoming line voltage, causing the drive to interpret normal voltage as overvoltage.
- **Excessive incoming line voltage (~25%)** The actual power supply voltage is higher than the drive's rated value due to grid overvoltage or a transformer issue.
- **Power factor correction capacitors or surge absorbers (~15%)** Capacitors or surge absorbers on the motor cable or supply line create voltage spikes or unbalance that elevate the DC bus.
- **DC bus capacitor residual charge (~7%)** The DC bus capacitors retain charge after a recent stop due to a faulty discharge circuit or a power interruption.
- **Contactor switching transients (~3%)** Contactors opening and closing on the motor cable while the drive is stopped induce voltage transients on the DC link.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does parameter 95.01 match your actual incoming line voltage (measured with a multimeter at L1, L2, L3)?</summary>
<div class="dtree-body"><strong>Yes:</strong> The parameter is correct. Proceed to measure the actual line voltage to see if it is too high or if capacitors are present.<br><strong>No:</strong> Correct parameter 95.01 to match your supply voltage, power cycle the drive, and test. This fixes the fault in most cases.</div>
</details>

<details class="dtree"><summary>Is the measured line voltage more than 10% above the drive's rated voltage?</summary>
<div class="dtree-body"><strong>Yes:</strong> The supply voltage is excessive. Check the upstream transformer or grid feed and contact your utility or electrician.<br><strong>No:</strong> Line voltage is normal. Inspect for power factor correction capacitors, surge absorbers, or contactors on the motor cable.</div>
</details>

<details class="dtree"><summary>Are there power factor correction capacitors or surge absorbers installed on the motor cable or supply side?</summary>
<div class="dtree-body"><strong>Yes:</strong> Remove these components. They cause voltage unbalance and spikes that trigger the A3A1 fault.<br><strong>No:</strong> Check motor parameter group 99 for mismatches and verify no contactors are switching the motor while stopped. If all settings are correct, call a technician to test the DC bus discharge circuit.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Check parameter 95.01 (Supply voltage)** using the drive keypad or Drive Composer software and verify it matches your actual nominal incoming voltage (e.g., 480V, 400V, 230V).
2. **Measure the AC line voltage** at the drive input terminals L1, L2, and L3 with a calibrated multimeter to confirm the actual supply voltage.
3. **Correct parameter 95.01** if it does not match the measured line voltage, then power cycle the drive and reset the fault.
4. **Inspect the motor cable and supply line** for power factor correction capacitors or surge absorbers and remove any you find.
5. **Check for contactors** in the motor circuit that may be opening or closing while the drive is stopped and eliminate any switching transients.
6. **Verify motor data in parameter group 99** to confirm that startup parameters (voltage, current, power) match the motor nameplate exactly.
7. **Power cycle the drive** (disconnect power for at least 30 seconds to allow DC bus capacitors to discharge) and test. If the fault persists, contact a qualified technician to test the DC bus discharge circuit and internal brake chopper.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 brake chopper module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a3a1-fault-code&k=ABB+ACS580+brake+chopper+module&tag=errorcodefixes-20) \| Only if internal chopper circuit is verified faulty by a technician |
| DC bus capacitor bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a3a1-fault-code&k=DC+bus+capacitor+bank&tag=errorcodefixes-20) \| Only if capacitors are leaking or failing to discharge; requires professional diagnosis |

## When to Call a Pro

Call a professional if you have corrected parameter 95.01, confirmed the incoming line voltage is within spec, removed any external capacitors or surge absorbers, and the A3A1 fault still appears after a power cycle. A technician with ABB Drive Composer software and a multimeter can test the DC bus discharge circuit, measure the DC link voltage directly, and inspect the brake chopper and capacitor bank for internal faults. High-voltage DC bus work requires specialized training and safety equipment. Also call a pro if the incoming line voltage is persistently too high, as that requires coordination with your utility or an electrician to adjust the transformer tap or supply configuration.

**Rough cost:** A pro service call runs about $150-400 depending on the root cause and required corrections.

## See Also

- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS580 A2B1 Fault Code - Causes & Fix](/posts/abb-acs580-a2b1-fault-code/)
- [ABB ACS580 A5A0 Fault - Causes & Fix](/posts/abb-acs580-vfd-a5a0-fault-code/)
- [ABB ACS580 FF63 Fault - STO Diagnostics Failure Fix](/posts/abb-acs580-vfd-ff63-fault-code/)
