---
title: "Yaskawa VFD Fault Codes — Complete Reference (V1000, A1000, GA700)"
description: "Yaskawa VFD fault codes: all major faults for V1000, A1000, J1000, and GA700 drives including OC, OV, UV, GF, and OH faults."
pubDatetime: 2026-04-22T16:00:00Z
modDatetime: 2026-04-22T16:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - vfd
  - yaskawa
---

## Yaskawa VFD Fault Codes — Quick Reference

Yaskawa drives (V1000, J1000, A1000, GA700, P1000, Z1000 series) display fault codes as abbreviated text on the LED keypad or LCD operator panel. Faults (FLT) stop the motor immediately; alarms (ALM) allow continued operation with reduced performance. Access the fault history via the operator panel diagnostic menu.

| [Code](https://www.amazon.com/s?k=Code&tag=errorcodefixe-20) | Meaning | Common Fix | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |---------|-----------|
| oC | [Overcurrent](https://www.amazon.com/s?k=Overcurrent&tag=errorcodefixe-20) | Check motor; extend accel time |
| [ov](https://www.amazon.com/s?k=ov&tag=errorcodefixe-20) | Overvoltage | Extend decel time; add braking resistor | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Uv1 | DC bus undervoltage | [Check input power supply](https://www.amazon.com/s?k=Check%20input%20power%20supply&tag=errorcodefixe-20) |  | GF | [Ground fault](https://www.amazon.com/s?k=Ground%20fault&tag=errorcodefixe-20) | Megger motor and cable |
| [oH](https://www.amazon.com/s?k=oH&tag=errorcodefixe-20) | Drive overtemperature | Clean cooling; check ambient temp | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | oL1 | Motor overload | [Check motor FLA parameter; reduce load](https://www.amazon.com/s?k=Check%20motor%20FLA%20parameter%3B%20reduce%20load&tag=errorcodefixe-20) |  | oL2 | [Drive overload](https://www.amazon.com/s?k=Drive%20overload&tag=errorcodefixe-20) | Reduce load or use larger drive |
| [SC](https://www.amazon.com/s?k=SC&tag=errorcodefixe-20) | Short circuit | Check motor winding and cable | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | PF | Power supply fault | [Check input voltage quality](https://www.amazon.com/s?k=Check%20input%20voltage%20quality&tag=errorcodefixe-20) |  | LF | [Output phase loss](https://www.amazon.com/s?k=Output%20phase%20loss&tag=errorcodefixe-20) | Check motor connection; cable |
| [CF](https://www.amazon.com/s?k=CF&tag=errorcodefixe-20) | Control fault | Check control board; reset | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | bb | Base block (safe torque off) | [Check STO/SFS input wiring](https://www.amazon.com/s?k=Check%20STO%2FSFS%20input%20wiring&tag=errorcodefixe-20) |  | Er | [EEPROM fault](https://www.amazon.com/s?k=EEPROM%20fault&tag=errorcodefixe-20) | Cycle power; replace control board |
| [GA700: CPF](https://www.amazon.com/s?k=GA700%3A%20CPF&tag=errorcodefixe-20) | Control power fault | Check 24V control power supply | [## Most Common Codes

### oC: Overcurrent
The output current exceeded the drive's trip level (usually 200% of rated current). Common causes: mechanical jam/stall, acceleration ramp too fast for the load inertia, motor parameters incorrectly set, or a motor/cable insulation fault that's not quite a ground fault.

**Fix:** (1) Verify C1-01 (acceleration time) is not too short. (2) Check motor FLA — set E2-01 (Motor Rated Current) to match the motor nameplate. (3) Check for mechanical binding. (4) If oC trips at startup, suspect undersized cables or motor terminal box wiring issues.

### ov: Overvoltage
DC bus exceeded trip level due to regenerative energy. The GA700 has built-in flux braking; the V1000 and A1000 require either increased decel time (C1-02) or an external braking resistor. Enable stall prevention during deceleration (L3-04) if overvoltage is intermittent.

### Uv1: Undervoltage
Input voltage too low. On 480V Yaskawa drives, DC bus undervoltage trips at approximately 190V DC (about 268V AC input). Check: (1) all three input phases are present and symmetrical, (2) input fuses/breaker is not open, (3) supply voltage is within spec (+10%/-15% of drive rating).

### GF: Ground Fault
A current path to ground was detected in the output circuit. This is a serious fault. Before restarting: (1) disconnect the motor from the drive, (2) megger test the motor phases to ground at 500V DC — should be >1 MΩ, (3) megger test the motor cable. Also check the drive output terminals for physical damage. If motor and cable are clean, the fault may be in the drive's output current sensors.

### oH: Overtemperature
The heatsink temperature exceeded the limit (usually 90–105°C depending on model). On V1000 drives, the cooling fan is automatic (runs when hot) — check that it spins. On A1000 and GA700, the fan is continuous — if it's failed, temperature rises steadily. Clear heatsink fins with compressed air annually.

### LF: Output Phase Loss
One motor phase is missing or has very high impedance. Check: motor cable for a broken conductor, terminal box connections at the motor (loose lug), and the drive's output terminals. LF can also trip if the motor is disconnected while the drive is running.

### bb: Base Block
The Base Block (safe torque off) input has been activated. The drive will not produce output while bb is active. Check: (1) STO/SFS terminals — they should have +24V when run is commanded, (2) safety relay wiring if a safety circuit is installed, (3) jumpers between SFS and SCF if no safety circuit is used (per the drive startup guide).

## Clearing Faults

- **Manual reset:** Press RESET key on the operator panel.
- **Digital input reset:** Configure a digital input for Fault Reset (H1-XX = 14).
- **Auto-reset:** Configure L5-01 (Number of Auto Restarts) and L5-02 (auto restart fault select).

## Parts Often Needed](https://www.amazon.com/s?k=%23%23%20Most%20Common%20Codes%0A%0A%23%23%23%20oC%3A%20Overcurrent%0AThe%20output%20current%20exceeded%20the%20drive's%20trip%20level%20(usually%20200%25%20of%20rated%20current).%20Common%20causes%3A%20mechanical%20jam%2Fstall%2C%20acceleration%20ramp%20too%20fast%20for%20the%20load%20inertia%2C%20motor%20parameters%20incorrectly%20set%2C%20or%20a%20motor%2Fcable%20insulation%20fault%20that's%20not%20quite%20a%20ground%20fault.%0A%0A**Fix%3A**%20(1)%20Verify%20C1-01%20(acceleration%20time)%20is%20not%20too%20short.%20(2)%20Check%20motor%20FLA%20%E2%80%94%20set%20E2-01%20(Motor%20Rated%20Current)%20to%20match%20the%20motor%20nameplate.%20(3)%20Check%20for%20mechanical%20binding.%20(4)%20If%20oC%20trips%20at%20startup%2C%20suspect%20undersized%20cables%20or%20motor%20terminal%20box%20wiring%20issues.%0A%0A%23%23%23%20ov%3A%20Overvoltage%0ADC%20bus%20exceeded%20trip%20level%20due%20to%20regenerative%20energy.%20The%20GA700%20has%20built-in%20flux%20braking%3B%20the%20V1000%20and%20A1000%20require%20either%20increased%20decel%20time%20(C1-02)%20or%20an%20external%20braking%20resistor.%20Enable%20stall%20prevention%20during%20deceleration%20(L3-04)%20if%20overvoltage%20is%20intermittent.%0A%0A%23%23%23%20Uv1%3A%20Undervoltage%0AInput%20voltage%20too%20low.%20On%20480V%20Yaskawa%20drives%2C%20DC%20bus%20undervoltage%20trips%20at%20approximately%20190V%20DC%20(about%20268V%20AC%20input).%20Check%3A%20(1)%20all%20three%20input%20phases%20are%20present%20and%20symmetrical%2C%20(2)%20input%20fuses%2Fbreaker%20is%20not%20open%2C%20(3)%20supply%20voltage%20is%20within%20spec%20(%2B10%25%2F-15%25%20of%20drive%20rating).%0A%0A%23%23%23%20GF%3A%20Ground%20Fault%0AA%20current%20path%20to%20ground%20was%20detected%20in%20the%20output%20circuit.%20This%20is%20a%20serious%20fault.%20Before%20restarting%3A%20(1)%20disconnect%20the%20motor%20from%20the%20drive%2C%20(2)%20megger%20test%20the%20motor%20phases%20to%20ground%20at%20500V%20DC%20%E2%80%94%20should%20be%20%3E1%20M%CE%A9%2C%20(3)%20megger%20test%20the%20motor%20cable.%20Also%20check%20the%20drive%20output%20terminals%20for%20physical%20damage.%20If%20motor%20and%20cable%20are%20clean%2C%20the%20fault%20may%20be%20in%20the%20drive's%20output%20current%20sensors.%0A%0A%23%23%23%20oH%3A%20Overtemperature%0AThe%20heatsink%20temperature%20exceeded%20the%20limit%20(usually%2090%E2%80%93105%C2%B0C%20depending%20on%20model).%20On%20V1000%20drives%2C%20the%20cooling%20fan%20is%20automatic%20(runs%20when%20hot)%20%E2%80%94%20check%20that%20it%20spins.%20On%20A1000%20and%20GA700%2C%20the%20fan%20is%20continuous%20%E2%80%94%20if%20it's%20failed%2C%20temperature%20rises%20steadily.%20Clear%20heatsink%20fins%20with%20compressed%20air%20annually.%0A%0A%23%23%23%20LF%3A%20Output%20Phase%20Loss%0AOne%20motor%20phase%20is%20missing%20or%20has%20very%20high%20impedance.%20Check%3A%20motor%20cable%20for%20a%20broken%20conductor%2C%20terminal%20box%20connections%20at%20the%20motor%20(loose%20lug)%2C%20and%20the%20drive's%20output%20terminals.%20LF%20can%20also%20trip%20if%20the%20motor%20is%20disconnected%20while%20the%20drive%20is%20running.%0A%0A%23%23%23%20bb%3A%20Base%20Block%0AThe%20Base%20Block%20(safe%20torque%20off)%20input%20has%20been%20activated.%20The%20drive%20will%20not%20produce%20output%20while%20bb%20is%20active.%20Check%3A%20(1)%20STO%2FSFS%20terminals%20%E2%80%94%20they%20should%20have%20%2B24V%20when%20run%20is%20commanded%2C%20(2)%20safety%20relay%20wiring%20if%20a%20safety%20circuit%20is%20installed%2C%20(3)%20jumpers%20between%20SFS%20and%20SCF%20if%20no%20safety%20circuit%20is%20used%20(per%20the%20drive%20startup%20guide).%0A%0A%23%23%20Clearing%20Faults%0A%0A-%20**Manual%20reset%3A**%20Press%20RESET%20key%20on%20the%20operator%20panel.%0A-%20**Digital%20input%20reset%3A**%20Configure%20a%20digital%20input%20for%20Fault%20Reset%20(H1-XX%20%3D%2014).%0A-%20**Auto-reset%3A**%20Configure%20L5-01%20(Number%20of%20Auto%20Restarts)%20and%20L5-02%20(auto%20restart%20fault%20select).%0A%0A%23%23%20Parts%20Often%20Needed&tag=errorcodefixe-20) | Part | Notes | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | ------ |-------| [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Braking resistor | Yaskawa ERF or ERV series, sized per drive catalog | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Cooling fan | Drive-specific; V1000: YPJP31-B fan assembly | [](https://www.amazon.com/s?k=&tag=errorcodefixe-20) | Control power fuse | 2A time-lag, model-specific |

## When to Call a Pro
GF (ground fault) and SC (short circuit) faults that persist after checking the motor and cable indicate a failed drive output stage. IGBT replacement in Yaskawa drives requires authorized service.
