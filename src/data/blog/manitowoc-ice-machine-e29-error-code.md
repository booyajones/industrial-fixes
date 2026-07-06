---
title: "Manitowoc E29 Error Code - Causes & Fix"
description: "E29 means USB Communication Fault. The control board can't talk to the USB drive. Replace the USB drive or reseat the connection."
pubDatetime: 2026-06-20T12:38:30Z
modDatetime: 2026-06-20T12:38:30Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - manitowoc
money_part: "Compatible USB flash drive"
most_likely_cause: "Defective or corrupted USB drive"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Remove the USB drive, inspect it for physical damage, and reseat it firmly in the port"
  - "Power off the machine for 10 seconds, then power it back on to see if the error clears"
part_price: "$10-30 for a compatible USB flash drive"
no_buy_pct: "40%"
---

## Manitowoc E29 Error Code — What It Means

The Manitowoc E29 error code indicates a USB Communication Fault. This means the control board cannot exchange data with the USB drive used for logging or service diagnostics. The error appears in the event log and often correlates with low ice production, though the fault itself is strictly a communication failure between the board and the USB interface.

This code is specific to Manitowoc ice machines, particularly the Indigo and Indigo NXT series. Unlike process faults (such as E01 for long freeze or E20 for water system issues), the E29 is a data link failure. The machine may continue to run, but service logs will not record properly, and concurrent production issues may be masked.

## Before You Replace Anything

Technicians sometimes replace the control board when the USB drive itself is simply corrupted or incompatible. Always test a known-good USB drive first before condemning the board.

[Jump to Fix](#fix)

## Common Causes

- **Defective or corrupted USB drive (~50%)** The flash drive itself is physically damaged, corrupted, or incompatible with the control board's logging system.
- **Loose or open USB port connection (~25%)** The USB port or internal ribbon cable connecting the port to the control board is loose, corroded, or has an open circuit.
- **Failed control board USB port (~15%)** The USB port on the control board has failed electronically and cannot read the drive signal.
- **Incompatible USB drive type (~7%)** The drive is not factory-compatible in form factor or capacity, causing the board to reject communication.
- **Control board failure (~3%)** The control board itself is defective and cannot process USB communication even with a good drive and port.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the USB drive show any physical cracks, bent contacts, or corrosion?</summary>
<div class="dtree-body"><strong>Yes:</strong> The drive is likely damaged. Replace it with a known-good, compatible USB flash drive and retest.<br><strong>No:</strong> The drive may be corrupted or incompatible. Try a different USB drive or proceed to check the port connection.</div>
</details>

<details class="dtree"><summary>Does the error clear after removing and reseating the USB drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The connection was loose. Monitor the machine to confirm the error does not return.<br><strong>No:</strong> The port, ribbon cable, or control board is likely at fault. Call a technician to test the board and port.</div>
</details>

<details class="dtree"><summary>Does the machine also show low ice production in the event log?</summary>
<div class="dtree-body"><strong>Yes:</strong> The USB fault may be secondary to a broader system issue. Address the E29 first, then troubleshoot production separately.<br><strong>No:</strong> The fault is isolated to the USB interface. Focus on the drive, port, and board connections.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power off the machine** and wait 10 seconds to safely access the USB port.
2. **Remove the USB drive** from the port and inspect it for physical damage, cracks, or bent pins.
3. **Replace the drive** with a known-good, factory-compatible USB flash drive and reseat it firmly in the port.
4. **Power the machine back on** by turning the selector to 'On' or 'Ice' and check if the E29 error clears from the display or event log.
5. **Inspect the USB port and internal ribbon cable** (if accessible) for loose connections, corrosion, or breaks in the circuit.
6. **Access the event log** through the service menu to confirm whether the error persists with the new drive.
7. **Replace the control board** if a known-good drive and secure connections still produce the E29 fault, indicating a failed USB port or board logic.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Compatible USB flash drive | Amazon \| Standard small-form USB drive, typically 2GB to 8GB capacity, factory-compatible type |
| Manitowoc control board (display membrane interface board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e29-error-code&k=Manitowoc+control+board+%28display+membrane+interface+board%29&tag=errorcodefixes-20) \| Required if the USB port or board logic has failed |
| Ribbon cable (USB port to control board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e29-error-code&k=Ribbon+cable+%28USB+port+to+control+board%29&tag=errorcodefixes-20) \| Needed if the internal cable shows an open circuit or damage |

## When to Call a Pro

Call a professional service technician if replacing the USB drive and reseating the connection do not clear the error. Diagnosing a failed control board or internal ribbon cable requires access to the machine's service panels, specialized knowledge of the Indigo control system, and tools to test board signals. If the error appears alongside low ice production, a technician can also check refrigerant charge, water flow, and other system parameters that may be contributing to the log event. Control board replacement is a moderately complex repair that should be done by someone trained in commercial refrigeration to avoid damaging the new board or missing concurrent faults.

**Rough cost:** A pro service call runs about $150-400 depending on whether the drive, port, or control board is replaced.

## See Also

- [Manitowoc Ice Machine Error Code 10 — Ice Full Sensor Causes & Fix](/posts/manitowoc-ice-machine-error-code-10/)
- [Manitowoc E33 Error Code - Causes & Fix](/posts/manitowoc-ice-machine-e33-error-code/)
- [Manitowoc Ice Machine E04 Error: High Condenser Temperature Causes and Fix](/posts/manitowoc-e04-high-condenser-temp/)
- [Manitowoc Ice Machine Error Code 9 — Causes & Fix](/posts/manitowoc-ice-machine-error-code-9/)
