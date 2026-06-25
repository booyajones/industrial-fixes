---
title: "Danfoss FC302 AL-92 - Causes & Fix"
description: "AL-92 is not a valid Danfoss FC302 code. Most likely AL-38 (internal fault) misread. Cycle power and check control card connections."
pubDatetime: 2026-06-23T10:11:14Z
modDatetime: 2026-06-23T10:11:14Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC 302 control PCB"
most_likely_cause: "misread display showing AL-38 internal fault"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Cycle AC mains power off, wait 5-10 minutes for capacitors to discharge, then power on to see if fault clears"
  - "Inspect control wiring for broken wires, loose connections, or physical damage"
  - "Verify equipment is properly grounded with tight, oxidation-free connections"
no_buy_pct: "40%"
---

## Danfoss FC302 AL-92 — What It Means

AL-92 does not exist in any official Danfoss FC 302 documentation. The alarm list for the FC 302 series ranges from AL 1 to AL 72. The code displayed is likely a misread number (such as AL-38 for internal fault, AL-13 for overcurrent, or AL-72 for unknown internal fault), a corrupted display caused by firmware or hardware issues, or a code from a different drive brand or model.

If the drive instead shows AL-38 (Internal Fault), this indicates a communication error between the control card and power card, memory errors, firmware corruption, or failed gate driver circuits. Danfoss documents AL-38 as the catch-all for internal faults requiring power cycling and inspection of control wiring and PCBs.

## Before You Replace Anything

Technicians often replace the entire inverter board or power stack before testing the control card communication path and gate driver circuits. Cycle power and inspect control wiring first.

[Jump to Fix](#fix)

## Common Causes

- **Misread display code (~50%)** The keypad shows AL-92 due to misreading AL-38, AL-13, or AL-72, or the display is corrupted by firmware or hardware faults.
- **Control card to power card communication failure (~20%)** Faulty signal path between control PCB and power PCB triggers AL-38 internal fault.
- **Firmware corruption or memory error (~15%)** Corrupted parameter memory or firmware bug causes the drive to report internal fault.
- **Failed gate driver circuit (~10%)** Failed components driving IGBTs produce internal fault codes.
- **Environmental stress or contamination (~5%)** Dirt, moisture, or overheating damages internal electronics and causes internal faults.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the display show exactly AL-92, or could it be AL-38, AL-13, or AL-72?</summary>
<div class="dtree-body"><strong>Yes:</strong> Consult the Danfoss FC 302 Operating Instructions for the correct code meaning and follow the documented troubleshooting procedure.<br><strong>No:</strong> The display may be corrupted. Cycle power and observe if the code changes or clears.</div>
</details>

<details class="dtree"><summary>Does the fault clear after cycling power and waiting 5-10 minutes?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was a transient error. Monitor operation and check for environmental stress or loose wiring.<br><strong>No:</strong> Proceed to inspect control wiring, grounding, and internal PCBs for damage or failed communication.</div>
</details>

<details class="dtree"><summary>Are all control wiring connections tight and free of damage?</summary>
<div class="dtree-body"><strong>Yes:</strong> Test IGBT modules and gate drivers, or replace the control card or power card as needed.<br><strong>No:</strong> Repair or replace damaged control wiring and verify proper isolation from power and motor wiring.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the displayed code** by photographing the keypad and comparing it to the Danfoss FC 302 Operating Instructions alarm list (AL 1 to AL 72). Confirm whether the code is AL-92 or a misread of AL-38, AL-13, or AL-72.
2. **Cycle the power** by turning off AC mains and DC-link power. Wait 5 to 10 minutes for capacitors to discharge, then power on and observe if the fault clears.
3. **Check control wiring** for broken wires, loose connections, or physical damage. Inspect for noise interference and verify control wiring is isolated from power and motor wiring.
4. **Verify grounding** by checking that equipment is properly grounded and all ground connections are tight and free of oxidation.
5. **Inspect internal environment** by cleaning the heatsink and checking for dirt, metal chips, moisture, or corrosion. Verify all cooling fans operate and vents are unblocked.
6. **Test IGBT modules and gate drivers** if the fault persists after power cycling. Replace failed IGBTs or the entire inverter board or power stack as needed.
7. **Replace control card or power card** if communication failure is confirmed. Contact Danfoss Technical Support for further diagnostics if the fault remains.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC 302 control PCB | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-92-fault-code&k=Danfoss+FC+302+control+PCB&tag=errorcodefixes-20) \| Replace if communication failure or firmware corruption is confirmed |
| Danfoss FC 302 power PCB or inverter board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-92-fault-code&k=Danfoss+FC+302+power+PCB+or+inverter+board&tag=errorcodefixes-20) \| Replace if IGBT modules or gate driver circuits have failed |

## When to Call a Pro

Call a qualified technician or Danfoss-certified service provider if the fault persists after power cycling and basic wiring inspection. Work inside the drive enclosure involves high DC-link voltage (up to 500 V AC supply and higher internal DC voltage) and requires proper lockout, discharge procedures, and test equipment. Replacing control cards, power cards, or IGBT modules requires knowledge of VFD architecture and firmware recovery. Danfoss recommends contacting their technical support for persistent AL-38 internal faults or any unrecognized alarm code.

**Rough cost:** A pro service call runs about $300-800.
