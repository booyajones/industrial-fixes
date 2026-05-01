---
title: "Goodman 3 Flash Error Code — Pressure Switch Stuck Open Fix"
author: "Industrial Error Code Fixes"
pubDatetime: 2024-03-11T08:00:00Z
modDatetime: 2024-03-11T08:00:00Z
slug: goodman-3-flash-error-code
featured: false
draft: false
tags:
  - hvac
  - goodman
  - furnace
  - pressure-switch
  - inducer
description: "Goodman 3 flash error code means the pressure switch is stuck open. This guide covers every cause and fix for the 3-blink fault on Goodman, Amana, and Daikin furnaces."
---

## Error Code: Goodman 3 Flashes

**What it means:** Three flashes on a Goodman furnace diagnostic LED indicates the pressure switch is stuck in the open position. Goodman uses a 2-second pause followed by rapid blinks to communicate fault codes — three blinks, pause, three blinks. The same code applies to Amana and Daikin-branded furnaces built on the Goodman platform.

The pressure switch is a safety device that verifies the inducer motor is generating adequate negative pressure (draft) before allowing the gas valve to open. When the switch is stuck open — meaning it never closes and signals "safe to ignite" — the board refuses to start the burners. This protects against carbon monoxide buildup from a blocked flue or failed inducer.

## Common Causes

- **Blocked or overflowing condensate drain** — High-efficiency (90%+) furnaces produce condensate. If the condensate drain line is clogged or the trap is full, water backs up into the pressure switch hose port and holds the switch open. This is the most common cause of 3-flash codes on 90%+ furnaces.
- **Cracked or disconnected pressure switch hose** — The small rubber hose connecting the inducer housing to the pressure switch can crack, collapse, or pull free. Any air leak in this hose prevents the switch from seeing correct negative pressure.
- **Failed inducer motor** — If the inducer isn't spinning fast enough (worn bearings, failed capacitor, weak motor), it can't generate enough negative pressure to close the pressure switch. The motor may run but sound labored or vary in speed.
- **Failed pressure switch** — The diaphragm inside the switch can crack or the electrical contacts can fail. A failed switch stays open regardless of the pressure being applied.
- **Blocked flue or intake pipe** — A bird nest, ice dam, or debris in the PVC flue or combustion air intake restricts airflow and starves the inducer of the pressure differential it needs to close the switch.

## Step-by-Step Fix {#step-by-step-fix}

1. **Check the condensate drain first.** On 90%+ furnaces, locate the condensate trap (typically a clear plastic J-trap or U-trap on the side of the furnace cabinet). Look for standing water or blockage. Pour water into the drain and confirm it flows freely. If blocked, use a wet/dry vacuum on the drain line outlet to clear the clog. This resolves roughly 40% of 3-flash codes on high-efficiency Goodman furnaces.

2. **Inspect all condensate hoses and pressure switch hoses.** With the furnace off, trace the small-diameter rubber tubes from the inducer housing to the pressure switch. Look for cracks, kinks, or loose connections at either end. Squeeze the hose along its length — a collapsed or cracked hose won't spring back properly. Replace any suspect hose with matching diameter rubber tubing from a hardware store.

3. **Verify the inducer motor is running.** With power restored and a call for heat active, listen for the inducer to start first — it should spin up before anything else happens. A healthy inducer sounds smooth and consistent. If you hear grinding, vibration, or the motor struggles to reach speed, suspect a failing inducer capacitor (cheap fix, ~$10) or a worn inducer motor.

4. **Test the inducer capacitor.** Shut off power. Locate the small oval capacitor on or near the inducer motor. Use a capacitor tester or a multimeter with capacitance function to test it against the rated value printed on the capacitor (typically 3–7 µF for Goodman inducers). A reading more than 10% below rated value means the capacitor needs replacement.

5. **Test the pressure switch with a manometer or hand pump.** Disconnect the hose from the pressure switch inlet. Using a hand vacuum pump or your mouth (gently), apply negative pressure to the switch port. You should hear a distinct click and see continuity on a multimeter across the switch terminals when sufficient vacuum is applied. No click = failed switch.

6. **Check the flue and intake pipes outside.** Go outside and visually inspect the white PVC pipes exiting the building. Look for bird nests, wasp nests, ice, leaves, or any blockage. Both the flue pipe and the combustion air intake must be completely clear. On windy days, check that the pipe terminations aren't too close together or too close to a wall — recirculated exhaust can back-pressure the system.

7. **Replace the pressure switch if all else checks out.** The Goodman pressure switch **B1370112** fits most GMSS, GMEC, and AMVC series furnaces (~$35 at Repair Clinic). Confirm the switch rating (typically -0.65 in. W.C. or -0.45 in. W.C.) matches the original before ordering.

8. **Run the furnace through three complete heat cycles** after any repair to confirm the 3-flash code is resolved.

## Parts That May Need Replacement {#parts-that-may-need-replacement}

| Part | Part Number | Typical Cost | Where to Buy |
|------|------------|-------------|---------------|
| Pressure switch | B1370112 | $30–$45 | [Amazon](https://www.amazon.com/dp/B013J2J97A?tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=B1370112) |
| Inducer motor capacitor | B175-1068 | $8–$15 | [Amazon](https://www.amazon.com/s?k=Goodman+B175-1068+inducer+capacitor&tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=B175-1068) |
| Inducer motor assembly | B1859005 | $120–$180 | [Amazon](https://www.amazon.com/dp/B00FDZ90B2?tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=B1859005) |
| Condensate drain trap | B1787419 | $12–$20 | [Amazon](https://www.amazon.com/dp/B077J4Y763?tag=errorcodefixes-20) \| [RepairClinic](https://www.repairclinic.com/Search/SearchResult?searchterm=B1787419) |

## When to Call a Professional

If the pressure switch, inducer motor, and condensate drain all check out and the 3-flash code persists, the problem may be inside the heat exchanger — a cracked secondary heat exchanger can upset combustion airflow in ways that prevent the pressure switch from closing. Cracked heat exchanger diagnosis requires combustion analysis equipment and should be performed by a licensed HVAC technician. A cracked heat exchanger also poses a carbon monoxide risk and should be treated as a safety issue, not just a repair issue.

> **Pro tip:** Before buying a new pressure switch, take off the hose and blow through the switch port — you should feel resistance and hear a click when vacuum is applied. If you can blow freely with no click, the diaphragm is already blown and the switch is trash. This 10-second test saves the round trip of installing a new switch only to find the real problem was the inducer.

## See Also

- [Goodman Furnace E3 Error Code — Draft Motor Fault](/posts/goodman-furnace-e3-error-code/)
- [Goodman 1 Flash Error Code — What It Means](/posts/goodman-1-flash-error-code/)
- [Goodman ComfortNet Communicating System Error Codes — Complete Guide](/posts/goodman-communicating-error-codes/)
- [Amana / Goodman Furnace 3 Flash Error Code — Causes & Fix](/posts/goodman-amana-furnace-3-flash/)

## Related Articles

- [Goodman 1 Flash Error Code — What It Means](/posts/goodman-1-flash-error-code/)
- [Goodman 2 Flash Error Code — Causes & Fix](/posts/goodman-2-flash-error-code/)
- [Goodman 4 Flash Error Code — Causes & Fix](/posts/goodman-4-flash-error-code/)
- [Goodman 5 Flash Error Code — Causes & Fix](/posts/goodman-5-flash-error-code/)
- [Goodman 6 Flash Error Code — Rollout Switch Open Fix](/posts/goodman-6-flash-error-code/)
