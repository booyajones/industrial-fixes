---
title: "Danfoss FC302 VFD AL-126 - Causes & Fix"
description: "AL-126 is not a valid Danfoss FC302 code. You likely see AL 38 sub-code 126 (internal control fault). Power cycle 10 min, reseat logic card."
pubDatetime: 2026-06-24T10:22:01Z
modDatetime: 2026-06-24T10:22:01Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control Card (Logic Board)"
most_likely_cause: "control card (logic board) failure or firmware corruption"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Power down the drive completely for 10 minutes, then restart to clear transient memory faults"
  - "Check parameter 15-32 on the keypad for extended alarm details"
  - "Remove and reseat the control card connectors to eliminate loose or corroded pins"
part_price: "$250-500 for a replacement control card"
no_buy_pct: "30%"
---

## Danfoss FC302 VFD AL-126 — What It Means

The Danfoss FC302 does not have an alarm code numbered AL-126 in its official fault list. All documented FC302 alarms fall between AL 1 and AL 90. If your display shows a three-digit number like 126, you are most likely seeing AL 38 with sub-code 126. AL 38 is an internal fault that points to a problem inside the drive's control logic, firmware, memory, or hardware components such as the logic card, power board, or IGBT module. The sub-code 126 is a specific internal diagnostic identifier used by Danfoss for advanced troubleshooting and typically indicates a control board memory error, firmware corruption, or logic card failure.

Because AL 38 is an internal fault, the drive has detected a failure in its own circuitry rather than an external wiring or motor problem. Common triggers include corrupted firmware from a power interruption during an update, a failed control card, voltage spikes damaging the logic circuitry, moisture or dust causing connector corrosion, or instability in the power board affecting the control logic. The drive will not operate until the internal fault is cleared by either a successful power cycle or replacement of the faulty internal component.

## Before You Replace Anything

Technicians sometimes replace the entire power board or IGBT module when the real fault is a loose or corroded connector on the control card. Always reseat the logic board and check parameter 15-32 for extended diagnostic codes before swapping expensive power electronics.

[Jump to Fix](#fix)

## Common Causes

- **Control card (logic board) failure (~40%)** Corrupted firmware, memory error, or hardware malfunction in the drive's main control circuitry triggers AL 38 with internal diagnostic sub-codes.
- **Firmware corruption (~25%)** Power interruptions during firmware updates or voltage transients can corrupt the drive's operating software and lock it into an internal fault state.
- **Loose or corroded connector (~15%)** Moisture, dust, or vibration can cause poor contact between the control card and its mating connectors, generating false internal fault codes.
- **Power board instability (~10%)** Failing DC link capacitors or degraded IGBT modules can send unstable signals to the control logic, triggering internal fault protection.
- **Voltage spike damage (~7%)** Lightning strikes or utility switching transients can damage sensitive logic circuitry on the control card without destroying the entire drive.
- **Environmental contamination (~3%)** Conductive dust or chemical vapors can create current leakage paths on the control card, causing erratic behavior and internal faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after a 10-minute power-down and restart?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was a transient memory or logic error. Monitor the drive for recurrence and consider updating firmware to the latest version.<br><strong>No:</strong> The fault is persistent. Proceed to reseat the control card and check for connector corrosion.</div>
</details>

<details class="dtree"><summary>Does parameter 15-32 show any extended diagnostic information?</summary>
<div class="dtree-body"><strong>Yes:</strong> Note the extended code and consult Danfoss Table 9.4 in the operating guide for the specific internal fault definition. This will guide component-level diagnosis.<br><strong>No:</strong> The fault remains generic. Move to control card reseating and replacement testing.</div>
</details>

<details class="dtree"><summary>After reseating the control card, does the fault persist?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control card or power board has a hardware failure. Replace the control card first, then test the power board if the fault remains.<br><strong>No:</strong> The issue was a loose or corroded connector. Clean contacts with electronics cleaner and secure all connections.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off mains power** to the drive and wait 10 minutes for all internal capacitors to discharge before touching any circuitry.
2. **Restart the drive** and observe whether the AL 38 sub-code 126 fault clears. Many transient internal faults resolve after a full power cycle.
3. **Check parameter 15-32** on the keypad display for extended alarm code details that may refine the diagnosis beyond the generic internal fault message.
4. **Remove the control card** by unlatching the plastic retaining clips and disconnecting all ribbon cables and terminal connectors from the logic board.
5. **Inspect all connectors** for corrosion, bent pins, or dust buildup. Clean contacts with electronics contact cleaner and reseat the card firmly.
6. **Update or reload firmware** if you suspect corruption. Download the latest firmware version from the Danfoss website and follow the upload procedure in the operating guide.
7. **Swap in a replacement control card** if the fault persists after reseating and firmware update. Source a genuine Danfoss logic board matching your drive frame size and voltage rating.
8. **Test the power board** if a new control card does not clear the fault. Check DC bus voltage and inspect IGBT modules for shorts to ground using a megohm meter.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control Card (Logic Board) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-126-fault-code&k=Danfoss+FC302+Control+Card+%28Logic+Board%29&tag=errorcodefixes-20) \| Match your drive frame size (A, B, C, D, E) and firmware version. Available from Danfoss or Wake Industrial. |
| Danfoss FC302 Power Board (Rectifier/IGBT Module) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-126-fault-code&k=Danfoss+FC302+Power+Board+%28Rectifier%2FIGBT+Module%29&tag=errorcodefixes-20) \| Only replace if control card swap does not clear the fault and DC bus voltage is unstable or IGBTs test shorted. |

## When to Call a Pro

Call a qualified VFD technician or contact your local Danfoss supplier if the fault persists after a full power cycle, control card reseating, and firmware update. Internal faults on the FC302 often require component-level diagnostics with specialized test equipment to isolate failures in the power board, IGBT modules, or gate driver circuits. Professional repair or factory service is necessary if you lack experience working inside variable frequency drives or if your facility does not allow in-house repair of high-voltage industrial electronics. Danfoss provides technical support and can arrange for authorized service centers to perform board-level repair or drive replacement under warranty.

**Rough cost:** A pro service call runs about $300-800 for control card replacement and diagnostics.
