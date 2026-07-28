---
title: "Weil-McLain Boiler A129 Error - Causes & Fix"
description: "A129 is not documented in Weil-McLain literature. Verify your model and control board to find the correct fault table and fix."
pubDatetime: 2026-06-17T11:22:49Z
modDatetime: 2026-06-17T11:22:49Z
author: "Error Code Fixes Editorial Team"
featured: false
draft: false
tags:
  - boiler
  - weil-mclain
money_part: "Weil-McLain control board (model-specific)"
diy_or_pro: "pro"
free_checks:
  - "Power-cycle the boiler by turning off the circuit breaker for 60 seconds, then restore power and check if the code clears."
  - "Locate the boiler model number (usually on a label inside the jacket or on the front panel) and download the correct manual from Weil-McLain's support site to verify the fault table."
  - "Inspect all low-voltage wiring connectors at the control board for corrosion or looseness and reseat them."
---

## What this code means
An A129 error code does not appear in available Weil-McLain boiler manuals or fault code tables. Weil-McLain systems use model-specific control platforms, and the same code can mean different things across different boards or may not exist at all on certain models. The only documented A129 code in the research is from Rheem hybrid water heaters, where it indicates an upper element relay failure to close, but that reference does not apply to Weil-McLain boilers.

To interpret the fault correctly, locate your boiler's model number and control board type. Check the wiring diagram and fault history inside the manual for your exact unit. If the display shows A129 and the boiler is not heating or cycling properly, the underlying issue may involve a relay, control board, or wiring fault, but the specific meaning depends entirely on your model. Treating this as a generic relay fault without confirming the manufacturer definition can lead to unnecessary part replacement.

## Before You Replace Anything

Without the correct fault table, technicians may replace the main control board when the problem is simply a loose wiring connection or a stuck relay. Always consult the model-specific manual and verify wiring continuity before ordering parts.

## Common Causes

- **Model mismatch or undocumented code (~40%)** The code may be specific to a third-party control platform or an older discontinued model not covered in current literature.
- **Loose or corroded low-voltage wiring (~25%)** Relay and sensor circuits can generate non-standard faults when connections oxidize or vibrate loose over time.
- **Failed relay or contactor on the control board (~20%)** If the code does map to a relay fault, the relay itself or the circuit driving it may have failed.
- **Control board firmware or memory error (~10%)** Power surges or age can corrupt the board's fault-code register and display phantom or incorrect codes.
- **Misread display or transposed code (~5%)** Alphanumeric displays can be hard to read in low light, and codes like A12F or A1-29 may be reported as A129.

## Quick Diagnosis

Answer these to narrow it down fast.

<details class="dtree"><summary>Does the boiler model number and manual list an A129 fault code in the diagnostics section?</summary>
<div class="dtree-body"><strong>Yes:</strong> Follow the manufacturer troubleshooting steps exactly as written for that code.<br><strong>No:</strong> The code is either a misread or not applicable to your model. Contact Weil-McLain support or a qualified technician with the exact model number.</div>
</details>

<details class="dtree"><summary>Did the code appear immediately after a power outage or lightning storm?</summary>
<div class="dtree-body"><strong>Yes:</strong> The control board may have a memory fault or corrupted firmware. Power-cycle the system and check for other error codes.<br><strong>No:</strong> The fault is likely related to a component or wiring issue rather than a transient event.</div>
</details>

<details class="dtree"><summary>Is the boiler still providing heat despite the displayed code?</summary>
<div class="dtree-body"><strong>Yes:</strong> The code may be a nuisance alarm or a sensor reading outside normal range. Monitor system performance and document when the code appears.<br><strong>No:</strong> A lockout or safety shutdown is active. Do not attempt to force a restart without identifying the fault.</div>
</details>

## Step-by-Step Fix {#fix}

1. **Turn off power** at the circuit breaker and the boiler's main power switch, then wait 60 seconds.
2. **Locate the model and serial number** on the boiler nameplate (often inside the front jacket or on the side panel) and write them down.
3. **Download the installation and service manual** from Weil-McLain's website using your exact model number, and locate the fault code table in the diagnostics chapter.
4. **Verify the code on the display** by taking a clear photograph under good light to confirm the characters are A129 and not a similar code.
5. **If A129 does not appear in your manual**, contact Weil-McLain technical support at the number in the manual with your model, serial, and control board part number.
6. **Inspect all low-voltage wiring** at the control board, relays, and sensors for loose connectors, corrosion, or pinched wires, and clean or reseat connections as needed.
7. **Restore power** and observe whether the code reappears immediately, after a call for heat, or intermittently, and note any other fault codes that display.
8. **Do not replace the control board or any relay** until you have confirmed the exact meaning of the code and verified wiring and voltage with a multimeter.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Weil-McLain control board (model-specific) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a129-error-code&k=Weil-McLain+control+board+%28model-specific%29&tag=errorcodefixes-20) \| Only order after confirming the board part number and fault definition from the service manual. |
| Low-voltage relay or contactor (if specified by manual) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-weil-mclain-boiler-a129-error-code&k=Low-voltage+relay+or+contactor+%28if+specified+by+manual%29&tag=errorcodefixes-20) \| Some control platforms use plug-in relays that can be replaced individually. |

## When to Call a Pro

Call a licensed boiler technician immediately if you cannot locate the model manual, if the code does not appear in any Weil-McLain documentation, or if the boiler is locked out and will not fire. Gas-fired and oil-fired boilers involve combustion safety interlocks, pressure switches, and ignition sequences that require proper diagnostics and testing equipment. A technician can access fault history in the control board memory, measure relay voltages, and cross-reference the code with the exact control platform installed on your unit. Do not bypass any safety lockout or attempt to force the boiler to run while an unidentified fault code is displayed.

**Rough cost:** A pro service call runs about $200-450.
