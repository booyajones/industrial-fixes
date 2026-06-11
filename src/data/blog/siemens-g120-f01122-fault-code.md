---
title: "Siemens G120 F01122 - Causes & Fix"
description: "Siemens G120 F01122 means frequency at the measuring probe input is too high. Learn the causes, diagnostic steps, and repair."
pubDatetime: 2026-05-27T10:45:35Z
modDatetime: 2026-05-27T10:45:35Z
author: "James Rutherford"
featured: false
draft: false
tags:
  - vfd
  - siemens
money_part: "Siemens G120 Control Unit (CU)"
---

## Siemens G120 F01122 — What It Means

F01122 on a SINAMICS G120 indicates that the pulse frequency at the measuring probe input has exceeded acceptable limits. This fault relates to a technological function using a digital input for encoder or probe signals, not to the motor power stage itself. The drive detects that the incoming pulse train is too fast for the configured application, which triggers the fault to protect the control logic and prevent erroneous operation.

Siemens identifies this as an application or technological function fault. The fault value in parameter r0949 tells you which input is involved: a value of 1 means DI 1 at terminal 6, and a value of 2 means DI 3 at terminal 8. The primary remedy is to reduce the frequency of the pulses arriving at that input.

[Jump to Fix](#fix)

## Common Causes

- **Pulse frequency from encoder or probe exceeds configured limit** The connected measuring device is sending pulses faster than the drive expects for the application.
- **Noisy or bouncing signal wiring at the probe input** Poor shielding or loose connections create extra pulses that the drive counts as valid signals.
- **Incorrect parameterization of the measuring probe function** The technological function is assigned to the wrong input or configured for a lower pulse rate than the actual source produces.
- **Wrong encoder or sensor type for the application** The installed measuring device outputs a higher pulse count per revolution or cycle than the drive is set to accept.
- **Mechanical overspeed condition** The driven machine is running faster than intended, which increases the pulse rate from a correctly installed encoder.

## Step-by-Step Fix {#fix}

1. Read the fault value in parameter r0949 to identify which digital input is triggering the fault (DI 1 at terminal 6 or DI 3 at terminal 8).
2. Check the signal source connected to the identified input, such as an encoder or measuring probe, and verify its output frequency matches the application requirements.
3. Inspect the wiring and shielding to the probe input for damage, loose terminals, or induced electrical noise that could generate extra pulses.
4. Compare the actual pulse frequency with the drive's configured parameters for the technological function and adjust the drive settings or reduce the signal frequency at the source if it is too high.
5. Verify the encoder or sensor type is correct for your application and that its pulses per revolution or cycle match the drive's expected input range.
6. Reset the fault after correcting the signal condition and run the machine to confirm the fault does not return.
7. If the fault persists with a known-good signal source and correct wiring, consult your drive manual for advanced troubleshooting or consider control unit input circuitry issues.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Siemens G120 Control Unit (CU) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01122-fault-code&k=Siemens+G120+Control+Unit+%28CU%29&tag=errorcodefixes-20) \| Replace only if input circuitry is confirmed defective after correcting the signal source and wiring. |
| Encoder or measuring probe compatible with G120 digital inputs | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01122-fault-code&k=Encoder+or+measuring+probe+compatible+with+G120+digital+inputs&tag=errorcodefixes-20) \| Required if the existing sensor outputs a pulse frequency incompatible with your drive configuration. |
| Shielded cable for encoder or probe wiring | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-siemens-g120-f01122-fault-code&k=Shielded+cable+for+encoder+or+probe+wiring&tag=errorcodefixes-20) \| Use to replace damaged or poorly shielded signal cables that introduce noise. |

## When to Call a Pro

Call a qualified technician or automation specialist if you cannot identify which measuring device is connected to the faulted input, if you are unfamiliar with reading drive parameters such as r0949, or if the fault returns after you have verified correct wiring and signal frequency. Also seek professional help if you need to modify the technological function parameters or if you suspect the control unit input stage is damaged, since incorrect parameterization can cause machine malfunction or safety hazards.

## See Also

- [Siemens Micromaster F0085 - Causes & Fix](/posts/siemens-micromaster-f0085-fault-code/)
- [Siemens G120 F01105 - Causes & Fix](/posts/siemens-g120-f01105-fault-code/)
- [Siemens G120 F30002 - Causes & Fix](/posts/siemens-g120-f30002-fault-code/)
- [Siemens Micromaster F0221 - Causes & Fix](/posts/siemens-micromaster-f0221-fault-code/)
