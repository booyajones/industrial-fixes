---
title: "ABB ACS580 A5A1 Fault - Causes & Fix"
description: "A5A1 means the drive lost cooling fan feedback. Most often a failed fan motor or loose wiring. Check fan spin and connections first."
pubDatetime: 2026-06-21T10:39:50Z
modDatetime: 2026-06-21T10:39:50Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB ACS580 cooling fan assembly"
most_likely_cause: "failed fan motor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive off and back on, then reset the fault to see if the fan starts and the fault clears"
  - "Visually confirm whether the fan is spinning when the drive is powered on"
  - "Inspect the fan connector at the control board for loose or corroded pins"
---

## ABB ACS580 A5A1 Fault — What It Means

The A5A1 fault on an ABB ACS580 drive means the internal control system cannot detect the expected feedback signal from one of the cooling fans while that fan should be running. The drive supplies power to the fan and monitors a return signal to confirm the fan is spinning. When that signal is absent, the drive throws A5A1 to protect itself from overheating.

The auxiliary code displayed alongside A5A1 tells you which fan is affected. Code 0 indicates Main Fan 1 (the primary cooling fan). Other codes point to secondary or auxiliary fans if your unit has them. The fault does not mean the drive is too hot yet, but it cannot continue to run safely without cooling.

## Before You Replace Anything

Technicians sometimes replace the control board when the fan itself is simply jammed or has failed mechanically. Always verify the fan spins freely by hand and measure 24VDC at the fan terminals before ordering a new control board.

[Jump to Fix](#fix)

## Common Causes

- **Failed fan motor (~45%)** The fan windings are burnt, bearings are seized, or the fan is physically damaged and no longer spins.
- **Loose or disconnected wiring (~30%)** The harness connecting the fan to the control board is loose, corroded, or has broken strands.
- **Blown fuse or power supply issue (~15%)** The 24VDC supply feeding the fan circuit is interrupted or a fuse protecting the fan is blown.
- **Failed fan driver circuit on control board (~8%)** The logic circuit that monitors fan feedback or supplies power to the fan is defective.
- **Transient glitch or false alarm (~2%)** A momentary signal dropout or noise spike caused the fault even though the fan is working normally.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fan spin when the drive is powered on?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fan motor is working. The problem is likely a feedback wiring issue or a failed driver circuit on the control board.<br><strong>No:</strong> The fan motor is likely dead or it is not receiving power. Check wiring and voltage at the fan terminals next.</div>
</details>

<details class="dtree"><summary>Do you measure 24VDC at the fan terminals with the drive on?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power is reaching the fan but the fan is not spinning. Replace the fan assembly.<br><strong>No:</strong> No power is reaching the fan. Check the wiring harness and connectors. If wiring is good, the control board power output or fuse is faulty.</div>
</details>

<details class="dtree"><summary>Did the fault clear after a power cycle and reset?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue may have been a transient glitch. Monitor the drive. If the fault returns, proceed with physical inspection.<br><strong>No:</strong> The fault is persistent. Proceed with visual and electrical checks of the fan and wiring.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Note the auxiliary code** displayed with A5A1 to identify which fan is affected (code 0 is Main Fan 1).
2. **Power cycle the drive** by turning it off, waiting for the display to clear completely, then powering it back on and resetting the fault to see if the fan restarts.
3. **Visually inspect the fan** while the drive is powered on (observing all lockout-tagout and electrical safety procedures) to confirm whether it is spinning.
4. **Open the control compartment** (after proper lockout) and check that the fan connector at the control board is fully seated and pins are not corroded or bent.
5. **Measure voltage at the fan terminals** using a multimeter set to DC volts. You should see 24VDC when the drive is on and calling for fan operation.
6. **Replace the fan assembly** if the fan does not spin and 24VDC is present at the terminals, indicating the fan motor itself has failed.
7. **Replace the control board** if the fan is good, wiring is secure, and no 24VDC is present at the fan, pointing to a failed driver circuit or blown internal fuse. Contact ABB or an authorized service center for board replacement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB ACS580 cooling fan assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a5a1-fault-code&k=ABB+ACS580+cooling+fan+assembly&tag=errorcodefixes-20) \| Match the part number on your existing fan or consult your drive frame size and model documentation. |
| ABB ACS580 control board (NINT-xx series) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-a5a1-fault-code&k=ABB+ACS580+control+board+%28NINT-xx+series%29&tag=errorcodefixes-20) \| Only if fan and wiring are confirmed good but no 24VDC output is present. Verify part number with ABB. |

## When to Call a Pro

Call a qualified technician or ABB service partner if you are not trained to work on variable frequency drives. These units operate at high voltage and require lockout-tagout procedures. If you are unsure how to measure DC voltage safely or how to access the control compartment, do not attempt the repair yourself. Also call a pro if the fan and wiring check out but the control board appears to be at fault, since board-level diagnosis and replacement require specialized knowledge and calibration.

**Rough cost:** A pro service call runs about $200-500 for fan replacement and labor, more if control board is involved.

## See Also

- [ABB ACS880 Fault 2310 - Overcurrent Diagnosis and Fix](/posts/abb-acs880-fault-2310/)
- [ABB ACS580 A0 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-a0-fault-code/)
- [ABB ACS550 EFB 2 Fault - Causes & Fix](/posts/abb-acs550-vfd-efb2-fault-code/)
- [ABB ACS550 EFB3 Fault - Causes & Fix](/posts/abb-acs550-efb3-fault-code/)
