---
title: "Manitowoc E03 Error Code - Causes & Fix"
description: "E03 on Manitowoc Indigo/NXT ice machines means Input Power Loss. Check for tripped breakers, blown fuses, or a power interruption."
pubDatetime: 2026-06-19T10:29:49Z
modDatetime: 2026-06-19T10:29:49Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - manitowoc
money_part: "Branch-circuit fuse"
most_likely_cause: "Tripped breaker or blown fuse in the branch circuit"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Verify the main power switch is ON and the disconnect has not been opened."
  - "Check the branch-circuit breaker at the panel and reset if tripped."
  - "Inspect the fuse at the machine or condensing unit and replace if blown."
no_buy_pct: "75%"
---

## What this code means
E03 on a Manitowoc Indigo or NXT series ice machine means Input Power Loss. The control board logs this code when it detects that incoming electrical power was interrupted and then confirms that loss when power returns. The fault is stored in the event log and displayed after the machine restarts.

This is not a refrigeration or sensor failure. The code tells you the machine lost utility power at some point, either from an external interruption or a problem in the branch circuit feeding the ice machine or condensing unit. Once you restore stable power and clear the fault, the machine should resume normal operation.

## Before You Replace Anything

Technicians sometimes replace the control board when the real problem is upstream in the electrical supply. Always verify incoming line voltage at the disconnect and check the fuse and breaker before replacing any control components.

## Common Causes

- **Tripped breaker or blown fuse (~40%)** A tripped circuit breaker or blown fuse in the branch circuit feeding the ice machine is the most common reason for an E03 power-loss event.
- **Utility power interruption (~30%)** A momentary power outage or voltage drop in the building supply can trigger the code even if power returns quickly.
- **Main switch or disconnect opened (~15%)** Someone may have turned off the main power switch or opened the upstream disconnect for cleaning or maintenance and then restored power.
- **Loose or damaged input-power wiring (~10%)** Loose terminations, a damaged power cord, or a failing disconnect can cause intermittent power loss and repeated E03 codes.
- **Failing contactor or control power issue (~5%)** An intermittent contactor or control-power circuit fault can interrupt the supply to the board and log a power-loss event.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the main power switch ON and the disconnect closed?</summary>
<div class="dtree-body"><strong>Yes:</strong> Power is reaching the machine. Move to the next check.<br><strong>No:</strong> Turn the switch ON or close the disconnect and cycle power to clear the fault.</div>
</details>

<details class="dtree"><summary>Is the circuit breaker in the ON position and not tripped?</summary>
<div class="dtree-body"><strong>Yes:</strong> The breaker is fine. Check the fuse next.<br><strong>No:</strong> Reset the breaker. If it trips again immediately, call a technician to check for a short or overload.</div>
</details>

<details class="dtree"><summary>Does the machine run normally after you restore power and cycle the control?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was a one-time power interruption. Monitor the machine for repeat codes.<br><strong>No:</strong> The code returns despite stable power. Call a technician to troubleshoot the supply path and control circuitry.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the main disconnect and verify it is safe to work.
2. **Inspect the branch-circuit breaker** at the electrical panel. If tripped, reset it. If blown, replace the fuse at the machine or condensing unit with the correct rating.
3. **Confirm the main power switch** at the machine is in the ON position and any upstream disconnects are closed.
4. **Restore power** and observe the control board. The machine should power up and clear the E03 fault after a few moments.
5. **Check for incoming line voltage** at the disconnect and at the machine using a multimeter. Verify that supply voltage matches the machine nameplate rating.
6. **Inspect all power terminations** inside the machine for loose, corroded, or burned connections. Tighten any loose wires and replace damaged terminals.
7. **Monitor the machine** through a full ice-making cycle. If E03 returns, proceed with electrical troubleshooting of the supply path, contactor, and control power components, or call a qualified service technician.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Branch-circuit fuse | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e03-error-code&k=Branch-circuit+fuse&tag=errorcodefixes-20) \| If the fuse at the machine or condensing unit is blown, replace it with the exact amp rating shown on the machine nameplate or wiring diagram. |
| Main power disconnect | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e03-error-code&k=Main+power+disconnect&tag=errorcodefixes-20) \| If the disconnect has signs of arcing, melted contacts, or fails to stay closed, replace the entire disconnect assembly. |

## When to Call a Pro

Call a professional service technician if the E03 code returns after you have verified stable incoming power and reset the breaker and fuse. Repeated power-loss events despite a good supply indicate an intermittent fault in the contactor, control power circuit, or the board itself. A technician will use a multimeter and event log to trace the interruption and test control-power continuity. Also call a pro if you are not comfortable working inside a live electrical panel or if the machine shares a multi-appliance circuit that requires load balancing or rewiring to prevent future trips.

**Rough cost:** A pro service call runs about $100-250.
