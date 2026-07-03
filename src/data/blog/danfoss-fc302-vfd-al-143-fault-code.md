---
title: "Danfoss FC302 AL-143 Fault - Causes & Fix"
description: "AL-143 is not a documented Danfoss FC302 code. You likely have Alarm 13 (Overcurrent). Check motor cables and connections first."
pubDatetime: 2026-06-25T09:29:56Z
modDatetime: 2026-06-25T09:29:56Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - danfoss
money_part: "Danfoss FC302 Power Board (Rectifier/Inverter Assembly)"
most_likely_cause: "Motor cable or connection issue causing current spikes"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect all motor cable connections at the drive output (U, V, W) and motor terminal box for loose or corroded terminals"
  - "Check parameter 1-24 (motor nominal current) matches the motor nameplate rating exactly"
---

## Danfoss FC302 AL-143 Fault — What It Means

AL-143 is not a valid or documented fault code for the Danfoss FC302 VLT AutomationDrive. You may have misread Alarm 13 (Overcurrent), which is one of the most common Danfoss VFD faults. Alarm 13 means the drive detected output current exceeding safe operating limits during normal operation or acceleration. The IGBTs are delivering more current than the drive's rated capacity, triggering an immediate trip to protect the inverter power section.

If your display shows a different number or you see "AL" followed by digits, consult your drive's manual or check the alarm history in parameter 16-90 to confirm the exact code. The troubleshooting below assumes Alarm 13 (Overcurrent), the most probable match for a code reference containing "13" or "143."

## Before You Replace Anything

Technicians often replace the entire power board or IGBT modules when the real fault is a loose motor connection or a motor winding with insulation breakdown. Always disconnect the motor and run the drive unloaded first to isolate whether the fault is internal to the drive or external in the motor circuit.

[Jump to Fix](#fix)

## Common Causes

- **Loose or corroded motor cable connections (~35%)** Resistance at a poor connection causes voltage drop and current spikes that trip Alarm 13.
- **Motor winding insulation failure (~25%)** A partial short in the motor windings draws excessive current even under light load.
- **Failed IGBT modules in the inverter section (~20%)** Aging or damaged IGBTs lose current regulation ability and cause the drive to measure overcurrent.
- **Incorrect motor parameter settings (~10%)** If parameter 1-24 (nominal motor current) is set lower than the actual motor rating, the drive trips prematurely.
- **Mechanical overload on the motor shaft (~7%)** A jammed pump, seized bearing, or other mechanical bind forces the motor to draw high current during acceleration.
- **Damaged power board (rectifier or inverter assembly) (~3%)** A failing rectifier or DC link capacitor creates current imbalance and triggers overcurrent protection.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the alarm appear immediately on power-up, before the motor even starts?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is likely internal to the drive (power board or IGBTs) or a shorted motor cable. Proceed to the isolation test in Step 1.<br><strong>No:</strong> The fault occurs under load, pointing to motor, cable, or mechanical issues. Check connections and motor insulation first.</div>
</details>

<details class="dtree"><summary>When you disconnect the motor and run the drive unloaded, does Alarm 13 still appear?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault is internal to the drive. Inspect the IGBT modules, DC link capacitors, and input fuses. You need a drive repair or replacement.<br><strong>No:</strong> The fault is in the motor or motor cable. Test motor winding insulation and check for mechanical overload.</div>
</details>

<details class="dtree"><summary>Does your motor insulation test (megohm meter to ground) read above 2 megohms on all three phases?</summary>
<div class="dtree-body"><strong>Yes:</strong> Motor insulation is acceptable. Check for loose connections, mechanical binding, or incorrect parameter 1-24 setting.<br><strong>No:</strong> Motor winding insulation has broken down. The motor needs rewinding or replacement.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Verify the alarm code** by pressing the Info button and checking parameter 16-90 (Alarm Log) on the drive keypad to confirm you have Alarm 13 and not a different fault.
2. **Disconnect the motor** from the drive output terminals (U, V, W) and attempt to run the drive in manual mode with no load connected. If Alarm 13 persists with no motor attached, the fault is internal to the drive and you should skip to Step 6.
3. **Test motor winding insulation** using a megohm meter set to 500V DC. Measure resistance from each motor winding (U, V, W) to the motor frame ground. Readings below 2 megohms indicate insulation failure and the motor needs service or replacement.
4. **Inspect all cable connections** at both the drive output terminals and the motor terminal box. Tighten any loose terminals, clean corrosion with contact cleaner, and check for signs of arcing or heat damage.
5. **Check parameter 1-24** (Motor Nominal Current) in the drive menu. Compare the value to the motor nameplate current rating. If the parameter is set lower than the motor's actual rating, adjust it to match the nameplate exactly and reset the alarm.
6. **Inspect drive internal components** if the alarm persists with the motor disconnected. Remove the drive cover and visually check the inverter board for burned or cracked IGBT modules, look for bulging or leaking DC link capacitors, and check input fuses for continuity. Replace damaged components or the entire power board assembly.
7. **Reconnect the motor** after repairs and run a test cycle. Monitor the drive display for current readings during acceleration. If current spikes above the motor rated current, check for mechanical binding in the driven equipment (pump, fan, conveyor) and resolve any overload conditions.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Danfoss FC302 Power Board (Rectifier/Inverter Assembly) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-143-fault-code&k=Danfoss+FC302+Power+Board+%28Rectifier%2FInverter+Assembly%29&tag=errorcodefixes-20) \| Order by your drive's frame size and voltage rating from the nameplate |
| IGBT Module Set for Danfoss FC302 | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-danfoss-fc302-vfd-al-143-fault-code&k=IGBT+Module+Set+for+Danfoss+FC302&tag=errorcodefixes-20) \| Match the part number on the existing IGBT if replacing modules individually |

## When to Call a Pro

Call a qualified industrial electrician or VFD technician if you are not trained in high-voltage DC work. The DC bus inside the drive can hold lethal voltage (up to 800V DC) for several minutes after power is removed. Professionals have the meters and lockout procedures to safely discharge capacitors, test IGBT junctions, and replace power boards. Also call a pro if the motor insulation test fails, because rewinding or replacing a three-phase motor requires specialized equipment and knowledge of motor specifications. If your process cannot tolerate downtime, a technician can often diagnose the fault remotely via the drive's communication port and arrive with the correct spare parts.

**Rough cost:** A pro service call runs about $300-800.

## See Also

- [Danfoss FC302 ALARM 24 - Causes & Fix](/posts/danfoss-fc302-vfd-alarm-24-fault-code/)
- [Danfoss FC302 W66 - Causes & Fix](/posts/danfoss-fc302-vfd-al-66-fault-code/)
- [Danfoss VFD Fault W30 — Brake Resistor Overtemperature Fix](/posts/danfoss-vfd-fault-w30/)
- [Danfoss FC302 AL-112 - Causes & Fix](/posts/danfoss-fc302-vfd-al-112-fault-code/)
