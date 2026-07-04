---
title: "Danfoss FC302 AL-146 - Causes & Fix"
description: "AL-146 is not a standard FC302 code. Most likely Alarm 14 (DC undervoltage). Check incoming power at input terminals first."
pubDatetime: 2026-06-26T09:46:26Z
modDatetime: 2026-06-26T09:46:26Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "FC302 Power Board (IGBT module and rectifier assembly)"
most_likely_cause: "Loose or corroded connections at input power terminals"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Measure incoming voltage at L1, L2, L3 to confirm all three phases are present and balanced within 3%"
  - "Check terminal torque at input power screws and look for charring or loose wires"
  - "Verify that no facility breakers or fuses upstream of the drive have blown"
no_buy_pct: "60%"
---

## Danfoss FC302 AL-146 — What It Means

The code AL-146 does not appear as a standard fault code in Danfoss FC302 documentation. The closest match is Alarm 14, which signals DC Undervoltage. This means the DC bus voltage inside the drive has dropped below the minimum threshold (typically around 200V for a 400V class drive). The drive shuts down because it cannot maintain stable motor control without sufficient DC link voltage. If you are seeing a display that reads 146, double-check the fault history menu or the manual to confirm whether it is Alarm 14, a parameter number, or an extended sub-code.

Assuming the fault is Alarm 14, the drive is telling you that the incoming AC power is not being converted and held at a high enough DC level. This can happen because of weak incoming power, failed rectifier diodes, aging DC link capacitors, or poor connections at the input terminals. Unlike an overcurrent fault (Alarm 13), which trips on peak current, Alarm 14 trips on low voltage and points to the power supply side of the drive.

## Before You Replace Anything

Technicians sometimes replace the entire power board when the real problem is a blown fuse in the building's distribution panel or a loose wire at the drive input terminals. Always measure incoming line voltage and check torque on terminal screws before ordering parts.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded input terminal connections (~35%)** Vibration or thermal cycling can loosen the input power screws, creating high resistance and voltage drop under load.
- **Blown fuse or tripped breaker upstream (~25%)** A phase loss in the building panel starves the rectifier and collapses the DC bus.
- **Incoming voltage sag or imbalance (~15%)** Weak utility supply or large equipment starting nearby can drag line voltage below spec.
- **Failed rectifier diodes on the power board (~15%)** Aging or overstressed diodes fail to convert AC to DC, dropping the DC link voltage.
- **Degraded DC link capacitors (~10%)** Capacitors lose capacitance over time and cannot hold the DC bus during transient loads.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the fault clear when you disconnect the motor and run the drive unloaded?</summary>
<div class="dtree-body"><strong>Yes:</strong> The motor or output wiring may be creating a load condition that drags down the DC bus (rare for Alarm 14 but possible). Inspect motor and cable insulation.<br><strong>No:</strong> The problem is internal to the drive or in the incoming power supply. Proceed with input voltage checks.</div>
</details>

<details class="dtree"><summary>Are all three incoming line voltages present and balanced within 3% of each other?</summary>
<div class="dtree-body"><strong>Yes:</strong> Incoming power is good. The fault is likely inside the drive (rectifier, capacitors, or power board).<br><strong>No:</strong> You have a phase loss, voltage sag, or blown fuse upstream. Repair the building electrical supply before servicing the drive.</div>
</details>

<details class="dtree"><summary>Can you see any signs of overheating, charring, or bulging capacitors inside the drive?</summary>
<div class="dtree-body"><strong>Yes:</strong> Failed components are visible. Replace the power board or the specific failed parts (rectifier assembly, DC link capacitors).<br><strong>No:</strong> The fault may be intermittent or caused by a marginal component. Monitor incoming voltage under load and consult a VFD technician.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Power down and lockout** the drive at the main disconnect. Wait at least five minutes for capacitors to discharge before opening the enclosure.
2. **Measure incoming line voltage** at terminals L1, L2, and L3 with a multimeter. Confirm all three phases are present and within 3% of each other.
3. **Inspect input terminal connections** for loose screws, corrosion, or charring. Retorque to the spec in the installation manual (consult your model's table).
4. **Check upstream fuses and breakers** in the facility panel. Replace any blown fuses and reset tripped breakers.
5. **Disconnect the motor** from output terminals U, V, W. Restore power and run the drive unloaded to see if Alarm 14 persists.
6. **Open the drive enclosure** (after lockout and discharge wait). Visually inspect the rectifier assembly and DC link capacitors for signs of failure (bulging, leaking, charring).
7. **Test the rectifier diodes** with a multimeter in diode-check mode if you have the skill. Replace the power board or rectifier assembly if diodes are shorted or open.
8. **Monitor the drive** under normal load after repairs. Log the DC bus voltage in the drive parameters to confirm it stays above the minimum threshold.

## Parts Often Needed

| Part | Notes |
|------|-------|
| FC302 Power Board (IGBT module and rectifier assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-146-fault-code&k=FC302+Power+Board+%28IGBT+module+and+rectifier+assembly%29&tag=errorcodefixes-20) \| Order by your exact drive frame size and voltage class from a Danfoss distributor. |
| DC Link Capacitor Bank | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-146-fault-code&k=DC+Link+Capacitor+Bank&tag=errorcodefixes-20) \| Sold as a matched set for your drive frame. Do not mix capacitor types or values. |

## When to Call a Pro

Call a qualified VFD technician or industrial electrician if you are not trained to work inside high-voltage equipment. Even after disconnecting power, the DC link capacitors can hold a lethal charge for several minutes. A technician will safely measure DC bus voltage, test rectifier diodes and IGBTs, and replace the power board or capacitor bank if needed. Also call a pro if incoming power issues require work in the building's main distribution panel or if the drive is part of a critical process that cannot tolerate downtime during troubleshooting.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [Danfoss FC-302 Alarm 12 — Overcurrent Fix](/posts/danfoss-fc302-alarm-12/)
- [Danfoss FC302 ALARM 37 - Causes & Fix](/posts/danfoss-fc302-alarm-37-fault-code/)
- [Danfoss FC302 Alarm 47 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-47-fault-code/)
- [Danfoss VLT AL 4 Fault - Causes & Fix](/posts/danfoss-vlt-vfd-al-4-fault-code/)
