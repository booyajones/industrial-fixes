---
title: "Carrier 21 Error Code — Gas Heating Lockout Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-02T08:00:00Z
modDatetime: 2024-03-02T08:00:00Z
slug: carrier-21-error-code
featured: true
draft: false
tags:
  - hvac
  - carrier
  - furnace
  - gas
  - lockout
description: "Carrier error code 21 signals a gas heating lockout — the furnace failed to ignite after multiple attempts. Learn the exact steps to diagnose and reset it."
---

## Error Code: Carrier 21

**What it means:** Code 2-1 is a gas heating lockout. The furnace initiated an ignition sequence, failed to prove flame within the allotted time, retried the manufacturer-set number of times (typically 3), and then locked out completely. Unlike a soft fault, this is a hard lockout — the furnace will not retry on its own. Power must be cycled (or thermostat cycled off for 30+ seconds) to clear. The control board logs this as a persistent failure to establish combustion.

## Common Causes

- **Repeated ignition failures triggering lockout** — Code 21 is often the *result* of code 34 (ignition proving failure) happening too many times in sequence. Fix the underlying ignition issue first.
- **Failed draft inducer motor** — If the inducer doesn't reach proper speed, the pressure switch won't close and the gas valve will never open. The board sees this as a heating failure and locks out.
- **Pressure switch stuck open or failed** — A faulty pressure switch prevents the control board from getting the "inducer is running" confirmation needed to proceed with ignition.
- **Gas valve not opening** — A failed gas valve solenoid means no gas reaches the burners even when the igniter is hot and everything else checks out.
- **Control board failure** — Boards that can't properly sequence the ignition cycle will produce repeated heating lockouts without an obvious component failure.

## Step-by-Step Fix {#step-by-step-fix}

1. **Document the flash code before resetting.** Note how many times the LED blinks — 2 flashes, pause, 1 flash = code 21. Then cycle the thermostat to OFF and wait 60 seconds to clear the lockout. This is not a fix; it's just clearing the board to allow diagnosis.

2. **Listen and watch the startup sequence.** Turn the thermostat to heat and watch what happens: (a) draft inducer should start within 5–10 seconds, (b) you should hear it ramp up to speed, (c) the pressure switch click should be audible, (d) the igniter should glow 30–60 seconds in. If the inducer never starts, or starts and stops, or the igniter never glows — each tells you exactly where the sequence breaks.

3. **Check the draft inducer.** Remove the cabinet and locate the round motor on top of the heat exchanger. With the furnace calling for heat, the inducer should run continuously and sound smooth. Grinding, squealing, or intermittent operation means a failing motor bearing — replace the inducer assembly.

4. **Test the pressure switch.** With the furnace running and the inducer spinning, use a multimeter to check continuity across the pressure switch terminals. If it reads open (infinite resistance) while the inducer is running, the switch is stuck or the hose is blocked. Inspect the small rubber tubing connecting the inducer to the switch — crack or collapse = replace the hose. Switch stuck open = replace the switch (around $20–$40).

5. **Verify the gas valve is opening.** During a heat call (with the inducer running and pressure switch closed), put a clamp meter on the gas valve wiring harness. You should see 24V AC when the board commands the valve to open. If 24V is present but no gas flows, the valve solenoid has failed.

6. **Check for error codes stored on the board.** Many Carrier control boards have a memory function — hold the "fault recall" button to display stored fault history. This tells you if this is a first-time lockout or a recurring pattern over days.

7. **Clear and verify.** After any repair, cycle power fully (kill the 120V disconnect), wait 30 seconds, restore power, and run 3–5 full heat cycles back-to-back without resetting to confirm the lockout doesn't recur.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Typical Cost | Where to Buy |
|------|-------------|---------------|
| Draft inducer motor assembly (Carrier OEM #HC21ZE120) | $120–$250 | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-21-error-code&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=HC21ZE120&utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-21-error-code) |
| Pressure switch (Carrier #HK06WC085) | $20–$45 | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-21-error-code&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=HK06WC085&utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-21-error-code) |
| Gas combination valve (White-Rodgers 36J) | $90–$200 | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-carrier-21-error-code&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=White-Rodgers+36J&utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-21-error-code) |
| Ignition control board (Carrier HK42FZ series) | $150–$320 | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-carrier-21-error-code&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=HK42FZ&utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-21-error-code) |

## When to Call a Professional

If you've reset the lockout, confirmed the inducer runs smoothly, the pressure switch closes, and you're still getting code 21, you need a tech with a combustion analyzer and gas pressure gauge. A gas valve that's partially opening (low gas flow) or a cracked heat exchanger disrupting the flame will both produce a 21 lockout that looks like a control board problem. Tell your tech: "Code 21, hard lockout. Inducer runs, pressure switch is closed, igniter glows. Gas valve gets 24V but I still can't prove flame."

> **Pro tip:** Before assuming a board failure on a 21 lockout, check if someone recently replaced the gas valve with an aftermarket unit that has a slightly different pressure rating. A mismatched valve regulator can produce the exact right resistance to cause intermittent ignition failures that accumulate into a lockout.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
