---
title: "Danfoss FC302 AL-88 Fault - Causes & Fix"
description: "AL-88 Option Detection means an option card was added or removed while the VFD's option layout is frozen. Change parameter 14-89 to allow."
pubDatetime: 2026-06-23T10:08:06Z
modDatetime: 2026-06-23T10:08:06Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 communication option card"
most_likely_cause: "Option card removed or added after programming with parameter 14-89 set to Frozen"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Visually inspect all option card slots to confirm which cards are physically present"
  - "Check that all option cards are fully seated and locked into their slots"
  - "Review parameter 14-89 on the LCP to see if it is set to Frozen Configuration"
no_buy_pct: "85%"
---

## Danfoss FC302 AL-88 Fault — What It Means

Alarm 88 (Option Detection) on a Danfoss FC302 VFD means the drive has detected that an option card has been added or removed from the VFD, changing the option layout from what was previously configured and frozen in the parameter settings. This alarm appears when parameter 14-89 is set to Frozen Configuration (or Protect Option Config) and the actual hardware option layout no longer matches. The drive will not run until the option configuration is either re-accepted by changing the parameter to allow the new layout, or the hardware is restored to match the frozen configuration.

## Before You Replace Anything

Technicians sometimes replace option cards assuming they failed when the actual issue is simply a mismatch between the frozen parameter configuration and the current hardware layout. Always check parameter 14-89 first before ordering new cards.

[Jump to Fix](#fix)

## Common Causes

- **Option card removed after programming (~35%)** A communication, I/O, or encoder card was programmed into the drive then physically removed before power-up, triggering the mismatch alarm.
- **Parameter 14-89 set to Frozen while hardware changed (~30%)** The option detection parameter is locked to Frozen Configuration but the actual hardware layout does not match the stored configuration.
- **Option card added unexpectedly (~15%)** Someone installed a new option card without updating the parameter configuration to allow the change.
- **Loose or improperly seated option card (~12%)** The card is present but not fully inserted, causing the drive to detect it as missing or changed.
- **Power cycle after hardware change without re-enabling option changes (~8%)** The system was powered off and on after a hardware change, but option detection remains frozen and blocks startup.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>When you open the option card area, are all cards that were originally programmed still present and fully seated?</summary>
<div class="dtree-body"><strong>Yes:</strong> The hardware matches the original configuration. Check parameter 14-89 and change it to Enable Option Change, then power cycle the drive.<br><strong>No:</strong> A card is missing, loose, or added. Either reseat or restore the original card layout, or change parameter 14-89 to accept the new layout.</div>
</details>

<details class="dtree"><summary>Can you access parameter 14-89 without a password prompt?</summary>
<div class="dtree-body"><strong>Yes:</strong> Change the parameter from Frozen Configuration to Enable Option Change, then power cycle the drive to clear the alarm.<br><strong>No:</strong> You will need to enter the password 00000100 on the LCP to unlock parameter 14-89 before you can change it.</div>
</details>

<details class="dtree"><summary>After changing parameter 14-89 to Enable Option Change and power cycling, does the alarm clear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The option layout mismatch is resolved. The drive should now run normally with the new hardware configuration.<br><strong>No:</strong> There may be a deeper hardware fault with the option card or backplane. Inspect the card for damage and test in another slot if possible.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the alarm and hardware state.** On the Local Control Panel (LCP), confirm the alarm reads Alarm 88 Option Detection. Open the option card slot area and note which option cards are physically present, missing, or loose.
2. **Access parameter 14-89.** Press Main Menu on the LCP, navigate to sub menu 14- Special Functions, then sub menu 14-8 Options, then parameter 14-89 Option Detection. If prompted for a password, enter 00000100 using the arrow keys and press OK.
3. **Change the option detection setting.** At parameter 14-89, change the value from Protect Option Config (or Frozen configuration) to Enable Option Change (or Enable Option Change). Press OK to confirm the change.
4. **Power cycle the drive completely.** Turn off all power to the VFD, wait at least 10 seconds for capacitors to discharge, then restore power. The alarm will not clear with a simple reset button press.
5. **Verify the alarm has cleared.** On the LCP, check that Alarm 88 no longer appears and the drive status shows ready to run. Test the drive under normal operating conditions.
6. **If the alarm persists, inspect option card hardware.** Remove and reseat each option card firmly into its slot. Check for bent pins, corrosion, or physical damage on the card edge connectors and backplane.
7. **Document the new option configuration.** If you accepted a new hardware layout, update your parameter backup file and any system documentation to reflect the current option card arrangement.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 communication option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-88-fault-code&k=Danfoss+FC302+communication+option+card&tag=errorcodefixes-20) \| Only needed if the original card is physically damaged or missing and you want to restore the frozen configuration rather than accept the change. |
| Danfoss FC302 I/O expansion option card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-88-fault-code&k=Danfoss+FC302+I%2FO+expansion+option+card&tag=errorcodefixes-20) \| Only needed if the original card is physically damaged or missing and you want to restore the frozen configuration rather than accept the change. |

## When to Call a Pro

Call a qualified VFD technician or controls engineer if you are not familiar with Danfoss parameter programming or do not have access to the LCP. If changing parameter 14-89 and power cycling does not clear the alarm, or if you see physical damage to option cards or backplane connectors, professional diagnosis is required. Also call a pro if the drive is part of a networked system where changing option settings could affect upstream controllers or HMI configurations. High-voltage work around VFD terminals and bus bars should always be performed by trained personnel with proper lockout/tagout procedures.

**Rough cost:** A pro service call runs about $150-400 depending on service call minimum and labor time.
