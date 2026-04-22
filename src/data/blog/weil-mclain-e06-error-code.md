---
title: "Weil-McLain E06 Error Code — Ignition Lockout"
description: "Weil-McLain E06 means the boiler failed to establish flame after multiple ignition attempts and entered lockout. Here's how to diagnose and reset it."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - weil-mclain
  - boiler
  - hvac
  - error-code
  - ignition
---

## Weil-McLain E06 Error — Ignition Lockout

**E06 on a Weil-McLain boiler** means the boiler attempted ignition and **failed to establish or prove a flame**, triggering a safety lockout. The control board will not attempt ignition again until the fault is reset.

E06 appears on Ultra series, Gold Plus, and CGi boilers. It differs from E02 (ignition failure — first attempt) in that E06 represents a **hard lockout** after the control board has exhausted its allowed retry attempts.

## Ignition Sequence That Must Succeed

1. Combustion blower starts
2. Draft pressure switch closes (draft proved)
3. Igniter energizes (hot surface or spark)
4. Gas valve opens
5. Flame sensor detects flame within 4–7 seconds
6. Flame proven — burner continues

Failure at any step causes E06 after retries.

## Most Common E06 Causes

| [Cause](https://www.amazon.com/s?k=Cause&tag=errorcodefixe-20) | What to Check |
|---|---|
| [No gas supply](https://www.amazon.com/s?k=No%20gas%20supply&tag=errorcodefixe-20) | Gas valve at boiler, main shutoff, utility supply |
| [Dirty flame sensor](https://www.amazon.com/s?k=Dirty%20flame%20sensor&tag=errorcodefixe-20) | Rod coated with oxide — clean with emery cloth |
| [Failed igniter](https://www.amazon.com/s?k=Failed%20igniter&tag=errorcodefixe-20) | Cracked or weak hot surface igniter |
| [Failed gas valve](https://www.amazon.com/s?k=Failed%20gas%20valve&tag=errorcodefixe-20) | Valve not opening on command |
| [Draft pressure fault](https://www.amazon.com/s?k=Draft%20pressure%20fault&tag=errorcodefixe-20) | Blocked flue, failed inducer, blocked condensate |
| [Fuel pressure too low](https://www.amazon.com/s?k=Fuel%20pressure%20too%20low&tag=errorcodefixe-20) | Check gas pressure at manifold (3.5" WC natural gas) |

## How to Reset E06

**Locate the reset button** on the control board or front panel of the boiler. On most Weil-McLain Ultra models, it's a red button labeled RESET near the display. Press and hold for 3 seconds until the display clears.

The boiler will immediately attempt a new ignition sequence. Watch and listen:
1. Do you hear the combustion blower start?
2. Does the igniter glow (if you can see through the view window)?
3. Does the gas valve click open?
4. Does the flame light and stabilize?

## Step-by-Step Diagnosis

**Step 1 — Verify gas supply.** Is the gas shutoff valve on the supply pipe to the boiler fully open? Check other gas appliances in the home — if none work, call your gas utility.

**Step 2 — Clean the flame sensor.** This is the most common fix. The rod-style sensor near the burner must be clean metal to conduct microamps. Remove it, polish with fine steel wool or 400-grit emery cloth, reinstall.

**Step 3 — Check the condensate drain.** If the condensate drain is blocked, the draft pressure switch won't close, preventing ignition. Find the drain trap, disconnect it, and blow it clear.

**Step 4 — Inspect the igniter.** If you can see the igniter through the observation window, watch it during startup. It should glow orange-red within 30 seconds. If it glows but no flame — gas isn't reaching it. If it doesn't glow at all — the igniter or its circuit is failed.

**Step 5 — Check gas valve operation.** With a multimeter, verify the gas valve coil terminals see 24VAC when the board calls for ignition. If voltage is present and the valve doesn't open, the gas valve has failed.

**Step 6 — Measure gas manifold pressure.** A tech with a manometer can verify manifold pressure. Low pressure (below 3.0" WC for natural gas) means supply pressure or regulator issue.

## Parts Reference

| Part | Cost |
|---|---|
| [Flame sensor rod](https://www.amazon.com/s?k=Flame%20sensor%20rod&tag=errorcodefixe-20) | $15–35 |
| [Hot surface igniter](https://www.amazon.com/s?k=Hot%20surface%20igniter&tag=errorcodefixe-20) | $30–70 |
| [Gas valve](https://www.amazon.com/s?k=Gas%20valve&tag=errorcodefixe-20) | $150–350 |
| [Condensate trap](https://www.amazon.com/s?k=Condensate%20trap&tag=errorcodefixe-20) | $15–30 |
| [Control board](https://www.amazon.com/s?k=Control%20board&tag=errorcodefixe-20) | $200–500 |

## E06 vs. E02

- **E02** = First ignition failure (board will retry)
- **E06** = Ignition lockout after all retries exhausted (requires manual reset)

If E06 comes back within one heating cycle after a reset, the root cause hasn't been fixed. Call a qualified heating technician if self-diagnosis doesn't resolve it — repeated lockouts on a boiler often indicate a gas pressure or combustion system issue.
