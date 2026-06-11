---
title: "Carrier 54 Error Code — Soft Lockout: Low Pressure Switch Open"
description: "What Carrier error code 54 means, why the low pressure switch won't close, and how to fix it step by step."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
money_part: "Condensate trap"
---

## Carrier 54 Error Code — What It Means

Carrier fault code 54 is a **soft lockout triggered by the low-pressure switch staying open**. It appears on Carrier Performance and Comfort series furnaces (typically 2-stage 96% AFUE models like the 59TP6 and 59SC5). The control board saw the low-pressure switch remain open during the trial for ignition — so it stopped the heating sequence and set code 54.

[Jump to Fix](#fix)

A "soft lockout" means the board will retry after a wait period (usually 1 hour) rather than requiring a manual power cycle. However, the root cause must be addressed or the fault will keep recurring.

## Common Causes

- **Blocked condensate drain trap** — On 96% AFUE furnaces, condensate water builds up in the heat exchanger and flows to a PVC trap. If the trap is clogged, back-pressure prevents the inducer from creating sufficient negative pressure to close the low-pressure switch.
- **Cracked or disconnected pressure switch hose** — The short rubber hose between the inducer housing and the pressure switch develops cracks with age, leaking the vacuum signal.
- **Weak inducer motor** — An inducer motor that's losing power or whose wheel is clogged with dust/debris generates less draft and may not create enough suction to trip the pressure switch.
- **Failed low-pressure switch** — The pressure switch itself can fail in the open position. Test with a multimeter — it should close (continuity) when suction is applied with a vacuum pump or by mouth.

## Step-by-Step Fix {#fix}

1. **Turn off power to the furnace** at the disconnect switch or breaker.
2. **Locate the condensate trap** — it's the clear or white U-shaped plastic trap at the base of the secondary heat exchanger, near the bottom of the furnace cabinet. Disconnect the outlet hose and pour a cup of water through it. If water doesn't flow freely, the trap is plugged. Clean or replace it.
3. **Inspect the pressure switch hose** — trace the small-diameter rubber hose from the side of the inducer housing to the pressure switch. Look for cracks, kinks, or disconnections. Replace the hose if damaged (3/8" ID rubber tubing, available at any hardware store).
4. **Test the pressure switch** — with power off, disconnect one wire from the pressure switch and use a multimeter set to continuity. The switch should be open (no continuity) at rest. Connect a handheld vacuum pump to the switch port — the switch should close (continuity) when you apply 0.5–0.8" WC of suction. If it doesn't close, replace the switch.
5. **Check the inducer motor** — restore power briefly and verify the inducer starts and runs smoothly. If it hums but doesn't spin, the motor or capacitor is bad. If it runs but you can hear debris hitting the wheel, clean the wheel.
6. **Restore power and test** — set the thermostat to Heat and observe if the pressure switch closes when the inducer starts. If the code clears and the furnace completes a heat cycle, the repair is confirmed.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Condensate trap | [Amazon](https://www.amazon.com/dp/B077J4Y763?ascsubtag=ecf-carrier-54-error-code&tag=errorcodefixes-20) \| Brand-specific; check model label for Carrier part number |
| Pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-54-error-code&tag=errorcodefixes-20) \| 0.60" or 0.80" WC setpoint depending on model |
| Pressure switch hose | [Amazon](https://www.amazon.com/dp/B0CPTHML1N?ascsubtag=ecf-carrier-54-error-code&tag=errorcodefixes-20) \| 3/8" ID rubber vacuum hose, ~6–12" length |
| Inducer motor assembly | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?ascsubtag=ecf-carrier-54-error-code&tag=errorcodefixes-20) \| LH680016 or similar — match by model number |
## When to Call a Pro
If the trap is clear, hose is intact, and the pressure switch tests good but code 54 still appears, you likely have a failing inducer motor or a secondary heat exchanger that's partially plugged. Both require tools and expertise beyond basic DIY — contact an HVAC technician.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier Greenspeed Heat Pump Error Codes: Complete Guide](/posts/carrier-greenspeed-heat-pump-codes/)
- [Carrier 44 Error Code — Causes & Fix](/posts/carrier-44-error-code/)
- [Carrier Rooftop Unit Error Codes: Common Faults Guide](/posts/carrier-rooftop-unit-error-codes/)
- [Carrier Infinity Touch Thermostat Error Codes - What It Means and How to Fix It](/posts/carrier-infinity-touch-thermostat-error-codes/)
