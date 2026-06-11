---
title: "Frigidaire Range F15 Error Code - Causes & Fix"
description: "F15 on a Frigidaire range indicates a signal fault between the main control board and the relay board. Check wiring and boards."
pubDatetime: 2026-06-08T06:03:16Z
modDatetime: 2026-06-08T06:03:16Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - appliance
  - oven
  - frigidaire
most_likely_cause: "Failed or loose connection between the EOC and the relay board"
likelihood: "the most common cause"
diy_or_pro: "diy"
money_part: "Electronic Oven Control (EOC) / Main Control Board"
---

## Frigidaire Range F15 Error Code — What It Means

F15 is generally used to indicate a communication or signal-loss fault between the Electronic Oven Control (EOC) and the oven relay board on Frigidaire ranges. In some Electrolux-family models built by the same manufacturer, field technicians also report F15 being tied to a cooling-fan limiter thermostat or safety thermostat opening after a self-clean event. The exact meaning is model-dependent and should be confirmed against your product's tech sheet or wiring diagram for your specific serial and model number.

Frigidaire's owner-facing error-code page does not list F15 in the general consumer guide, which reinforces that the precise meaning is likely model-specific rather than universal across all Frigidaire ranges. Because the code can point to either a board communication issue or a thermal safety device on different models, always confirm the exact model number first before ordering parts.

## Before You Replace Anything

Many people replace the main control board first, but a loose or corroded wiring harness or connector between the EOC and relay board is often the real culprit. Inspect and reseat all connectors before replacing either board.

[Jump to Fix](#fix)

## Common Causes

- **Loose, damaged, or corroded wiring harness or connectors (~35%)** The ribbon cable or connectors between the main control board and relay board can come loose, develop corrosion, or suffer burned terminals, interrupting the synchronization signal.
- **Failed oven relay board (~25%)** The power relay board may fail internally, preventing it from responding to commands from the main control.
- **Failed Electronic Oven Control (EOC) (~20%)** The main control board can lose the ability to send or receive the handshake signal to the relay board.
- **Open safety thermostat or cooling-fan limiter thermostat (~15%)** On models that use a limiter thermostat architecture, the device can open after a self-clean overheating event and trigger F15.
- **False latch-up requiring a power cycle (~5%)** A temporary firmware or signal glitch can cause the code to latch even when all hardware is intact.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the F15 code clear after you disconnect power at the breaker for at least one minute and restore it?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault was a temporary glitch. Monitor the range during normal use to see if the code returns.<br><strong>No:</strong> You have a persistent hardware fault. Continue to the wiring and board checks below.</div>
</details>

<details class="dtree"><summary>Did the F15 code appear immediately after running a self-clean cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The safety thermostat or cooling-fan limiter may have opened due to overheating. Test the thermostat for continuity and replace if open.<br><strong>No:</strong> The fault is more likely a board communication issue. Focus on wiring harness and board inspection.</div>
</details>

<details class="dtree"><summary>Can you see any burned, loose, or corroded pins in the connectors between the main control and the relay board?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean or replace the harness and connectors, then test. A poor connection is often the root cause.<br><strong>No:</strong> The wiring is intact. One of the boards has likely failed internally. Replace the relay board first, then the EOC if the fault persists.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** at the circuit breaker or unplug the range and wait at least one minute to clear any latched fault before starting diagnostics.
2. **Confirm your exact model number** by checking the rating plate inside the oven door or on the back of the range, because F15 behavior varies across Frigidaire and Electrolux-family models.
3. **Restore power and check** whether the code clears and the timer or control resumes normally. If it does, the fault was a temporary glitch. If F15 returns immediately, continue.
4. **Remove the rear access panel** (or front control panel on slide-in models) to expose the main control board and relay board, then unplug power again before touching any wiring.
5. **Inspect the wiring harness and connectors** between the EOC and the relay board for loose seating, burned or corroded terminals, and damaged ribbon cable. Reseat all connectors firmly and clean any corrosion with contact cleaner.
6. **If the code appeared after self-clean**, locate the safety thermostat or cooling-fan limiter thermostat (consult your model's wiring diagram) and test it for continuity. Replace if open.
7. **Replace the relay board first** if the wiring and thermostat check good but the sync signal is still absent, then test. If the fault persists, replace the EOC main control board.
8. **Restore power and run a basic function test** by selecting bake and verifying the oven heats normally and the F15 code does not return.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Electronic Oven Control (EOC) / Main Control Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-frigidaire-range-f15-error-code&k=Electronic+Oven+Control+%28EOC%29+%2F+Main+Control+Board&tag=errorcodefixes-20) \| Match the part number on your existing board or use your model number to make sure the correct firmware version. |
| Oven Relay Board / Power Relay Board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-frigidaire-range-f15-error-code&k=Oven+Relay+Board+%2F+Power+Relay+Board&tag=errorcodefixes-20) \| Usually mounted below or beside the main control; verify the connector layout matches your original. |
| Wiring Harness / Interconnect Cable | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-frigidaire-range-f15-error-code&k=Wiring+Harness+%2F+Interconnect+Cable&tag=errorcodefixes-20) \| Order the exact harness for your model if the ribbon or connectors are damaged beyond cleaning. |
| Safety Thermostat / Cooling-Fan Limiter Thermostat | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-frigidaire-range-f15-error-code&k=Safety+Thermostat+%2F+Cooling-Fan+Limiter+Thermostat&tag=errorcodefixes-20) \| Only on models that use this architecture; consult your wiring diagram to confirm location and part number. |

## When to Call a Pro

Call a pro if you are uncomfortable working inside the control panel area or if you cannot positively identify which board has failed after inspecting the wiring. A technician can use a multimeter and the factory wiring diagram to trace the sync signal between the EOC and relay board, saving you the cost of replacing the wrong board. Also call a pro if your range is hardwired to a junction box and you are not confident isolating power safely, or if the fault involves gas ignition components that must be verified after a board replacement.

**Rough cost:** DIY runs about $80–250 in parts, 30–90 min. A pro service call runs about $150–350.
