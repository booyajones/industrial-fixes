---
title: "Trane CenTraVac Chiller Fault Codes — Common Faults Guide"
description: "Guide to Trane CenTraVac centrifugal chiller fault codes, what each fault means, and how to diagnose the most common problems."
pubDatetime: 2026-04-22T14:00:00Z
modDatetime: 2026-04-22T14:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - hvac
  - trane
---

## Trane CenTraVac Chiller Fault Codes — What They Mean

The Trane CenTraVac (CVHE, CVHF, CVHG series) is a water-cooled centrifugal chiller used in large commercial and institutional buildings. It uses the Tracer AdaptiView or CH530 control system, which displays fault messages on the touchscreen panel. CenTraVac chillers operate at low pressure (below atmospheric on the suction side) using R-134a or R-1233zd refrigerant. Faults are classified as informational, warnings, or shutdowns. Shutdowns lock the chiller off and require manual reset; repeated shutdowns without clearing the root cause can damage the machine.

[Jump to Fix](#fix)

## Most Common CenTraVac Fault Codes

| [Fault](https://www.amazon.com/s?k=Fault&tag=errorcodefixe-20) | Meaning |
|-------|---------|
| [Chilled Water Flow Lost](https://www.amazon.com/s?k=Chilled%20Water%20Flow%20Lost&tag=errorcodefixe-20) | Loss of chilled water flow switch signal |
| [Condenser Water Flow Lost](https://www.amazon.com/s?k=Condenser%20Water%20Flow%20Lost&tag=errorcodefixe-20) | Loss of condenser water flow switch signal |
| [Low Refrigerant Pressure](https://www.amazon.com/s?k=Low%20Refrigerant%20Pressure&tag=errorcodefixe-20) | Suction pressure below minimum limit |
| [High Condenser Pressure](https://www.amazon.com/s?k=High%20Condenser%20Pressure&tag=errorcodefixe-20) | Condenser pressure above limit |
| [High Motor Temperature](https://www.amazon.com/s?k=High%20Motor%20Temperature&tag=errorcodefixe-20) | Motor winding overtemperature |
| [Starter Fault](https://www.amazon.com/s?k=Starter%20Fault&tag=errorcodefixe-20) | Motor starter failure |
| [Oil Pressure Low](https://www.amazon.com/s?k=Oil%20Pressure%20Low&tag=errorcodefixe-20) | Lubrication system oil pressure below limit |
| [High Discharge Temperature](https://www.amazon.com/s?k=High%20Discharge%20Temperature&tag=errorcodefixe-20) | Compressor discharge temp exceeded limit |

## Common Causes

- **Chilled / Condenser Water Flow Lost** — The flow switch (differential pressure or paddle type) is not proving flow. Causes include: pump not running, pump running backwards (phase rotation), closed isolation valve, clogged strainer, flow switch failure, or flow switch setpoint drift.
- **Low Refrigerant Pressure** — Air infiltration into the low-pressure circuit (a unique CenTraVac characteristic — leaks allow air in, not refrigerant out), refrigerant loss from a seal leak, or a non-condensable gas accumulation in the condenser. Low suction pressure on a CenTraVac means something entered the system, not that refrigerant left.
- **High Condenser Pressure** — Condenser water temperature too high (cooling tower issue), condenser tube fouling (scaling), or non-condensable gas accumulated in the condenser shell.
- **Oil Pressure Low** — Oil pump failure, oil separator fouling, or oil dilution by refrigerant. Oil dilution occurs when the chiller sits idle for extended periods and refrigerant migrates into the oil sump.
- **High Motor Temperature** — High ambient temperature in the machine room, inadequate motor cooling water flow, or a winding insulation breakdown beginning to develop.

## Step-by-Step Fix {#fix}

1. **Access the fault log on AdaptiView/CH530** — Navigate to the diagnostics screen and review the complete fault history with timestamps. The sequence of faults reveals the chain of events (e.g., flow fault followed by low pressure indicates the root cause is flow).
2. **For Water Flow Faults** — Verify both pumps are running and confirmed by flow switch status on the CH530 screen. Check strainers (both chilled and condenser water sides). Confirm isolation valves are fully open. Test the flow switch independently if pump operation is confirmed.
3. **For Low Refrigerant Pressure** — On CenTraVac units, this means air infiltration. Perform a leak test of shaft seals and purge system connections. The CenTraVac has a built-in purge unit that removes non-condensable gases — check that the purge unit is operational and its purge log.
4. **For High Condenser Pressure** — Check condenser water entering temperature (should match cooling tower design). Pull a condenser water sample and test for scaling tendency. Inspect condenser tubes for fouling (requires tube brushing).
5. **For Oil Pressure Low** — Check oil level in the sump sight glass. Run the oil pump manually from the CH530 service menu and verify pressure rise. Inspect oil for refrigerant odor or milky appearance (refrigerant dilution).
6. **Reset and monitor** — After repairs, reset the fault from the AdaptiView panel and restart the chiller. Monitor the first 30 minutes of operation closely for any recurrence.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Flow switch (chilled or condenser side)](https://www.amazon.com/s?k=Flow%20switch%20(chilled%20or%20condenser%20side)&tag=errorcodefixe-20) | Trane OEM preferred; confirm differential pressure setpoint |
| [Oil pump](https://www.amazon.com/s?k=Oil%20pump&tag=errorcodefixe-20) | For persistent oil pressure faults with correct oil level |
| [Purge unit components](https://www.amazon.com/s?k=Purge%20unit%20components&tag=errorcodefixe-20) | Purge compressor, desiccant, and purge valves — annual service item |
| [Condenser tube brush set](https://www.amazon.com/s?k=Condenser%20tube%20brush%20set&tag=errorcodefixe-20) | For tube fouling cleaning |

## When to Call a Pro

CenTraVac chillers are high-value, complex machines — a single diagnostic mistake can cause compressor damage worth hundreds of thousands of dollars. All refrigerant work (including non-condensable purging), oil analysis, and shaft seal service must be performed by Trane-certified technicians using the Tracer CH530 service software. Never attempt to add refrigerant to a CenTraVac without a full leak test and Trane engineering authorization.
