---
title: "Trane / American Standard 2-Blink Error Code — External Lockout Fix"
description: "A 2-blink code on a Trane or American Standard furnace means external lockout: the board tried three times to light the burners, failed every attempt, and..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Dana Kowalski"
slug: trane-2-blink-error-code
featured: false
draft: false
tags:
  - trane
  - hvac
  - error-codes
  - external-lockout-failed-retries
---
## Quick answer

A 2-blink code on a Trane or American Standard furnace means external lockout: the board tried three times to light the burners, failed every attempt, and shut everything down for safety. The real fault isn't "2-blink" — it's whatever made all three ignition attempts fail. Usually that's a dirty flame sensor, a tired hot surface igniter, or a gas supply issue, and you find the actual culprit by power-cycling and watching the very first ignition attempt carefully.

## What 2-blink means on a Trane / American Standard

Trane and American Standard are the same furnace under different badges — both owned by Trane Technologies (formerly Ingersoll Rand), and they share control boards, parts, and diagnostic codes line-for-line. On older units with an LED status light (usually green or red), count two slow blinks, pause, two more. On newer XV and XC variable-speed models with a two-digit alphanumeric display, you'll see "2" or "21" depending on the platform.

The 2-blink is a meta-code. It does not point to a specific component. It means: "I attempted ignition three times in a row, each attempt failed to prove flame, and per code I am locking out for one hour or until you reset me." On almost every Trane platform the lockout will auto-clear after about 60 minutes, or you can clear it by cycling the thermostat to OFF for 30 seconds, or by pulling the door switch and letting the board reboot.

The trick is this: once the board is in lockout, the 2-blink tells you nothing about *why*. To diagnose, you need to power-cycle the system, set the thermostat to heat, and stand at the furnace watching that very first ignition sequence. Trane's 2-blink is really a meta-code — "I tried 3 times and gave up." To find the real fault you need to power-cycle and watch the FIRST ignition sequence carefully. Don't just go straight to parts replacement.

## Common causes (ranked by frequency)

1. **Dirty flame sensor** — about 35%. The sensor rod is coated with carbon or silicate from combustion. It can't conduct enough microamps to prove flame.
2. **Weak or cracked hot surface igniter (HSI)** — about 20%. HSI lights briefly then cracks open mid-cycle, or it never gets hot enough.
3. **Flame sensor positioned outside the flame envelope** — about 10%. Sensor rod is bent or burner has shifted.
4. **Gas supply issue (low pressure, partial closure)** — about 10%. Inlet pressure below 5" WC for NG, valve regulator drifted.
5. **Gas valve failure (slow to open, partial opening)** — about 8%.
6. **Igniter electrical fault (broken lead, bad connector)** — about 7%.
7. **Burner crossover restriction (debris between burners)** — about 5%.
8. **Control board ignition output failure** — about 5%.

Note that all of these end in the same place: three failed tries, then lockout. The 2-blink doesn't pick a favorite. You have to.

## Step-by-step fix

Before you start: shut off power at the disconnect and gas at the valve. Wait five minutes for the inducer to fully spin down and the HSI to cool. The HSI is brittle and you can crack it just by touching it.

1. **Clear the lockout and watch one full ignition attempt.** Restore power and gas. Set thermostat above setpoint by 5°F. Stand at the open burner area with a flashlight. You should see: inducer spins → pressure switch clicks closed → HSI glows orange-white (about 30-45 seconds) → gas valve clicks open → flame ignites all burners → HSI de-energizes → flame remains for 7-10 seconds → blower starts. Watch each step. Whichever one fails is your diagnostic anchor.

2. **If the HSI never glows or glows dimly:** Power down. Pull the HSI (two screws and a quick-disconnect plug). Cold-resistance test with a multimeter — typical Trane HSI reads 40-90Ω cold. Open circuit = replace. Visibly cracked or pitted = replace. Trane part 23W51 (Norton series) or aftermarket equivalents work; do not handle the new HSI element with bare fingers.

3. **If the HSI glows but burners don't light:** You have HSI but no gas, or gas without successful proving. Visually confirm the burner flame appears (gas valve worked) — if no flame, check gas inlet pressure with a manometer at the valve inlet tap. NG should read 5-7" WC static, holding 4.5-5" WC during operation. LP should be 10-11" WC. Low inlet pressure means your gas supply is choked — could be a partially-closed shutoff, a tripped excess-flow valve at the meter, or in extreme cold, an undersized gas line dropping pressure during high demand.

4. **If burners light but extinguish in ~5 seconds:** This is the flame sensor failing to prove. Power down. Pull the flame sensor (usually one screw, easy access right next to the burner box). Clean the metal rod gently with a Scotch-Brite pad or 0000 steel wool — no sandpaper, no emery cloth (the abrasive embeds in the metal and ruins it). The rod should be bright silver-gray with no carbon. Reinstall, making sure the rod sits in the flame envelope of the burner.

5. **Measure flame current.** With burners firing, put a multimeter in series with the flame sensor lead — set to DC microamps. Healthy flame current is 2-6 µA DC on most Trane platforms. Below 0.7 µA the board will not reliably prove flame and you'll get inconsistent ignition. If you can't get above 1 µA even with a clean sensor, the sensor itself or its ceramic insulator may be cracked.

6. **Check the gas valve.** Hook the manometer to the outlet (manifold) pressure tap with burners running. NG manifold should read 3.5" WC, LP 10" WC. If it's drifting low, the valve regulator is failing — replace the valve. White-Rodgers 36J24 series is what's in most Trane residential furnaces.

7. **Inspect burner crossover ports.** Burners light sequentially via flame crossover between adjacent burners. If the cross-lighting ports are clogged with rust scale or spider webs, the first burner lights but #2, #3, #4 don't — flame sensor sees a flame but on cycle two or three only some burners catch, and the board calls it a failed light. Vacuum the burner area and use compressed air to blow out the crossover slots.

8. **Reassemble and test three full cycles.** After repair, run the unit through three consecutive heat calls (lower then raise the thermostat each time). All three should light cleanly within 5 seconds of HSI shutoff. If one of three fails, you still have a marginal issue — usually flame current on the edge of spec.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Hot surface igniter (Norton-style) | Trane IGN00065 / 23W51 | $35-65 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-2-blink-error-code), [Amazon](https://www.amazon.com) |
| Flame sensor rod | Trane SEN01114 | $20-40 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-2-blink-error-code), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-2-blink-error-code) |
| Gas valve (White-Rodgers 36J24) | Trane VAL06642 / 36J24-614 | $130-220 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-2-blink-error-code), [Amazon](https://www.amazon.com) |
| Integrated furnace control | Trane CNT06077 / D341396P01 | $220-360 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-2-blink-error-code), [Amazon](https://www.amazon.com) |
| Burner assembly (per burner) | Trane BNR01049 | $30-55 each | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-2-blink-error-code) |
| HSI installation kit (universal) | White-Rodgers 767A-373 | $35-50 | [Amazon](https://www.amazon.com), [Lowes](https://www.lowes.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=trane-2-blink-error-code) |

Brand-share note: American Standard furnaces of the same era use identical control boards, igniters, and gas valves. The part number prefix may differ (e.g., AS uses ACONT vs Trane TCONT) but the components are the same. Check the original sticker.

## When to call a professional

Two scenarios that warrant a tech:

**Gas supply problems beyond a partial shutoff.** If you confirmed low inlet pressure (below 5" WC NG static) and the upstream shutoff is fully open, you may have a meter regulator issue, a buried line problem, or an undersized supply line. These are utility-coordinated repairs, not homeowner work.

**Repeat 2-blink after replacing HSI, flame sensor, AND verifying gas pressure.** That points to either a control board with a marginal flame-sensing circuit, or a heat exchanger issue distorting the flame pattern. Both need experienced eyes and a combustion analyzer to diagnose properly. Running a furnace with persistent ignition issues is also a CO risk — incomplete combustion during repeated retry attempts puts unburned fuel into the heat exchanger.

Never bypass any safety, never jumper the flame-prove circuit. The whole point of these controls is to keep raw gas out of your house. They are not the enemy.

## FAQs

**The furnace lights fine when I'm watching but locks out overnight. Why?**
You have an intermittent — usually a marginal flame sensor (flame current right at 1 µA), a thermal-expansion gas valve issue, or a loose connector that vibrates open. Clean the sensor, measure flame current, and wiggle every connector on the burner side. Intermittent ignition is almost always a "low-margin" problem rather than a hard failure.

**Can I clean the flame sensor with steel wool or sandpaper?**
Use 0000 steel wool or a fine Scotch-Brite pad. No sandpaper, no emery cloth — abrasives leave grit on the rod that interferes with flame ionization. A simple wipe is often enough if buildup is light.

**My HSI looks fine but won't glow. Just replace it?**
Test with an ohmmeter first. Cold reading should be 40-90Ω. Open circuit (OL) = bad. Within spec but still no glow = check the lead, the connector, and the 120V output from the board to the HSI socket. HSIs are usually around $40-60; if you've ruled out everything else, swap it.

**Will the 2-blink reset on its own?**
Yes — most Trane boards auto-clear after 60 minutes. But it'll lock out again next call if you haven't fixed the underlying cause.

**My furnace is an XV80 with a display showing "21" — is that the same code?**
Yes, "21" on the digital display is the same external lockout fault, just shown numerically on the variable-speed boards instead of as flashes. Same diagnostic process.

## Related guides

- [Trane 4-Blink Error Code — Limit Circuit Trip Fix](/posts/trane-4-blink-error-code)
- [Lennox Error Code 240 — Ignitor Failed Fix](/posts/lennox-error-code-240)
- [Goodman 3-Flash Error Code — Pressure Switch Open Fix](/posts/goodman-3-flash-error-code)

## See Also

- [Trane XV80 Furnace Error Codes — Flash Code Diagnostic Guide](/posts/trane-xv80-error-codes/)
- [Trane XL20i Variable Speed Error Codes — Complete Guide](/posts/trane-xl20i-error-codes/)
- [Trane Precedent Rooftop Unit Error Codes: Complete Guide](/posts/trane-precedent-error-codes/)
- [Trane 8 Flashes Error Code — Causes & Fix](/posts/trane-8-flashes-error-code/)
