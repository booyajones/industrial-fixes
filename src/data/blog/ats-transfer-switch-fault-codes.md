---
title: "Automatic Transfer Switch Fault Codes — Complete Guide"
description: "Automatic transfer switch (ATS) fault codes for Generac, Kohler, Asco, and Russelectric ATS units: all fault codes, error states, causes, and fixes."
pubDatetime: 2026-04-22T19:00:00Z
modDatetime: 2026-04-22T19:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - generator
  - transfer-switch
  - electrical
---

## Automatic Transfer Switch Fault Codes — Quick Reference

Automatic transfer switches (ATS) monitor utility power and transfer loads to a generator when utility power fails. Major ATS brands include Generac (RTSY, RTSN series), Kohler (RDT, KCTS series), Asco (Series 300, 7000), and Russelectric. Faults appear on the ATS controller display and are often transmitted to the generator's controller.

| Fault | Brand / Type | Meaning | Quick Fix |
|-------|-------------|---------|-----------|
| [Source 1 Fail](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Source+1+Fail&tag=errorcodefixes-20) | All | Utility power has failed | Normal — ATS should transfer to generator |
| [Source 2 Fail](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Source+2+Fail&tag=errorcodefixes-20) | All | Generator not available | Check generator; check ATS-to-gen wiring |
| [Transfer Inhibit](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Transfer+Inhibit&tag=errorcodefixes-20) | All | Transfer blocked by external input | Check inhibit wiring |
| [Time Delay Active](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Time+Delay+Active&tag=errorcodefixes-20) | All | Transfer delay counting down | Normal — wait for delay to expire |
| [Overcurrent](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Overcurrent&tag=errorcodefixes-20) | Asco, Russelectric | Load current exceeded ATS rating | Reduce load; check for faults |
| [Motor Fault](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Motor+Fault&tag=errorcodefixes-20) | Asco, Kohler | Transfer mechanism motor fault | Inspect motor; check contacts |
| [Position Fault](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Position+Fault&tag=errorcodefixes-20) | All | ATS didn't reach commanded position | Check mechanism; check contacts |
| [Neutral Overlap](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Neutral+Overlap&tag=errorcodefixes-20) | 3-pos ATS | In neutral position during transfer | Normal brief state |
| [Generator Not In Auto](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Generator+Not+In+Auto&tag=errorcodefixes-20) | All | Generator controller not in AUTO mode | Set generator to AUTO |
| [Maintenance Mode](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Maintenance+Mode&tag=errorcodefixes-20) | All | ATS manually set to bypass | Return to AUTO after maintenance |
| [Com Fault](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Com+Fault&tag=errorcodefixes-20) | Networked ATS | Communication to remote device lost | Check network wiring |

## Most Common Faults

### Source 2 Fail — Generator Not Available
When utility power fails and the ATS calls for the generator, "Source 2 Fail" means the generator did not come online within the expected time or is not producing correct voltage. Check:
1. The generator itself — is it running? Check the generator controller for its own fault codes.
2. Generator voltage and frequency — should be 120/240VAC, 60 Hz at rated speed (3600 RPM for 2-pole).
3. The wiring between the generator and ATS — specifically the generator output breaker and the ATS input terminals.
4. The generator controller is in AUTO mode — many generators will not start if the controller is in MANUAL or OFF position.

### Position Fault — Transfer Mechanism
The ATS transfer mechanism (typically a solenoid-operated or motor-driven contactor) did not move to the commanded position within the timeout window. Check:
- The ATS mechanism for physical obstructions
- The coil voltage at the ATS solenoid or motor (verify rated voltage is present when commanded)
- The position feedback switches inside the ATS enclosure — these micro-switches tell the controller where the contacts actually are
- Contact wear — in older ATS units, worn contacts can prevent the mechanism from seating fully in either position

### Generator Not In Auto
This is the simplest fault to fix — but also one of the most common reasons a generator fails to start during an actual power outage. After any maintenance on the generator, always verify the generator controller is returned to AUTO mode. The ATS will display this fault continuously when the generator is in manual or off mode.

### Transfer Inhibit
The transfer inhibit input is a dry-contact input on the ATS that allows external systems to temporarily prevent transfer. Common sources of transfer inhibit signals include:
- Process control systems signaling "not ready to transfer"
- Emergency lighting control panels
- Manually-installed inhibit jumpers left in place after maintenance

Check the inhibit wiring terminal on the ATS and verify no unintended inhibit signal is present.

## Asco Series 7000 Specific Faults

| [Display](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=Display&tag=errorcodefixes-20) | Meaning |
|---------|---------|
| [S1 FAIL](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=S1+FAIL&tag=errorcodefixes-20) | Source 1 (normal) power failure |
| [S2 NOT AVL](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=S2+NOT+AVL&tag=errorcodefixes-20) | Source 2 (emergency) not available |
| [XFER INHIBIT](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=XFER+INHIBIT&tag=errorcodefixes-20) | Transfer prevented by external signal |
| [PWR SUPP FLT](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=PWR+SUPP+FLT&tag=errorcodefixes-20) | ATS internal power supply fault |
| [COM FAIL](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=COM+FAIL&tag=errorcodefixes-20) | Remote monitoring communication fault |
| [MAINT BYPSS](https://www.amazon.com/s?ascsubtag=ecf-ats-transfer-switch-fault-codes&k=MAINT+BYPSS&tag=errorcodefixes-20) | Manual bypass mode active |

## Generac RTSY/RTSN ATS Notes

- Generac ATS units are matched to specific Generac generator models — verify compatibility before replacement
- The RTSN series uses a motorized ATS — the transfer motor is a common service item
- Configuration parameters (time delays, voltage windows) are accessible via the generator's Evolution controller when the ATS is connected

## When to Call a Pro
ATS maintenance and repairs involve both utility-side and generator-side electrical hazards. **Always** have a qualified electrician perform any physical work inside an ATS enclosure — the utility-side terminals remain energized even when the generator is supplying the load.
