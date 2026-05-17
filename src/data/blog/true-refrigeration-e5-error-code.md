---
title: "True Refrigeration E5 Error Code — Defrost Sensor Causes & Fix"
description: "What True Refrigeration E5 means, why the defrost sensor faults, and how to fix it step by step."
pubDatetime: 2026-04-24T23:50:00Z
modDatetime: 2026-04-24T23:50:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - refrigeration
  - true-refrigeration
---

## True Refrigeration E5 Error Code — What It Means

True Refrigeration error code E5 usually points to a defrost probe or evaporator sensor fault. On reach-in coolers and freezers that use Dixell, LAE, or True-branded electronic controls, the board expects a stable temperature signal from the evaporator area during defrost and recovery. When that signal goes open, shorted, or outside the controller's allowed range, the cabinet posts E5 and may extend defrost time, lock the compressor out, or run into a fail-safe cycle that protects the evaporator from icing up.

[Jump to Fix](#fix)

## Common Causes

- **Failed defrost sensor** — The probe itself drifts out of range or fails open after years of heat and moisture exposure.
- **Sensor lead rubbing through** — Sheet metal edges around the evaporator cover can cut the insulation and short the probe wire.
- **Ice or water intrusion at the connector** — Moisture wicks into the plug and gives the controller unstable resistance readings.
- **Defrost heater problem creating abnormal temperatures** — A heater that never energizes can leave the evaporator buried in ice, which sometimes gets misread as a sensor fault.
- **Bad controller input** — If a known-good probe still reads incorrectly, the board input can be damaged.

## Step-by-Step Fix {#fix}

1. **Power the cabinet off and remove the evaporator cover** — You need access to the evaporator section and the probe clipped to the coil.
2. **Inspect the evaporator for heavy ice** — If the coil is packed with ice, melt it fully before testing. A frozen coil can hide a failed sensor lead.
3. **Measure the probe resistance** — Disconnect the sensor at the controller and compare resistance to the manufacturer chart. A 10 kΩ NTC probe should read close to 10 kΩ at 77°F.
4. **Trace the full wire run** — Look for pinched, cut, or wet sections near fan brackets, drain pans, and pass-through grommets.
5. **Check the defrost heater circuit** — If the sensor tests good, confirm the heater energizes and the termination path is intact. A heater failure often creates the icing that triggers repeated E5 complaints.
6. **Substitute a known-good probe** — Plug in a matching replacement sensor at the controller. If the code clears, replace the original probe permanently.
7. **Restart and monitor a full cycle** — Let the cabinet run through refrigeration and defrost. Confirm the E5 code stays gone and the coil clears normally.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Defrost / evaporator temperature probe | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-true-refrigeration-e5-error-code&k=True+refrigeration+defrost+probe&tag=errorcodefixes-20) \| Match the controller family and probe curve before ordering |
| Probe harness or extension lead | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-true-refrigeration-e5-error-code&k=refrigeration+probe+harness&tag=errorcodefixes-20) \| Useful when the original lead is cut or water-damaged |
| Defrost heater | [Amazon](https://www.amazon.com/dp/B07FVP4CY6?ascsubtag=ecf-true-refrigeration-e5-error-code&tag=errorcodefixes-20) \| Replace if the coil stays iced even with a good probe |
| Electronic temperature controller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-true-refrigeration-e5-error-code&k=true+refrigeration+temperature+controller&tag=errorcodefixes-20) \| Only after confirming the probe and heater circuit test good |

## When to Call a Pro

Call a commercial refrigeration tech if the coil keeps icing after probe replacement, or if you confirm the probe reads correctly and the board still throws E5. At that point you may have a controller fault or a defrost circuit problem that needs live electrical testing.

## See Also

- [True Refrigeration Error Codes — Complete Guide](/posts/true-refrigeration-error-codes/)
- [True Refrigeration E1 Error Code — Causes & Fix](/posts/true-refrigeration-e1-error-code/)
- [True Refrigeration E2 Error Code — Causes & Fix](/posts/true-refrigeration-e2-error-code/)
- [True Refrigeration T-Series Error Codes — Complete Guide](/posts/true-refrigeration-t-series-error-codes/)

## Related Articles

- [True Refrigeration E1 Error Code — Causes & Fix](/posts/true-refrigeration-e1-error-code/)
- [True Refrigeration E2 Error Code — Causes & Fix](/posts/true-refrigeration-e2-error-code/)
- [True Refrigeration E3 Error Code — Causes & Fix](/posts/true-refrigeration-e3-error-code/)
- [True Refrigeration E4 Error Code — Causes & Fix](/posts/true-refrigeration-e4-error-code/)
- [True Refrigeration E6 Error Code — High Temperature Alarm Causes & Fix](/posts/true-refrigeration-e6-error-code/)
