---
title: "Siemens SINAMICS G120 VFD Complete Setup and Fault Code Guide"
description: "Complete Siemens SINAMICS G120 VFD guide covering commissioning with Startdrive, all major fault codes F0001–F0106, parameter backup and restore, and BOP-2 keypad operation."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - vfd
  - industrial
  - error-codes
---

The Siemens SINAMICS G120 is a modular, high-performance VFD widely deployed in pumps, fans, conveyors, and compressors across manufacturing, water treatment, and building automation. Its modular Control Unit / Power Module architecture offers flexibility — but it also means setup and fault diagnosis require understanding which component is causing the problem. This guide walks through first-time commissioning with Startdrive, decoding the most common fault codes, backing up and restoring parameters, and navigating the BOP-2 operator panel.

---

## G120 Hardware Overview

The G120 consists of two primary components:

- **Control Unit (CU):** Contains the drive logic, fieldbus interface, and parameter memory. Common variants: CU230P-2 (pump/fan), CU240E-2 (general purpose with safety), CU250S-2 (positioning).
- **Power Module (PM):** Contains the rectifier, DC bus, and IGBT inverter stage. Sized by power rating and frame size (FSA through FSF+).

The two communicate via a high-speed backplane connector. Faults prefixed **Fxxxx** are active faults requiring acknowledgment. Alarms prefixed **Axxxx** are warnings that don't trip the drive.

---

## Commissioning with Startdrive

Siemens Startdrive is the PC commissioning tool for the G120, integrated as a TIA Portal add-in. It provides a guided wizard, full parameter access, and real-time diagnostics. Here's the standard commissioning sequence for a new installation.

### Step 1: Hardware Check Before Power-Up

Before applying power:
- Verify input voltage matches the PM's rated input (check PM nameplate).
- Confirm motor nameplate data is available: rated voltage, current, frequency, speed, power factor.
- Check that all power connections (L1/L2/L3 input, U/V/W output) are tight and correctly phased.
- Verify the motor cable shield is grounded at the drive end.

### Step 2: Connect Startdrive

1. Connect a USB cable from your PC to the CU's USB port (Type B, front of CU).
2. Open TIA Portal → Create new project → Add device → SINAMICS G120 CU variant matching your hardware.
3. Go Online — TIA Portal will detect the drive and sync the device configuration.

### Step 3: Quick Commissioning Wizard

In Startdrive, navigate to **Commissioning → Quick Commissioning**. The wizard walks through:

1. **Application class** — select Standard Drive Control or Vector Control based on load type.
2. **Motor data entry** — enter all nameplate values. Enable motor data identification if motor data is uncertain (parameter P1900 = 1 for stationary ID, P1900 = 2 for rotating ID).
3. **Control mode** — V/f (simple loads like fans) or Vector (higher dynamic response needed).
4. **Setpoint source** — analog input, fieldbus (PROFINET/PROFIBUS), or fixed speeds.
5. **Ramp times** — set P1120 (acceleration ramp) and P1121 (deceleration ramp) appropriate for your load inertia.
6. **Motor protection** — enable electronic thermal protection (P0610 = 1) and set the motor temperature warning threshold.

Accept and download the configuration to the drive. The drive will execute motor identification if selected — ensure the motor is connected and free to rotate (or locked for stationary ID).

### Step 4: Verify Operation

Run the motor from Startdrive's control panel at low speed (10–20 Hz). Monitor:
- Output current (r0027) — should match no-load current expectation
- Output voltage (r0025) — should track V/f ratio
- Drive temperature (r0037) — should remain stable

If the motor runs smooth with no faults, ramp to full speed and verify load current is within nameplate rating.

---

## BOP-2 Keypad Operation

The BOP-2 (Basic Operator Panel 2) is the front-mounted operator panel for the G120. It provides local control, parameter access, and fault readout without a PC.

### Key Functions

| Button | Function |
|--------|----------|
| ▲ / ▼ | Navigate parameter list or change value |
| OK | Confirm selection or value |
| ESC | Cancel / go back |
| ► (run) | Start drive (local mode) |
| ■ (stop) | Stop drive |
| FN (function) | Toggle between status display and parameter menu |

### Navigating Parameters

Press **OK** to enter the parameter menu. Use **▲/▼** to scroll to the parameter number (e.g., P1120). Press **OK** to select, **▲/▼** to change the value, and **OK** to confirm. Press **ESC** to exit without saving.

### Fault Acknowledgment via BOP-2

When a fault is active, the BOP-2 displays the fault code (e.g., F0001). After correcting the underlying cause, press **FN** then **OK** to acknowledge the fault. If the fault condition is still present, acknowledgment will fail and the code will reappear.

### Local vs. Remote Mode

The G120 defaults to remote (fieldbus/analog) control. To take local control at the BOP-2, press and hold **FN** for 2 seconds — the LOCAL indicator appears. Return to remote by pressing and holding **FN** again. Note: local mode setpoint is a separate parameter from remote setpoint — set P1040 for BOP-2 local reference speed.

---

## Fault Code Reference

### F0001 — Overcurrent

**Meaning:** Output current exceeded the trip threshold. The PM detected a phase current above the overcurrent limit.  
**Common causes:** Motor short circuit, ground fault in motor cable, acceleration ramp too fast for the load inertia, output contactor switching under load.  
**Fix:** Check motor insulation resistance (500V DC megohmeter — minimum 1 MΩ). Check motor cable for damaged insulation. Increase P1120 (acceleration ramp time). Never switch an output contactor while the drive is outputting voltage.

### F0002 — Overvoltage

**Meaning:** DC bus voltage exceeded the overvoltage trip threshold (approx. 820V DC for 400V input).  
**Common causes:** Regenerative energy from fast deceleration exceeding DC bus absorption capacity, input supply voltage too high, input voltage transients.  
**Fix:** Increase P1121 (deceleration ramp time). For high-inertia loads that must stop quickly, install a braking resistor connected to the PM's braking chopper terminals. Verify input supply voltage is within specification.

### F0003 — Undervoltage

**Meaning:** DC bus voltage fell below minimum threshold. Power supply disruption detected.  
**Common causes:** Input supply voltage dip or interruption, blown input fuse, loose input terminal, undersized supply transformer or cabling.  
**Fix:** Check input voltage at the PM terminals under load (voltage should remain above 85% of nominal). Check input fuses and terminal torque values. If the supply has known voltage dips, set P0210 (input voltage) correctly and review kinetic buffering options (P1240).

### F0004 — Overtemperature (Drive)

**Meaning:** Control unit or power module temperature exceeded the trip threshold.  
**Common causes:** Blocked cooling vents, ambient temperature above 40°C (50°C with derating), failed cooling fan, drive overloaded beyond thermal rating.  
**Fix:** Clean cooling vents and heatsink fins. Verify ambient temperature. Check fan operation. Review load current against drive rated current — derate if ambient is above 40°C per Siemens derating tables.

### F0011 — Motor Overtemperature

**Meaning:** Motor thermal model or external motor temperature sensor (PTC/KTY) indicates the motor is overheating.  
**Common causes:** Motor overloaded, ambient temperature too high at motor location, blocked motor cooling, incorrect motor thermal parameters in drive.  
**Fix:** Check motor load current against nameplate. Verify P0625 (ambient temperature at motor) is correctly set. If using a PTC thermistor, check wiring continuity to CU terminals. Review P0626–P0628 (motor temperature limits).

### F0100 — Power Unit: Overcurrent

**Meaning:** Power module hardware overcurrent protection triggered — distinct from F0001 (software-level overcurrent). This is a hardware trip inside the PM.  
**Common causes:** Output short circuit, ground fault close to drive output, IGBT gate driver fault.  
**Fix:** Disconnect motor cables and test for phase-to-phase and phase-to-ground shorts at the U/V/W terminals. If the fault clears without load connected, the fault is in the motor or cable. If fault persists with no load, the PM may have internal damage.

### F0101 — Power Unit: Overtemperature

**Meaning:** Power module temperature sensor detected overtemperature — hardware-level trip (vs. F0004 which can be CU thermal model).  
**Fix:** Same procedure as F0004. Check cooling fan in the PM, clean heatsink, verify ambient temperature and derating.

### F0102 — Power Unit: Voltage Fault

**Meaning:** Abnormal voltage detected in the power module — DC bus or phase voltage out of expected range.  
**Fix:** Check input supply voltage. Verify all input phases are present and within spec. Check for loose connections at L1/L2/L3 input terminals.

### F0105 — Power Unit: Communication Fault

**Meaning:** Communication between the Control Unit and Power Module has failed or timed out.  
**Common causes:** Loose CU-to-PM backplane connector, CU not fully seated on PM, damaged connector pins.  
**Fix:** Power down completely, remove CU from PM, inspect backplane connector for bent or corroded pins, reseat firmly until it clicks. Verify CU firmware is compatible with the PM variant.

### F0106 — Power Unit: Incompatible

**Meaning:** The Control Unit and Power Module are not compatible — mismatched firmware or hardware variants.  
**Fix:** Check CU and PM firmware versions against Siemens compatibility matrix (available in the G120 system manual). Update CU firmware via Startdrive if required. Confirm the PM is a supported type for the installed CU variant.

---

## Parameter Backup and Restore

Backing up parameters before any firmware update, major parameter change, or service event is essential. The G120 stores parameters in the CU's non-volatile memory, but a corrupted parameter set or wrong firmware update can reset everything to factory defaults.

### Backup via Startdrive

1. Connect Startdrive to the drive (USB or PROFINET).
2. Go Online with the drive.
3. Navigate to **Project → Upload from Device**.
4. Save the project file (`.ap16` / `.ap17` depending on TIA Portal version) to a labeled folder with the date.
5. For a parameter-only backup: **Drive → Parameters → Export to file** → save as `.xml` or `.dds` file.

### Restore via Startdrive

1. Open the saved project or parameter file.
2. Go Online with the drive.
3. Navigate to **Download to Device** → select parameter set.
4. Confirm and execute. The drive will restart to apply the new parameters.

### Backup via BOP-2 (to Onboard Memory Card — CU240E-2 / CU250S-2)

1. Navigate to parameter P0010 = 30 (upload parameters to memory card).
2. Set P0802 = 1 to start upload.
3. The BOP-2 will display a progress indicator. When complete, P0010 returns to 0.
4. To restore: Set P0010 = 30, P0803 = 1.

This method is useful for cloning parameters to a replacement CU in the field without a PC.

---

## Replacement Parts

| Part | Use Case | Link |
|------|----------|------|
| Siemens BOP-2 Operator Panel | Replacement keypad / local control | [View on Amazon](https://www.amazon.com/s?k=Siemens+BOP-2+operator+panel&tag=errorcodefixes-20) |
| SINAMICS G120 PM240-2 Power Module | Power module replacement (various kW ratings) | [View on Amazon](https://www.amazon.com/s?k=Siemens+SINAMICS+G120+power+module&tag=errorcodefixes-20) |
| USB Programming Cable (Type B) | Startdrive commissioning connection | [View on Amazon](https://www.amazon.com/s?k=USB+type+B+programming+cable+industrial&tag=errorcodefixes-20) |
| Megohmmeter / Insulation Tester | Motor insulation resistance check (F0001 diagnosis) | [View on Amazon](https://www.amazon.com/s?k=megohmmeter+insulation+tester+500v&tag=errorcodefixes-20) |
| Braking Resistor (400V, appropriate ohm/watt for drive size) | F0002 overvoltage on deceleration fix | [View on Amazon](https://www.amazon.com/s?k=VFD+braking+resistor+400v&tag=errorcodefixes-20) |
| Fluke 87V Industrial Multimeter | Terminal voltage and continuity checks | [View on Amazon](https://www.amazon.com/dp/B08ZJSN5X3?tag=errorcodefixes-20) |
| PTC Thermistor (Motor Protection) | Motor overtemperature protection (F0011) | [View on Amazon](https://www.amazon.com/s?k=PTC+thermistor+motor+protection&tag=errorcodefixes-20) |

---

## Frequently Asked Questions

**What is the difference between a fault and an alarm on the G120?**  
Faults (F-codes) cause the drive to trip and stop the motor — they require acknowledgment before the drive can restart. Alarms (A-codes) are warnings that indicate an approaching limit or abnormal condition but do not stop the drive. Monitor alarms seriously: an A0503 (Motor Overtemperature Warning), for example, will become an F0011 fault trip if not addressed.

**How do I acknowledge a G120 fault without a PC?**  
Using the BOP-2 keypad: after correcting the fault cause, press **FN** then **OK** to acknowledge. You can also acknowledge via a digital input configured for fault acknowledgment (P0700 = 2, P0701–P0706 = 9 for ACK). Via fieldbus, set control word bit 7 (RESET) from 0 to 1 to acknowledge.

**My G120 shows F0105 every time I power up. What's wrong?**  
F0105 (CU-PM communication fault) on every power-up almost always means the Control Unit is not fully seated on the Power Module backplane connector. Power down completely, remove the CU, inspect the backplane connector for bent pins, then reseat firmly until you feel/hear it click. Also check that you're not mixing incompatible CU/PM generations.

**Can I use Startdrive without TIA Portal?**  
No — Startdrive is a TIA Portal add-in and requires TIA Portal V14 or later to run. Siemens offers a trial version of TIA Portal for commissioning use. Alternatively, the STARTER tool (older, standalone) supports G120 commissioning but is no longer the recommended path for new installations.

**How do I clone parameters from one G120 to another in the field?**  
The fastest field method is using the BOP-2 memory card upload/download (P0802/P0803 procedure described above — available on CU240E-2 and CU250S-2 with a memory card installed). For large fleets, use Startdrive's project export/import workflow and download the same parameter set to multiple drives. Verify motor-specific parameters (nameplate data) are correct for each individual motor after cloning.

**What causes F0002 overvoltage on a G120 with a pump application?**  
Pumps with significant static head can act as generators when decelerating — the motor receives energy from the fluid column rather than absorbing drive energy. The DC bus charges up faster than the drive's internal snubber can handle. The fix is usually extending the deceleration ramp (P1121) to allow the motor to decelerate slowly enough that regenerated energy stays within the DC bus absorption capacity. If the process requires faster stopping, a braking chopper and braking resistor are required.
