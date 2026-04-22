---
title: "Trane Error Code 126 — Ignition Lockout Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-12T08:00:00Z
modDatetime: 2024-03-12T08:00:00Z
slug: trane-126-error-code
featured: false
draft: false
tags:
  - hvac
  - trane
  - furnace
  - ignition
  - lockout
description: "Trane error code 126 means the furnace entered hard lockout after multiple ignition failures. This guide covers every fix for code 126 on Trane XR80 and XR95 furnaces."
---

## Error Code: Trane 126

**What it means:** Error code 126 on a Trane furnace is a hard ignition lockout. Unlike a soft lockout (which resets automatically after a waiting period), code 126 requires a manual reset — cutting power to the furnace and restoring it — before the furnace will attempt to ignite again. The board declares hard lockout after the furnace has failed to establish a flame across multiple consecutive ignition trials. This is primarily a safety measure to prevent unburned gas from accumulating.

Code 126 is most commonly seen on Trane XR80, XR95, and S9V2 series furnaces. The diagnosis is almost always the hot surface igniter, the flame sensor, or gas supply — the same three suspects on virtually every modern gas furnace.

## Common Causes

- **Failed hot surface igniter** — The silicon nitride or silicon carbide igniter element has cracked or degraded and no longer reaches the temperature needed to reliably ignite the gas-air mixture. This is the leading cause of code 126 on Trane furnaces over 5 years old.
- **Dirty flame sensor** — The flame sensor rod accumulates a thin oxide coating over time that insulates the rod from the flame, preventing the control board from confirming ignition. The furnace may actually light briefly, then shut down because the board never detected a valid flame signal.
- **Low or interrupted gas supply** — A partially closed manual shutoff valve, low utility pressure, or a momentary interruption (from a simultaneously firing water heater or gas dryer) starves the burner during the ignition trial.
- **Wrong igniter for the application** — Trane furnaces require specific igniter models. A universal aftermarket igniter with the wrong resistance profile may not reach ignition temperature on Trane's timing sequence.
- **Draft or venting issue** — If the inducer pressure switch is marginal, the furnace may start an ignition trial but abort it mid-sequence when pressure drops, never completing a successful light.

## Step-by-Step Fix {#step-by-step-fix}

1. **Manual reset the hard lockout.** Turn the thermostat to OFF. Locate the furnace disconnect switch (on the furnace wall or breaker box) and cut power for 30 seconds. Restore power. The furnace will now attempt ignition on the next call for heat. This reset is required every time code 126 appears.

2. **Observe the ignition sequence carefully.** Set the thermostat several degrees above room temperature to trigger a heat call. Watch the status LED on the control board. On Trane boards, LED blink patterns tell you where in the sequence the failure occurs. A long blink followed by 2-6 blinks indicates specific faults — document the exact blink pattern before doing anything else.

3. **Test the igniter.** Power off the furnace. Locate the hot surface igniter mounted in the burner assembly — a fragile white or gray ceramic element. Visually inspect for cracks; any crack means replacement. Using a multimeter set to ohms, measure resistance across the igniter terminals. Trane silicon nitride igniters should measure between 35–75 ohms cold. An open circuit (OL) means the igniter is failed. Trane OEM igniter **SEN00484** is the correct part for XR80/XR95 series (~$40 at Repair Clinic or HVAC parts suppliers).

4. **Clean or replace the flame sensor.** Locate the flame sensor — a single metal rod mounted in the burner flame path with a ceramic insulator and a single wire lead. Remove the mounting screw and pull the sensor out. Using a fine Scotch-Brite pad or folded dollar bill (never sandpaper), lightly polish the metal rod to remove the oxide layer. Reinstall and reconnect. Trane flame sensor **SEN00106** (~$20) is the OEM replacement if cleaning doesn't resolve the issue.

5. **Verify gas supply pressure.** Confirm the manual gas shutoff is fully open. If you have a manometer, check inlet pressure at the gas valve — Trane specifies 5–7 inches W.C. for natural gas. If you don't have a manometer, confirm other gas appliances in the home are operating normally, which rules out a utility-side pressure issue.

6. **Check igniter wiring and connections.** Inspect the wire harness connecting to the igniter. A single loose pin or cracked connector can produce intermittent ignition failures that eventually accumulate into a hard lockout. Disconnect and reconnect each connector to verify seating.

7. **Test igniter power at the board.** Using a multimeter set to AC voltage, measure voltage at the igniter leads during the ignition trial (when the igniter should be glowing). Trane boards typically supply 120V AC to the igniter. No voltage indicates a board output failure.

8. **Replace the igniter and retest.** If the igniter tests failed or falls outside spec, replace it with the OEM part. After replacement, run the furnace through 3 full heat cycles to confirm no recurrence of code 126.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | [Where to Buy](https://www.amazon.com/s?k=Where%20to%20Buy&tag=errorcodefixe-20) |  |------|------------|-------------|-------------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Hot surface igniter | SEN00484 | [$35–$50](https://www.amazon.com/s?k=%2435%E2%80%93%2450&tag=errorcodefixe-20) | Repair Clinic / Amazon |
| [Flame sensor](https://www.amazon.com/s?k=Flame%20sensor&tag=errorcodefixe-20) | SEN00106 | $18–$28 | [Repair Clinic / Amazon](https://www.amazon.com/s?k=Repair%20Clinic%20%2F%20Amazon&tag=errorcodefixe-20) |  | Gas valve | [SV9541Q8544](https://www.amazon.com/s?k=SV9541Q8544&tag=errorcodefixe-20) | $150–$220 | HVAC Distributors | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Control board (X-13) | CNT05015 | [$180–$280](https://www.amazon.com/s?k=%24180%E2%80%93%24280&tag=errorcodefixe-20) | Repair Clinic |

## When to Call a Professional

If replacing the igniter and cleaning the flame sensor doesn't resolve code 126 within two reset cycles, the furnace likely has a gas supply problem, a failed control board, or a venting/pressure issue that requires diagnostic equipment — specifically a manometer for gas pressure and a multimeter capable of microamp measurement for the flame signal. Gas valve replacement on a Trane furnace involves working with the gas supply line and requires a licensed technician in most states. If you smell gas at any point, stop work immediately, ventilate, and call your gas utility.

> **Pro tip:** When ordering a replacement igniter for a Trane furnace, always use the Trane OEM part number if possible. Universal igniters rated at the wrong resistance can glow at a lower temperature than the Trane control board expects — the board's timing sequence may cut off power to the igniter before it reaches full ignition temperature, causing code 126 to return even with a brand-new igniter installed.
