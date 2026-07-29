---
title: "Rational Service 25 Error: CleanJet Water Circulation Fault on SCC and iCombi (Causes and Step-by-Step Fix)"
description: "Service 25 on a Rational combi means the CleanJet water circulation check failed: the oven saw no water flow, or the jet never loaded the fan wheel. The OEM check list is water supply, pressure, rack position, hoses, pump and CDS sensor, in that order."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: rational-service-25-cleanjet-error
featured: false
draft: false
tags:
  - rational
  - combi-oven
  - commercial-kitchen
  - oven
most_likely_cause: "Water supply shut off or pressure too low during CleanJet"
money_part: "CleanJet circulation pump"
free_checks:
  - "Confirm the water shut-off valve feeding the oven is fully open and the site has normal water pressure"
  - "Check that the GN racks or mobile trolley are actually in the cabinet before starting CleanJet"
  - "Inspect the visible hoses in the CleanJet circulation path for kinks, pinches, or debris"
---

## What this code means

Service 25 on a Rational combi oven is a CleanJet water circulation fault. During a CleanJet cleaning cycle the machine circulates water through the cooking cabinet and directs it at the fan wheel. Service 25 means that self-check failed: the control either detected no water flow in the CleanJet circuit, or it never saw the water jet load the spinning fan wheel.

The display wording depends on which generation you are standing in front of, but the fault family has been the same since the 2004 SCC line. Taken from the OEM service references:

| Series | How the OEM service reference words Service 25 |
|---|---|
| iCombi Pro / iCombi Classic | "Fan wheels not running/no increase in performance at the fan motor when water jet hits: Check the water supply, pressure, hoses, CDS sensor, position of GN conductors and mobile oven racks" |
| SelfCookingCenter whitefficiency (SCC WE) / CombiMaster Plus | "No water flow detected during CleanJet. Pump or circulation blocked by foreign particles, rack/trolley not in cabinet" |
| Legacy SCC / CombiMaster (2004-2011) | "CleanJet water circulation faulty, water doesn't hit fan wheel. Check pump, foreign bodies in water pipe, racks / trolley must be inside cabinet" |

That wording difference matters for diagnosis. On the iCombi platform the control is watching the fan motor: when the water jet strikes the fan wheel, motor load should rise, and if no performance increase appears the oven concludes water never arrived. On the SCC WE platform the check is flow detection in the circulation circuit. Either way, the machine is telling you the same thing: water is not moving through the CleanJet path the way it should.

This is not an obscure code. General Parts, which describes itself as a Rational Certified Authorized Service Agent, lists Service 25 among the five Rational codes its technicians are called out for most, alongside Service 10, Service 12, Service 40 and gas RESET. It ranks that high because it strands the oven mid-clean, often with cleaner chemical still in the cabinet, right when the kitchen wants the machine back for the next shift.

## Common Causes

Every cause below is named directly in one or more of the OEM service references. Work them in order of likelihood and effort:

- **Water supply off or pressure too low.** The iCombi references open their Service 25 check list with exactly this: check the water supply and pressure. It is the most common and cheapest fix. A shut-off valve closed during a plumbing job, a clogged inlet strainer, or a site-wide pressure drop means CleanJet has nothing to circulate.
- **GN racks or trolley not positioned in the cabinet.** All three references name it. The legacy document is the most direct: "racks / trolley must be inside cabinet." Starting a clean with the rack pulled out, or with a trolley not fully seated, changes how water reaches the fan wheel and can trigger the fault on its own.
- **Blocked hoses or circulation path.** The iCombi check list names hoses explicitly. Grease, food debris and scale accumulate in the CleanJet hoses and fittings, and a kinked or clogged hose starves the circuit even with good supply pressure.
- **Foreign particles in the circulation pump.** The SCC WE reference says "pump or circulation blocked by foreign particles"; the legacy reference says "check pump, foreign bodies in water pipe." Bone fragments, labels, plastic wrap and tab wrappers all end up there. A partially jammed impeller moves too little water to satisfy the check.
- **CDS sensor fault.** Named last in the iCombi check list, and last for a reason. If the sensor the control relies on fails or reads wrong, the oven reports Service 25 even when water is actually moving.

## Step-by-Step Fix {#fix}

**Before you start.** If the CleanJet cycle aborted partway through, assume there is cleaner chemical in the cooking cabinet. Rational's own safety data sheet for its Cleaner Tab Active Green classifies the product Skin Corr. 1B with hazard statement H314, "Causes severe skin burns and eye damage," under the signal word "Danger," and adds H335, "may cause respiratory irritation." Wear chemical-resistant gloves and eye protection when you open the door or handle anything wet inside the cabinet, keep the area ventilated, and rinse the cabinet thoroughly before the oven goes back to cooking.

1. **Check the water supply first.** Confirm the shut-off valve feeding the oven is fully open. Check site water pressure and confirm nothing upstream changed: a backflow preventer serviced that morning, a partially closed valve after plumbing work, or a clogged inlet strainer. This is where the OEM check list starts, and it costs nothing to rule out.
2. **Confirm the rack or trolley is in place.** Verify the GN racks, or the mobile oven rack on trolley units, are properly positioned in the cabinet, then restart CleanJet. All three OEM references name this as a cause, and a fair number of Service 25 calls end right here.
3. **Clear the interrupted clean cycle properly.** Do not just kill power. Both platforms provide a documented short programme for exactly this: the SCC WE reference describes a CleanJet function test as "a short program (8-10 min) to reset CleanJet + Care errors or water shortage," and the iCombi Pro reference describes an iCareSystem module test as "a short programme (10-15 min) to reset iCareSystem errors." Both carry the same instruction: start it only after the cause of the error has been eliminated. If Service 110 or Service 120 is showing alongside, run the flush before any cooking. On the iCombi references those two codes explicitly mean a fault occurred while care chemical is in the steam generator.
4. **Inspect the circulation hoses and path.** With the oven isolated from power, trace the CleanJet circulation path. Look for kinked, pinched or clogged hoses and for debris or heavy scale at fittings. Clear and flush anything suspect.
5. **Check the circulation pump for foreign particles.** Isolate and lock out power first, then open the pump per the service documentation and look for debris jamming the impeller. Bone chips, packaging fragments and scale flakes are the usual finds. On the iCombi platform the circulation pump is designated M17 and carries its own code, Service 48 (-1 fault, -2 output too low). If that is logged alongside Service 25, the pump is the prime suspect.
6. **Test the CDS sensor and run function tests.** If supply, rack position, hoses and pump all check out, use the service-level diagnostics to function-test the CleanJet components and verify the CDS sensor responds. A failed sensor reports no circulation regardless of actual flow. Note the OEM's own warning that in a function test, components are not protected against overload.
7. **Verify with a full CleanJet cycle.** After any fix, run a complete clean cycle and watch it past the point where it previously faulted. An oven that faults at the same step every time is telling you the fault is still there.

### Electrical safety before you open anything

The iCombi Pro service reference carries an explicit warning that residual charge remains after shutdown: "Beware of electric shock, even when the unit is switched off," naming the I/O power supply (A10), the pump board (A13), the eSTB (A15/A16) and the solenoid valve block. Isolate the unit at the disconnect, lock out and tag out, and give those assemblies time to bleed down before opening a panel or the pump. If you are not qualified for commercial electrical work, stop at step 4 and call a technician who is.

## Parts Often Needed

| Part | Notes |
|------|-------|
| CleanJet circulation pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rational-service-25-cleanjet-error&k=Rational+CleanJet+circulation+pump&tag=errorcodefixes-20) \| Match to your model and serial number; iCombi designator M17. Genuine Rational parts via an authorized distributor are the safe route |
| Drain ball valve assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rational-service-25-cleanjet-error&k=Rational+combi+oven+drain+ball+valve&tag=errorcodefixes-20) \| For companion Service 26/27 faults on the same call |
| Water pressure test gauge | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rational-service-25-cleanjet-error&k=water+pressure+test+gauge&tag=errorcodefixes-20) \| Verify inlet supply pressure before condemning any part |

## When to Call a Pro

Call a Rational-certified technician when the water supply, rack position, hoses and pump all check out and the code persists. At that point you are into CDS sensor testing and service-mode function tests that require the service documentation and diagnostic access.

Also stop and call a pro any time you are not comfortable working around the cleaning chemical. An aborted CleanJet can leave a product that Rational itself labels as causing severe skin burns and eye damage sitting in the cabinet, and on codes 110 and 120 there is care chemical in the steam generator. On gas units, anything that requires opening the combustion side belongs to a licensed gas technician, not to a water-side troubleshooting session.

## Related Rational service codes on the same CleanJet call

Compiled from the OEM service references. These codes travel with Service 25: a drain valve that will not cycle, or a pump family fault, frequently shows up on the same service visit.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| Service 26 | Drain valve permanently closed (iCombi: ball valve does not open). | Seized or scale-jammed drain ball valve, or a failed valve motor. | Test the valve in the function test, free or descale the ball valve, and replace the assembly if it will not cycle. |
| Service 27 | Drain valve does not close during initialisation; the SCC WE reference notes the consequence: CleanJet without function. | Debris or scale in the valve seat, or a failed valve actuator. | Function-test the valve and clean the seat; replace if it will not seal. CleanJet stays out of action until this is fixed. |
| Service 46.x | iCombi SC pump (M4): -1 fault, -2 output too low. | Pump motor failure, blockage reducing output, or wiring fault. | Function-test the SC pump, clear any blockage, replace the pump if output stays low. |
| Service 47.x | iCombi waste water pump (M15): -1 fault, -2 output too low. | Pump motor failure, blockage, or wiring fault. | Function-test the waste water pump, clear the blockage, replace if output stays low. |
| Service 48.x | iCombi circulation pump (M17): -1 fault, -2 output too low. | Pump motor failure, foreign particles reducing output, or wiring fault. | Function-test the circulation pump and clear debris; replace if output stays low. Directly relevant to a Service 25 diagnosis. |
| Service 49.x | iCombi care pump (M18): -1 fault, -2 output too low. | Pump motor failure, blockage, or wiring fault. | Function-test the care pump, clear any blockage, replace if output stays low. |
| Service 110 | iCombi: SC pump fault while care chemical is in the steam generator. SCC WE and legacy: SC pump defective or level electrode calcified. | SC pump failure mid-clean, or a calcified level electrode. | Run the documented CleanJet/iCareSystem reset programme so the chemical is flushed, then repair the pump or electrode before returning the oven to cooking. |
| Service 120 | iCombi: level electrode without signal while care chemical is in the steam generator. SCC WE: Y1 or level electrode defective. Legacy: care pump M12 or level electrode defective. | Calcified or failed level electrode, or a failed fill valve, during a care cycle. | Flush the chemical via the reset programme, then replace the electrode or valve. |

## How to troubleshoot Rational Service 25

Treat Service 25 as a plumbing-and-flow problem before treating it as a parts problem. The check that trips it only runs during CleanJet, so the whole diagnosis centres on the cleaning-water circuit: supply in, circulation through the cabinet, jet onto the fan wheel, detection by the control.

Triage in this order:

- **Cheapest first.** Water valve open, site pressure normal, rack or trolley seated in the cabinet. This is the order the OEM check list itself uses, and a meaningful share of these calls close without a tool coming out.
- **Then the path.** Hoses, fittings and the circulation pump. Kitchens feed these ovens grease, wrappers and bone fragments daily, and the circulation circuit collects all of it.
- **Then detection.** Only after flow is proven good should you suspect the CDS sensor, and that step belongs with service-mode diagnostics.
- **Read the companion codes.** Service 26 and 27 (drain valve), 46.x to 49.x (the iCombi pump family) and 110/120 each narrow the fault to a specific component. An oven that logs a 48.2 next to Service 25 has already told you the circulation pump output is low.

Two safety rules override all of it. First, chemical: an aborted clean can leave a corrosive cleaner in the cabinet or care chemical in the steam generator, so wear gloves and eye protection, complete the documented flush routine, and rinse the cabinet before cooking. Second, electrical: isolate, lock out and tag out before opening the pump or any panel, and respect the OEM warning that several assemblies hold charge after the unit is switched off. On gas models, leave the combustion side to a licensed gas technician.

## Frequently asked questions

### Can I keep cooking after a Service 25 fault?

Not until the cabinet is verifiably free of cleaning chemical. Service 25 interrupts CleanJet, which means cleaner solution may still be sitting in the cooking cabinet, and Rational's safety data sheet classifies that product as causing severe skin burns and eye damage. Run the machine's documented reset and flush routine and rinse the cabinet thoroughly first. If Service 110 or 120 is also showing on an iCombi, care chemical is in the steam generator and the flush must complete before any cooking.

### Does Service 25 mean the same thing on an iCombi as on an older SCC?

Same fault family, different detection wording. The legacy SCC and SCC WE references describe it as CleanJet water circulation faulty, or no water flow detected. The iCombi references word it as no increase in performance at the fan motor when the water jet hits. The check list the OEM gives is essentially the same across generations: supply, pressure, rack position, hoses, pump, sensor.

### Why does Service 25 only ever appear during cleaning?

Because the check that generates it only runs during CleanJet. The oven verifies cleaning water is actually circulating and reaching the fan wheel. Outside a clean cycle that verification never happens, so a marginal hose blockage or a weak pump can hide for weeks and only announce itself on the overnight clean.

### Is Service 48.1 or 48.2 the same fault as Service 25?

They are related but distinct. On the iCombi platform, Service 48 points directly at the circulation pump M17, with -1 meaning a fault and -2 meaning output too low, while Service 25 reports that the circulation check itself failed. If both appear, start at the pump: the 48 code has already localised the problem for you.

### What is the CDS sensor?

It is the water-measuring sensor the control relies on, and it appears throughout these code tables. The iCombi Service 25 check list names it as the last item to test, and the iCombi Classic reference has a separate code, 1022, for no water detected during the switch-on routine "via CDS measurement." Testing it properly requires service-level diagnostics, which is one of the standard reasons this code ends in a call to a Rational-certified technician once the free checks come up clean.

## Sources

All service references below were retrieved and read in full. The keelingcatering.co.uk links are third-party mirrors of the Rational-published PDFs; each file's printed document number and edition date is given so you can match it against the copy on Rational's own service portal.

- RATIONAL Service Reference iCombi Pro, 80.51.872_SR-iCombi Pro_en-GB 05/2020 — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-iCombi-Pro-1.pdf
- RATIONAL Service Reference iCombi Classic, 80.51.885_ServiceReferenz_iCombi Classic_en-GB — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/80.51.855-ServiceReferenz-iCombi-Classic-en-GB-1.pdf
- RATIONAL Service Reference SelfCookingCenter whitefficiency / CombiMaster Plus, 80.51.720_SR_en 11/2017 — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCCWE-CM_P-1.pdf
- RATIONAL Service Reference SCC / CombiMaster 2004-2011, 80.51.028-A4 Edition 09/2008 — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCC-CM-1.pdf
- RATIONAL Cleaner Tab Active Green, Safety Data Sheet (Regulation (EC) No. 1907/2006) — https://www.rational-online.com/media/downloads/en-sg/cleaning/sdb-rational-reiniger-tab-activegreen-kick-en-r2.pdf
- General Parts (Rational Certified Authorized Service Agent) — Top 5 Rational Error Codes — https://generalparts.com/top-5-rational-error-codes-and-what-they-mean-to-you/
