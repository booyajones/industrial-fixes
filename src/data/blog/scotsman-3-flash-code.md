---
title: "Scotsman 3-Flash Code — Long Harvest Cycle Fix"
description: "Three flashes on a Scotsman Prodigy (or \"HC\" / \"Long Harvest\" on Prodigy Plus) means the harvest cycle exceeded its programmed maximum — typically 3.5..."
pubDatetime: 2026-05-20T17:00:00Z
modDatetime: 2026-05-20T17:00:00Z
author: "Marcus Webb"
slug: scotsman-3-flash-code
featured: false
draft: false
tags:
  - scotsman
  - commercial-refrigeration
  - ice-machine
  - long-harvest-cycle
  - troubleshooting
---
## Quick answer

Three flashes on a Scotsman Prodigy (or "HC" / "Long Harvest" on Prodigy Plus) means the harvest cycle exceeded its programmed maximum — typically 3.5 minutes — without the harvest thermostat satisfying. Normal harvest is 60-120 seconds. If you're staring at this code, the hot gas isn't getting where it needs to go, or the harvest thermostat isn't sensing the warmup. Field split: maybe 50% dirty evaporator (mineral scale acting as insulation), 25% weak harvest gas (compressor valve plate, hot-gas solenoid), 15% sticking purge valve, 10% sensor or wiring.

## What the 3-flash code means on a Scotsman

When the freeze cycle satisfies, the controller energizes the hot-gas solenoid (and on some models the harvest-assist motor) to dump high-side discharge gas directly into the evaporator. The evap warms, the ice slab releases, the harvest thermostat — clipped to the evap suction line — senses the temperature rise and signals harvest complete. Normal harvest is 60-120 seconds on most Prodigy and Prodigy Plus heads; under 45 seconds and you're not fully releasing the slab; over 3 minutes and the controller starts the long-harvest timer.

If the harvest thermostat doesn't see the temperature rise within the max harvest time window (3.5 minutes on most firmware revisions), the board logs a 3-flash and either retries or locks out depending on retry count. Diagnostic mode reveals the history. Hold OFF+ON for 5 seconds on Prodigy; menu on Prodigy Plus.

Don't confuse a 3-flash with a stuck slab. A stuck slab will sometimes throw a 3-flash but will also throw thermal-overload or compressor-fault codes depending on how the firmware reacts. A clean 3-flash with no other codes is almost always a harvest energy or sensing problem, not a mechanical hangup.

## Common causes (ranked by frequency)

1. **Scaled / dirty evaporator** — the most common cause and the most underdiagnosed. Mineral scale on the evap face acts as thermal insulation; the slab won't release because the evap surface itself can't warm up fast enough.
2. **Weak harvest hot gas** — discharge pressure isn't high enough, or the hot-gas solenoid valve isn't opening fully. Could be a low charge, a tired compressor (valve plate leak-back), or a stuck solenoid.
3. **Sticking purge / water-dump valve** — purge water is dumping during harvest when it shouldn't, or the valve is partially open during the freeze and dribbling warm water that prevents a clean slab. Either way, harvest stretches.
4. **Failed or mis-clipped harvest thermostat** — bulb has lost charge, or the clip slipped off the suction line and the bulb is reading ambient.
5. **Harvest assist motor failure (units so equipped)** — slab takes longer to break free because the assist arm isn't pushing.
6. **Hot gas solenoid coil failure** — coil open or shorted, valve doesn't open at all. Will usually cause near-zero harvest gas flow and a slab that never drops.

## Step-by-step fix

1. **Pull diagnostic history and watch a full harvest live.** Enter diagnostic mode, note the 3-flash count and any other codes. Then power-cycle and observe the next complete harvest. Time it. Touch the discharge line at the compressor — it should be very hot (180-220°F) within 10 seconds of harvest initiation. Touch the hot-gas line going to the evap — it should warm noticeably within 20 seconds. If the evap inlet line stays cool, your hot gas isn't flowing.

2. **Inspect the evaporator face.** Pop the front panel and the splash curtain, look at the evap face. If it's white, crusty, or you can scratch off mineral scale with a fingernail, you've found your answer. Run a cleaning cycle with Scotsman-approved nickel-safe scale remover (Scotsman Clear-1 or equivalent) per the procedure on the inside of the front panel. On heavily scaled units, plan on two consecutive cleaning cycles plus a full water-side disassembly and soak.

3. **Verify hot gas solenoid operation.** With harvest initiated, listen and feel. The solenoid should click open audibly. Touch the coil — energized coils warm up within 30 seconds. If silent and cold, pull the leads at the solenoid and check voltage at harvest initiation; should be 115 VAC on most North American models. Voltage present, no click = bad coil or stuck valve body. **Field insight: on Prodigy Plus C0322 and C0522 heads built between 2020-2022, the hot-gas solenoid coil (12-2920-22) sits directly above the compressor and runs hot all day — coil failures cluster around the 4-5 year mark on units in 90°F+ mechanical rooms. If the unit is in that age window and in a hot room, just plan to swap the coil with the diagnostic visit.**

4. **Check purge/dump valve behavior.** The purge valve should be closed during the freeze cycle and open at the start of harvest to dump the sump water. With the unit cycling, listen for purge-valve action — there should be a distinct dump-and-refill sound. If you hear water trickling during the freeze cycle, the purge valve is leaking through, washing warm water over the evap, and extending both freeze and harvest. Pull the purge valve, inspect the diaphragm and seat, replace if scaled or torn.

5. **Take operating pressures during harvest.** Discharge pressure should climb fast at harvest initiation — on R-404A you should see 250-320 psig within 15 seconds of harvest start as the hot gas dumps into the cold evap. If discharge stays low (under 180 psig in harvest), you've got a weak compressor or a low charge. Verify subcooling on the next freeze cycle — under 5°F often indicates undercharge.

6. **Bench-test the harvest thermostat.** Pull both leads. Closed in ice water (or at room temp on a cold bulb), open at warm water (above 55-65°F depending on the model's cut-out). OEM is 11-0408-21 on most Prodigy heads. Confirm the bulb clip is tight and the bulb is fully contacting the suction line — gap there reads false-cold and stretches harvest.

7. **Inspect harvest assist motor (if equipped).** On heads with a harvest-assist arm, the motor energizes briefly during harvest to push the slab. Listen for the motor run; feel the gearbox warm slightly. A burned motor or stripped gear is common past 6 years. OEM motors in the 02-3950 series; verify by serial. **Insight: the harvest assist motor on C0530 / C0630 / C0830 units commonly seizes from refrigerant oil migrating onto the gear lubricant — symptom is a one-time crackling noise on harvest, then silence. Replace the gear assembly, not just the motor.**

8. **Reset, verify, and document.** Clear the code history, watch two full freeze/harvest cycles, and confirm harvest is back to 60-120 seconds. If you cleaned scale, follow up with the operator on water filtration — without filtration the scale will be back in 6 months.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|------|------------|--------------|--------------|
| Hot-gas solenoid coil (Prodigy Plus) | 12-2920-22 | $68-$112 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-3-flash-code) |
| Hot-gas solenoid valve body | 12-2920-21 | $145-$210 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-3-flash-code) |
| Purge/dump valve assembly | 12-2917-22 | $78-$118 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-3-flash-code) |
| Harvest thermostat | 11-0408-21 | $48-$72 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-3-flash-code) |
| Harvest assist motor (C0530/C0630) | 02-3950-21 | $215-$310 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-3-flash-code) |
| Scotsman Clear-1 nickel-safe scale remover | 19-0653-01 | $42-$68 | [Parts Town](https://partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=scotsman-3-flash-code) |
| Infrared thermometer (Fluke 62 MAX+) | — | $98-$135 | [Amazon](https://amazon.com) |
| Inline water filter cartridge | — | $48-$120 | [Amazon](https://amazon.com) |

## When to call a professional

Hot-gas solenoid valve body replacement involves opening the sealed system — recovery, brazing, evacuation, weigh-in charge — and is EPA Section 608 work. If you're a kitchen tech without 608 cert and an HVAC torch, stop at the solenoid coil swap and call out the valve body work. Same for any compressor-related diagnosis if you suspect a tired valve plate — leave that for the refrigeration contractor.

Brilliance R-290 units add another layer: hot-gas circuit work on hydrocarbon refrigerant requires HC-certified handling and the right recovery equipment. Don't improvise on R-290.

## FAQs

**Q: My harvest is exactly 3 minutes — is that a 3-flash waiting to happen?**
A: Yes. Healthy harvest is 60-120 seconds. Anything pushing 150 seconds is trending toward the limit and tells you something is off — usually early-stage scale or a weakening solenoid. Address it before it becomes a no-ice service call.

**Q: I cleaned the evap and the harvest is still long. Now what?**
A: Move to discharge pressure during harvest. If discharge isn't climbing fast at harvest initiation, the hot-gas circuit is weak — solenoid not fully open, low charge, or tired compressor. Take temps on the hot-gas line: cold or warm hot-gas line at the evap inlet during harvest is the giveaway.

**Q: The slab drops but the cycle still logs 3-flash. Why?**
A: The slab can drop before the harvest thermostat satisfies if the bulb isn't sensing the warm-up properly. Check the bulb clip, the suction-line contact, and the harvest thermostat itself. Bulb that's slipped off the suction line is a classic cause — the slab releases on the hot gas but the bulb still reads cold and the cycle times out.

**Q: How often does the evap actually need scale removal?**
A: Depends on water hardness. With municipal water under 4 grains hardness and a good filter, every 12-18 months is fine. Untreated well water or hard municipal (8+ grains), every 4-6 months. If the customer pushes back on scale-cleaning frequency, get a hardness reading off their water and show them the math.

**Q: Can I run the unit with a leaking purge valve until the part comes in?**
A: For a day or two, yes, but you'll see degraded cube quality and extended cycles. Don't let it ride a week — the constant water dribble on the evap during freeze will eventually trip the long-freeze code (2-flash) too, and the operator will think you missed something.

## Related guides

- [Scotsman 1-Flash Code — Bin Full / Bin Thermostat Fix](/posts/scotsman-1-flash-code)
- [Scotsman 2-Flash Code — Long Freeze Cycle](/posts/scotsman-2-flash-code)
- [Scotsman 4-Flash Code — High Discharge Temperature](/posts/scotsman-4-flash-code)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Hoshizaki vs Manitowoc ice machines](/posts/hoshizaki-vs-manitowoc-ice-machines/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc vs Scotsman ice machines](/posts/manitowoc-vs-scotsman-ice-machines/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best refrigeration vacuum pump](/posts/best-vacuum-pump-for-refrigeration/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc E01 long freeze cycle fix](/posts/manitowoc-e01-error-code/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Manitowoc HPCO high pressure cutout](/posts/manitowoc-hpco-error-code/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** Hoshizaki E2 long freeze cycle fix
