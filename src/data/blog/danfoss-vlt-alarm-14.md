---
title: "Danfoss VLT Alarm 14 - Earth Fault: What It Means and How to Fix It"
description: "Danfoss VLT Alarm 14 is an earth fault — current leaking from the output phases to ground has exceeded the safe threshold. This guide covers what causes alarm 14, how to diagnose it, and how to fix it safely."
pubDatetime: 2026-04-25T00:00:00Z
tags: [vfd, error-codes, danfoss, vlt, industrial]
---

## What Does Danfoss VLT Alarm 14 Mean?

**Alarm 14 — Earth Fault** on Danfoss VLT drives indicates that current is flowing from one or more output phases to ground. This is a protective trip — the drive detected ground current exceeding its threshold and shut down to protect the motor, the driven load, and personnel.

The VLT drive sums the instantaneous current in all three output phases (U, V, W). In a healthy system, this sum is zero — current flows out one phase and returns on the others. When current leaks to ground, the sum is no longer zero, and the drive trips on alarm 14.

This fault appears across the full Danfoss VLT family:
- VLT AQUA Drive FC 202
- VLT AutomationDrive FC 301 and FC 302
- VLT HVAC Drive FC 100 (older series)
- VLT Micro Drive FC 51
- VLT Refrigeration Drive FC 103

The underlying meaning and diagnostic approach is the same across all of them.

### What causes alarm 14?

**Motor winding fault (most common):**
Insulation breakdown in the motor windings allows current to leak from the winding to the motor frame (ground). This is the most serious cause — it means the motor insulation is degraded, which can be due to age, moisture ingress, repeated overloading, or a voltage spike that punctured the insulation.

**Motor cable fault:**
Damaged or pinched motor cable insulation allows current to leak from the conductor to the conduit, cable tray, or ground wire. High pulse voltages from the VFD switching (PWM waveform) can accelerate cable insulation degradation, especially on long cable runs.

**Moisture inside the motor:**
Water in the motor terminal box or windings provides a conductive path to ground. Common in pumps, outdoor motors, and motors in humid environments.

**Capacitive ground current on long cable runs:**
VFD output has high-frequency switching that creates capacitive current between cable conductors and cable armor/conduit. On cable runs above 50–100 meters, this capacitive current can be high enough to trigger alarm 14 even without a real insulation fault.

**Drive output IGBT fault:**
A failed IGBT in the drive's output stage can create a path to ground internally. This is less common but causes persistent alarm 14 that doesn't clear even with the motor disconnected.

---

## How to Diagnose Danfoss VLT Alarm 14

### Step 1: Isolate the motor from the drive

**Safety first: Disable the drive, open the disconnects, and verify zero voltage before disconnecting motor cables.**

Disconnect the motor cable at the drive output terminals (U, V, W). Do not just stop the motor — physically disconnect the cable.

Now attempt to restart the drive with no motor connected. If alarm 14 does not appear with the motor cable disconnected:
- The fault is in the motor or motor cable
- Proceed to steps 2 and 3

If alarm 14 appears even with the motor cable disconnected:
- The fault is internal to the drive (IGBT fault or internal ground path)
- The drive needs a qualified technician or factory service

### Step 2: Insulation resistance test on the motor

With the motor cable disconnected from both the drive and the motor, test the motor with a megohmmeter (megger):

1. Short all three motor terminals together (T1, T2, T3 tied together).
2. Apply 500V DC between the shorted terminals and the motor frame (ground).
3. Read insulation resistance after 60 seconds.

**Results interpretation:**
- **> 100 MΩ** — Excellent. Motor insulation is healthy.
- **1–100 MΩ** — Acceptable for a used motor. Monitor for decline.
- **< 1 MΩ** — Marginal. Motor should be inspected and possibly rewound.
- **< 0.1 MΩ (100 kΩ)** — Failed insulation. Motor needs repair or replacement.

For inverter-fed motors, a higher test voltage (1000V DC) is often used because VFD switching voltages stress insulation more than sine wave utility power. If using 1000V: healthy insulation should read well above 1 MΩ.

If the motor fails the megger test, motor repair or replacement is needed.

### Step 3: Insulation resistance test on the motor cable

Test the cable separately from the motor:

1. Disconnect the cable at both ends (drive terminals and motor terminal box).
2. Test insulation resistance between each conductor and the cable armor or ground wire.
3. All readings should be > 1 MΩ.

Failed cable insulation at one conductor-to-ground measurement means the cable has a fault at that conductor — likely a pinch point, damaged insulation at a conduit entry, or abrasion.

Replace the cable if any conductor fails.

### Step 4: Check for moisture

If the motor and cable test good on the megger:
1. Open the motor terminal box and inspect for water ingress — rust, condensation, or water marks.
2. If moisture is present, dry the motor (use a heat lamp or low-heat oven for the terminal box; a motor shop for full motor drying).
3. Inspect the motor shaft seals on pump motors — a leaking seal allows water into the motor housing.

### Step 5: Check cable length and consider output choke

On VLT drives with long cable runs (over 50m / 165 feet), capacitive ground current can exceed the alarm 14 threshold without any insulation fault. The fix is an **output choke (dU/dt filter)** between the drive and motor cable. This attenuates the high-frequency components of the VFD output, reducing capacitive current.

Danfoss publishes maximum cable length tables for each VLT model in the design guides — consult the table for your drive and motor cable type.

---

## How to Reset Alarm 14 on Danfoss VLT

After the fault cause is identified and corrected:

1. **Via keypad (LCP):** Navigate to the **Alarm Log** (Quick Menu → Alarm Log) and note the alarm. Press **OK** or the reset button (varies by LCP version). Then press **Start** to restart.

2. **Via digital input:** If the drive is configured for external reset via digital input, pulse the reset input.

3. **Via fieldbus (Profibus, Profinet, EtherNet/IP):** Write a reset command to the control word.

**Do not reset and restart without fixing the root cause.** Running a motor with failed insulation to ground risks electrical shock to personnel and can damage the drive's output stage.

---

## Parts You May Need

| Part | Why | Approx. Cost |
|------|-----|-------------|
| [Replacement motor (size-matched)](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-alarm-14&k=Replacement+motor+%28size-matched%29&tag=errorcodefixes-20) | Motor insulation failure — cannot repair economically | $200–$3,000+ |
| [Motor cable — shielded VFD-rated](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-alarm-14&k=Motor+cable+%E2%80%94+shielded+VFD-rated&tag=errorcodefixes-20) | Damaged cable causing ground fault | $2–$8/ft |
| [Danfoss output dU/dt filter](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-alarm-14&k=Danfoss+output+dU%2Fdt+filter&tag=errorcodefixes-20) | Reduce capacitive ground current on long cable runs | $150–$600 |
| [Megohmmeter / insulation tester](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-alarm-14&k=Megohmmeter+%2F+insulation+tester&tag=errorcodefixes-20) | Diagnose motor and cable insulation | $80–$300 (tool) |
| [Shaft seal kit (pump-specific)](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-alarm-14&k=Shaft+seal+kit+%28pump-specific%29&tag=errorcodefixes-20) | Water ingress from failed shaft seal | $20–$80 |
| [VLT drive power card / IGBT module](https://www.amazon.com/s?ascsubtag=ecf-danfoss-vlt-alarm-14&k=VLT+drive+power+card+%2F+IGBT+module&tag=errorcodefixes-20) | Internal drive fault causing alarm 14 with no motor | $300–$2,000+ |

Danfoss output filters are available from Danfoss distributors. Danfoss part numbers for dU/dt filters follow the format **132B...** for AHF and filter products — use the Danfoss VLT selection tool (drives.danfoss.com) to find the correct filter for your drive frame size and cable length.

---

## When to Call a Pro

- **Alarm 14 clears with motor disconnected but megger test passes:** This situation requires further investigation — possibly a ground fault in a junction box or conduit, or a test procedure issue. A technician with insulation testing experience can identify subtle fault locations.
- **Motor rewind or replacement:** Motor rewinding is a shop job. Replacement motor selection needs to match the drive's requirements (inverter-duty rating, speed range, frame size).
- **Internal drive fault (alarm 14 with motor disconnected):** The drive's output IGBTs may need replacement — this is a factory repair or qualified drive service center job on most VLT frames.
- **High-voltage system (above 480V):** All work on medium-voltage VFD systems requires qualified high-voltage personnel.
- **Food processing, pharmaceutical, or other regulated environments:** Insulation failures in regulated industries may require documentation, root cause analysis, and validation before resuming production.

---

## Frequently Asked Questions

**Q: Danfoss VLT Alarm 14 vs. Alarm 29 — what's the difference?**

Alarm 14 is an earth/ground fault at the output (to motor). Alarm 29 is a "Drive Fault" — an internal drive hardware fault not related to the motor. If you're seeing alarm 29, the drive itself has a problem. Alarm 14 points to the motor, cable, or external ground path.

**Q: My motor megger test shows 500 MΩ but alarm 14 keeps triggering. What's happening?**

Good insulation resistance but persistent alarm 14 usually means capacitive ground current from a long cable run. At VFD switching frequencies (2–16 kHz), cables act as capacitors between conductors and ground. Calculate your cable run length — if it exceeds the drive's maximum rated cable length, add an output dU/dt filter or sine wave filter.

**Q: Can I increase the earth fault sensitivity threshold to stop alarm 14 from tripping?**

Some VLT models allow adjusting the earth fault threshold sensitivity. On VLT AutomationDrive FC 302: **parameter 14-25 Trip Delay at Current Limit** doesn't directly address alarm 14, but **parameter 14-26 Trip Delay at Inverter Fault** and similar parameters control some protection behaviors. However, the correct approach is fixing the root cause, not desensitizing the protection.

**Q: The motor is new. Why would I get alarm 14?**

New motors can have moisture from storage or shipping. Open the terminal box and inspect. Also, some motors arrive from overseas with insulation that's been compromised by storage conditions. Run a megger test on any new motor before energizing it for the first time — this is standard commissioning practice.

**Q: Alarm 14 only appears during the first few minutes of operation on a cold morning. What's happening?**

Classic moisture symptom. When the motor is cold, condensation forms on windings and the terminal box, providing a ground path. As the motor warms up, the moisture evaporates and insulation resistance rises. The fix: drain plugs on the motor (if applicable), anti-condensation heaters, better motor sealing, or a heat trace on the motor cable if the run passes through cold areas.

## Related Articles

- [ABB ACS880 with PLC Integration Fault Codes — Troubleshooting Guide](/posts/abb-acs-drives-plc-fault/)
- [ABB ACS150 Micro Drive Fault Codes — Complete Diagnostic Reference](/posts/abb-acs150-fault-codes/)
- [ABB ACS310 Fault 3130 — Causes & Fix](/posts/abb-acs310-fault-3130/)
- [ABB ACS355 Fault 2330 — Ground Fault](/posts/abb-acs355-fault-2330/)
- [ABB ACS355 Fault 3130 — Input Phase Loss Fix](/posts/abb-acs355-fault-3130/)

## See Also

- [Danfoss FC302 Complete Fault Code Guide — All Faults and Fixes](/posts/danfoss-fc302-complete-guide/)
- [Danfoss VFD Fault OCL — Causes & Fix](/posts/danfoss-vfd-fault-ocl/)
- [Danfoss VFD Fault Codes — FC301, FC302, FC102 Reference](/posts/danfoss-vfd-fault-codes/)
- [Danfoss AKC Controller Fault Codes - Complete Guide](/posts/danfoss-akc-controller-fault/)
