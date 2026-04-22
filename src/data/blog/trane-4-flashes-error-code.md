---
title: "Trane 4 Flashes Error Code — Open High Limit Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-25T08:00:00Z
modDatetime: 2024-03-25T08:00:00Z
slug: trane-4-flashes-error-code
featured: false
draft: false
tags:
  - hvac
  - trane
  - furnace
  - limit-switch
description: "Trane 4 flashes means the high limit switch has opened due to overheating. This guide covers every cause and fix for the Trane furnace open high limit device fault."
---

## Error Code: Trane 4 Flashes

**What it means:** Four flashes on the Trane furnace diagnostic LED indicates an open high limit device. The high limit switch is a normally-closed thermal switch mounted on the heat exchanger plenum. It opens when plenum temperature exceeds its setpoint — typically 140–180°F depending on the furnace model. When the limit opens, the gas valve closes immediately but the blower continues running to cool the heat exchanger. If the limit trips repeatedly, the board locks out. The limit switch itself is the messenger — the real problem is whatever is causing the furnace to overheat.

## Common Causes

- **Dirty or clogged air filter** — The most common cause. Restricted airflow traps heat inside the heat exchanger. Replace the filter first, before any other diagnosis.
- **Blocked or closed supply/return registers** — Too many closed registers starves the system of airflow. Minimum 80% of registers should be open.
- **Failed blower motor or capacitor** — A blower running at reduced speed (weak capacitor, failing winding) cannot remove heat from the exchanger fast enough.
- **Blocked evaporator coil** — A dirty A-coil downstream of the furnace creates restriction equivalent to a clogged filter.
- **Undersized ductwork** — Common in older homes or after HVAC upgrades. Inadequate duct size prevents the system from moving enough CFM.
- **Cracked heat exchanger** — A crack disrupts airflow inside the exchanger, creating hot spots that trip the limit even with good filter and blower operation.

## Diagnosis Steps

1. Replace or inspect the air filter first. If it's gray and matted, that's the cause. Replace, reset the furnace, and run a heating cycle.
2. Verify all supply and return registers are open. Check for furniture blocking return air grilles.
3. Listen to the blower during operation. It should ramp up smoothly to full speed within 30–60 seconds of heat call. A blower running noticeably slower than normal or making a labored sound points to a motor or capacitor fault.
4. At the air handler, measure supply air temperature rise across the heat exchanger. Attach a thermometer probe in the supply plenum and return air. Temperature rise should be 40–70°F for most residential gas furnaces. Higher than 70°F indicates restricted airflow.
5. If all airflow components check out, inspect the limit switch with a multimeter. With the furnace cool, the switch should read continuity (closed). An open reading on a cool furnace means the switch has failed and needs replacement.

## Fix

Start with filter replacement and airflow corrections — these resolve the majority of 4-flash faults. If the blower capacitor has failed, replace it before the motor (capacitor is a $15–25 part; motors are $150–350). Match the capacitor MFD and voltage rating exactly.

If the high limit switch has failed open (reads OL when furnace is cold), replace it. Trane uses several limit switch configurations — order by furnace model number to get the correct temperature rating and body configuration.

If no airflow or mechanical cause is found, have the heat exchanger inspected for cracks. This requires a licensed tech with a combustion analyzer or inspection camera.

## Parts

| Part | Where to Buy |
|------|-------------|
| [High limit switch](https://www.amazon.com/s?k=High%20limit%20switch&tag=errorcodefixe-20) | RepairClinic, SupplyHouse |
| [Blower motor run capacitor](https://www.amazon.com/s?k=Blower%20motor%20run%20capacitor&tag=errorcodefixe-20) | Grainger, Amazon |
| [ECM or PSC blower motor](https://www.amazon.com/s?k=ECM%20or%20PSC%20blower%20motor&tag=errorcodefixe-20) | RepairClinic, Grainger |
| [Air filter (replacement)](https://www.amazon.com/s?k=Air%20filter%20(replacement)&tag=errorcodefixe-20) | Amazon, SupplyHouse |

## When to Call a Technician

If the 4-flash fault persists after filter replacement and airflow corrections, have a licensed HVAC tech inspect the heat exchanger for cracks. A cracked heat exchanger is a carbon monoxide risk and the furnace should not be operated until it is inspected and cleared.
