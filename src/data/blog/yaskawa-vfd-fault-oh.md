---
title: "Yaskawa VFD Fault OH — Causes & Fix"
description: "What Yaskawa VFD fault OH means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T09:00:00Z
modDatetime: 2026-04-22T09:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
money_part: "Drive cooling fan"
---

## Yaskawa VFD Fault OH — What It Means

Yaskawa VFD fault OH (Drive Overheat) indicates that the drive's internal heatsink temperature sensor exceeded the maximum allowable temperature, typically 90–95°C depending on the model. The drive measures heatsink temperature with a thermistor mounted on the output IGBT heatsink and shuts down when the temperature limit is reached to prevent permanent IGBT damage. OH is one of the most common Yaskawa faults in the field and is almost always caused by inadequate cooling — either the drive's cooling fan has failed, the ambient temperature is too high, or the drive is operating above its rated current for extended periods.

[Jump to Fix](#fix)

## Common Causes

- **Failed drive cooling fan** — The internal cooling fan in the drive's ventilation path fails to run or runs at reduced speed. Without active cooling, heatsink temperature rises rapidly under load.
- **High ambient temperature** — The drive's enclosure or installation environment is above the rated ambient (typically 104°F / 40°C for most Yaskawa drives). Equipment rooms without adequate air conditioning are a common cause in summer.
- **Blocked ventilation** — The drive's air inlet and outlet slots are blocked by dust accumulation, incorrect mounting (too close to the cabinet wall), or cables routed across the vents.
- **Sustained overload operation** — The drive is operating at or above 100% continuous current rating for extended periods, generating more internal heat than the cooling system can dissipate.

## Step-by-Step Fix {#fix}

1. **Check the cooling fan** — With the drive powered on, listen for the cooling fan. Yaskawa fans typically run during operation or kick in when the heatsink reaches a threshold temperature. A fan that's silent, rattling, or intermittent needs replacement.
2. **Measure ambient temperature at the drive** — Use a thermometer at the drive's air inlet. Ambient should be below 40°C (104°F) for standard drives, or below the model-specific limit. If the enclosure is hot, add enclosure cooling or ventilation.
3. **Clear ventilation paths** — Vacuum and blow out dust from the drive's top and bottom ventilation slots. Confirm the drive has the minimum clearance above and below as specified in the installation manual (typically 50–100mm minimum).
4. **Review drive output current** — Pull the drive's output current from the monitoring parameters. Compare to the drive's rated continuous current. If the drive is consistently running above 90% of rating, check whether the correct drive size was selected.
5. **Replace cooling fan** — Yaskawa cooling fans have a rated lifespan (typically 10 years or 30,000–50,000 hours at rated temperature). A fan that's over 5 years old in a warm environment is a strong replacement candidate.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Drive cooling fan | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-vfd-fault-oh&k=Drive+cooling+fan&tag=errorcodefixes-20) \| Match voltage (24VDC common), CFM rating, and connector; order by drive model |
| Enclosure fan/filter | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-vfd-fault-oh&k=Enclosure+fan%2Ffilter&tag=errorcodefixes-20) \| Add to panel or enclosure if ambient is too high |
| Drive (upsized) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-yaskawa-vfd-fault-oh&k=Drive+%28upsized%29&tag=errorcodefixes-20) \| If drive is running consistently near full current on an undersized application |
## When to Call a Pro

If the drive trips OH at normal loads with confirmed good fan operation and acceptable ambient, the IGBT heatsink thermal paste may be degraded, or the thermistor reading may be inaccurate. These repairs require full drive disassembly and are best handled by a certified repair center.

## Related Articles

- [Yaskawa A1000 OC Fault — Overcurrent](/posts/yaskawa-a1000-fault-oc/)
- [Yaskawa A1000 Fault UV1, DC Bus Undervoltage Causes & Fix](/posts/yaskawa-a1000-fault-uv1/)
- [Yaskawa A1000 Fault Code OC — Overcurrent Diagnosis & Fix](/posts/yaskawa-a1000-oc-fault-code/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa GA700 Fault UV1 — Main Circuit Undervoltage Causes & Fix](/posts/yaskawa-ga700-fault-uv1/)

## See Also

- [Yaskawa VFD Fault Codes — Complete Reference (V1000, A1000, GA700)](/posts/yaskawa-vfd-fault-codes/)
- [Yaskawa GA700 OC Fault — Overcurrent Fix](/posts/yaskawa-ga700-fault-oc/)
- [Yaskawa VFD Fault SC — Causes & Fix](/posts/yaskawa-vfd-fault-sc/)
- [Yaskawa A1000 Complete Guide - Fault Codes, Parameters, and Commissioning](/posts/yaskawa-a1000-complete-guide/)
