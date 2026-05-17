---
title: "Lennox Error Code 414 — Gas Valve Circuit Fault Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-15T08:00:00Z
modDatetime: 2024-03-15T08:00:00Z
slug: lennox-error-code-414-gas-valve-circuit-fault
featured: false
draft: false
tags:
  - hvac
  - lennox
  - furnace
  - gas-valve
description: "Lennox error code 414 means a gas valve relay or circuit fault on G61, G71, and EL296 series furnaces — here's how to diagnose and fix it."
---

## Error Code: Lennox Error Code 414

**What it means:** Lennox error code 414 on G61MP, G71MP, EL296V, and related series furnaces indicates a gas valve relay fault. The control board detected either a stuck-open gas valve relay (voltage present at the valve when it should be off) or a failed relay that can't energize the valve. This is a safety-critical lockout — Lennox boards are designed to shut down immediately when they detect any gas valve circuit anomaly, because a valve that won't close is a gas leak waiting to happen.

Code 414 is stored in the furnace's fault history and displayed on the diagnostic LED array or the system's thermostat interface if you have an iComfort or EL-compatible thermostat.

## Common Causes

- **Failed gas valve relay on the control board** — The relay that switches 24VAC to the gas valve coil wears out over time, especially in systems with frequent short-cycling. The relay contacts fuse or fail open.
- **Shorted or open gas valve coil** — The valve's internal solenoid can develop a short to ground or open circuit, which the board reads as a relay/circuit fault rather than a valve fault specifically.
- **Wiring issue between board and valve** — A chafed, burnt, or corroded wire in the W-to-valve circuit can cause intermittent opens or shorts that trigger 414.
- **Control board internal fault** — If the relay driver transistor on the board fails, it can generate 414 even with a known-good gas valve.
- **Miswiring after service** — If the furnace was recently serviced, a valve wire reinstalled on the wrong terminal can cause this code immediately.

## Step-by-Step Fix {#step-by-step-fix}

1. **Shut off gas and power before any inspection.** Turn the gas shutoff valve to OFF (handle perpendicular to pipe). Turn off the furnace power switch. Wait 5 minutes for residual gas to clear before opening the cabinet.

2. **Retrieve the fault history.** On Lennox G61/G71/EL296 units with the SureLight control board, hold the diagnostic button for 3 seconds to scroll through stored codes. Confirm 414 is present and note whether any other codes precede it (a 223 inducer fault preceding a 414 tells a different story than a standalone 414).

3. **Inspect the gas valve wiring harness.** Locate the gas valve (it's the brass body with two electrical terminals on the inlet side of the burner manifold). Check both wire terminals for corrosion, burning, or loose connections. The two leads are typically red and blue on Lennox units. Tug each connector firmly — it should not pull off without deliberate effort.

4. **Measure gas valve coil resistance.** Disconnect both wires from the valve terminals and measure resistance across the valve terminals with a multimeter. A healthy Lennox gas valve coil reads approximately 40–70 ohms. Open circuit (OL) = failed valve. Short to ground (near zero ohms between terminal and valve body) = failed valve. Either reading justifies valve replacement.

5. **Check for 24VAC at the valve during a call for heat.** With the wiring reconnected, restore power and gas, set the thermostat to call for heat, and measure AC voltage at the gas valve terminals during the ignition sequence. You should see 24VAC appear briefly after the igniter heats up and the pressure switch closes. No voltage = board relay failure. Voltage present but no flame = bad valve. This test requires a helper to watch the LED sequence while you measure.

6. **Replace the control board if voltage is absent.** The Lennox SureLight control board part number **51M33** covers a wide range of G61/G71/EL296 units (verify against your model label — Lennox uses multiple board revisions). Boards run $220–$280.

7. **Replace the gas valve if coil is failed.** Lennox gas valve part number **1171688** is the standard replacement for most G61/G71 series. Gas valve replacement requires a licensed contractor in most jurisdictions — the gas line must be disconnected and reconnected, which requires leak testing with a manometer.

8. **Clear fault history and test.** After repair, hold the diagnostic button for 5+ seconds to clear stored faults, then run a full heat cycle and confirm normal operation through two consecutive heat calls.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|---------------|
| Lennox Gas Valve | 1171688 | $140–$165 | [Amazon](https://www.amazon.com/dp/B0015KAHHA?ascsubtag=ecf-lennox-error-code-414-gas-valve-circuit-fault&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=1171688) |
| Lennox SureLight Control Board | 51M33 | $220–$275 | [Amazon](https://www.amazon.com/dp/B0CNZGZ1HS?ascsubtag=ecf-lennox-error-code-414-gas-valve-circuit-fault&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=51M33) |
| Wiring Harness (if burnt) | — | $40–$80 | [Lennox dealer](https://www.lennox.com/dealers) |

## When to Call a Professional

Gas valve replacement is not a DIY repair in most states. Disconnecting a gas line requires a licensed contractor in jurisdictions that enforce local mechanical codes, and the work must be leak-tested before the system is returned to service. If your 414 code points to a gas valve failure, call a licensed HVAC contractor — the gas valve itself is inexpensive, but the labor and leak test are required steps, not optional ones. Control board replacement is generally within the skill set of a competent DIYer with electrical troubleshooting experience, but don't replace the board before confirming the gas valve and wiring are healthy — you'll spend $250 and still have a 414 code.

> **Pro tip:** Lennox 414 codes that appear only on the first heat call of the day (and clear after a manual reset) often indicate a gas valve that's sticking closed due to debris in the valve seat — not a relay fault at all. Ask your tech to check inlet gas pressure and run the valve through several cycles before condemning either the board or the valve.

## Related Articles

- [Lennox Error Code 292 — Ignition Failure Fix](/posts/lennox-292-error-code/)
- [Lennox EL296V Error Codes — Variable-Speed Furnace Diagnostic Guide](/posts/lennox-el296v-error-codes/)
- [Lennox Elite Series Furnace Error Codes — Fault Code Diagnostic Guide](/posts/lennox-elite-series-furnace-codes/)
- [Lennox 103 Error Code — Causes & Fix](/posts/lennox-error-code-103/)
- [Lennox Error Code 111 — Causes & Fix](/posts/lennox-error-code-111/)
