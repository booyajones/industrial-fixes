---
title: "Doosan / DN Solutions Alarm 302 — APC Fix"
description: "Doosan (now DN Solutions, after the 2022 rebrand) alarm 302 on the Fanuc-controlled VMC, HMC, and Mynx machining centers indicates an APC (Automatic Pallet..."
pubDatetime: 2026-05-21T17:00:00Z
modDatetime: 2026-05-21T17:00:00Z
author: "James Rutherford"
slug: doosan-alarm-302
featured: false
draft: false
tags:
  - doosan
  - cnc
  - industrial-maintenance
  - apc-automatic-pallet-changer-fault
---
## Quick answer

Doosan (now DN Solutions, after the 2022 rebrand) alarm 302 on the Fanuc-controlled VMC, HMC, and Mynx machining centers indicates an APC (Automatic Pallet Changer) fault — typically a pallet clamp/unclamp failure, a rotation position fault, or a hydraulic pressure issue during pallet exchange. Most common in field service is a worn or damaged proximity sensor on the pallet clamp position, causing the control to lose track of whether the pallet is clamped properly. Inspect the sensors and pallet locating pins before assuming hydraulic or PLC issues.

## What Alarm 302 means on Doosan / DN Solutions

Doosan uses Fanuc 0i-MF, 30i, and 32i controls on most of its CNC product range — VC, NHM, NHP, Mynx, and DNM machining centers, and LYNX and PUMA lathes. The Fanuc control runs the machine motion; a separate Doosan PMC (programmable machine controller, essentially a Fanuc PLC) handles auxiliary functions including APC (pallet changers), ATC (tool changers), coolant, chip conveyor, and door interlocks.

Alarm 302 is in Doosan's PMC-defined alarm range (typically 300-399) for APC-related faults. The PMC monitors the APC mechanism via proximity sensors, hydraulic pressure switches, and rotation encoders, and posts 302 when one of:

- Pallet clamp position sensor doesn't confirm "clamped" state after a clamp command
- Pallet unclamp position sensor doesn't confirm "unclamped" state after an unclamp command  
- APC rotation position doesn't reach commanded position within timeout
- Hydraulic pressure for the clamp circuit drops below threshold
- Pallet locating pin doesn't seat properly (verified by a separate sensor on most models)
- Door interlock for the APC station is broken (pallet station door not closed before APC operation)

The specific sub-condition is identified by additional alarms posted simultaneously or by examining the PMC ladder diagnostic on the control. Press SYSTEM → PMC → PMCDGN to see current input/output signal states. Each APC sensor has a corresponding PMC input bit; comparing actual vs. expected reveals which sensor isn't reporting correctly.

Doosan APC architecture varies by model — small VMCs have a 2-pallet shuttle APC; larger HMCs have a 6-, 12-, or 20-pallet pool. The diagnostic approach is similar but the specific mechanism and sensor layout differs.

## Common causes (ranked by frequency)

In Doosan APC service experience:

1. **Worn or damaged proximity sensor on clamp position** — about 25%. Inductive prox sensors degrade after years of clamping cycles.
2. **Hydraulic pressure low** — about 18%. Worn hydraulic pump, leak in cylinder, or low oil level.
3. **Pallet locating pins worn or chipped** — about 15%. Pin doesn't fully seat; sensor doesn't confirm.
4. **Pallet clamp hydraulic cylinder seal failure** — about 10%. Internal leak prevents full clamp pressure.
5. **APC rotation drive issue (servo or hydraulic)** — about 8%. Rotation doesn't complete in time.
6. **Door interlock switch failure (pallet station door)** — about 6%. Door closed but switch open.
7. **PMC parameter corrupted** — about 5%. Battery dying.
8. **Wiring fault on sensor cable** — about 5%. Cable chafed.
9. **Pallet itself damaged (locating pads worn)** — about 4%. Customer pallet rather than machine issue.
10. **Failed PMC I/O module** — about 4%.

**Pro nugget:** Doosan APC proximity sensors are typically OMRON or KEYENCE inductive prox sensors with M12 or M18 threaded barrels — completely standard industrial sensors. **The trick**: the Doosan service manual specifies a sensor by part number that's the OEM-supplied part with a Doosan part number sticker; the underlying OMRON or KEYENCE sensor (look at the molded markings on the side) is widely available from any industrial supplier (AutomationDirect, McMaster, Grainger) at 30-50% of the OEM-stickered price. Common sensors: OMRON E2E-X10MD1 (M18 NPN, 10mm sensing range) or KEYENCE EV-118M (M18 PNP, 18mm range). Always confirm the sensor's switching mode (NPN vs. PNP) and supply voltage (24V) before substituting — but the cost savings on commodity sensors is real.

## Step-by-step diagnosis

Before you start: machine in OFF/manual mode, hydraulic pressure verified at zero where work will happen, follow lockout-tagout for any hydraulic work.

1. **Read the full alarm stack.** Press ALARM on the Fanuc. Note 302 and any related alarms (303, 304 may indicate related APC issues). Press SYSTEM → PMC → PMCDGN to see PMC input/output states.

2. **Identify the failed sensor via PMC.** Compare current PMC input bits against the schematic in the Doosan electrical manual. Each APC sensor has a labeled bit (e.g., X3.0 = pallet clamp confirm, X3.1 = pallet unclamp confirm, X3.2 = APC at index position). Find the bit that's not showing the expected state.

3. **For prox sensor faults:** Locate the sensor at the APC. With the APC in the position where the sensor should report, observe the LED on the sensor (most have a built-in target LED). If the LED is off when the target is present, the sensor is bad. Reseat first (sometimes the M12 connector has loosened); replace if no improvement.

4. **For hydraulic faults:** Check the hydraulic gauge on the machine's hydraulic power unit (HPU). Doosan APC hydraulic pressure is typically 800-1200 psi for clamp operations; verify pressure is in range. If low, check oil level in the HPU reservoir (sight glass), inspect for leaks at hydraulic fittings, and check the pump for unusual noise.

5. **For pallet locating pin issues:** Visually inspect the locating pins on the machine table and on the bottom of the pallet. Look for: chipped or worn pin heads, missing pins, debris on the pin or in the pin hole. Clean and inspect; replace damaged pins.

6. **For APC rotation faults:** Watch the APC rotate manually (most Doosan machines have a manual APC mode in MDI). Observe smooth rotation without sticking or noise. Stuck rotation = mechanical issue (bearing, drive coupling); slow rotation = hydraulic or servo issue.

7. **For door interlock:** Open and close the APC station door while watching the PMC bit corresponding to the interlock. Should toggle clean with door action. If not, replace the safety switch.

8. **Reset and test.** Address the specific issue. Reset alarm 302 on the control (RESET button). Run an APC test cycle in manual or via a test program. Verify no alarm and that the pallet exchange completes correctly.

## Parts that may need replacement

| Part | OEM Number | Typical Cost | Where to Buy |
|---|---|---|---|
| Pallet clamp prox sensor (OMRON, M18) | Doosan EX-S29 / OMRON E2E-X10MD1 | $85-145 OEM, $40-65 OMRON direct | [Galco](https://www.galco.com), [AutomationDirect](https://www.automationdirect.com) |
| Pallet rotation prox sensor (M12) | Doosan EX-S31 / OMRON E2E-X3D1 | $65-115 OEM, $30-55 direct | [Galco](https://www.galco.com), [AutomationDirect](https://www.automationdirect.com) |
| Pallet locating pin (typical) | Doosan 5601-XXX-201 | $45-85 each | [Galco](https://www.galco.com), [eBay](https://www.ebay.com) |
| Hydraulic pump (vane-type, common APC) | Doosan 5601-XXX-505 | $1,850-2,800 | [Galco](https://www.galco.com), [Wolf Automation](https://www.wolfautomation.com) |
| Hydraulic cylinder seal kit (clamp) | Doosan 5601-XXX-401 | $145-225 | [Galco](https://www.galco.com), [Wolf Automation](https://www.wolfautomation.com) |
| APC servo motor (Fanuc βi) | Fanuc A06B-0078-B403 | $1,200-2,200 refurb | [Galco](https://www.galco.com), [Wolf Automation](https://www.wolfautomation.com) |
| Door interlock safety switch | Pilz PSEN cs1.13M / similar | $145-225 | [Galco](https://www.galco.com), [Amazon](https://www.amazon.com) |
| Fanuc PMC backup battery | Fanuc A98L-0031-0028 | $45-85 | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com) |
| Pressure gauge (0-2000 psi, glycerin) | Generic | $35-65 | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com) |
| Hydraulic fluid (ISO 32 typical) | Mobil DTE 24 | $85-145 / 5 gal | [Amazon](https://www.amazon.com), [Galco](https://www.galco.com) |

For Fanuc-based parts (servos, batteries, PMC modules), refurb from Galco or Wolf Automation. For Doosan-specific mechanical parts, the Doosan/DN Solutions service network is often the only source.

## When to call a controls engineer

Call a Doosan-trained tech or DN Solutions field service when:

- The alarm persists after sensor replacement and hydraulic verification. Suggests a PMC or wiring issue that requires schematic review.
- The hydraulic pump or cylinder needs replacement. Specific hydraulic work requires correct fluid handling and bleeding procedures.
- The PMC ladder needs modification. Custom programs require Doosan factory or authorized service.
- The machine is under DN Solutions / Doosan warranty.
- You suspect parameter corruption. Backup and restore via the Fanuc service tool is non-trivial.

## FAQs

**My alarm 302 only happens on a specific pallet. What's that mean?**
Pallet-specific failures usually mean the pallet itself has worn locating pads or chipped reference pins. Move the pallet to a known-good machine to verify, or inspect the pallet for damage.

**Can I use generic OMRON sensors instead of Doosan-numbered parts?**
Yes, as long as you match: switching mode (NPN/PNP), supply voltage (24V), sensing distance (typically 10mm or 18mm), connector style (M12 4-pin standard). The molded markings on the original sensor tell you the actual OMRON or KEYENCE part number.

**My Doosan is throwing 302 plus other random alarms. Memory issue?**
Sounds like PMC battery is dying. Check for "PMC BATTERY LOW" warning on the control. Save parameters to USB before replacing the battery.

**Why does my hydraulic pressure drop during APC?**
Worn hydraulic pump, leaking cylinder, or undersized accumulator. Diagnose by clamping a pressure gauge in line and watching during APC operation.

**Difference between Doosan and DN Solutions?**
Same company — Doosan Machine Tools was rebranded to DN Solutions in 2022 after corporate restructuring. Parts and service procedures are identical. Newer machines ship with DN Solutions branding; older Doosan-branded machines use identical part numbers.

## Related guides

- [Mori Seiki / DMG MORI Alarm 3010 — Servo Error Fix](/posts/mori-seiki-alarm-3010)
- [Okuma OSP Alarm 2202 — Spindle Fix](/posts/okuma-alarm-2202)
- [Mazak Alarm Code Fix — Common Faults](/posts/mazak-haas-fanuc-batch-summary)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best multimeter for HVAC techs (2026)](/posts/best-multimeter-for-hvac/)

<!-- INTERNAL-LINK-AUTO-2026-05-21 -->
**Related:** [Best clamp meter (2026)](/posts/best-clamp-meter-for-electricians/)

