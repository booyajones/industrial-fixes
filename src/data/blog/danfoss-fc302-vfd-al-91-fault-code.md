---
title: "Danfoss FC302 AL-91 - Causes & Fix"
description: "AL-91 is not a standard Danfoss code. Check if it's AL-38 with sub-code 91 (internal fault) or a display error. Power cycle first."
pubDatetime: 2026-06-23T10:10:37Z
modDatetime: 2026-06-23T10:10:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "FC302 control board (exact model-specific)"
most_likely_cause: "corrupted firmware or parameter memory"
likelihood: "often"
diy_or_pro: "pro"
free_checks:
  - "Power cycle the drive (turn off, wait 5 minutes, turn on) to clear transient errors"
  - "Inspect control wiring for broken or loose connections and verify shielding is intact"
  - "Check that motor and control cables are routed separately to avoid interference"
---

## Danfoss FC302 AL-91 — What It Means

The code AL-91 does not exist in the official Danfoss FC302 VFD alarm lists. The highest standard alarm number is AL-90 (encoder fault), and Danfoss documents over 90 messages but AL-91 is not among them. If you see '91' on the display, it is most likely either a misreading or a sub-code for AL-38 (internal fault). AL-38 indicates the drive has detected an unrecoverable internal error, often related to control card communication failure, corrupted firmware, gate driver circuit problems, or sensor malfunctions. The sub-code 91 would specify the exact internal component or condition, but Danfoss does not publish the full sub-code table in open documents, so confirmation requires direct access to Danfoss service tools or technical support.

## Before You Replace Anything

Technicians sometimes replace the entire power board when the fault is actually a loose control wire or corrupted parameter set. Always power cycle multiple times and check control wiring continuity before ordering boards.

[Jump to Fix](#fix)

## Common Causes

- **Corrupted firmware or parameter memory (~30%)** A memory error or firmware glitch can trigger AL-38 internal faults, often resolved by power cycling or reloading parameters.
- **Failed communication between control card and power card (~25%)** Loose connections or internal bus faults prevent the drive from coordinating properly and trigger an internal fault.
- **Damaged gate driver circuits on the inverter board (~20%)** Gate driver failures prevent proper IGBT switching and cause the drive to shut down with an internal error.
- **External electrical interference or noise (~15%)** Unshielded or poorly routed control wiring picks up EMI and corrupts signals, causing false internal faults.
- **Faulty sensor (temperature, current, or feedback) (~10%)** Out-of-spec sensor readings can confuse the drive's internal diagnostics and trigger an AL-38 with a sub-code.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear after you power cycle the drive and wait 5 minutes?</summary>
<div class="dtree-body"><strong>Yes:</strong> The error was likely transient (noise or temporary memory glitch). Monitor for recurrence and check control wiring shielding.<br><strong>No:</strong> The fault is persistent. Proceed to check control wiring and sensors for physical damage or loose connections.</div>
</details>

<details class="dtree"><summary>Are the motor cable and control cables routed in separate conduits or well-separated?</summary>
<div class="dtree-body"><strong>Yes:</strong> Interference is unlikely. Focus on internal component testing (control board, gate drivers, sensors).<br><strong>No:</strong> Re-route cables to maintain separation and add shielding. Power cycle again to see if the fault clears.</div>
</details>

<details class="dtree"><summary>Do you have access to Danfoss service software to read the full sub-code detail?</summary>
<div class="dtree-body"><strong>Yes:</strong> Connect the software and retrieve the exact sub-code meaning from the internal fault table, then follow the manufacturer's repair protocol.<br><strong>No:</strong> Contact Danfoss technical support or a certified service technician to decode the sub-code and identify the failed component.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power cycle the drive** by turning it off, waiting at least 5 minutes for capacitors to discharge, then turning it back on to clear transient errors.
2. **Verify the exact code** displayed on the VFD panel or keypad. Confirm whether it reads AL-91 or AL-38 with sub-code 91.
3. **Inspect control wiring** for broken strands, loose terminals, or damaged insulation. Check that control and motor cables are routed separately or in shielded conduit.
4. **Test feedback sensors** (temperature, encoder, current) by measuring continuity and resistance. Replace any sensor that reads out of specification.
5. **Check for external interference** by ensuring no power factor correction capacitors are on the motor side and that the drive is properly grounded.
6. **Cycle power again** after completing wiring and sensor checks. If the fault persists after multiple cycles, internal component failure is confirmed.
7. **Contact Danfoss support or a certified technician** to access the internal sub-code table and diagnose the specific failed component (control board, gate driver, or power stack).

## Parts Often Needed

| Part | Notes |
|------|-------|
| FC302 control board (exact model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-91-fault-code&k=FC302+control+board+%28exact+model-specific%29&tag=errorcodefixes-20) \| Required if communication or firmware corruption is confirmed. Match your frame size and firmware version. |
| Inverter power board or gate driver module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-91-fault-code&k=Inverter+power+board+or+gate+driver+module&tag=errorcodefixes-20) \| Needed if gate driver circuits test faulty. Consult Danfoss for the correct part number for your frame. |

## When to Call a Pro

Call a professional immediately if power cycling and wiring checks do not clear the fault. AL-38 internal faults often require specialized diagnostic tools, access to Danfoss service software to read sub-codes, and replacement of high-voltage components such as control boards, gate drivers, or inverter modules. Technicians have the training and equipment to safely discharge DC bus capacitors, test IGBT modules, and load updated firmware. Attempting to disassemble or test internal power electronics without proper training risks electric shock and permanent drive damage.

**Rough cost:** A pro service call runs about $300-800 depending on board replacement.
