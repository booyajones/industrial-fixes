---
title: "True Refrigeration E1 Error Code — Causes & Fix"
description: "What True Refrigeration E1 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - refrigeration
  - true-refrigeration
---

## True Refrigeration E1 Error Code — What It Means

True Refrigeration error code E1 indicates a temperature sensor fault. On True reach-in coolers and freezers using Dixell, LAE, or True-branded electronic controls, E1 usually points to the cabinet temperature probe reading open, shorted, or outside the controller's valid range. Once the controller loses that probe input, it cannot regulate box temperature correctly, so it falls back to a timed safety strategy or shuts the compressor circuit down depending on controller family. In the field, E1 is usually a failed NTC probe or damaged probe wiring in the evaporator compartment.

[Jump to Fix](#fix)

## Common Causes

- **Failed cabinet temperature probe** — The NTC sensor drifts out of range or fails open. Controllers read that as an E1 almost immediately at startup.
- **Probe wire damage** — Probe leads routed near fan guards, evaporator covers, or hinge channels can rub through and short or open.
- **Moisture at probe connector** — Condensation or washdown moisture wicks into the probe connector and creates unstable resistance readings.
- **Controller input fault** — If a known-good probe still reads wrong, the control board's probe input circuit may have failed.

## Step-by-Step Fix {#fix}

1. **Identify which probe the controller labels as E1** — Check the controller documentation on the unit. On many True cabinets, E1 is the cabinet probe, while evaporator probes use a different code.
2. **Measure probe resistance** — Disconnect the probe from the controller and measure resistance with a multimeter. A common 10 kΩ NTC probe should read about 10 kΩ at 77°F. Open or near-zero readings mean replace it.
3. **Inspect the full probe lead** — Follow the probe wire from the sensor bulb to the controller. Look for crushed insulation, broken splices, or rubbed sections near sheet metal edges.
4. **Substitute a known-good probe** — Plug in a matching sensor at the controller. If the display returns to normal, install the replacement probe permanently.
5. **Reset the system** — Cycle power to the controller, confirm the E1 code clears, and verify the cabinet pulls down to setpoint normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Cabinet temperature probe (NTC) | [Amazon](https://www.amazon.com/s?k=Cabinet+temperature+probe+%28NTC%29&tag=errorcodefixes-20) \| Match controller type and resistance curve before ordering |
| Probe extension harness | [Amazon](https://www.amazon.com/s?k=Probe+extension+harness&tag=errorcodefixes-20) \| Replace if the wire run is damaged inside the cabinet chase |
| Electronic temperature controller | [Amazon](https://www.amazon.com/s?k=Electronic+temperature+controller&tag=errorcodefixes-20) \| Replace only after testing with a known-good probe |
## When to Call a Pro

If the probe checks good and the controller still posts E1, you may have a board-level input fault or moisture damage inside the control housing. A commercial refrigeration tech can confirm the controller and reprogram the replacement if needed.

## Related Articles

- [True Refrigeration E2 Error Code — Causes & Fix](/posts/true-refrigeration-e2-error-code/)
- [True Refrigeration E3 Error Code — Causes & Fix](/posts/true-refrigeration-e3-error-code/)
- [True Refrigeration E4 Error Code — Causes & Fix](/posts/true-refrigeration-e4-error-code/)
- [True Refrigeration E5 Error Code — Defrost Sensor Causes & Fix](/posts/true-refrigeration-e5-error-code/)
- [True Refrigeration E6 Error Code — High Temperature Alarm Causes & Fix](/posts/true-refrigeration-e6-error-code/)
