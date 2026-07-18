---
title: "Weil-McLain E04 Error Code: Power Lost After Lockout Fix"
description: "Weil-McLain E04 means power was lost after a lockout, usually unstable voltage. See real causes, the Ultra fault-code list, and how to clear it."
pubDatetime: 2026-04-22T12:00:00Z
modDatetime: 2026-04-22T12:00:00Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Supply thermistor (S1)"
most_likely_cause: "Failed supply or return thermistor"
---

## Weil-McLain E04 Error Code — What It Means

Weil-McLain E04 indicates a **temperature sensor fault** — one of the boiler's thermistors (supply, return, or DHW sensor depending on the model) is reading outside its valid range. On Weil-McLain ultra and gas-fired condensing boilers, the control monitors multiple temperature points; an open or shorted sensor on any one of them triggers E04 and shuts down the boiler to prevent uncontrolled operation. The specific sensor that failed can often be identified by consulting the boiler's display history or service menu.

[Jump to Fix](#fix)

## Common Causes

- **Failed supply or return thermistor** — The most common cause; thermistors fail open or short after years of thermal cycling.
- **Loose sensor well connection** — The thermistor bulb may have backed out of the immersion well, losing contact with the water and reading ambient air temperature.
- **Corroded connector** — Moisture in the boiler room causes corrosion at the thermistor connector pins, increasing resistance past the valid range.
- **PCB thermistor input failure** — Uncommon, but the board's input circuit for one sensor can fail while others remain functional.

## Step-by-Step Fix {#fix}

1. **Read the fault history** — Access the boiler's diagnostics menu (consult your model's installation manual). Identify which sensor is flagged: supply (S1), return (S2), or DHW (S3). This narrows your search immediately.
2. **Inspect the sensor immersion well** — The thermistor probe inserts into a brass or stainless well in the water-side piping. Confirm the probe is fully seated and the mounting nut is tight. A partially withdrawn probe reads air temp.
3. **Check the connector** — Disconnect the sensor connector at the boiler control. Inspect for corrosion, pushed-out pins, or moisture. Clean with contact cleaner.
4. **Measure thermistor resistance** — Disconnect the sensor and measure resistance at room temperature (~70°F/21°C). Weil-McLain thermistors typically read ~10 kΩ at 77°F (25°C). Consult your model's table for exact specs. Out-of-range = replace.
5. **Replace the thermistor** — Drain the relevant section of piping (or the boiler if required), remove the immersion well thermistor, install the new sensor, and tighten to the specified torque.
6. **Reset and verify** — Power cycle the boiler (off for 30 seconds) and fire it through a complete heating cycle. Confirm E04 is cleared and supply/return temps display correctly on the control.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Supply thermistor (S1) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-e04-error-code&k=Supply+thermistor+%28S1%29&tag=errorcodefixes-20) \| Weil-McLain model-specific; verify for Ultra vs. Gold/CGa series |
| Return thermistor (S2) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-e04-error-code&k=Return+thermistor+%28S2%29&tag=errorcodefixes-20) \| Match immersion well length and resistance spec |
| DHW sensor (S3) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-e04-error-code&k=DHW+sensor+%28S3%29&tag=errorcodefixes-20) \| Only on combi models with domestic hot water capability |
## When to Call a Pro

If sensor replacement doesn't clear E04, the boiler control board may have a failed input. Weil-McLain control board replacement on condensing boilers requires proper setup and parameter configuration — have a licensed heating contractor handle board replacement to ensure the boiler is commissioned correctly.

## Related Articles

- [American Water Heater Error Codes — Complete Guide](/posts/american-water-heater-error-codes/)
- [AO Smith Water Heater 3 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-3-flashes/)
- [AO Smith Water Heater 4 Flashes — What It Means and How to Fix It](/posts/ao-smith-water-heater-4-flashes/)
- [A.O. Smith Water Heater Error Codes Guide](/posts/ao-smith-water-heater-error-codes/)
- [Bradford White Water Heater Error Code 1 — Pilot Outage Fix](/posts/bradford-white-error-code-1/)

## See Also

- [Weil-McLain Boiler Error Code E01 — Lockout Fix](/posts/weil-mclain-e01-error-code/)
- [Weil-McLain Boiler Error Code E10 — Low Water Pressure Fix](/posts/weil-mclain-e10-low-pressure/)
- [Weil-McLain E02 Error Code — Causes & Fix](/posts/weil-mclain-e02-error-code/)
- [Weil-McLain Boiler Error Code E10 — Causes & Fix](/posts/weil-mclain-e10-error-code/)

## More Weil Mclain E04 Error Code fault codes

Compiled from manufacturer service manuals and authorized documentation.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| E03 | Internal control failure. | Fault detected inside the boiler control module. | Power-cycle once; if E03 returns, the control board typically needs service or replacement by a licensed contractor. |
| E12 | External limit open (a device wired into the hard-lockout / limit circuit is open). | Tripped external high-limit, LWCO, or other safety wired in series; broken wire in that circuit. | Check and reset the external limit devices and verify the limit-circuit wiring is intact. Do not jumper safeties. |
| E18 | Outlet (supply) water temperature exceeded 210 deg F. | Low flow, air-bound system, closed valve, seized/failed circulator, or fouled heat exchanger. | Purge air, confirm the circulator runs and isolation valves are open, verify adequate flow, and check the heat exchanger for scale. |
| E19 | Return water temperature exceeded 210 deg F. | Same low-flow / no-flow conditions affecting the return side. | Restore proper system flow (circulator, valves, air) and confirm return sensor reads correctly. |
| E25 | Temperature rise greater than 58 deg across the boiler. | Insufficient flow through the heat exchanger (weak/failed pump, partial blockage, air). | Verify circulator output and system flow; purge air and clear any restriction so delta-T stays in range. |
| E28 | No signal from the blower. | Failed blower, disconnected blower wiring/tach, or control-to-blower communication loss. | Check blower power and wiring harness; if the blower will not run or report speed, it usually needs replacement. |
| E31 | Outlet (supply) temperature sensor shorted. | Shorted supply thermistor or pinched/chafed sensor wiring. | Inspect and ohm the supply sensor against the resistance table; replace if shorted. |
| E32 | Return temperature sensor shorted. | Shorted return thermistor or damaged wiring. | Ohm the return sensor against spec and replace if out of range. |
| E36 | Outlet (supply) temperature sensor open. | Open supply thermistor, disconnected connector, or broken lead. | Reseat the connector, check for a broken wire, and replace the supply sensor if the circuit reads open. |
| E37 | Return temperature sensor open. | Open return thermistor, loose connector, or broken lead. | Reseat/inspect the connector and replace the return sensor if the circuit reads open. |
| E52 | Flue temperature exceeded 225 deg F. | Fouled/scaled heat exchanger, low flow, or flue restriction driving flue temp high. | Inspect and clean the heat exchanger and flue path and restore proper water flow. |


## How to troubleshoot Weil Mclain E04 Error Code

## How to actually diagnose Weil-McLain E04

E04 is a power-quality lockout, not a broken component. It means the boiler was already in a hard lockout when incoming 120V power was interrupted or fluctuated. On restart the control cannot recover the original fault, so it posts E04 and the code that actually shut the boiler down is erased. Treat E04 as a clue: something else locked the boiler out, then the power blinked.

**Work it in this order:**

1. **Restore and verify clean power first.** Confirm stable 120V at correct polarity (hot and neutral not reversed) with a solid ground. Loose terminal-block connections, a shared circuit with a large intermittent load, utility brownouts, or an undersized generator/UPS all trigger E04.

2. **Reset once and watch what returns.** Because the original code was lost, the useful signal is the fault that reappears. If it locks out again, read that new code (ignition, high-limit, blower, or sensor) and chase that, not E04.

3. **Look for a pattern.** E04 that recurs after storms, at a set time of day, or whenever a large appliance cycles points to the building's electrical supply, not the boiler. A dedicated grounded circuit, a line-voltage monitor, or a UPS is the durable fix, and Weil-McLain offers an incoming-power time-delay relay to let voltage stabilize before the control energizes.

**Safety and scope.** Line-voltage wiring, polarity/ground correction, and control-board work belong to a licensed heating contractor. A homeowner can safely confirm the outlet is live and correctly wired, reset once, and note the recurring code. If a real fault keeps returning on known-good power, call a pro rather than repeatedly resetting a boiler that is trying to protect itself.


## Frequently asked questions

### Does E04 mean my Weil-McLain temperature sensor is bad?

No. On the Weil-McLain Ultra, E04 means voltage was lost after a lockout already occurred, not a sensor failure. The genuine temperature-sensor codes are E31, E32, E36, and E37 (and E13/E14 on the original Ultra). If you are chasing a sensor, look at those codes, not E04.

### Why does E04 keep coming back after I reset the boiler?

Two reasons. Either the underlying fault that first locked the boiler out is still present and it re-locks, or your incoming power is unstable and keeps dropping during a lockout. Reset once, then read the code that reappears. If the power itself is flaky (brownouts, a generator, a loose neutral), stabilize it with a dedicated circuit or UPS.

### Can I clear a Weil-McLain E04 myself?

You can safely press reset and run a cycle, and you can confirm the boiler's outlet is live and correctly wired. But correcting reversed polarity, a bad ground, or control-board wiring is line-voltage work for a licensed contractor. Do not jumper any safety to make a code go away.

### Will a UPS or time-delay relay stop E04 lockouts?

It helps when the cause is bad incoming power. Weil-McLain offers a time-delay relay (part 383-500-021) that lets voltage stabilize before the control powers up, and a UPS on the incoming feed rides through short utility glitches and brownouts. Neither fixes a genuine boiler fault, so still confirm the real recurring lockout code.

### The original lockout code disappeared after E04. How do I find what really failed?

That is expected: E04 erases the prior code. Reset the boiler and let it run until it either operates normally or locks out again, then read the new code. That code identifies the true problem (ignition, high-limit, blower, or sensor). E04 by itself only tells you power was interrupted mid-lockout.

