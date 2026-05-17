---
title: "Carrier 43 Error Code — Rollout Switch Open Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-23T08:00:00Z
modDatetime: 2024-03-23T08:00:00Z
slug: carrier-43-error-code
featured: false
draft: false
tags:
  - hvac
  - carrier
  - furnace
  - rollout-switch
description: "Carrier error code 43 means the rollout switch has tripped due to flame rollout. This guide covers every cause and fix for the Code 43 rollout lockout on Carrier furnaces."
---

## Error Code: Carrier 43

**What it means:** Code 43 is a rollout switch lockout. The rollout switch (also called a flame rollout limit) is a manual-reset thermal fuse mounted on the burner box. It trips when it detects flame escaping out of the burner compartment instead of staying in the heat exchanger. Normal flame should be contained inside the heat exchanger — rollout means something is forcing combustion gases backward. Code 43 requires a manual reset of the rollout switch itself; cycling power to the furnace will not clear it.

## Common Causes

- **Cracked or failed heat exchanger** — A heat exchanger crack allows combustion gases to escape into the air plenum. Negative pressure from the blower draws combustion air backward, causing rollout. This is the most serious cause and requires immediate action — cracked heat exchangers can allow CO to enter living spaces.
- **Blocked flue or heat exchanger** — Scale buildup, debris, or animal nests in the flue or secondary heat exchanger restrict combustion gas flow. Gases back up and roll out.
- **Inducer motor failure** — If the inducer is running slowly or not at all, there is insufficient draft to pull combustion gases through the heat exchanger. Flame spills backward.
- **Blocked combustion air supply** — Furnaces installed in small closets or utility rooms can starve for combustion air. Insufficient air supply disrupts burner flame direction.
- **Wrong gas pressure** — High gas pressure causes an oversized, turbulent flame that can escape the burner ports.

## Diagnosis Steps

1. Do NOT reset the rollout switch until you identify the cause. Repeated resets without diagnosis is a CO safety risk.
2. Visually inspect the burner compartment with the front panel removed. Look for soot deposits on the inside of the burner box — soot outside the normal burn zone indicates rollout has occurred.
3. Start the inducer motor manually (using a jumper or test mode) and hold your hand near the burner area before ignition. You should feel strong draft pulling inward. Weak or reversed airflow points to a blocked flue or failed inducer.
4. Inspect the flue pipe for blockages: disconnected sections, bird nests, ice (in cold climates), or excess condensate backup.
5. Perform a heat exchanger inspection with a camera or mirror. Cracks often appear at the clam-shell seams. If in doubt, perform a combustion analysis or call for a pressure test.

## Fix

If the flue is blocked: clear the obstruction and test. If the inducer is weak: check inducer motor amperage and RPM against spec — replace if below rating.

If the heat exchanger is cracked, the furnace must be taken out of service. A cracked heat exchanger is not a DIY repair — the entire heat exchanger or furnace needs replacement. This is a safety-critical failure.

If no structural fault is found: check gas manifold pressure with a manometer. For natural gas, manifold pressure should typically be 3.5 inches W.C. at the burner. Adjust the gas valve regulator if pressure is out of spec.

Once the root cause is corrected, locate the rollout switch (typically a disc-shaped device with a red reset button mounted on the burner box). Press the reset button firmly. Restore power and run a test cycle.

## Parts

| Part | Where to Buy |
|------|-------------|
| [Rollout switch / limit switch](https://www.amazon.com/dp/B0BN3TRG9R?ascsubtag=ecf-carrier-43-error-code&tag=errorcodefixes-20) | RepairClinic, SupplyHouse |
| [Inducer motor assembly](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-43-error-code&tag=errorcodefixes-20) | RepairClinic, Grainger |
| [Gas valve](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-carrier-43-error-code&tag=errorcodefixes-20) | SupplyHouse, Grainger |

## When to Call a Technician

Any Code 43 with suspected heat exchanger failure requires a licensed HVAC technician immediately. A cracked heat exchanger is a carbon monoxide hazard. Do not operate the furnace until the heat exchanger is inspected and cleared. Gas valve adjustments also require proper test equipment and licensing in most jurisdictions.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)
