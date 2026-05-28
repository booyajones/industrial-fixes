---
title: "Mitsubishi Mr. Slim Error Code P6 - What It Means and How to Fix It"
description: "Mitsubishi Mr. Slim error code P6 indicates an outdoor unit inverter or compressor protection fault. This guide covers the P6 diagnosis process, reset procedure, inverter board testing, and when compressor replacement is required."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

Mitsubishi Mr. Slim mini-split systems are known for their reliability, but when error code **P6** appears on the indoor unit display, it's one of the more serious codes in the Mr. Slim fault library. P6 indicates a problem with the outdoor unit's inverter circuit or compressor — and because the inverter controls the variable-speed compressor that makes Mr. Slim systems so efficient, this fault shuts the system down completely.

This guide covers what P6 means, the difference between a fixable inverter fault and a failed compressor, how to reset the system, and what a technician will do to diagnose the root cause.

## What Does P6 Mean on a Mitsubishi Mr. Slim?

**P6 = Inverter Fault / Outdoor Unit Compressor Protection**

On Mitsubishi Mr. Slim systems, P6 indicates the outdoor unit's inverter (the variable-speed drive circuit that controls the compressor) has detected an abnormal condition. The inverter monitors several parameters and triggers P6 when any of them go out of range:

- **Overcurrent protection** — the compressor is drawing more current than the inverter can safely supply
- **Inverter module overheating** — the IPM (Intelligent Power Module) or heat sink has exceeded its thermal limits
- **DC bus voltage fault** — the inverter's internal DC voltage is abnormal (too high or too low from the rectifier)
- **Compressor lock-up** — the compressor is mechanically seized or stuck at startup, causing the inverter to see a locked-rotor overcurrent condition

### P6 vs Other Compressor Codes

It's useful to know how P6 differs from related Mr. Slim fault codes:

| Code | Meaning |
|------|---------|
| P6 | Inverter/compressor protection trip (primary compressor-side fault) |
| E6 | Communication error between indoor and outdoor unit |
| P8 | Outdoor unit DC fan motor fault |
| U8 | Transmission error (master/slave configuration) |
| E8 | Outdoor unit protection circuit fault |

If you're seeing P6, the problem is in the outdoor unit's inverter or compressor — not a communication or wiring issue.

---

## What Causes P6?

### 1. Inverter Board (IPM) Failure

The Intelligent Power Module inside the inverter board is a high-power semiconductor device. It can fail from:
- Age and thermal cycling
- Voltage spikes from the power supply
- Inadequate heat sink contact or failed thermal paste
- Operating in high ambient temperatures for extended periods

### 2. Compressor Winding Short or Ground Fault

If the compressor's motor windings have developed a short (winding-to-winding or winding-to-ground), the inverter sees an immediate overcurrent and trips P6. A compressor with shorted windings draws excessive current that the IPM interprets as a load fault.

### 3. Mechanical Compressor Seizure

A compressor that's mechanically seized (bearing failure, refrigerant flood-back causing hydraulic lock) prevents the inverter from spinning up the motor. The inverter trips P6 rather than burning itself out trying to force a locked rotor.

### 4. Low Refrigerant Charge

Severely low refrigerant can cause the compressor to overheat (loss of refrigerant = loss of compressor cooling). The thermal protection in the inverter or compressor triggers P6.

### 5. Power Supply Issues

Low line voltage, voltage imbalance on 3-phase systems (commercial units), or poor power quality can trigger DC bus faults that the inverter reports as P6.

---

## How to Fix It

### Step 1 — Reset the System

Before assuming a component has failed, attempt a full system reset:

1. Turn the unit off at the thermostat or remote control.
2. Turn off the circuit breaker for the outdoor unit. Wait 10 minutes — this allows the inverter's DC bus capacitors to discharge and the thermal protection to reset.
3. Restore power at the breaker.
4. Turn the unit on. If P6 clears and the system runs normally, the fault may have been a transient condition (voltage spike, brief overload).

**If P6 returns within a few minutes of startup:** The fault condition is persistent and a cause must be identified.

### Step 2 — Check Refrigerant Charge

Low refrigerant is a treatable cause. If the system has been running poorly (insufficient cooling/heating before the P6 appeared), or if it's been years since the last service:

- Have a technician check refrigerant pressure with manifold gauges
- Low suction pressure on R-410A (below 70 PSI) indicates undercharge
- Fix any leak and recharge before replacing any electronic components

### Step 3 — Check Power Supply Voltage

At the outdoor unit's disconnect, verify line voltage with a multimeter while the unit is attempting to start. It should be within 10% of rated voltage (typically 208–253V on a 240V system, or within spec for 230V systems). Low voltage under load is a common inverter stressor.

### Step 4 — Inspect the Inverter Board

This step requires powering down and accessing the outdoor unit's electrical compartment:

1. **Check the heat sink.** The inverter's IPM module should be firmly mounted to an aluminum heat sink with thermal paste between them. If the mounting screws are loose or thermal paste has dried out and cracked, the module overheats and trips P6.

2. **Inspect for burnt components.** Look for darkened areas, cracked components, or obvious damage on the inverter PCB.

3. **Check capacitors.** Bulging or leaking capacitors on the inverter board indicate the board is aging and should be replaced.

### Step 5 — Test the Compressor Windings

With power off and the compressor wiring disconnected from the inverter:

1. Use a multimeter set to resistance (ohms) on the compressor motor terminals (typically labeled U, V, W for 3-phase inverter compressors).
2. Test U-to-V, V-to-W, and U-to-W. Readings should be equal and low — typically 0.5–3 ohms depending on the model.
3. Test each terminal to the compressor ground (chassis). You should read infinite resistance (open circuit). Any measurable resistance indicates a ground fault.
4. On a megohm meter (megger), test winding-to-ground at 500V. Healthy compressor windings read 1 megohm or higher. Below 1 megohm is a failed winding.

**Result interpretation:**
- Unequal winding-to-winding readings: open or partially shorted winding — compressor failed
- Any continuity to ground: winding ground fault — compressor failed
- Good winding readings: compressor may be mechanical failure or refrigerant-related; inverter board is suspect

---

## Parts You May Need

| Part | What It Fixes | Amazon Link |
|------|--------------|-------------|
| Mitsubishi Mr. Slim Inverter PCB Board | Inverter board failure causing P6 | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mr-slim-error-code-p6&k=mitsubishi+mr+slim+inverter+board+outdoor+unit&tag=errorcodefixes-20) |
| IPM Intelligent Power Module (IGBT module) | IPM failure within inverter board | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mr-slim-error-code-p6&k=ipm+intelligent+power+module+mini+split+inverter&tag=errorcodefixes-20) |
| Thermal Paste for Inverter Heatsink | Overheating IPM due to dried thermal compound | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mr-slim-error-code-p6&k=thermal+paste+heatsink+compound+electronics&tag=errorcodefixes-20) |
| Mitsubishi Mini Split Capacitor Kit | Aging capacitors on inverter board | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mr-slim-error-code-p6&k=mitsubishi+mini+split+capacitor+replacement&tag=errorcodefixes-20) |
| Megohm Meter (Megger) | Testing compressor winding insulation | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mr-slim-error-code-p6&k=megohm+meter+megger+500v+compressor+test&tag=errorcodefixes-20) |
| Refrigerant Leak Detector (R-410A) | Diagnosing low refrigerant as P6 cause | [View on Amazon](https://www.amazon.com/s?ascsubtag=ecf-mitsubishi-mr-slim-error-code-p6&k=r410a+refrigerant+leak+detector&tag=errorcodefixes-20) |

---

## Inverter Board Replacement — What's Involved

Replacing the outdoor unit inverter board is an intermediate-level repair. The inverter board is the large PCB mounted inside the outdoor unit's electrical compartment. The process:

1. Power off and wait for capacitors to discharge (10 minutes minimum after power off).
2. Photograph all wiring connections on the existing board.
3. Disconnect the DC bus wiring, the AC input wiring, the compressor output wiring (U/V/W), and the signal connector harnesses.
4. Unmount the old board.
5. Transfer thermal paste (or apply fresh) to the IPM mounting surface on the heat sink.
6. Mount and wire the new board in reverse order.
7. Restore power and test.

**Order an OEM-equivalent board** with the matching model number. Aftermarket inverter boards are available at significant cost savings but quality varies. For premium Mr. Slim units, an OEM board is the lower-risk choice.

---

## When to Call a Pro

P6 is one of the Mr. Slim codes where professional diagnosis is strongly recommended before spending money on parts:

- **Inverter board replacement ($300–$800 for the part)** is wasted if the compressor has failed — a new board connected to a seized or shorted compressor will trip P6 immediately and may damage the new board.
- **Compressor replacement** on a mini-split requires refrigerant recovery, brazing, system evacuation, and recharge — requiring EPA 608 certification and proper tools.
- **A technician can use the unit's service mode diagnostic functions** — Mr. Slim systems have detailed diagnostic menus accessible via the remote control that record fault history and can identify the specific overcurrent or voltage fault that triggered P6.

Call a pro if:
- P6 returns within 30 minutes of reset
- You find abnormal compressor winding readings
- The system is under warranty (DIY repairs void Mitsubishi's limited warranty)
- The system is less than 5 years old (P6 on a new system almost always has a correctable root cause)

---

## FAQ

**Q: How do I access Mr. Slim diagnostic mode to see more details about P6?**
A: On most Mr. Slim units, you can access the self-diagnostic code history by pressing the CHECK button (or using a paperclip in the CHECK port) on the indoor unit while it's in standby. The LED or display will flash a code sequence. The service manual for your specific model decodes the flash pattern.

**Q: My P6 came on right after a power outage. Is the unit damaged?**
A: Possibly not — power restoration surges can trip the inverter's protection circuit without causing component damage. Try the full 10-minute reset procedure. If P6 clears and the system runs normally for several days, the power event was likely the cause.

**Q: Can a dirty outdoor unit cause P6?**
A: Yes, indirectly. A heavily fouled outdoor coil (clogged with debris, grass clippings, or cottonwood fluff) forces the compressor to work harder, which increases current draw and can trigger inverter overcurrent protection. Clean the outdoor coil with a garden hose (rinsing outward from inside the coil) before diagnosing further.

**Q: The unit shows P6 but the outdoor unit is completely silent. Is the compressor seized?**
A: Not necessarily — a completely silent outdoor unit after a P6 trip just means the inverter shut everything down. Reset and listen carefully on startup. If the fan runs but the compressor makes a clunk and stalls, that's a possible seizure. If nothing at all happens even after reset, check power supply and the contactor.

**Q: How long do Mitsubishi Mr. Slim inverter boards typically last?**
A: 10–15 years under normal operating conditions. Units in extreme climates (very high ambient temperatures in attic-mounted outdoor units, or heavy industrial environments) may see board failures earlier.

## See Also

- [Mitsubishi E5 Error Code — Causes & Fix](/posts/mitsubishi-e5-error-code/)
- [Mitsubishi City Multi P8 / E6 Error Codes — Causes & Fix](/posts/mitsubishi-city-multi-error-codes/)
- [Mitsubishi Mini Split E9 Error Code — Outdoor Thermistor 2 Fault Fix](/posts/mitsubishi-mini-split-e9-error/)
- [Mitsubishi U3 Error Code — Causes & Fix](/posts/mitsubishi-u3-error-code/)
