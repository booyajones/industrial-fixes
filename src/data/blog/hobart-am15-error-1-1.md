---
title: "Hobart AM15 Error 1-1 — Wash Motor Overload Fix"
description: "Hobart AM15 Error 1-1 means the wash pump motor drew current past the overload trip during a wash cycle — the motor is binding, the impeller is jammed, or..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "Marcus Webb"
slug: hobart-am15-error-1-1
featured: false
draft: false
tags:
  - hobart
  - wash-motor-overload
  - troubleshooting
---
## Quick answer

Hobart AM15 Error 1-1 means the wash pump motor drew current past the overload trip during a wash cycle — the motor is binding, the impeller is jammed, or the overload protector itself has failed. Six out of ten times I clear this in the field, it's debris jammed in the impeller (paper labels, broken glass, a fork tine), not a dead motor.

## What Error 1-1 means on a Hobart AM15

The AM15 (and the related AM15T and AM15VL models) is Hobart's high-volume single-rack door-style dishwasher used in K-12, healthcare, and mid-size restaurant operations. The control board monitors the wash pump motor through a current-sensing input on the motor contactor circuit and a thermal overload protector built into the motor windings. When motor current exceeds the trip threshold (typically around 14-16 A on the 208/240 V 3-phase wash motor) or the thermal overload opens, the board logs Error 1-1, kills the wash cycle, and parks the machine.

The "1-1" format is Hobart's two-number diagnostic code system: the first digit indicates the subsystem (1 = wash motor circuit) and the second digit indicates the fault type (1 = overload trip). Related codes you might see stacked or alternating with 1-1 include 1-2 (wash motor no-current, motor disconnected or contactor failed open) and 1-3 (wash motor undercurrent, low voltage condition).

Error 1-1 is mechanical or electrical at the motor side — it's almost never the control board. The diagnostic order: inspect the wash pump housing for debris, verify motor windings and bearing condition, check incoming voltage, and only then suspect the contactor or overload relay.

A subtle point on the AM15: the wash pump impeller is a cast bronze open-impeller design with a relatively tight clearance to the volute housing. A piece of broken china or a steel fork tine can wedge between the impeller and housing in a way that doesn't immediately stop rotation but creates enough drag to push current past trip. You'll find the debris when you pull the impeller cover, not when you spin the motor by hand.

## Common causes (ranked by frequency)

1. **Debris jammed in wash pump impeller** — broken glass, china fragments, silverware, paper labels, food bones.
2. **Wash motor bearing failure** — older motors (8+ years) develop bearing drag that pushes current toward trip on hot, full-load cycles.
3. **Failed thermal overload protector inside motor** — trips at lower current than spec, especially after the motor has had a real overload event.
4. **Low incoming voltage** — voltage drop on a hot kitchen circuit can cause motor amperage to climb to compensate, triggering overload.
5. **Locked-rotor from a stuck seal or impeller-to-housing rub** — usually after a long off-period when seal materials swell from sitting wet.
6. **Wash arm restriction creating excessive back-pressure** — clogged spray nozzles force the pump to operate at higher head pressure, drawing more current.
7. **Failed motor contactor with welded contacts** — chatters, motor sees intermittent supply, draws inrush repeatedly, trips overload.
8. **Failed control board overload sensing input** — rare. Last on the diagnostic list.

## Step-by-step fix

1. **Power down the dishwasher at the disconnect.** Lockout-tagout if you're in a commercial kitchen environment — AM15s are typically 208 or 230 V 3-phase, and you do not want this to start on you while your hand is in the pump housing.

2. **Drain the tank and access the wash pump.** Open the door, pull the rack, lift out the wash arms (top and bottom), and remove the strainer baskets. Drain the wash tank through the drain — there's typically a manual drain lever on the front of the AM15. With the tank empty, you can see down into the pump suction port at the bottom of the tank.

3. **Inspect the impeller suction for debris.** Shine a light down into the pump suction port. You're looking for any foreign object — broken china, glass shards, silverware, plastic, paper labels (the AM15 tank screen catches most but not labels under 2"). If you can see debris, pull the wash arm assembly fully and use a long mechanic's grabber to fish it out. Don't put your hand into the pump suction without confirming power is off and locked out.

4. **Pull the wash pump housing cover.** On the AM15 the pump housing has a clamshell cover held by 4-6 stainless bolts. Drain any residual water, remove the bolts, and lift the cover. Now you can see the impeller and the volute. Inspect for: debris wedged in the impeller vanes, impeller-to-housing rub marks (scored housing or bent impeller vanes), and any deposit of scale or hard water buildup that's reduced clearance.

5. **Spin the impeller by hand.** With the cover off, the impeller should rotate freely with light finger pressure. Significant drag, grinding, or detent-like resistance points to bearing failure or seal failure. Note that some seal drag is normal — the mechanical seal has a face spring — but it should be smooth resistance, not grinding.

6. **Reassemble and check motor windings electrically.** Once you've cleared debris and verified the impeller spins freely, button up the pump and check the motor electrically. With power off, measure phase-to-phase resistance at the motor terminals — should be 1-3 Ω on a 1.5 HP 3-phase wash motor, all three readings within about 10%. Megger-test winding-to-ground at 500 VDC; should read above 50 MΩ. Open windings, shorted phase, or ground fault condemns the motor (Hobart parts in the 00-XXXXXX-XXX format; the AM15 wash motor is typically 00-913665-XXX series).

7. **Verify incoming voltage during a wash cycle.** Restore power, close the door, and start a wash cycle while watching voltage at the wash motor contactor line side. On a 208 V 3-phase service, you should see 200-216 V phase-to-phase. Drops below 195 V during compressor start in adjacent equipment indicate a voltage sag that's triggering overload — this is a building electrical issue, not a dishwasher fault.

8. **Test the contactor and overload relay.** With the motor energized, the contactor should pull in cleanly with no chatter. Use a clamp meter on the motor leads — running current should sit at 8-12 A on a healthy 1.5 HP wash motor under load. Climbing toward 15 A indicates motor or impeller drag. Inspect the overload relay (mounted with the contactor in the control panel) for any signs of past trip events — discolored heaters or visible arc damage.

> **Field knowledge nugget:** On Hobart AM15 machines installed in K-12 cafeterias, I see a specific 1-1 pattern related to the paper milk-carton straws and small condiment cup lids that sneak through pre-rinse. The trap: these items are small enough to pass through the strainer baskets but rigid enough to wedge between the impeller and the volute housing on the discharge side. They don't show on the suction-side inspection (step 3 above) because they get pushed through the impeller eye and lodge on the *outlet* side. The diagnostic tell: you've cleared the suction, verified the impeller spins free by hand, reassembled, and 1-1 returns on the first cycle. The fix is to pull the entire pump housing cover (the second clamshell on the discharge side, behind the wash arm distribution manifold) and inspect there. I've pulled milk-carton straws, plastic spoon fragments, condiment cup lids, and once a kindergarten-grade plastic toy out of AM15 discharge sides. Worth knowing on any school account where Error 1-1 keeps returning after pump cleaning. The discharge cover seal kit is Hobart 00-274846-001 and should be replaced any time you open it.

**Safety:** Commercial dishwashers handle caustic chemicals — typically a chlorinated alkaline detergent and a rinse-aid sanitizer. When you open the pump housing or wash arm assembly, you'll likely encounter residual chemical solution. Wear chemical-resistant gloves (nitrile, not latex), eye protection, and have running water nearby for accidental contact. Before any service work that involves opening chemical injector lines, **flush the chemical injectors completely** by triggering a no-detergent cycle or by disconnecting the detergent feed line from the chemical pump — undiluted detergent in the supply line can splash on you when you break a fitting. The MSDS for the chemicals used in your specific account should be on file in the manager's office; review for exposure limits and first-aid procedures.

## Parts that may need replacement

| Part | OEM Number (typical) | Typical Cost | Where to Buy |
|---|---|---|---|
| Wash pump motor (1.5 HP 3-phase) | 00-913665-XXX | $585–$895 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=hobart-am15-error-1-1) |
| Wash pump impeller | 00-274700-001 | $145–$215 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=hobart-am15-error-1-1) |
| Pump housing seal kit | 00-274846-001 | $35–$65 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=hobart-am15-error-1-1) |
| Motor contactor (24 V coil) | 00-771530-001 | $95–$165 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=hobart-am15-error-1-1) |
| Overload relay | 00-771544-001 | $105–$185 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=hobart-am15-error-1-1) |
| Wash arm assembly (upper) | 00-887580-001 | $175–$285 | [Parts Town](https://www.partstown.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=hobart-am15-error-1-1) |

For any pump cover open, replace the housing seal. Hobart seals don't reliably reseat once compressed.

## When to call a professional

Call a CFESA-certified commercial dishwasher tech if:

- Motor windings test bad and you don't have experience pulling a 1.5 HP motor from a wash pump assembly (the AM15 motor is shaft-coupled with a Lovejoy coupler and requires alignment on reinstall).
- You suspect a building electrical issue (voltage sag, phase imbalance) — a CFESA tech can coordinate with the building electrician.
- The control board is suspect after ruling out everything else. Hobart board replacements should be done with proper config-jumper verification.
- The machine is under Hobart warranty (typically 1 year parts and labor on full machine, 2 years on certain components). Hobart-authorized servicer required.
- You see any chemical injection issue, leak, or unusual chemical accumulation — chemical system problems are a separate service discipline.

## FAQs

**How do I clear Error 1-1 on a Hobart AM15?**
Power down at the disconnect for 30 seconds, restore power. The board clears the fault. If the underlying cause isn't fixed, 1-1 returns within 1-2 cycles.

**Can I just push the reset button on the overload relay?**
On AM15s with a manual-reset overload, yes — pop the reset button after diagnosing and clearing the cause. But always diagnose first; don't make a habit of resetting and walking away.

**Why does my AM15 throw 1-1 mid-cycle?**
Mid-cycle 1-1 (vs. startup 1-1) usually means the impeller is OK at idle but binds under load — a partial obstruction that pumps for a few minutes then catches debris and trips. Inspect both suction and discharge sides of the pump housing.

**What current draw is normal for the AM15 wash motor?**
On a 208 V 3-phase service, a healthy 1.5 HP wash motor draws 8-12 A under load. Anything climbing to 14+ A indicates drag — bearing, impeller obstruction, or motor issue.

**Will hard water cause Error 1-1?**
Indirectly, yes. Heavy scale buildup in the pump housing reduces impeller-to-volute clearance, increases drag, and pushes current toward trip. Quarterly delime with Hobart Delimer (or equivalent acid descaler) is preventive. Hard water also clogs spray nozzles, increasing pump backpressure.

## Related guides

- [Jackson Conserver Series Error 1 — Low Water Fix](/posts/jackson-conserver-error-1)
- [Champion UH130 Error Code — Fill Cycle Fix](/posts/champion-uh130-error-code)
- [Manitowoc E01 Error Code — Long Freeze Cycle Fix](/posts/manitowoc-e01-error-code)
