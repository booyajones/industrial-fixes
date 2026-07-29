---
title: "Yaskawa V1000 OV Fault - What It Means and How to Fix It"
description: "Complete guide to the Yaskawa V1000 OV fault code (overvoltage). Covers all causes, parameter adjustments, braking resistor selection, and step-by-step repair for this common VFD fault."
pubDatetime: 2026-04-25T00:00:00Z
author: "Dana Kowalski"
tags:
  - hvac
  - error-codes
---

The Yaskawa V1000 is a compact, high-performance variable frequency drive used in pumps, fans, conveyors, and machinery across industrial and commercial applications. The **OV fault** stands for **Overvoltage** — the DC bus voltage inside the drive has exceeded its safe limit. This guide explains exactly why it happens, how to diagnose it, and how to fix it permanently — including when a braking resistor is the right answer.

## What Does Yaskawa V1000 OV Fault Mean?

The V1000 maintains a DC bus voltage by rectifying the AC input power. Nominal DC bus voltage for a 480V drive is approximately 660–680V DC. The OV fault trips when DC bus voltage exceeds **820V DC** (on 480V drives) or **410V DC** (on 240V drives).

Overvoltage doesn't mean the incoming AC power is too high (though it can contribute). It most often means the motor is **generating power back into the drive** — a condition called regeneration.

### Why Does Regeneration Cause OV?

When you decelerate a spinning load — especially a high-inertia load like a fan, flywheel, or conveyor — the motor acts as a generator. That generated power flows back into the drive's DC bus. With no way to dissipate it, the bus voltage climbs until it reaches the OV trip threshold.

The V1000 has a standard braking transistor built in, but it needs a **braking resistor** (sometimes called a dynamic braking resistor or DB resistor) connected to the B1/B2 terminals to actually dissipate the energy. Without a resistor, the transistor has nowhere to send the excess energy.

### Other Causes of OV

1. **Deceleration ramp too fast** — The load can't slow down fast enough, regenerating energy into the drive.
2. **No braking resistor installed** — The built-in transistor can't dissipate energy without an external resistor.
3. **Incorrect deceleration time parameters** — C1-02 (Decel Time 1) is set too short for the load inertia.
4. **Input voltage too high** — AC line voltage above rated (e.g., running a 460V drive on a 480V+5% line can push the bus close to the trip threshold).
5. **Power factor correction capacitors switching** — Large PF correction capacitor banks nearby can cause voltage transients.
6. **Load overhauling the motor** — In applications like a loaded conveyor going downhill, the load drives the motor rather than the other way around — constant regeneration.

## How to Fix It

**Step 1: Check when OV occurs.** Is it tripping during deceleration, during constant speed, or at startup?

- **Deceleration:** Classic case — the decel ramp is too fast or a braking resistor is needed.
- **Constant speed:** Input voltage transient or overhauling load.
- **Startup:** Less common — check input voltage and verify the correct drive voltage class.

**Step 2: Increase deceleration time.** Navigate to:
- **C1-02 (Deceleration Time 1)**
- Default is often 10 seconds. Try doubling it to 20 seconds.
- If the application allows slower stops, this is the simplest fix.

**Step 3: Enable Stall Prevention during deceleration.** If you can't slow the decel time (the application requires fast stops):
- Navigate to **L3-04 (Stall Prevention Selection during Decel)**
- Set to **1 (Enable)**. The drive will automatically extend the decel ramp if the bus voltage rises too high.

**Step 4: Check DC Bus voltage.** The V1000 can display real-time DC bus voltage through the monitor parameters:
- Navigate to **U1-07 (DC Bus Voltage)**. Watch this during deceleration. If it spikes above 750V on a 480V drive, regeneration is confirmed.

**Step 5: Install a braking resistor.** For applications with high inertia loads or frequent stops, a braking resistor is the permanent solution.

**Selecting the right braking resistor for the Yaskawa V1000:**

| Drive Rating | Minimum Resistance | Recommended Resistor |
|-------------|-------------------|---------------------|
| 1 HP / 240V | 40 Ω | 40 Ω, 100W–200W |
| 2 HP / 240V | 30 Ω | 30 Ω, 150W–300W |
| 1 HP / 480V | 150 Ω | 150 Ω, 100W–200W |
| 2 HP / 480V | 100 Ω | 100 Ω, 150W–300W |
| 5 HP / 480V | 50 Ω | 50 Ω, 300W–600W |
| 10 HP / 480V | 30 Ω | 30 Ω, 500W–1000W |

Connect the resistor between terminals **B1 and B2** on the V1000. Do not connect it to the ground terminal. Do not use resistance lower than the minimum — this can damage the braking transistor.

**Step 6: Enable the braking transistor.** After installing the resistor, enable the DB function:
- Navigate to **L3-04** and set appropriately.
- Also check **L8-55 (Internal DB Transistor Protection)** — ensure it's enabled to protect the transistor from thermal overload.

**Step 7: Verify input voltage.** Check the incoming voltage at the drive's L1/L2/L3 input terminals under load with a true RMS meter. If consistently above 500V on a nominal 480V system, the input voltage is too high — consult your utility.

## Parts You May Need

| Part | Why You Need It | Approx. Cost |
|------|----------------|-------------|
| Braking resistor 150 Ω / 200W (480V 1HP) | Dissipates regenerative energy on small V1000 | $30–$70 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-v1000-fault-ov&k=braking+resistor+150+ohm+200W+VFD&tag=errorcodefixes-20) |
| Braking resistor 50 Ω / 500W (480V 5HP) | DB resistor for mid-size V1000 | $50–$120 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-v1000-fault-ov&k=dynamic+braking+resistor+50+ohm+500W&tag=errorcodefixes-20) |
| Yaskawa V1000 replacement drive | If braking transistor is damaged | $300–$900 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-v1000-fault-ov&k=Yaskawa+V1000+VFD+replacement&tag=errorcodefixes-20) |
| Line reactor (3%, 480V) | Reduces voltage transients from utility | $80–$250 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-v1000-fault-ov&k=3%25+line+reactor+480V+VFD+input&tag=errorcodefixes-20) |
| True RMS multimeter | Accurate voltage measurement | $40–$150 — [View on Amazon](https://www.amazon.com/dp/B08ZJSN5X3?ascsubtag=ecf-yaskawa-v1000-fault-ov&tag=errorcodefixes-20) |
| DIN rail resistor mounting bracket | Mount DB resistor safely in panel | $10–$25 — [Search on Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-v1000-fault-ov&k=DIN+rail+resistor+mounting+bracket&tag=errorcodefixes-20) |

## When to Call a Pro

- The OV fault persists even after increasing decel time and installing a correctly sized braking resistor — the braking transistor may have failed internally.
- The drive shows OV during constant speed operation with no obvious load changes — internal capacitor degradation or an external voltage transient source requires more advanced diagnosis.
- The application involves explosive or fire-risk environments — braking resistor selection and installation must follow NEC/NFPA guidelines.
- You're unsure how to size a braking resistor for a high-inertia load — undersizing can cause resistor fires.
- The braking resistor is getting extremely hot (too hot to touch) after a few stop cycles — it's undersized for the duty cycle. Recalculate.

**Safety note:** Braking resistors get hot — some reach 300°F+ under load. Mount them outside the electrical enclosure or in a ventilated resistor box. Never mount directly adjacent to wiring, cable trays, or flammable materials.

## Frequently Asked Questions

**Q: The Yaskawa V1000 shows OV but only in winter. Fine in summer. Why would temperature matter?**

A: In cold weather, incoming utility voltage tends to be slightly higher (lighter summer AC loads mean less voltage drop on the distribution system). If your drive is already close to the OV trip threshold, a seasonal 5–10V increase in line voltage can push it over. Check your input voltage in winter vs. summer. A line reactor at the drive input reduces voltage spikes and can solve this without any other changes.

**Q: I installed a braking resistor but still get OV on fast stops. What's wrong?**

A: Check resistance value — if the resistor is too high in resistance, it can't dissipate energy fast enough. Also verify the wire gauge from the drive B1/B2 terminals to the resistor is adequate (undersized wire adds resistance). Finally, confirm the internal braking transistor is actually switching by monitoring DC bus voltage — if it's not dropping during deceleration, the transistor may have already failed.

**Q: Can I use a braking resistor from a different VFD brand on my Yaskawa V1000?**

A: Yes, as long as the resistance value meets or exceeds the Yaskawa minimum resistance specification and the wattage rating is adequate for your duty cycle. The resistor doesn't need to be Yaskawa-branded. Confirm the maximum voltage rating of the resistor is appropriate for your drive voltage class (600V or higher rating is standard for 480V drives).

**Q: My V1000 drives a fan. Should I expect OV faults on it?**

A: Fan applications have high rotational inertia. When you command a fast stop, the fan continues spinning and drives the motor as a generator. This is a classic OV scenario. Solution: extend the decel time to allow the fan to coast to a stop naturally (sometimes 60–120 seconds for large fans), or install a braking resistor if fast stops are genuinely required. Most fan HVAC applications do not require fast stops — a long decel time is the right answer.

**Q: What's the difference between OV and ov on the Yaskawa V1000 display?**

A: Uppercase **OV** is a hard fault — the drive has tripped and stopped output. Lowercase **ov** (if your HIM shows it) is typically a minor alarm or warning before the trip occurs. The V1000 doesn't always distinguish these on the basic display, but if you're seeing a warning indication before the trip, you have a brief window to identify the deceleration event that's causing it before it becomes a full lockout.
