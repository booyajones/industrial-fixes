---
title: "ABB ACS580 VFD E0028 Fault Code - Causes & Fix"
description: "E0028 signals a VFD communication fault. Check wiring and network settings first; if those are secure, the I/O board may need attention."
pubDatetime: 2026-07-18T07:57:51Z
modDatetime: 2026-07-18T07:57:51Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: true
tags:
  - vfd
  - abb
money_part: "ABB fieldbus communication card"
most_likely_cause: "Loose or damaged control wiring"
likelihood: "the most common cause"
diy_or_pro: "pro"
free_checks:
  - "Inspect all control wiring and communication cable connections for looseness or damage and reseat connectors"
  - "Power-cycle the drive to clear transient communication faults"
  - "Review drive parameters for communication protocol settings and verify they match the network or PLC configuration"
---

## ABB ACS580 VFD E0028 Fault Code — What It Means

The E0028 fault code on an ABB ACS580 variable frequency drive typically indicates a communication or I/O error. This fault appears when the drive detects a problem communicating with external devices, fieldbus networks, or internal I/O modules. The exact definition can vary slightly depending on your drive's firmware version and installed options, so consult your ACS580 user manual for the precise meaning for your model.

Common triggers include loose or damaged wiring to control terminals, incorrect parameter settings for communication protocols (such as Modbus, Profibus, or Ethernet/IP), failed communication cards or I/O expansion modules, or a loss of connection to a supervisory controller or PLC. In some cases the fault may also point to an internal board fault within the drive itself.

## Before You Replace Anything

Technicians sometimes replace the main control board or communication card before verifying that parameter settings match the network configuration and that all control wiring is intact and properly terminated.

[Jump to Fix](#fix)

## Common Causes

- **Loose or damaged control wiring (~35%)** Vibration or installation errors can cause terminals to loosen or wires to fray, interrupting communication signals.
- **Incorrect communication parameters (~25%)** Mismatched baud rate, protocol type, or node address settings prevent the drive from handshaking with the network.
- **Failed communication card or I/O module (~20%)** An installed fieldbus adapter or expansion I/O card may have failed or become unseated from its slot.
- **Network or PLC fault (~10%)** The upstream controller or network segment may have dropped offline or changed configuration.
- **Internal control board fault (~10%)** The drive's main control board may have developed a fault affecting its I/O circuitry.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Is the drive connected to an external PLC or fieldbus network?</summary>
<div class="dtree-body"><strong>Yes:</strong> Verify the network is online and the drive's communication parameters (protocol, address, baud rate) match the network settings.<br><strong>No:</strong> Check local control wiring and I/O expansion modules for loose connections or damage.</div>
</details>

<details class="dtree"><summary>Does the fault clear after a power cycle?</summary>
<div class="dtree-body"><strong>Yes:</strong> The fault may have been transient due to electrical noise or a brief network interruption; monitor for recurrence.<br><strong>No:</strong> A persistent fault points to wiring damage, parameter mismatch, or a failed communication card or control board.</div>
</details>

<details class="dtree"><summary>Are all communication and control terminal screws tight and wires undamaged?</summary>
<div class="dtree-body"><strong>Yes:</strong> The problem is likely in parameter settings, a failed communication card, or the main control board.<br><strong>No:</strong> Re-terminate any loose or frayed wires and retest before replacing parts.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Disconnect power** to the drive and lock out the main breaker following proper electrical safety procedures.
2. **Inspect all control wiring** at the drive's terminal blocks, looking for loose screws, broken strands, or signs of overheating.
3. **Reseat any communication cards** or I/O expansion modules by removing and firmly re-inserting them into their slots.
4. **Restore power** and navigate the drive's keypad or HMI to the parameter menu; verify communication protocol, node address, and baud rate match your network or PLC settings.
5. **Perform a parameter reset** to factory defaults if settings are uncertain, then re-enter your application-specific parameters according to the drive manual.
6. **Test communication** by sending a simple command from the PLC or monitoring software to confirm handshake and data exchange.
7. **Replace the communication card or I/O module** if the fault persists and wiring and parameters are confirmed correct; consult ABB for the correct part number for your drive model and network type.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB fieldbus communication card | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0028-fault-code&k=ABB+fieldbus+communication+card&tag=errorcodefixes-20) \| Match the card type (Profibus, Modbus, EtherNet/IP, etc.) to your network; consult ABB for the exact part number for the ACS580. |
| ABB I/O expansion module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-vfd-e0028-fault-code&k=ABB+I%2FO+expansion+module&tag=errorcodefixes-20) \| Only needed if your application uses additional digital or analog I/O beyond the drive's standard terminals. |

## When to Call a Pro

Call a qualified industrial electrician or automation technician if you are not trained to work with three-phase power, variable frequency drives, or industrial networks. High-voltage work on VFDs requires lockout/tagout procedures and multimeter skills. Communication troubleshooting often demands familiarity with fieldbus protocols, PLC programming software, and drive parameter structures. If you have verified wiring and parameters but the fault remains, a technician with diagnostic tools and access to ABB technical support can isolate whether the issue lies in the communication card, main control board, or external network infrastructure.

**Rough cost:** A pro service call runs about $200-600.

## See Also

- [ABB ACS580 VFD E0037 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0037-fault-code/)
- [ABB ACS580 VFD E0011 Fault Code - Causes & Fix](/posts/abb-acs580-vfd-e0011-fault-code/)
- [ABB VFD Fault 2310 — Causes & Fix](/posts/abb-vfd-fault-2310/)
- [ABB ACS580 A5A0 Fault - Causes & Fix](/posts/abb-acs580-a5a0-fault-code/)
