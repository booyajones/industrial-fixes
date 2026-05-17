---
title: "Navien NPE Series Error Codes — Tankless Water Heater Fault Guide"
description: "Complete guide to Navien NPE series tankless water heater error codes, what each fault means, and step-by-step troubleshooting for ignition, flow, and sensor failures."
pubDatetime: 2026-04-22T22:00:00Z
modDatetime: 2026-04-22T22:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - plumbing
  - navien
  - tankless-water-heater
---

## Navien NPE Series Error Codes — What They Mean

The Navien NPE series (including NPE-180A, NPE-210A, NPE-240A, NPE-180S, NPE-210S, NPE-240S) are condensing tankless water heaters with efficiency ratings of up to 0.97 UEF. They display fault codes on the front panel display with both a code number and a brief description. The NPE series also supports connection to the NaviLink Wi-Fi module and NaviCirc recirculation.

[Jump to Fix](#fix)

## Navien NPE Series Error Code Reference

| Code | Meaning |
|------|---------|
| E001 | Abnormal ignition — failed to ignite |
| E002 | Abnormal ignition — flame loss during operation |
| E003 | Ignition failure (repeated attempts failed) |
| E004 | False flame detection |
| E006 | Hot water outlet temperature is too high (overtemp) |
| E007 | Hot water outlet temperature sensor fault |
| E008 | Cold water inlet temperature sensor fault |
| E009 | Exhaust overheat sensor fault |
| E010 | Abnormal air pressure switch |
| E011 | Cascade communication error (multiple units) |
| E012 | Gas valve fault |
| E013 | Gas pressure sensor fault |
| E016 | Cold water bypass valve fault |
| E024 | Fan motor fault |
| E030 | Freeze protection active |
| E031 | PCB temperature sensor fault |
| E302 | Abnormal water flow sensor |

## Common Causes by Code

- **E001 / E003 — Ignition failure** — The NPE igniter is electronic spark type. Common causes: low gas pressure (check meter pressure under load), dirty burner or igniter gap, failed gas valve, or blocked flue causing failed combustion air pressure switch. Check E010 first if E001 appears.
- **E002 — Flame loss** — Flame established but then lost during operation. Low gas pressure dropping under load, a defective gas valve that closes prematurely, or combustion problems from dirty burner or incorrect gas type (LP vs. NG setting).
- **E006 — Overtemp** — The NPE has a maximum outlet temp of 140°F. If the set temperature is high and flow rate is low (slow water draw), the heat exchanger can overheat. Reduce setpoint or increase flow rate.
- **E010 — Air pressure switch** — The NPE uses a differential pressure switch to confirm proper venting. A blocked exhaust (birds' nest, ice, debris), a disconnected vent pipe, or a failed pressure switch causes E010. Always check the exterior vent termination.
- **E024 — Fan motor** — The inducer fan motor has failed or is not reaching operating speed. A dirty fan wheel or failed motor bearing is the most common cause. The fan should audibly spin up before every ignition attempt.
- **E302 — Water flow sensor** — The flow sensor detects water flow to trigger the burner. Scale buildup on the sensor rotor in hard water areas is common — the sensor can be removed and descaled with white vinegar.

## Step-by-Step Fix {#fix}

1. **Read the display** — The NPE display shows the error code and a short description. Press the INFO button to see current operating parameters (inlet temp, outlet temp, flow rate, fan speed).
2. **For E001 / E003** — Confirm the gas supply is on. Check for other gas appliances in the home — if they also have low pressure, call your gas utility. Inspect the exterior vent termination for blockage.
3. **For E010** — Go outside and inspect the PVC vent termination. The NPE vents through two concentric PVC pipes (or two separate pipes). Confirm both the combustion air intake and the exhaust are clear of ice, debris, or bird activity.
4. **For E024** — With the unit off, listen for the fan spinning on the next startup attempt. No spin = power or motor failure. Spin without reaching speed = motor or controller issue.
5. **For E302** — Turn off water supply to the NPE. Remove the cold water inlet cover and locate the flow sensor. Remove and soak in white vinegar for 30 minutes to dissolve scale. Reinstall and test.
6. **For E006** — Lower the temperature setpoint. Ensure the flow rate through the unit is at least the minimum activation flow (typically 0.5 GPM for NPE). If scale has built up in the heat exchanger, a descaling flush is needed.
7. **Reset** — After correcting the fault, press the RESET button on the NPE front panel. For E003 lockout, hold RESET for 5 seconds.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Flow sensor | [Amazon](https://www.amazon.com/s?i=industrial&k=Flow+sensor&tag=errorcodefixes-20) \| E302; descale first before replacing |
| Air pressure switch | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| E010 after vent confirmed clear |
| Gas valve assembly | [Amazon](https://www.amazon.com/dp/B0015KAHHA?tag=errorcodefixes-20) \| E001/E002 after pressure confirmed |
| Fan motor assembly | [Amazon](https://www.amazon.com/dp/B0D2L5NSMM?tag=errorcodefixes-20) \| E024; includes wheel |
| Outlet temperature sensor | [Amazon](https://www.amazon.com/dp/B09FFFPF5L?tag=errorcodefixes-20) \| E007; NTC type |
| Igniter | [Amazon](https://www.amazon.com/s?i=industrial&k=Igniter&tag=errorcodefixes-20) \| For E001 with confirmed gas supply |
## When to Call a Pro

Gas pressure testing requires a calibrated manometer and gas work knowledge. Navien NPE units should be descaled annually in hard water areas — descaling requires a circulating pump and descaling solution kit. Contact Navien technical support (1-800-519-8794) for warranty issues or complex fault diagnoses.

## Related Articles

- [Navien Error Code E001 — No Ignition Fix](/posts/navien-error-code-e001/)
- [Navien E002 Error Code — Causes & Fix](/posts/navien-error-code-e002/)
- [Navien Error Code E003 — Ignition Failure Fix](/posts/navien-error-code-e003-ignition-failure/)
- [Navien Error Code E004 — Causes & Fix](/posts/navien-error-code-e004/)
- [Navien E006 Error Code — Causes & Fix](/posts/navien-error-code-e006/)
