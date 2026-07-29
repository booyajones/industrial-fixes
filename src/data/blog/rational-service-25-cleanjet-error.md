---
title: "Rational Service 25 Error: CleanJet Water Circulation Fault on SCC and iCombi (Causes and Step-by-Step Fix)"
description: "Service 25 on a Rational combi means the CleanJet water circulation check failed — the oven never saw water flow or the jet never hit the fan wheel. Check the water supply, rack position, hoses, circulation pump, and CDS sensor in that order before condemning parts."
pubDatetime: 2026-07-28T08:00:00Z
modDatetime: 2026-07-28T08:00:00Z
author: "Error Code Fixes Editorial Team"
slug: rational-service-25-cleanjet-error
featured: false
draft: true
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

Service 25 on a Rational combi oven is a CleanJet water circulation fault. During a CleanJet cleaning cycle, the machine circulates water through the cooking cabinet and directs it at the fan wheel. Service 25 means that self-check failed: the control either detected no water flow in the CleanJet circuit, or it never saw the water jet actually hit the spinning fan wheel.

The exact display wording depends on which generation you are standing in front of, but the underlying fault family has been the same since the 2004 SCC line:

| Series | How the OEM service reference words Service 25 |
|---|---|
| iCombi Pro / iCombi Classic | Fan wheels not running / no performance increase at the fan motor when the water jet hits |
| SelfCookingCenter whitefficiency (SCC WE) / CombiMaster Plus | No water flow detected during CleanJet |
| Legacy SCC / CombiMaster (2004–2011) | CleanJet water circulation faulty — water doesn't hit the fan wheel |

That wording difference matters for diagnosis. On the iCombi platform the control is watching the fan motor: when the water jet strikes the fan wheel, motor load should rise, and if no performance increase appears the oven concludes water never arrived. On the SCC WE platform the check is flow detection in the circulation circuit. Either way, the machine is telling you the same thing: water is not moving through the CleanJet path the way it should.

This is not an obscure code. General Parts, an authorized national service company, lists Service 25 among the handful of Rational codes technicians actually get called out for — alongside Service 10, Service 12, Service 40, and gas RESET events. It ranks that high because it strands the oven mid-clean, often with cleaner chemical still in the cabinet, right when the kitchen wants the machine back for the next shift.

## Common Causes

Per the OEM service references, work these in order of likelihood and effort:

- **Water supply off or pressure too low.** The most common and cheapest fix. A shut-off valve that got closed during a plumbing job, a clogged inlet strainer, or a site-wide pressure drop means CleanJet has nothing to circulate.
- **GN racks or trolley not positioned in the cabinet.** CleanJet expects the hinging rack or mobile oven rack in place during cleaning. Starting a clean with the rack pulled out, or with a trolley not fully seated, disrupts how water reaches the fan wheel and can trigger the fault.
- **Blocked hoses or circulation path.** Grease, food debris, and scale accumulate in the CleanJet hoses and fittings. A kinked or clogged hose starves the circuit even with good supply pressure.
- **Foreign particles in the circulation pump.** Bone fragments, labels, plastic wrap, and tab wrappers end up in the pump. A partially jammed impeller moves too little water to satisfy the check.
- **CDS sensor fault.** If the sensor the control relies on to detect CleanJet water circulation fails or reads wrong, the oven reports Service 25 even when water is actually moving.

## Step-by-Step Fix {#fix}

Before you start: if the CleanJet cycle aborted partway through, assume there is cleaner chemical in the cooking cabinet. Rational cleaner tabs are caustic. Wear chemical-resistant gloves and eye protection when you open the door or handle anything wet inside the cabinet, and rinse the cabinet thoroughly before the oven goes back to cooking.

1. **Check the water supply first.** Confirm the shut-off valve feeding the oven is fully open. Check the site's water pressure and confirm nothing upstream changed — a backflow preventer serviced that morning, a partially closed valve after plumbing work, or a clogged inlet strainer. This is the single most common cause, and it costs nothing to rule out.
2. **Confirm the rack or trolley is in place.** Verify the GN racks (or the mobile trolley on trolley units) are properly positioned in the cabinet, then restart CleanJet. An empty cabinet or an unseated trolley is a legitimate trigger for this code, and plenty of Service 25 calls end here.
3. **Clear the interrupted clean cycle properly.** Let the machine run whatever abort or rinse routine it offers rather than just killing power. If Service 110 or Service 120 appears alongside — both mean a fault occurred while care chemical is in the steam generator — completing the abort/rinse programme so the chemical is flushed out is mandatory before any cooking.
4. **Inspect the circulation hoses and path.** With the oven isolated from power, trace the CleanJet circulation path. Look for kinked, pinched, or clogged hoses and for debris or heavy scale at fittings. Clear and flush anything suspect.
5. **Check the circulation pump for foreign particles.** Lock out power, then open the pump per the service documentation and look for debris jamming the impeller — bone chips, packaging fragments, and scale flakes are the usual finds. On the iCombi platform the circulation pump carries the OEM designator M17, and it has its own fault codes (Service 48.1 for a pump fault, 48.2 for output too low); if those appear with Service 25, the pump is the prime suspect.
6. **Test the CDS sensor and run function tests.** If supply, rack position, hoses, and pump all check out, use the service-level diagnostics to function-test the CleanJet components and verify the CDS sensor responds. A failed sensor reports no circulation regardless of actual flow, and this is where a Rational-certified technician with service-mode access earns their fee.
7. **Verify with a full CleanJet cycle.** After any fix, run a complete clean cycle and watch it past the point where it previously faulted. An oven that faults at the same step every time is telling you the fault is still there.

## Parts Often Needed

| Part | Notes |
|------|-------|
| CleanJet circulation pump | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rational-service-25-cleanjet-error&k=Rational+CleanJet+circulation+pump&tag=errorcodefixes-20) \| Match to your model and serial number; iCombi designator M17. Genuine Rational parts via an authorized distributor are the safe route |
| Drain ball valve assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rational-service-25-cleanjet-error&k=Rational+combi+oven+drain+ball+valve&tag=errorcodefixes-20) \| For companion Service 26/27 faults on the same call |
| Water pressure test gauge | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-rational-service-25-cleanjet-error&k=water+pressure+test+gauge&tag=errorcodefixes-20) \| Verify inlet supply pressure before condemning any part |

## When to Call a Pro

Call a Rational-certified technician when the water supply, rack position, hoses, and pump all check out and the code persists — at that point you are into CDS sensor testing and service-mode function tests that require the service documentation and diagnostic access. Also stop and call a pro any time you are not comfortable working around the cleaning chemical: an aborted CleanJet can leave caustic solution in the cabinet and, on codes 110/120, care chemical in the steam generator. On gas units, anything beyond these water-side checks that requires opening the combustion side belongs to a licensed gas technician.

## Related Rational service codes on the same CleanJet call

Compiled from manufacturer service references and authorized documentation. These codes travel with Service 25 — a drain valve that will not cycle or a pump family fault frequently shows up on the same service visit.

| Code | What it means | Likely cause | How to fix |
| --- | --- | --- | --- |
| Service 26 | Drain/ball valve does not open (iCombi: ball valve does not open; SCC WE/legacy: drain valve permanently closed). | Seized or scale-jammed drain ball valve, or a failed valve motor. | Run the valve in the function test, free or descale the ball valve, and replace the assembly if it will not cycle. |
| Service 27 | Drain/ball valve does not close (SCC WE: doesn't close during initialisation — CleanJet without function). | Debris or scale in the valve seat, or a failed valve actuator. | Function-test the valve and clean the seat; replace if it will not seal. CleanJet stays disabled until this is fixed. |
| Service 46.x | iCombi SC pump (M4) fault; x = .1 fault, .2 output too low. | Pump motor failure, blockage reducing output, or wiring fault. | Function-test the SC pump, clear any blockage, replace the pump if output stays low. |
| Service 47.x | iCombi waste water pump (M15) fault; x = .1 fault, .2 output too low. | Pump motor failure, blockage, or wiring fault. | Function-test the waste water pump, clear the blockage, replace if output stays low. |
| Service 48.x | iCombi circulation pump (M17) fault; x = .1 fault, .2 output too low. | Pump motor failure, foreign particles reducing output, or wiring fault. | Function-test the circulation pump and clear debris; replace the pump if output stays low. Directly relevant to a Service 25 diagnosis. |
| Service 49.x | iCombi care pump (M18) fault; x = .1 fault, .2 output too low. | Pump motor failure, blockage, or wiring fault. | Function-test the care pump, clear any blockage, replace if output stays low. |
| Service 110 | SC pump fault while care chemical is in the steam generator (SCC WE/legacy: SC pump defective or level electrode calcified). | SC pump failure mid-clean, or a calcified level electrode. | Complete the abort/rinse programme so the chemical is flushed, then repair the pump or electrode before returning the oven to cooking. |
| Service 120 | Level electrode without signal while care chemical is in the steam generator (SCC WE: Y1 or level electrode defective; legacy: care pump M12 or level electrode defective). | Calcified or failed level electrode or fill valve during a care cycle. | Complete the abort/rinse programme to flush the chemical, then replace the electrode or valve. |

## How to troubleshoot Rational Service 25

Treat Service 25 as a plumbing-and-flow problem before treating it as a parts problem. The check that trips it only runs during CleanJet, so everything about the diagnosis centers on the cleaning-water circuit: supply in, circulation through the cabinet, jet onto the fan wheel, detection by the control.

Triage in this order:

- **Cheapest first.** Water valve open, site pressure normal, rack or trolley seated in the cabinet. A large share of these calls close without a single tool coming out.
- **Then the path.** Hoses, fittings, and the circulation pump. Kitchens feed these ovens grease, wrappers, and bone fragments daily; the circulation circuit collects all of it.
- **Then detection.** Only after flow is proven good should you suspect the CDS sensor, and that step belongs with service-mode diagnostics.
- **Read the companion codes.** Service 26/27 (drain valve), 46.x–49.x (pump family on iCombi), and 110/120 (chemical in the steam generator) each narrow the fault to a specific component. An oven that logs 48.2 next to Service 25 has already told you the circulation pump output is low.

Two safety rules override all of it. First, chemical: an aborted clean can leave caustic solution in the cabinet or care chemical in the steam generator — gloves, eye protection, complete the rinse routines, and rinse the cabinet before cooking. Second, electrical: lock out and tag out before opening the pump or any panel. And on gas models, leave the combustion side to a licensed gas technician.

## Frequently asked questions

### Can I keep cooking after a Service 25 fault?

Not until the cabinet is verifiably free of cleaning chemical. Service 25 interrupts CleanJet, which means cleaner solution may still be sitting in the cooking cabinet. Complete the machine's abort/rinse routine and rinse the cabinet thoroughly first. If Service 110 or 120 is also showing, care chemical is in the steam generator and the flush routine must complete before any cooking.

### Does Service 25 mean the same thing on an iCombi as on an older SCC?

Same fault family, different detection wording. The legacy SCC and SCC WE references describe it as CleanJet water circulation faulty / no water flow detected, while the iCombi reference words it as no performance increase at the fan motor when the water jet hits. The causes and the checklist — supply, rack position, hoses, pump, sensor — are the same across generations.

### Why does Service 25 only ever appear during cleaning?

Because the check that generates it only runs during CleanJet. The oven verifies cleaning water is actually circulating and hitting the fan wheel; outside a clean cycle that verification never happens, so a marginal hose blockage or weak pump can hide for weeks and only announce itself on the overnight clean.

### Is Service 48.1 or 48.2 the same fault as Service 25?

They are related but distinct. On the iCombi platform, Service 48.x points directly at the circulation pump M17 (48.1 pump fault, 48.2 output too low), while Service 25 reports that the circulation check itself failed. If both appear, start at the pump — the 48.x code has already localized the problem for you.

### What is the CDS sensor?

It is the sensor the control uses to detect water circulation during CleanJet on these machines. If it fails, the oven can report Service 25 even with good flow. Testing it properly requires the service-level diagnostics, which is one of the standard reasons this code ends in a call to a Rational-certified technician after the free checks come up clean.

## Sources

- RATIONAL Service Reference iCombi Pro (doc 80.51.872_SR-iCombi Pro_en-GB, 05/2020) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-iCombi-Pro-1.pdf
- RATIONAL Service Reference iCombi Classic (doc 80.51.855, en-GB) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/80.51.855-ServiceReferenz-iCombi-Classic-en-GB-1.pdf
- RATIONAL Service Reference SelfCookingCenter whitefficiency / CombiMaster Plus (doc 80.51.720_SR_en, 11/2017) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCCWE-CM_P-1.pdf
- RATIONAL Service Reference SCC / CombiMaster 2004–2011 (doc 80.51.028-A4, 09/2008) — https://www.keelingcatering.co.uk/wp-content/uploads/2021/05/Service-refrance-SCC-CM-1.pdf
- Parts Town — Rational Combi Oven Error Codes (authorized distributor guide) — https://www.partstown.com/cm/resource-center/guides/gd2/rational-combi-oven-error-codes
- General Parts — Top 5 Rational Error Codes (authorized service company) — https://generalparts.com/top-5-rational-error-codes-and-what-they-mean-to-you/
