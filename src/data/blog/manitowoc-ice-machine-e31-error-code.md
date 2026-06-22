---
title: "Manitowoc E31 Error Code - Causes & Fix"
description: "E31 means Safe Mode due to ITP sensor failure. Machine runs in limited capacity. Replace the ITP sensor or repair its wiring."
pubDatetime: 2026-06-20T12:40:12Z
modDatetime: 2026-06-20T12:40:12Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - refrigeration
  - manitowoc
money_part: "Manitowoc ITP sensor"
most_likely_cause: "Failed ITP sensor"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Check the event log on the Indigo control to confirm E31 is the active or most recent fault code"
  - "Inspect the ITP sensor harness and connectors for visible damage, corrosion, or loose plugs and reseat them"
---

## Manitowoc E31 Error Code — What It Means

E31 on a Manitowoc Indigo ice machine indicates the controller has entered Safe Mode because it detected an ITP sensor failure. Instead of shutting down completely, the machine continues to operate in a limited capacity to keep producing ice temporarily while flagging the fault. Safe Mode is designed to allow production until a technician can service the unit.

The ITP sensor monitors ice thickness or production parameters, and when its signal is lost or invalid, the controller cannot regulate ice making properly. The E31 code tells you the machine is compensating for that missing input by using fallback logic, but efficiency and ice quality may suffer until the sensor circuit is repaired.

## Before You Replace Anything

Technicians sometimes replace the control board first when E31 appears intermittently, but the code explicitly points to the ITP sensor. Inspect and test the sensor and its wiring harness before swapping the controller.

[Jump to Fix](#fix)

## Common Causes

- **Failed ITP sensor (~55%)** The sensor itself has failed internally and no longer provides a valid signal to the controller, triggering Safe Mode.
- **Loose or corroded wiring to the ITP sensor (~25%)** Connectors or wiring between the sensor and control board are damaged, wet, or intermittently open, causing signal loss.
- **Water intrusion at the sensor or connector (~10%)** Ice machine environment allows water to enter the sensor housing or terminal block, shorting or degrading the signal.
- **Control board input circuit fault (~10%)** The controller's ITP sensor input has failed, reading the sensor as bad even when the sensor is good.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the machine still making ice, just less efficiently or with irregular cycles?</summary>
<div class="dtree-body"><strong>Yes:</strong> Safe Mode is active and the machine is compensating for the missing ITP signal. Proceed with sensor and wiring diagnostics.<br><strong>No:</strong> Check for additional fault codes in the event log, because E31 alone should allow limited production rather than a complete shutdown.</div>
</details>

<details class="dtree"><summary>Does the ITP sensor connector show corrosion, moisture, or a loose fit when you unplug and inspect it?</summary>
<div class="dtree-body"><strong>Yes:</strong> Clean the pins with contact cleaner, dry thoroughly, reseat firmly, and clear the fault. If E31 returns, replace the sensor.<br><strong>No:</strong> The sensor or its internal circuit is likely failed. Replace the ITP sensor and retest.</div>
</details>

<details class="dtree"><summary>After replacing the ITP sensor, does E31 return immediately or within a few cycles?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board's ITP input circuit is suspect. Verify correct sensor installation and wiring routing, then test or replace the controller.<br><strong>No:</strong> The new sensor has resolved the fault. Monitor the machine over the next day to confirm stable operation.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Access the Indigo control panel** and navigate to the diagnostics or event log menu to confirm E31 is the active or most recent code.
2. **Locate the ITP sensor** on your model (consult the service manual for exact placement, typically near the evaporator or ice thickness probe area).
3. **Unplug the sensor connector** and inspect both the sensor terminals and the mating harness plug for corrosion, water, or damaged pins.
4. **Clean and reseat the connector** if any contamination is visible. Use electrical contact cleaner and allow it to dry completely before reconnecting.
5. **Clear the E31 fault** from the control and run a harvest or production cycle to see if the code returns.
6. **Replace the ITP sensor** if the fault reappears or if the connector and wiring are clean but the code persists.
7. **Verify normal operation** by running several freeze and harvest cycles and checking the event log to confirm no new E31 entries appear.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Manitowoc ITP sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e31-error-code&k=Manitowoc+ITP+sensor&tag=errorcodefixes-20) \| Match the part number to your Indigo model series; sensor types vary by machine configuration. |
| Sensor wiring harness | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-manitowoc-ice-machine-e31-error-code&k=Sensor+wiring+harness&tag=errorcodefixes-20) \| Order if the original harness shows cuts, burns, or terminal damage that cleaning cannot fix. |

## When to Call a Pro

Call a qualified commercial refrigeration technician for E31 diagnosis and repair. The ITP sensor is part of the ice machine's refrigeration control circuit, and troubleshooting requires familiarity with Manitowoc Indigo diagnostics, sensor testing, and safe handling of electrical components in a wet environment. If the sensor replacement does not clear the code, the technician will need to test the control board's input circuit and verify refrigerant cycle operation. Attempting sensor or control board work without proper training risks damaging the controller, voiding your warranty, or creating unsafe electrical conditions around water and ice.

**Rough cost:** A pro service call runs about $200-450.
