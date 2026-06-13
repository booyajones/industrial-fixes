---
title: "Allen-Bradley PowerFlex 525 F004 - Causes & Fix"
description: "F004 = UnderVoltage fault on the PowerFlex 525 VFD. The DC bus voltage dropped below minimum. Most often caused by low incoming AC."
pubDatetime: 2026-06-11T10:14:37Z
modDatetime: 2026-06-11T10:14:37Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - vfd
  - allen-bradley
money_part: "Input fuses (drive-rated class and amperage)"
most_likely_cause: "low or interrupted incoming AC line voltage"
likelihood: "the primary cause Rockwell lists"
diy_or_pro: "pro"
---

## Allen-Bradley PowerFlex 525 F004 — What It Means

F004 on a Rockwell/Allen-Bradley PowerFlex 525 means UnderVoltage. The drive has detected that its internal DC bus voltage fell below the minimum allowable threshold. This fault protects the drive from operating with insufficient supply power, which can damage components or cause erratic motor behavior.

Rockwell's fault documentation points technicians first to incoming AC line problems such as low voltage or a line interruption. The fault can also appear if an analog input is configured to fault on signal loss and that signal is lost, though the primary F004 condition is always a DC bus voltage drop. The drive will not run until the supply issue is corrected and the fault is cleared.

## Before You Replace Anything

Technicians sometimes replace the drive power module or control board without first verifying incoming AC voltage at the input terminals and checking all line-side fuses, disconnects, and wiring terminations. A simple multimeter check of supply voltage under load and a visual inspection of input fuses and connections usually reveals the true cause.

[Jump to Fix](#fix)

## Common Causes

- **Low or sagging incoming AC line voltage (~35%)** A brownout, undersized supply transformer, or shared load on the same circuit drops the AC voltage below the drive's minimum rated input, causing the DC bus to fall.
- **Loose or poor input power connections (~25%)** Intermittent contact at the drive's line-side terminals, terminal blocks, or upstream disconnects interrupts or reduces power delivery.
- **Blown or weak input fuses (~20%)** An open or degraded fuse on one or more input phases cuts off power or creates unbalanced voltage, dropping the bus below threshold.
- **Momentary line interruption from upstream equipment (~12%)** A contactor, breaker, or utility supply glitch causes a brief dropout that the drive detects as an undervoltage event.
- **Overhauling or regenerative load condition (~5%)** A descending or braking load can feed energy back into the drive, and if bus voltage control fails or supply is unstable, the bus may drop instead of rise.
- **Failed drive power section or control module (~3%)** An internal fault in the rectifier, bus capacitors, or control circuitry prevents the drive from maintaining proper DC bus voltage even with good input power.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the incoming AC line voltage within the drive's rated input range while the fault occurs?</summary>
<div class="dtree-body"><strong>Yes:</strong> The supply is adequate, so move to checking input fuses, connections, and upstream contactors for intermittent opens.<br><strong>No:</strong> The line voltage is low or interrupted. Investigate the facility supply, transformer sizing, and shared loads on the same circuit.</div>
</details>

<details class="dtree"><summary>Are all input fuses, disconnects, and line-side terminal connections tight and intact?</summary>
<div class="dtree-body"><strong>Yes:</strong> Wiring and fuses are good. Check for momentary line dropouts or regenerative load issues during decel or load transitions.<br><strong>No:</strong> Tighten loose terminals, replace blown or degraded fuses, and repair any damaged upstream disconnects or wiring.</div>
</details>

<details class="dtree"><summary>Does the fault clear and stay away after correcting supply voltage and connections?</summary>
<div class="dtree-body"><strong>Yes:</strong> The root cause was external to the drive. Monitor for recurrence and verify upstream supply stability.<br><strong>No:</strong> If F004 persists with confirmed good input power and wiring, the drive power module or control section may be faulty and require replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify incoming AC line voltage** at the drive's input terminals using a multimeter while the machine is running or during the fault event, and compare the reading to the drive's rated input voltage class.
2. **Inspect all input fuses** on each phase for opens, heat damage, or visible degradation, and test them with a continuity meter or replace if suspect.
3. **Check line-side terminal connections** at the drive, disconnect, breaker, and any intermediate terminal blocks for tightness, corrosion, or heat marks, and tighten or clean as needed.
4. **Look for momentary line interruptions** from upstream contactors, breakers, or utility events by monitoring the supply with a data logger or asking facility staff about recent power disturbances.
5. **Inspect the load and application** for overhauling or regenerative conditions during deceleration or load transitions, and review the drive's decel time and braking configuration if dynamic loads are present.
6. **Correct the supply issue** by repairing upstream power interruptions, replacing blown fuses, tightening all terminations, or addressing undersized or unstable AC sources.
7. **Clear the fault and restart the drive** after the root cause is fixed, either by cycling power or using the drive's keypad fault-reset function per Rockwell's fault-table guidance.
8. **Test the drive power section** if F004 remains with confirmed good input voltage and wiring, and substitute or test the drive's power module or control board per standard troubleshooting practice.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Input fuses (drive-rated class and amperage) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f004-fault-code&k=Input+fuses+%28drive-rated+class+and+amperage%29&tag=errorcodefixes-20) \| Replace if open, discolored, or tested weak. Consult your drive's input-current specification for the correct fuse rating. |
| Line-side terminal lugs or crimp connectors | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f004-fault-code&k=Line-side+terminal+lugs+or+crimp+connectors&tag=errorcodefixes-20) \| Use if existing terminals are corroded, heat-damaged, or not making full contact. |
| PowerFlex 525 power module or control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-allen-bradley-powerflex-525-vfd-f004-fault-code&k=PowerFlex+525+power+module+or+control+board&tag=errorcodefixes-20) \| Only after confirming good supply and wiring. Match the drive's catalog number and voltage class. |

## When to Call a Pro

Call a qualified electrician or controls technician if you are not trained to work with industrial three-phase power, if you cannot safely access the drive's input terminals, or if you lack the test equipment to measure line voltage under load. A professional should handle all inspection and repair of upstream disconnects, breakers, and facility supply. If the fault persists after verifying good incoming power and replacing fuses and terminals, a technician with drive-repair experience should test or replace the drive's power module or control board, since internal DC-bus faults require specialized diagnostics and may involve high stored voltages even after power is removed.

**Rough cost:** A pro service call runs about $150-500.

## See Also

- [Allen-Bradley PowerFlex 525 Fault F003 - What It Means and How to Fix It](/posts/allen-bradley-powerflex-525-fault-f003/)
- [Allen-Bradley PowerFlex Fault F004 — Causes & Fix](/posts/allen-bradley-powerflex-fault-f004/)
- [Allen-Bradley PowerFlex Fault F063 — Causes & Fix](/posts/allen-bradley-powerflex-fault-f063/)
- [Allen Bradley PowerFlex 525 F005 Fault, Overvoltage Causes & Fix](/posts/allen-bradley-powerflex-525-fault-f005/)
