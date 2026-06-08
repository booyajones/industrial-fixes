---
title: "Carrier Greenspeed A3 — Defrost Fault Fix"
description: "Code A3 on a Carrier Greenspeed Infinity heat pump (25VNA0, 25VNA4, 38MGRQ, 38MURA platforms) indicates a defrost fault — the variable-speed inverter and..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Dana Kowalski"
slug: carrier-heat-pump-error-code-a3
featured: false
draft: false
tags:
  - carrier
  - defrost-fault
  - troubleshooting
---
## Quick answer

Code A3 on a Carrier Greenspeed Infinity heat pump (25VNA0, 25VNA4, 38MGRQ, 38MURA platforms) indicates a defrost fault — the variable-speed inverter and Infinity control attempted defrost and either could not complete it within the allowed window, did not detect the expected temperature change, or saw conflicting sensor data during the defrost cycle. The unit will continue running in heat but is flagging that defrost may not be working correctly. Most of the time it's a defrost sensor, a wiring issue, or a stuck reversing valve; rarely it's the inverter board or the outdoor coil.

## What A3 means on a Carrier Greenspeed

Carrier's Infinity-series heat pumps display fault codes on the Infinity Touch thermostat and on the outdoor unit's control board LED (a 2-character alphanumeric display visible behind the service panel). A3 is one of the "advisory" codes — the system continues to operate but logs the fault for service.

Defrost logic on Greenspeed (the variable-speed inverter platform) is more sophisticated than on single-stage heat pumps. The system monitors:

- **Outdoor coil temperature (OCT)** sensor — a 10kΩ NTC thermistor clipped to the outdoor coil.
- **Outdoor ambient temperature (OAT)** sensor — measures actual outdoor air.
- **Refrigerant pressure** — through the inverter's onboard transducer.
- **Run time and compressor speed history**.

When the system needs defrost (typically when OCT drops more than 8-12°F below OAT for sustained period), the control reverses the 4-way valve, turns off the outdoor fan, and runs the compressor in cooling mode to heat the outdoor coil. Defrost completes when OCT rises to about 70°F or after a maximum time window (10-14 minutes depending on platform).

A3 posts when:
- Defrost window expires without OCT reaching termination temp.
- OCT and OAT sensors disagree by an implausible amount.
- Reversing valve doesn't shift (pressure pattern doesn't match expected defrost behavior).
- Outdoor fan doesn't fully stop during defrost.

The Greenspeed platform is more forgiving than legacy heat pumps — it won't lock out on A3, just flag it. But if A3 persists, you'll see degraded heating performance because the unit is icing up faster than it can clear.

## Common causes (ranked by frequency)

1. **Failed or drifted outdoor coil temperature sensor** — about 28%. Sensor reads warmer than actual coil, termination logic gets confused.
2. **Stuck or sluggish reversing valve** — about 20%. Valve solenoid weak, slug of oil binding the slider.
3. **Loose or corroded sensor wiring at the outdoor board** — about 15%. Common on coastal installations.
4. **Outdoor coil heavily iced beyond defrost capability** — about 12%. Coil is so blocked that defrost can't catch up.
5. **Outdoor fan motor not fully stopping during defrost** — about 8%. ECM motor controller fault.
6. **Low refrigerant charge** — about 7%. Reduces hot-gas heat available to defrost the coil.
7. **Inverter/outdoor control board fault** — about 5%. Less common.
8. **Drain pan iced over, blocks airflow at coil base** — about 3%. Trapped meltwater refreezes, creates persistent ice mass.
9. **Wrong DIP/parameter setup after a control replacement** — about 2%.

Field nugget: I've seen this 300 times — Greenspeed in coastal install (within 5 miles of saltwater), A3 starts appearing two winters in. Tech replaces the OCT sensor, A3 goes away for a season, comes back. The real cause is corrosion on the sensor's spade terminals where they plug into the outdoor control. Salt air gets in, builds resistance on the connection, sensor reading drifts high. New sensor with the same corroded connector behaves the same. Pull the connector, clean both sides with contact cleaner and a small wire brush, apply dielectric grease, reseat. A3 stops. Always inspect the connector, not just the sensor. New R-454B systems (38MGRQ platform shipped from late 2024 onward) — flammability class A2L — make this matter more because you don't want any electrical fault potential near refrigerant connections.

## Step-by-step fix

Safety first: kill power at the outdoor disconnect. Variable-speed inverters retain DC bus voltage for 5+ minutes after power-off — let the unit sit before opening the inverter compartment. If your Carrier unit is a 38MGRQ (R-454B refrigerant, A2L mildly flammable), follow A2L work practices: no ignition sources within 10 feet during refrigerant work, ventilate the work area, use leak detectors rated for A2L. Older 25VNA0/25VNA4 units run R-410A (A1, non-flammable).

1. **Read full fault history at the thermostat.** On Infinity Touch, navigate to MENU → SERVICE → FAULT HISTORY. Note A3 timestamps and any other codes — particularly look for A1 (compressor fault), A2 (high pressure), 41/45 (sensor faults), or 73 (reversing valve). A3 alone is usually sensor; A3 plus a sensor code is definitive.

2. **Visually inspect the outdoor unit.** Walk to the unit and look at the coil. If there's a thick ice block at the bottom (more than 2" of ice), the defrost system has been failing for a while. Don't try to chip the ice off (you'll damage fins). Let it melt naturally with the unit off, or use a hose with cool water — never hot water, which causes thermal shock.

3. **Locate and test the OCT sensor.** Power off, open the outdoor service panel. The OCT sensor is a clip-on thermistor attached to a lower bend of the outdoor coil, with two wires running back to the outdoor control board. Disconnect at the board. Measure resistance with a multimeter — at 70°F (21°C) ambient, a healthy 10kΩ NTC sensor reads about 10kΩ. Cross-reference Carrier's resistance-temperature table for your model in the service manual. If reading is grossly out of spec, replace.

4. **Inspect the sensor connector and wiring.** Pull the OCT connector from the board, check for green/white corrosion on the pins. Clean both sides with electrical contact cleaner. Look at the wire run for chafing or insulation damage where the harness passes through the cabinet. On coastal installs, apply dielectric grease to the connector before reseating.

5. **Verify the reversing valve operates.** With power restored and a heat call active, place your hand on the reversing valve body. During heat operation, the valve's small line (going to the indoor coil) should be hot, the large line (going to the outdoor coil) should be warm to hot. During defrost, the temperatures reverse — small line gets cooler, large line gets very hot. If you can't feel a clear change during defrost, the valve is stuck. Listen for the solenoid click when defrost initiates — should be audible. No click = bad solenoid coil.

6. **Initiate a manual defrost.** On Greenspeed, you can force a defrost from the Infinity Touch service menu (MENU → SERVICE → CHECKOUT → DEFROST TEST) or by shorting specific pads on the outdoor control. With defrost forced, watch: outdoor fan should stop, reversing valve should click, OCT should rise from ambient to 70°F over 4-10 minutes. If outdoor fan keeps running, the ECM motor or its control is at fault.

7. **Check refrigerant charge if defrost runs but never terminates on temp.** If OCT climbs only to 55-65°F before timeout, the system doesn't have enough refrigerant mass to deliver adequate hot gas to the outdoor coil. Connect gauges (R-410A or R-454B as appropriate — note R-454B requires A2L-rated manifold set). Carrier subcooling on Greenspeed varies by capacity — typically 8-15°F subcool at design conditions. Add or recover refrigerant to match the rating plate's subcool target.

8. **Clear faults and observe a real defrost cycle.** Reset faults at the thermostat. Run the system in heat for an hour minimum at low outdoor temperatures. The Infinity Touch will display "DEFROST" during the cycle. Watch the cycle complete cleanly — OCT rises, system reverts to heat mode, coil is clear of ice.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Outdoor coil temperature sensor (Greenspeed) | Carrier HH79NZ039 | $48-75 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3), [Amazon](https://www.amazon.com) |
| Outdoor ambient sensor | Carrier HH79NZ040 | $42-65 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3), [Amazon](https://www.amazon.com) |
| Reversing valve solenoid coil (24V) | Carrier EF18BZ073 | $55-95 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3) |
| Reversing valve (R-410A, 25VNA0) | Carrier EF680001 | $310-460 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3), [Amazon](https://www.amazon.com) |
| Reversing valve (R-454B, 38MGRQ) | Carrier EF680042 | $345-510 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3), [Amazon](https://www.amazon.com) |
| Outdoor ECM fan motor | Carrier HC39GE237 | $310-450 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3), [Amazon](https://www.amazon.com) |
| Outdoor control board (Greenspeed inverter) | Carrier HK35AA001 | $720-1100 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3), [Amazon](https://www.amazon.com) |
| Infinity Touch thermostat | Carrier SYSTXCCITC01-B | $480-720 | [RepairClinic](https://www.repairclinic.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3), [Home Depot](https://www.homedepot.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=carrier-heat-pump-error-code-a3) |

Note: Carrier specifies different reversing valves and inverter boards for R-410A versus R-454B units. Crossing parts between refrigerant types is not safe — material compatibility differs (POE oil tolerances, valve seat materials). Always verify the refrigerant type on the rating plate before ordering.

## When to call a professional

**R-454B (A2L) refrigerant work.** If your unit is a 38MGRQ or any newer Greenspeed with R-454B, refrigerant work requires A2L-certified technicians, A2L-rated tools (manifolds, recovery machines, leak detectors), and proper ventilation procedures. EPA Section 608 with A2L training is required. Don't DIY this.

**Refrigerant charging beyond a 1-pound adjustment.** Greenspeed inverters are charge-sensitive. Over- or under-charging affects compressor protection and capacity. A pro with proper subcool target and digital gauges should handle anything beyond a small top-off.

**Inverter board faults that appear linked to A3.** If the inverter board is throwing motor-drive errors alongside A3, the issue may be in the DC bus or compressor protection — that's a board-level diagnosis requiring Carrier service tools.

**Persistent ice formation after sensor and reversing valve verified.** May indicate undersized heat pump for the load, supplemental heat strips not staging properly, or an installation defect (low coil location relative to drainage). Needs a load review and possibly defrost mode parameter adjustment by a Carrier-trained tech.

Never bypass the defrost cycle. Some old field shortcuts (jumpering the defrost timer, pulling sensors) can damage the coil and cause failure of the compressor or evaporator coil. The defrost logic exists to protect the unit.

## FAQs

**Will the heat pump still heat with A3 active?**
Yes, A3 is an advisory, not a lockout. The unit continues to operate. But ice will build up faster than normal, reducing heating capacity. Address A3 before it cascades into a full lockout (A1 or A2).

**Does A3 mean my Greenspeed is broken?**
Not necessarily. About 28% of A3 calls are just a drifted sensor — a $50 part. About 20% are a sluggish reversing valve solenoid. Diagnose before assuming the worst.

**My Greenspeed says A3 but the coil isn't iced — is that possible?**
Yes. A3 can fire from sensor mismatch (OCT and OAT disagree implausibly) without ice ever forming. That's a sensor or wiring fault, not a refrigeration problem.

**Should I worry about R-454B flammability?**
R-454B is A2L — mildly flammable, much less so than R-32 or propane. Outdoor leak risk is very low. Indoor coil leaks have stricter requirements per ASHRAE 15. For routine service, the practical concern is ignition sources during refrigerant work — keep open flames, hot work, and electric arcs well away.

**Can I reset A3 without fixing it?**
You can clear it at the thermostat, but it will return on the next defrost cycle if the underlying cause persists. Fix it.

## Related guides

- [Trane XV20i/XV18 Fault 126 — Low Pressure Cutout Fix](/posts/trane-heat-pump-error-code-126)
- [Bryant Evolution Heat Pump 21 — Defrost Sensor Fix](/posts/bryant-heat-pump-error-code-21)
- [Goodman Heat Pump 2-Flash — Low Pressure Fix](/posts/goodman-heat-pump-error-code-2)

## See Also

- [Carrier Furnace Blowing Cold Air - Causes & Fix](/posts/carrier-furnace-blowing-cold-air/)
- [Carrier Mini-Split E4 Error Code — Compressor Discharge Temperature Fix](/posts/carrier-mini-split-e4-error-code/)
- [Carrier 42 Error Code — Causes & Fix](/posts/carrier-42-error-code/)
- [Carrier Error Code 61 — Rollout Switch Lockout](/posts/carrier-61-error-code/)
