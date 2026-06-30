---
title: "LG Mini-Split CH07 Error Code - Causes & Fix"
description: "CH07 means indoor units are set to different modes. Fix: set all units on the same outdoor system to the same mode (all cool or all heat)."
pubDatetime: 2026-05-31T00:52:38Z
modDatetime: 2026-05-31T00:52:38Z
author: "Marcus Webb"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - lg
money_part: "Indoor unit control board (PCB)"
most_likely_cause: "Indoor units set to different modes"
---

## LG Mini-Split CH07 Error Code — What It Means

The CH07 error code on LG multi-split and 2-in-1 mini-split systems indicates a mode mismatch between indoor units connected to the same outdoor unit. In multi-split or Multi V systems, CH07 appears when the connected indoor units are not all operating in the same mode (for example, one unit is set to cooling while another is set to heating). On LG 2-in-1 systems, the code triggers when the standing unit and wall-mounted unit are set to different modes.

This is a communication and configuration fault, not a mechanical failure. The system cannot run efficiently when indoor units fight each other by calling for opposite modes. LG designed this error to protect the compressor and prevent damage from conflicting commands.

[Jump to Fix](#fix)

## Common Causes

- **Indoor units set to different modes** One or more indoor units on the same outdoor unit are in cooling mode while others are in heating mode, which the system cannot support simultaneously.
- **Manual mode changes without synchronization** A user changed the mode on one remote or controller without updating all other connected indoor units to match.
- **2-in-1 system mode conflict** On LG 2-in-1 systems, the standing unit and wall-mounted unit are commanded to different operating modes.
- **Control wiring or communication fault** Loose or damaged wiring between indoor units and the outdoor unit can prevent mode signals from synchronizing properly.
- **System power interruption during mode change** A brief power loss or brownout during mode selection can leave units in mismatched states when power returns.
- **Control board configuration error** Incorrect DIP switch settings or system configuration on multi-split installations can cause persistent mode conflicts.

## Step-by-Step Fix {#fix}

1. **Identify your system type** by checking whether you have a multi-split system (multiple indoor units on one outdoor unit) or a 2-in-1 system (standing unit plus wall-mounted unit).
2. **Check the mode setting on every indoor unit** using each remote or controller and note whether each is set to cool, heat, fan, or another mode.
3. **Set all indoor units to the same mode** by selecting either cooling or heating on every remote so all units connected to the same outdoor unit match exactly.
4. **Turn off the system** and locate the circuit breaker or disconnect switch that powers the outdoor unit.
5. **Trip the breaker and wait approximately three minutes** to allow the system to fully power down and clear the fault from memory.
6. **Restore power** and turn on each indoor unit one at a time, verifying that all units start in the same mode you selected earlier.
7. **Monitor the system** for at least 15 minutes of continuous operation to confirm the CH07 code does not return and all units respond to mode changes together.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Indoor unit control board (PCB) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch07-error-code&k=Indoor+unit+control+board+%28PCB%29&tag=errorcodefixes-20) \| Only if mode synchronization fails repeatedly and a specific indoor unit cannot communicate or accept mode commands. |
| Communication wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch07-error-code&k=Communication+wiring+harness&tag=errorcodefixes-20) \| If inspection reveals damaged, pinched, or corroded wiring between indoor and outdoor units after mode alignment does not resolve the fault. |
| Outdoor unit main control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-lg-mini-split-ch07-error-code&k=Outdoor+unit+main+control+board&tag=errorcodefixes-20) \| Required only when the outdoor unit fails to coordinate mode signals even after all indoor units are properly synchronized and wiring is verified intact. |

## When to Call a Pro

Call a qualified HVAC technician if the CH07 code returns after you have verified all indoor units are set to the same mode and completed a full power reset. Persistent CH07 faults after proper mode alignment usually indicate a wiring problem, a communication failure between units, or a control board configuration issue that requires diagnostic tools and system-specific knowledge. A technician can test communication voltage, inspect interconnecting wiring for faults, and verify that DIP switches and system settings match your installation. If you have a newly installed multi-split system showing CH07 from the start, the issue is likely a configuration error during installation and should be covered under warranty.

## See Also

- [LG Mini Split Error Codes — All CH Codes Explained](/posts/lg-mini-split-error-codes/)
- [LG DLEX4000W Dryer Problems & Error Codes](/posts/lg-dlex4000w-dryer-problems/)
- [LG Refrigerator FF Error Code - Causes & Fix](/posts/lg-refrigerator-ff-error-code/)
- [LG LMV2031ST Microwave Problems & Error Codes](/posts/lg-lmv2031st-microwave-problems/)
