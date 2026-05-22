---
title: "Mori Seiki / DMG MORI Alarm 3010 — Servo Error Fix"
description: "Mori Seiki / DMG MORI Alarm 3010 (sometimes formatted as \"SV-3010\" or \"Servo Alarm 3010\" in the OPERATOR screen) is a Fanuc servo amplifier error indicating..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "James Rutherford"
slug: mori-seiki-alarm-3010
featured: false
draft: false
tags:
  - mori-seiki
  - cnc
  - industrial-maintenance
  - servo-amplifier-error
---
## Quick answer

Mori Seiki / DMG MORI Alarm 3010 (sometimes formatted as "SV-3010" or "Servo Alarm 3010" in the OPERATOR screen) is a Fanuc servo amplifier error indicating the servo drive detected an internal fault — most commonly an IPM (intelligent power module) overcurrent event, a DC link capacitor undervoltage, or a feedback line communication fault between the amp and the motor encoder. About 35% of 3010 alarms after years of service are caused by aged DC link capacitors in the servo amplifier, not motor or encoder failures.

## What Alarm 3010 means on Mori Seiki / DMG MORI

Mori Seiki (now DMG MORI Co., Ltd. after the 2013 merger with German DMG Mori AG) uses Fanuc control systems as the dominant CNC platform — typically the 0i-MF, 30i, 31i, or 32i series on lathes (NL, NLX, NTX series) and machining centers (NV, NMV, DMU series). Fanuc servo systems use a common architecture across all Fanuc-equipped builders: a power supply module (PSM), one or more servo amplifier modules (SVM) for the axes, and brushless AC servo motors with absolute encoders.

Alarm 3010 on the Fanuc control specifically points to a fault detected by a servo amplifier — the amp self-monitors its IGBTs, DC link capacitors, encoder feedback signal, and command bus, and posts 3010 with a sub-code on the amp itself (small 7-segment display on the amp's front face). The control display shows "3010" followed by the affected axis (e.g., "3010 X-AXIS" or "3010 Z-AXIS").

To get the specific sub-code, look at the amp's front face directly — there's a small status display showing a two-character alarm code:
- **8** — Power module overheating
- **8.** (8 with period) — Power module overcurrent (IPM trip)
- **5** — DC link low voltage
- **A** — Encoder feedback error (communication or signal)
- **C** — Cooling fan failure (on amps with internal fans)
- **L** — Lifetime exceeded warning on DC link capacitors

The sub-code is critical — it changes the diagnostic path entirely. A "5" alarm (low DC bus) points to the PSM or to a tripped supply contactor; an "8." alarm (IPM overcurrent) points to a motor short or excessive load; an "A" alarm (encoder) points to a feedback cable or encoder failure.

## Common causes (ranked by frequency)

In DMG MORI / Mori Seiki Fanuc-equipped CNC service:

1. **Aged DC link capacitors in the SVM** — about 25%. Caps lose capacitance after 7-12 years, posts low-voltage faults.
2. **Failed cooling fan inside the SVM or on the PSM** — about 18%. Overheats, posts thermal trip.
3. **Encoder feedback cable damage** — about 15%. The encoder cable from motor to amp runs through cable carriers and chafes over time.
4. **Motor winding short or partial insulation breakdown** — about 12%. Decades of coolant exposure degrades motor insulation.
5. **PSM (power supply module) failure or fuse blown** — about 8%.
6. **Brake circuit problem on motors with holding brakes** — about 6%. Stuck brake causes overcurrent.
7. **Servo amplifier (SVM) module failure** — about 6%. Power module IGBT failed.
8. **Encoder battery dead causing absolute position loss** — about 4%.
9. **Cable connector corrosion at amp or motor** — about 3%.
10. **Parameter mismatch after a recent service** — about 3%.

**Pro nugget:** Fanuc servo amplifiers (SVM) and power supply modules (PSM) carry a documented capacitor service life — Fanuc publishes a "lifetime warning" parameter that begins counting at first power-up and triggers warning code "L" on the amp display when ~80% of design life is reached. **This warning is conservative** — most amps continue to function fine for years past the warning. But once you see a 3010 with a "5" sub-code (low DC link), the warning has become reality and the caps need replacement (or the entire amp). Don't ignore lifetime warnings; they're trying to tell you something. The fastest field fix is amp swap — a refurbished SVM from Wolf Automation or Galco runs $1500-3500 vs. $5000-8000 new from Fanuc, and the refurb shops bench-test before shipping.

## Step-by-step diagnosis

Before you start: machine off, control off, main disconnect locked and tagged. Wait at least 10 minutes after power-down for DC link capacitors to discharge. Verify zero voltage at the PSM DC bus terminals with a CAT-IV meter before touching anything — Fanuc DC bus runs at 300-600 VDC and stays lethal for 5-10 minutes after main power drops.

1. **Read the amp's sub-code.** Open the electrical cabinet, locate the affected axis's SVM (each amp has its axis labeled on a sticker — X, Y, Z, etc.). Read the small 7-segment display on the front of the amp. Note the sub-code (8, 8., 5, A, C, or L).

2. **Read the Fanuc diagnostic screens.** On the control, press SYSTEM → DIAG. Read the diagnostic parameters specific to the affected axis. Look at: position error, current command vs. actual, encoder absolute position. A sudden jump in position error preceding the alarm often indicates a mechanical event (crash, sudden load change).

3. **For sub-code 5 (low DC link):** Check the PSM output voltage with a meter on the DC bus terminals. Should be 300-600 VDC depending on the model (typically 600 VDC class for medium and large machines). If low, the PSM is failing or the main contactor isn't fully closed. If correct, the SVM's internal caps are failing — replace amp.

4. **For sub-code 8 or 8. (IPM thermal or overcurrent):** Verify the cooling fan on the amp is spinning (mounted on top of the amp typically). Check the heat sink for dust accumulation; clean. If thermal sustained, replace the amp. For overcurrent, disconnect the motor cable and re-power — if alarm clears, the motor or cable has a short.

5. **For sub-code A (encoder error):** Inspect the encoder cable from the motor to the amp. Look for: chafing in cable carriers, melt damage, broken connectors. Ohm-test continuity on each conductor end-to-end. Bench-test the encoder if possible (Fanuc encoders communicate via a serial protocol; specialized test gear required).

6. **For sub-code C (cooling fan):** Fan failure is straightforward — replace the fan. Most Fanuc amps use a snap-in 80mm or 120mm DC fan on top of the unit; replacements are commodity and inexpensive ($25-50).

7. **Megger the motor.** Disconnect the U-V-W leads from the SVM output. With a 500V megohmmeter, test each phase to ground. Anything below 1 megohm at 25°C is degraded insulation; below 100 kΩ and you have a motor that's about to fail. Replace motor if grounded.

8. **Check encoder battery if motors have absolute encoders.** Fanuc absolute encoders use a small battery in the amp cabinet to maintain position when main power is off. Dead battery = absolute position lost on power cycle = alarm 3010 sub-code A and homing required. Replace the battery ($50-100 for OEM Fanuc) and re-establish home position.

9. **Replace the SVM if the diagnostic isolates to the amp.** Order by exact Fanuc part number (typically A06B-6164-Hxxx format). Confirm match by both the model number and the firmware revision shown on the amp sticker.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Servo amp (αi SVM 1-axis 20A, common) | Fanuc A06B-6240-H105 | $1,850-3,200 (refurb), $4,800-6,800 (new) | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010), [Wolf Automation](https://www.wolfautomation.com) |
| Servo amp (αi SVM 2-axis 40A) | Fanuc A06B-6240-H226 | $2,200-3,800 (refurb), $5,500-7,500 (new) | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010), [Wolf Automation](https://www.wolfautomation.com) |
| Power supply module (αi PSM) | Fanuc A06B-6240-H030 | $1,500-2,800 (refurb), $3,800-5,800 (new) | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010) |
| Servo motor (αi 8/3000 typical Y-axis) | Fanuc A06B-0235-B400 | $1,800-2,600 (refurb), $3,800-5,500 (new) | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010), [eBay](https://www.ebay.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010) |
| Encoder cable (per meter) | Fanuc A66L-6001-0026 | $45-85/m | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010) |
| Power cable (per meter) | Fanuc A06B-6093-K803 | $35-65/m | [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010) |
| Cooling fan (amp top, 80mm DC) | Fanuc A90L-0001-0481 | $35-65 | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010) |
| Encoder battery (3V lithium, BR-2/3AGCT4A) | Fanuc A98L-0031-0028 | $45-85 | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010) |
| Megger insulation tester (500V) | Fluke 1577 | $385-485 | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010) |
| CAT-IV true-RMS multimeter | Fluke 87V | $445-585 | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com?utm_source=errorcodefixes&utm_medium=affiliate&utm_campaign=mori-seiki-alarm-3010) |

Wolf Automation and Galco are the dominant US refurb sources for Fanuc servo components. Confirm exact part number including firmware revision before ordering — Fanuc has multiple sub-revisions of similar-looking amps that aren't interchangeable.

## When to call a controls engineer

Call a Fanuc-trained controls engineer when:

- The alarm involves the PSM or main control unit. Fanuc system replacements require parameter backup and restoration via the Fanuc service tool.
- You need to set up a refurbished or used amp on the machine. The serial number of the new amp may need to be registered with Fanuc maintenance parameters, and motor / amp matching parameters may need adjustment.
- Encoder absolute position has been lost and you can't re-establish home. Reference setting on Mori Seiki machines requires specific procedure that varies by axis type.
- The machine is under DMG MORI service contract. Most factory contracts require authorized service for warranty preservation.

## FAQs

**Why is my new amp throwing 3010 immediately after install?**
Most common: parameter mismatch. The amp's serial-number-locked parameters in the Fanuc control need to match the actual amp installed. Either the new amp's serial needs to be registered, or you need to update parameter 1942 (and related) to match.

**Can I use a non-Fanuc amp on my DMG MORI?**
No. The PSM-SVM intercom bus is proprietary Fanuc; only Fanuc amps speak it.

**My amp shows "L" warning but no 3010 yet. What should I do?**
"L" means lifetime warning — the caps are approaching end of life. Plan for amp replacement in the next 12-24 months. Order a refurb amp ahead of failure to minimize downtime.

**Will replacing the encoder battery clear an "A" sub-code?**
Only if the underlying issue was battery-related. If the encoder cable or encoder itself has failed, battery replacement won't help.

**Difference between 3010 (servo) and other Fanuc alarms?**
3010 = servo amplifier error. 401 = ready signal absent. 414 = servo position deviation excessive. 432 = overload alarm. Different alarm numbers point to different subsystems.

## Related guides

- [Okuma OSP Alarm 2202 — Spindle Fix](/posts/okuma-alarm-2202)
- [Doosan Fanuc-based Alarm 302 — APC Fix](/posts/doosan-alarm-302)
- [Mazak Alarm Code Fix — Common Faults](/posts/mazak-haas-fanuc-batch-summary)
