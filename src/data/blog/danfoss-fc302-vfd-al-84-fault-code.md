---
title: "Danfoss FC302 AL-84 Fault - Causes & Fix"
description: "AL-84 means communication loss between the drive and Local Control Panel (LCP). Most often the LCP is loose or unplugged. Reseat it first."
pubDatetime: 2026-06-23T10:02:16Z
modDatetime: 2026-06-23T10:02:16Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss LCP (Local Control Panel) for FC302"
most_likely_cause: "Disconnected or loose LCP module"
likelihood: "the most common cause"
diy_or_pro: "diy"
free_checks:
  - "Power down the drive, remove and firmly reseat the LCP in its slot, ensuring the locking tabs click into place."
  - "Perform a full power cycle (disconnect mains power for at least 30 seconds) to clear any transient communication faults."
  - "Inspect the LCP connector and cable for visible corrosion, bent pins, or physical damage, and clean with isopropyl alcohol if needed."
part_price: "$50-120 for a replacement LCP module (varies by model)"
no_buy_pct: "70%"
---

## Danfoss FC302 AL-84 Fault — What It Means

Error code 84 (AL-84 or Err 84) on a Danfoss FC302 VFD signals that the frequency converter has lost communication with the Local Control Panel (LCP), the physical keypad and display unit mounted on the drive. When this fault is active, the LCP cannot send commands or show real-time parameters like speed, current, or voltage. The drive itself may continue running if it was already configured and operating, but you lose all operator interface and monitoring capability. Unlike hardware faults such as overvoltage or motor shorts, AL-84 is primarily a connectivity or interface problem between the LCP module and the drive's logic board.

## Before You Replace Anything

Technicians sometimes replace the entire drive logic board when AL-84 appears, assuming the communication port is dead. Before ordering any board, reseat the LCP firmly and test with a known-good LCP unit if possible. Most AL-84 faults clear with a simple reconnection or cable replacement.

[Jump to Fix](#fix)

## Common Causes

- **Disconnected or Loose LCP (~45%)** The Local Control Panel module is physically unplugged from the drive's communication slot or the locking mechanism is not fully engaged, breaking the data link.
- **Damaged Communication Cable (~25%)** The internal cable connecting the LCP to the drive logic board has frayed insulation, corroded conductors, or broken wires, interrupting signal transmission.
- **Incorrect LCP Settings (~15%)** The LCP is configured with a mismatched baud rate or protocol in parameter 8-07, so the LCP and drive cannot understand each other's signals.
- **LCP Hardware Failure (~10%)** The LCP unit itself has a failed microcontroller, damaged display driver, or internal circuit defect that prevents it from communicating.
- **Drive Communication Interface Fault (~5%)** Rarely, the FC302's internal logic card or communication port is damaged by voltage spikes, moisture intrusion, or component failure.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the LCP display light up at all when power is applied?</summary>
<div class="dtree-body"><strong>Yes:</strong> The LCP has power but cannot talk to the drive. Check parameter 8-07 for correct protocol settings, then swap in a known-good LCP to isolate the fault.<br><strong>No:</strong> The LCP may have no power connection or is completely failed. Verify the LCP is fully seated, inspect the cable for damage, and test with a replacement LCP.</div>
</details>

<details class="dtree"><summary>Does reseating the LCP module and power cycling the drive clear the AL-84 fault?</summary>
<div class="dtree-body"><strong>Yes:</strong> The issue was a temporary poor connection or transient fault. Monitor for recurrence and secure the LCP locking tabs firmly.<br><strong>No:</strong> The fault is persistent. Proceed to test with a known-good LCP and inspect the internal cable and logic board communication port.</div>
</details>

<details class="dtree"><summary>Does the fault clear when you connect a different, known-good LCP to the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> The original LCP is defective. Replace the LCP module.<br><strong>No:</strong> The drive's logic card or communication interface is faulty. Inspect the logic board connector and replace the control PCB if the port is damaged.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down the drive completely** by disconnecting mains power and waiting at least 30 seconds for capacitors to discharge.
2. **Remove and inspect the LCP module** by releasing the locking tabs or screws, then examining the connector pins for corrosion, bent contacts, or debris.
3. **Reseat the LCP firmly** into the communication slot, ensuring the locking mechanism engages fully and the module sits flush against the drive.
4. **Inspect the internal cable** (if accessible) that runs from the LCP port to the logic board, looking for frayed insulation, broken conductors, or signs of overheating.
5. **Verify parameter 8-07** (Communication Protocol) settings in the drive's parameter list to confirm the baud rate and protocol match the LCP requirements (consult the FC302 manual for your specific LCP model).
6. **Swap in a known-good LCP** if available, power up the drive, and check whether AL-84 clears. If it does, the original LCP is faulty and must be replaced.
7. **Test the drive logic board** by examining the communication port on the board for physical damage, burn marks, or loose solder joints. If the port is damaged and a new LCP does not resolve the fault, replace the logic or control PCB.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss LCP (Local Control Panel) for FC302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-84-fault-code&k=Danfoss+LCP+%28Local+Control+Panel%29+for+FC302&tag=errorcodefixes-20) \| Verify compatibility with your FC302 model and firmware version before ordering. |
| LCP Communication Cable (Internal) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-84-fault-code&k=LCP+Communication+Cable+%28Internal%29&tag=errorcodefixes-20) \| Replacement cable for the link between the LCP port and drive logic board, if accessible and serviceable. |
| FC302 Logic/Control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-84-fault-code&k=FC302+Logic%2FControl+PCB&tag=errorcodefixes-20) \| Required only if the communication port on the drive is physically damaged and a new LCP and cable do not resolve the fault. |

## When to Call a Pro

Call a qualified drives technician or industrial electrician if reseating the LCP, checking cables, and verifying parameter settings do not clear AL-84. Replacing the drive's logic board or control PCB requires knowledge of VFD internal wiring, static discharge precautions, and firmware compatibility. A pro will have diagnostic tools to test the communication interface voltage levels and signal integrity, and can source the correct replacement board for your drive's firmware revision. If the drive is under warranty or mission-critical, always involve the manufacturer or an authorized service center to avoid voiding coverage or introducing new faults.

**Rough cost:** DIY runs about $0-150 in parts (if LCP or cable needed), 15-45 min. A pro service call runs about $100-250 service call plus parts.

## See Also

- [Danfoss FC302 VFD ALARM 57 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-57-fault-code/)
- [Danfoss FC302 VFD AL-154 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-154-fault-code/)
- [Danfoss FC302 AL-93 - Causes & Fix](/posts/danfoss-fc302-vfd-al-93-fault-code/)
- [Danfoss FC302 AL-72 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-72-fault-code/)
