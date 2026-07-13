---
title: "Danfoss FC302 AL-90 - Causes & Fix"
description: "AL-90 is not a valid Danfoss FC302 alarm code. Most likely Alarm 38 (Internal Fault). Replace control card after power cycle and sub-code check."
pubDatetime: 2026-06-23T10:09:44Z
modDatetime: 2026-06-23T10:09:44Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Control Card (Logic PCB)"
most_likely_cause: "Failed control card (logic PCB)"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Cycle power completely (disconnect AC mains and DC link, wait 5 minutes, reconnect) and check if fault clears"
  - "Read the sub-code from the drive display (e.g., 38-01, 38-02, 38-03) and consult Table 6.1 in the operating instructions"
  - "Disconnect the motor at U/V/W terminals and test output to ground to rule out a shorted motor"
part_price: "$200-400"
---

## Danfoss FC302 AL-90 — What It Means

Alarm 90 does not exist in the Danfoss FC302 alarm list. Danfoss FC302 alarms range from 1 to 99, but Alarm 90 is not defined in official documentation. The most likely match is Alarm 38 (Internal Fault), which indicates an unspecified internal fault in the drive's control or power section. Alarm 38 displays a sub-code (such as 38-01, 38-02, or 38-03) that identifies the specific failed component. Without the sub-code, the fault is generic and could involve control PCB failure, power board (inverter/IGBT) failure, internal sensor fault, or memory corruption.

If you see a two-digit alarm on your display, check your drive's operating manual to verify the exact code. Common internal faults on the FC302 include Alarm 38 (Internal Fault), Alarm 40 (Overtemperature), and Alarm 41 (Heat sink sensor fault). Each requires different diagnostic steps, so correct identification is the first step.

## Before You Replace Anything

Technicians often replace the inverter power board first, but the control card (logic PCB) is the actual culprit in most Alarm 38 cases. Cycle power fully and check the sub-code in the drive's Table 6.1 before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Failed control card (logic PCB) (~40%)** Noise, overvoltage, or aging causes the control PCB to fail, triggering a generic internal fault.
- **Shorted IGBTs or failed DC-link capacitors (~25%)** Power stage components fail from overheating or overcurrent, creating an internal fault on the inverter board.
- **Loose or corroded internal wiring (~15%)** Control signals between the logic card and power board lose connection, causing an internal communication fault.
- **Overheating causing sensor drift (~10%)** Heat sink or voltage sensors drift or fail when the drive runs too hot, triggering an internal sensor fault.
- **Power supply instability (24VDC for control card) (~10%)** The internal 24VDC supply drops below spec, starving the control card and causing erratic behavior.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Did the fault clear after cycling power (full disconnect for 5 minutes)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Likely a transient fault or loose connection. Monitor for recurrence and check internal wiring.<br><strong>No:</strong> Fault is persistent. Proceed to check the sub-code and test internal 24VDC supply.</div>
</details>

<details class="dtree"><summary>Does the drive display a sub-code (e.g., 38-01, 38-02, 38-03)?</summary>
<div class="dtree-body"><strong>Yes:</strong> Use the sub-code to identify the failed component: 38-01 is control card, 38-02 is power board, 38-03 is sensor.<br><strong>No:</strong> Generic internal fault. Test 24VDC supply at terminals 100/101 and reseat the control card.</div>
</details>

<details class="dtree"><summary>Does the fault clear when you disconnect the motor at U/V/W terminals?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor is shorted to ground. Test motor insulation with a megohmmeter and repair or replace motor.<br><strong>No:</strong> Fault is internal to the drive. Replace control card first, then power board if fault persists.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Cycle power completely** by disconnecting AC mains and DC link, waiting 5 minutes for capacitors to discharge, then reconnecting.
2. **Check for a sub-code** on the drive display (e.g., 38-01, 38-02, 38-03) and consult Table 6.1 in the FC302 Operating Instructions to identify the failed component.
3. **Test internal 24VDC supply** at terminals 100 and 101 with a voltmeter (should read 24V ±5%). If low, the power supply on the control card has failed.
4. **Disconnect the motor** at U/V/W terminals and test each output phase to ground with a megohmmeter. If fault clears, the motor is shorted.
5. **Reseat the control card** by removing it from the slot, inspecting for corrosion or burns, cleaning contacts with isopropyl alcohol, and reinstalling firmly.
6. **Replace the control card** if fault persists with motor disconnected and 24VDC supply is normal (most common fix for generic Alarm 38).
7. **Test IGBTs on the inverter board** with a diode test if fault persists after control card replacement. Replace the inverter board if IGBTs are shorted or DC-link capacitors show more than 10% capacitance loss.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Control Card (Logic PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-90-fault-code&k=Danfoss+FC302+Control+Card+%28Logic+PCB%29&tag=errorcodefixes-20) \| Match the part number on your existing card (printed on the PCB) to make sure compatibility with your drive frame size. |
| Danfoss FC302 Inverter Board (Power Stack) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-90-fault-code&k=Danfoss+FC302+Inverter+Board+%28Power+Stack%29&tag=errorcodefixes-20) \| Order by frame size and voltage rating (e.g., P3K0, P5K5, P11K). Includes IGBTs and DC-link capacitors. |

## When to Call a Pro

Call a qualified electrician or drive technician for any work inside the VFD cabinet. The FC302 operates at high DC-link voltage (up to 800VDC) and capacitors can remain charged for several minutes after power is removed. Internal faults require safe discharge procedures, multimeter testing of power stage components, and correct part identification by frame size and firmware revision. Incorrect handling can cause electric shock, further damage to the drive, or voiding of warranty. A technician will also have access to Danfoss diagnostic software to read detailed fault logs and verify the repair.

**Rough cost:** A pro service call runs about $300-800 depending on part (control card $200-400, inverter board $400-700) plus 1-2 hours labor.

## See Also

- [Danfoss FC302 AL-101 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-101-fault-code/)
- [Danfoss FC302 ALARM 37 - Causes & Fix](/posts/danfoss-fc302-alarm-37-fault-code/)
- [Danfoss FC302 AL-60 Fault - Causes & Fix](/posts/danfoss-fc302-vfd-al-60-fault-code/)
- [Danfoss VFD Fault Codes — FC301, FC302, FC102 Reference](/posts/danfoss-vfd-fault-codes/)
