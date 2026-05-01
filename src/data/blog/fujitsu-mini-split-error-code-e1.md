---
title: "Fujitsu Mini Split E1 Error Code — Causes & Fix"
description: "What Fujitsu E1 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "Marcus Webb"
featured: false
draft: false
tags:
  - mini-split
  - fujitsu
---

## Fujitsu Mini Split E1 Error Code — What It Means

Fujitsu error code E1 (displayed as "E:01" on the remote or flashed on the unit) indicates an outdoor unit communication fault — the indoor unit is not receiving valid communication signals from the outdoor unit. Fujitsu uses a two-wire serial communication bus between indoor and outdoor units. When the indoor PCB detects no valid signal from the outdoor board for a set time period, it triggers E1 and shuts the system down. This fault is common after power interruptions, during installation, and when control wiring has been compromised.

[Jump to Fix](#fix)

## Common Causes

- **Miswired or loose communication terminals** — Fujitsu connects indoor and outdoor units with a 3-wire cable (L1, L2, and S/communication). If the S wire is loose, disconnected, or swapped with a power terminal, E1 appears immediately.
- **Blown fuse on the outdoor PCB** — Fujitsu outdoor boards have a small fuse protecting the control circuit. A power surge or wiring fault can blow this fuse, cutting communication.
- **Failed outdoor PCB** — If the outdoor control board has failed (power surge, moisture ingress, component failure), it stops transmitting communication signals and the indoor unit faults with E1.
- **Power interruption to outdoor unit** — If the outdoor unit lost power while the indoor unit is still powered, the indoor unit logs E1. Verify both units are receiving power.

## Step-by-Step Fix {#fix}

1. **Verify power to both units** — Check that the outdoor unit has power at its disconnect. Listen for the contactor clicking or any fan activity. If the outdoor unit has no power, check the disconnect fuse or breaker.
2. **Inspect communication wiring** — At both the indoor and outdoor PCBs, check the S terminal (communication wire, typically different in color from power leads). Confirm it's seated, not oxidized, and correctly landed.
3. **Check the outdoor PCB fuse** — On the outdoor PCB, locate the small blade or glass fuse. Test for continuity. If blown, replace with the same rated fuse. A blown fuse that keeps blowing indicates a short in the communication circuit.
4. **Power cycle both units simultaneously** — Cut power at the breaker serving both units for 5 minutes. Restore and let the system initialize. Some E1 faults clear after a full power cycle.
5. **Reset the system** — After verifying wiring and power, cycle the breaker and observe. If E1 clears and the unit runs a cooling or heating cycle, the fault was transient.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Outdoor PCB | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| The most common board failure for persistent E1; Fujitsu part number is model-specific |
| Fuse (for outdoor PCB) | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?tag=errorcodefixes-20) \| Typically 6.3A or 10A; check the PCB silkscreen for rating |
| Communication cable (shielded 3-conductor) | [Amazon](https://www.amazon.com/s?k=Communication+cable+%28shielded+3-conductor%29&tag=errorcodefixes-20) \| Replace if damaged; 18 AWG minimum |
## When to Call a Pro

If wiring is confirmed correct and both units have power, but E1 persists, a Fujitsu-authorized technician should diagnose the PCBs with manufacturer-specific test procedures. Replacing the wrong board is an expensive mistake.

## Related Articles

- [Bosch Heat Pump E1 Error Code — Causes & Fix](/posts/bosch-heat-pump-e1-error-code/)
- [Carrier 24ANA Heat Pump Error Codes — Performance Series Diagnostic Guide](/posts/carrier-24ana-heat-pump-error-codes/)
- [Carrier Heat Pump E1 Error Code — Causes & Fix](/posts/carrier-heat-pump-e1-error-code/)
- [Carrier Heat Pump E4 Error Code — Causes & Fix](/posts/carrier-heat-pump-e4-error-code/)
- [Carrier Heat Pump E5 Error Code — Defrost Fault: Causes & Fix](/posts/carrier-heat-pump-e5-error-code/)
