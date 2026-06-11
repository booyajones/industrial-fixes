---
title: "Carrier 30XA Commercial Chiller Fault Codes — Common Faults and Fixes"
description: "Guide to Carrier 30XA air-cooled chiller fault codes, what each fault means, and how to diagnose and fix the most common problems."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - hvac
  - carrier
money_part: "Condenser fan motor"
---

## Carrier 30XA Commercial Chiller Fault Codes — What They Mean

The Carrier 30XA is a scroll-compressor air-cooled chiller used in commercial buildings, industrial processes, and district cooling applications. It uses the Pro-Dialog Plus or Pro-Dialog+ control system, which displays fault codes on the front panel display. Faults are categorized as alarms (auto-reset) or lockouts (require manual reset). The display shows a plain-English fault message alongside a fault number. The most critical faults trip a circuit or the entire chiller; understanding them is essential for minimizing downtime.

[Jump to Fix](#fix)

## Most Common 30XA Fault Codes

| Fault | Meaning |
|-------|---------|
| Cir. HP Trip | High pressure trip — discharge pressure exceeded limit |
| Cir. LP Trip | Low pressure trip — suction pressure below limit |
| Cir. Mtr OL | Compressor motor overload |
| EWT High | Entering water temperature too high |
| LWT Low | Leaving water temperature too low — freeze protection |
| Fan Fault | Condenser fan motor failure |
| Cir. Disch Tmp | High discharge temperature |
| Control Pwr Fail | Loss of control power (24VAC) |

## Common Causes

- **HP Trip (High Pressure)** — Dirty condenser coils are the most common cause. Restricted airflow through the coil causes refrigerant to condense at higher pressure. Also caused by refrigerant overcharge, non-condensable gases, failed condenser fan, or condenser air recirculation.
- **LP Trip (Low Pressure)** — Low refrigerant charge (leak), evaporator fouling reducing heat transfer, low chilled water flow, or evaporator entering water temperature below design conditions (cold winter startup).
- **Motor Overload** — Low supply voltage causes compressors to draw excess current. Also caused by a failing compressor, high pressure differential, or a tripped thermal overload that needs manual reset.
- **LWT Low (Freeze)** — Chilled water flow failure (pump not running, valve closed, strainer blocked) allows the water in the evaporator to approach freezing. This is a serious fault — prolonged exposure freezes and bursts the evaporator.
- **Fan Fault** — A condenser fan motor has failed, tripped its motor protector, or the associated capacitor has failed. On multi-fan chillers, a single fan fault may not trip the circuit but should be addressed promptly.

## Step-by-Step Fix {#fix}

1. **Record all active faults from the Pro-Dialog display** — The display shows current faults and a fault history log. Note the fault code, circuit number (A or B on dual-circuit units), and timestamp. Multiple simultaneous faults tell a more complete story than a single fault in isolation.
2. **For HP Trip** — Inspect condenser coils for fouling. Wash coils from the inside out with a low-pressure hose (or coil cleaner). Confirm all condenser fans are running. Check refrigerant charge via gauges if coils are clean. Verify the chiller is not in an air recirculation environment (inadequate clearance or wind walls needed).
3. **For LP Trip** — Check chilled water flow rate and pump operation. Connect refrigerant gauges to assess circuit charge. Inspect the evaporator barrel for fouling (reduced delta-T across evaporator indicates fouling). Charge should only be added after confirming a leak is repaired.
4. **For Motor Overload** — Measure supply voltage at the compressor terminal block under load (all compressors running). Should be within ±10% of nameplate. If voltage is correct, measure compressor amp draw and compare to nameplate RLA.
5. **For LWT Low / Freeze** — Confirm chilled water pump is running and delivering design flow. Check the chilled water strainer for blockage. If flow is confirmed, check the entering water temperature and ensure the chiller is not operating outside its minimum EWT specification.
6. **For Fan Fault** — Identify which fan motor tripped. Check the fan motor overload protector (reset if tripped). Test the fan capacitor (if single-phase motor). Megger the motor windings if the capacitor is good and the motor won't start.
7. **Reset and test** — After repairs, reset faults from the Pro-Dialog panel (Menu > Service > Reset Faults). Run the chiller through a full load cycle and monitor fault log for recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Condenser fan motor | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?ascsubtag=ecf-carrier-commercial-chiller-fault&tag=errorcodefixes-20) \| Match voltage, HP, and frame size from motor nameplate |
| Condenser fan capacitor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-commercial-chiller-fault&k=Condenser+fan+capacitor&tag=errorcodefixes-20) \| Test before replacing motor — capacitor is the more common failure |
| Refrigerant charge | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-commercial-chiller-fault&k=Refrigerant+charge&tag=errorcodefixes-20) \| R-410A on most 30XA models; confirm on data plate |
| High/low pressure switches | [Amazon](https://www.amazon.com/dp/B013J2J97A?ascsubtag=ecf-carrier-commercial-chiller-fault&tag=errorcodefixes-20) \| Replace if trips occur at incorrect pressures with confirmed refrigerant charge |
| Compressor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-carrier-commercial-chiller-fault&k=Compressor&tag=errorcodefixes-20) \| Last resort — confirm all other causes before replacing a scroll compressor |
## When to Call a Pro

The Carrier 30XA operates with refrigerant circuits at high pressure and involves 460V three-phase electrical systems. Refrigerant work requires EPA 608 certification. Compressor replacements require recovery of the refrigerant charge, oil analysis, and system flush — all requiring specialized equipment and certification. Contact Carrier's commercial service network for warranty and major component work.

## Related Articles

- [Carrier 11 Error Code — Causes & Fix](/posts/carrier-11-error-code/)
- [Carrier 12 Error Code — Causes & Fix](/posts/carrier-12-error-code/)
- [Carrier 13 Error Code — Limit Switch Lockout Fix](/posts/carrier-13-error-code/)
- [Carrier 13 Soft Lockout — What's Different from Hard Lockout](/posts/carrier-13-soft-lockout/)
- [Carrier 14 Error Code — Causes & Fix](/posts/carrier-14-error-code/)

## See Also

- [Carrier Error Code 16 - Causes & Fix](/posts/carrier-error-code-16/)
- [Carrier Error Code 58 — Causes & Fix](/posts/carrier-58-error-code/)
- [Carrier 58UX Furnace Error Codes — Flash Code Diagnostic Guide](/posts/carrier-58ux-error-codes/)
- [Carrier Chiller Fault Codes — Complete Troubleshooting Guide](/posts/carrier-chiller-fault-codes/)
