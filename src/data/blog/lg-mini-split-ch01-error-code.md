---
title: "LG Mini Split CH01 Error Code — Causes & Fix"
description: "What LG CH01 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - mini-split
  - lg
---

## LG Mini Split CH01 Error Code — What It Means

LG error code CH01 (also displayed as "C1" or "CH 01") means the indoor unit room temperature sensor has failed or is reading an out-of-range value. The indoor PCB reads the thermistor resistance at startup and continuously during operation. When the resistance falls outside the expected range — either open circuit, short circuit, or a value that corresponds to an implausible temperature — the board shuts down and displays CH01. This protects the system from running in a mode where it can't properly regulate temperature. The fix is almost always a simple sensor replacement.

[Jump to Fix](#fix)

## Common Causes

- **Failed indoor room temperature thermistor** — The thermistor is a small NTC (negative temperature coefficient) bead on a wire harness, located behind the front panel near the return air intake. These sensors fail open or short with age and exposure to condensation.
- **Loose or corroded thermistor connector** — The thermistor plugs into the indoor PCB with a small 2-pin connector. Corrosion or a partially seated connector produces an out-of-range reading that triggers CH01.
- **Short to ground or damaged wire** — The thermistor lead wire (typically 3–5 inches long) can chafe against a sharp edge inside the unit casing and short to the chassis.
- **Failed indoor PCB** — Rare, but if the thermistor tests in-spec but CH01 persists, the PCB input circuit for the sensor may have failed.

## Step-by-Step Fix {#fix}

1. **Power off and access the sensor** — Shut off the unit and remove the front panel and filter. The room temperature sensor is typically a small bead on a wire, clipped to the evaporator coil frame or mounted in an air intake slot.
2. **Test the thermistor** — Disconnect the sensor from the PCB. Using a multimeter set to resistance (ohms), measure across the two sensor leads. At room temperature (70°F/21°C), a typical LG thermistor reads approximately 10–15 kΩ. An open (infinite resistance) or shorted (near 0) reading means replace it.
3. **Check the connector** — Even if the sensor reads in-spec, clean the 2-pin connector contacts with electrical contact cleaner. Re-seat firmly and test.
4. **Inspect the lead wire** — Follow the wire from the sensor to the PCB connector. Look for any point where it contacts sharp metal or could be pinched.
5. **Reset the system** — Restore power after installing a new sensor or reseating the connector. CH01 should clear immediately if the sensor now reads in-range.

## Parts Often Needed

| Part | Notes |
|------|-------|
| LG indoor thermistor (room temp) | [Amazon](https://www.amazon.com/s?k=LG+indoor+thermistor+%28room+temp%29&tag=errorcodefixes-20) \| LG part 6615A20042A or equivalent; confirm for your model series |
| Contact cleaner | [Amazon](https://www.amazon.com/s?k=Contact+cleaner&tag=errorcodefixes-20) \| For connector maintenance |
| Indoor PCB | [Amazon](https://www.amazon.com/s?k=Indoor+PCB&tag=errorcodefixes-20) \| If sensor tests good and fault persists |
## When to Call a Pro

If you've replaced the sensor and the fault persists, the PCB input circuit is suspect. LG service tools can read live thermistor values directly; an authorized LG tech can confirm board vs. sensor without guesswork.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
