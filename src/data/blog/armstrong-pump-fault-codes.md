---
title: "Armstrong Pump Fault Codes: Complete Guide"
description: "Armstrong pump fault codes and error diagnostics. Design Envelope pump fault codes, causes, and technician-level troubleshooting."
pubDatetime: 2026-04-22T23:45:00Z
modDatetime: 2026-05-01T08:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - pumps
  - armstrong
  - hvac
  - industrial
---

# Armstrong Pump Fault Codes

Armstrong Design Envelope pumps with integrated VFD and Pump Manager controls display fault codes on the integrated display. Armstrong's IPS (Intelligent Pump System) adds cloud diagnostics. For pumps with external drives, refer to the VFD fault codes (typically ABB or Danfoss).

## Armstrong Design Envelope Fault Code Table

| Code | Fault Description | Common Cause | Action |
|------|------------------|--------------|--------|
| F01 | Motor overcurrent | Motor overload or winding fault | Check motor amps and winding |
| F02 | Drive overtemperature | High ambient or blocked cooling | Clean fins, check fan |
| F03 | Motor overtemperature | Motor thermal limit | Check motor cooling and load |
| F04 | Undervoltage | Low supply voltage | Check supply voltage |
| F05 | Overvoltage | Supply voltage high | Check voltage supply |
| F06 | Input phase loss | Missing supply phase | Check input fuses and supply |
| F07 | Ground fault | Winding or cable insulation fault | Megger test motor |
| F08 | Communication fault | BAS or Bluetooth loss | Check BAS wiring |
| F09 | Sensor fault | Pressure sensor failure | Check sensor wiring and calibration |
| F10 | Low flow warning | Flow below minimum | Check system valves and demand |
| F11 | Pump blocked | Impeller jam | Check for debris in casing |
| F12 | Dry run | No water detected | Check system pressure and fill |

## Most Common Armstrong Faults

### F01 — Motor Overcurrent
Armstrong Design Envelope pumps are sized for specific system curves. If system resistance increases (closed balancing valve, clogged strainer), current increases. Check system strainer (typically Y-strainer on pump inlet) — clean if dirty. Verify pump impeller diameter matches design conditions.

### F02 — Drive Overtemperature
The integrated VFD must have adequate airflow. Armstrong Design Envelope pumps should be installed with a minimum 6-inch clearance above and below the drive section. In hot mechanical rooms, add auxiliary cooling if ambient exceeds 40°C.

### F09 — Sensor Fault
Armstrong Design Envelope uses differential pressure sensors for automatic control. Check sensor tubing for blockage or air locks. Verify 4–20 mA signal at controller. Clean sensor pressure ports if system has debris.

### F12 — Dry Run
System water pressure below minimum triggers dry run protection. Check fill pressure (minimum 12 PSI for closed hydronic systems). Check for open drain valves or system leaks.

## Parts Commonly Needed

| Part | Notes |
|------|-------|
| Drive assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-armstrong-pump-fault-codes&k=Drive+assembly&tag=errorcodefixes-20) \| Armstrong-specific VFD — contact Armstrong |
| Pressure sensor | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-armstrong-pump-fault-codes&k=Pressure+sensor&tag=errorcodefixes-20) \| Differential pressure transducer |
| Motor seal kit | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-armstrong-pump-fault-codes&k=Motor+seal+kit&tag=errorcodefixes-20) \| Annual replacement on higher-flow models |
| Impeller | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-armstrong-pump-fault-codes&k=Impeller&tag=errorcodefixes-20) \| Match pump model and size |
| Y-strainer basket | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-armstrong-pump-fault-codes&k=Y-strainer+basket&tag=errorcodefixes-20) \| Clean or replace — prevents F11 and F12 |
> **Pro tip:** Armstrong Design Envelope pumps with Pump Manager technology log operational data. Register the pump with Armstrong Fluid Technology's cloud portal for remote monitoring, fault alerts, and efficiency trending accessible from any browser.
