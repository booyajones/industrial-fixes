---
title: "Danfoss FC302 WARNING 77 - Causes & Fix"
description: "WARNING 77 means the VFD entered reduced-power mode to protect itself. Most often caused by overtemperature or input voltage imbalance."
pubDatetime: 2026-06-22T10:28:55Z
modDatetime: 2026-06-22T10:28:55Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 replacement cooling fan or heat sink fan assembly"
most_likely_cause: "overtemperature due to blocked vents or failed cooling fans"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Clear all intake and exhaust vents of dust and debris"
  - "Verify all cooling fans are running when the drive is powered"
  - "Measure three-phase input voltages with a voltmeter to confirm imbalance is under 3 percent"
part_price: "$60-150 for replacement cooling fan or heat sink fan assembly"
no_buy_pct: "60%"
---

## Danfoss FC302 WARNING 77 — What It Means

WARNING 77 indicates the Danfoss FC302 frequency converter has entered reduced power mode to prevent thermal damage or stress. This is a warning, not a fault or trip, so the motor continues running but the drive automatically limits output current and power. The condition is triggered when internal sensors detect overtemperature (heat sink or ambient air too hot) or input voltage imbalance exceeding 3 percent. The drive does not require immediate shutdown unless the warning persists after corrective action.

## Before You Replace Anything

Technicians sometimes suspect a failed rectifier section or control board, but input voltage imbalance and blocked vents account for most WARNING 77 events. Always measure three-phase input voltage and check fan operation before ordering power modules.

[Jump to Fix](#fix)

## Common Causes

- **Overtemperature from blocked vents or failed fans (~45%)** Heat sink temperature rises when intake or exhaust vents are clogged with dust, the drive is mounted too close to other heat sources, or cooling fans have failed.
- **Input voltage imbalance exceeding 3 percent (~35%)** Three-phase input voltages differ by more than 3 percent due to loose input connections, damaged rectifier diodes, or unbalanced mains supply.
- **Incorrect motor data in parameters 120 through 125 (~10%)** Motor rated current, voltage, or speed entered incorrectly causes the drive to misjudge thermal limits and enter reduced power mode during normal operation.
- **Ambient temperature exceeds drive rating (~7%)** Enclosure or room temperature exceeds 40 degrees Celsius (or the specified limit for your model) and the drive cannot dissipate heat fast enough.
- **External fan not configured in parameter 1-91 (~3%)** If an external motor cooling fan is installed but parameter 1-91 is not set to 1, the drive does not account for the extra cooling and may over-protect the motor.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Are all cooling fans running when the drive is powered on?</summary>
<div class="dtree-body"><strong>Yes:</strong> Fans are working. Proceed to check input voltage balance and vent blockage.<br><strong>No:</strong> A failed fan is causing overtemperature. Replace the fan assembly and clear any debris from the heat sink.</div>
</details>

<details class="dtree"><summary>Is the three-phase input voltage imbalance less than 3 percent (for example 400 V plus or minus 12 V)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Input voltage is balanced. Focus on cooling, ambient temperature, and motor parameter settings.<br><strong>No:</strong> Voltage imbalance is too high. Check for loose input terminals or contact your utility; if imbalance persists swap input phases and retest to isolate whether the problem is in the mains or the rectifier.</div>
</details>

<details class="dtree"><summary>Do parameters 1-20 through 1-25 match the actual motor nameplate (rated current, voltage, speed)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor data is correct. Run AMA (parameter 1-29 set to 1) to optimize thermal protection.<br><strong>No:</strong> Incorrect motor data is causing the drive to miscalculate power limits. Enter correct nameplate values and run AMA.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Measure three-phase input voltage** using a volt meter at the drive's input terminals and calculate the percent imbalance (maximum deviation divided by average voltage). If imbalance exceeds 3 percent, tighten all input connections and swap phases to determine whether the problem follows the wire (mains supply issue) or stays in the same position (rectifier fault).
2. **Inspect all cooling fans** while the drive is powered. Confirm every fan spins freely and moves air. Replace any failed fan or heat sink assembly.
3. **Clear intake and exhaust vents** of dust, paper, and debris. Check that the drive is mounted on an unpainted metal surface with at least 10 cm clearance above and below for airflow.
4. **Verify motor parameters** 1-20 through 1-25 match the motor nameplate values (rated current, voltage, frequency, speed). Correct any mismatches.
5. **Run Automatic Motor Adaptation (AMA)** by setting parameter 1-29 to 1. If an external motor fan is used, set parameter 1-91 to 1 before running AMA.
6. **Power cycle the drive** by removing mains power for at least five seconds, then reconnecting. Monitor the display for WARNING 77.
7. **Monitor ambient temperature** with a thermometer near the drive. If temperature exceeds 40 degrees Celsius or the drive's specification, improve ventilation or relocate the drive to a cooler location.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 replacement cooling fan or heat sink fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-77-fault-code&k=Danfoss+FC302+replacement+cooling+fan+or+heat+sink+fan+assembly&tag=errorcodefixes-20) \| Verify fan voltage (typically 24 VDC or 230 VAC) and mounting pattern from the drive service manual before ordering. |
| Three-phase line reactor or input choke | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-77-fault-code&k=Three-phase+line+reactor+or+input+choke&tag=errorcodefixes-20) \| Used when input voltage imbalance cannot be corrected at the mains; consult Danfoss sizing tables for your drive frame. |

## When to Call a Pro

Call a qualified technician or Danfoss service partner if WARNING 77 persists after you have cleared vents, confirmed fan operation, and verified input voltage balance. High-voltage troubleshooting of the rectifier section and internal temperature sensors requires specialized test equipment and familiarity with VFD power modules. If swapping input phases shows the low-current phase stays in the same position (indicating a rectifier fault rather than a mains problem), the drive will need internal repair or module replacement. Similarly, if ambient conditions are within specification but the drive continues to enter reduced power mode, an internal heat sink sensor or control board fault is likely.

**Rough cost:** A pro service call runs about $150-400 for cleaning, fan replacement, and voltage correction.

## See Also

- [Danfoss FC302 AL-123 Fault Code - Causes & Fix](/posts/danfoss-fc302-vfd-al-123-fault-code/)
- [Danfoss FC302 AL-98 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-98-fault-code/)
- [Danfoss VLT AL 4 Fault - Causes & Fix](/posts/danfoss-vlt-vfd-al-4-fault-code/)
- [Danfoss FC302 Alarm 13 - Causes & Fix](/posts/danfoss-fc302-vfd-al-137-fault-code/)
