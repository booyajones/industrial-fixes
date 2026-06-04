---
title: "Bosch xE9 Error Code - Causes & Fix"
description: "xE9 on a Bosch heat pump means EEPROM mismatch of compressor in the outdoor unit. Often fixed by reseating or replacing the control board."
pubDatetime: 2026-05-31T09:15:44Z
modDatetime: 2026-05-31T09:15:44Z
author: "Dana Kowalski"
featured: false
draft: true
tags:
  - hvac
  - mini-split
  - bosch
---

## Bosch xE9 Error Code — What It Means

The xE9 error code on Bosch industrial and commercial heat pumps indicates an EEPROM mismatch of the compressor in the outdoor unit. This means the outdoor-unit controller has detected a mismatch between the compressor's stored electronic data or identity and what the control system expects. The fault points to a communication or data-integrity issue between the compressor's memory chip and the main control board, preventing normal operation until resolved.

[Jump to Fix](#fix)

## Common Causes

- **Unseated or loose EEPROM chip** The IC20 EEPROM chip on the outdoor-unit control board may have worked loose from vibration or thermal cycling, breaking the data connection.
- **Failed or corrupted EEPROM chip** The EEPROM memory chip itself may have failed or become corrupted, causing the controller to read incorrect or garbled compressor identity data.
- **Faulty outdoor-unit control board** The main control board in the outdoor unit may have developed a fault in the circuit that reads or writes EEPROM data, triggering the mismatch.
- **Compressor or control board replacement mismatch** If the compressor or control board was recently replaced, the new component's EEPROM data may not match the system configuration, causing the controller to reject it.
- **Power surge or electrical event damage** A power surge, lightning strike, or electrical transient may have damaged the EEPROM chip or the board's memory circuits, corrupting stored data.

## Step-by-Step Fix {#fix}

1. **Power off the heat pump** at the breaker or disconnect switch and wait at least five minutes for all capacitors to discharge before opening the outdoor-unit service panel.
2. **Locate the outdoor-unit control board** inside the electrical compartment of the outdoor cabinet and visually inspect the EEPROM chip (often labeled IC20 or similar) for burn marks, discoloration, or loose seating in its socket.
3. **Reseat the EEPROM chip** by gently removing it from its socket (if socketed) and pressing it firmly back into place, making sure all pins are aligned and fully inserted.
4. **Restore power** to the unit and attempt to run a heating or cooling cycle to see if the xE9 code clears and normal operation resumes.
5. **If the code persists**, power off again and replace the outdoor-unit control board, obtaining the correct part number from the Bosch Aftermarket Resource Center or your model's service documentation before ordering.
6. **After board replacement**, restore power and run the system through a full heating and cooling cycle to verify the code is cleared and the compressor operates normally.
7. **Document the repair** and check that all wiring connections to the new board are secure and match the original configuration before closing the service panel.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Bosch outdoor-unit control board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-heat-pump-xe9-error-code&k=Bosch+outdoor-unit+control+board&tag=errorcodefixes-20) \| Match the exact board part number from your heat pump model's service label or Bosch parts lookup before ordering. |
| EEPROM memory chip (IC20) | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-bosch-heat-pump-xe9-error-code&k=EEPROM+memory+chip+%28IC20%29&tag=errorcodefixes-20) \| Only if the chip is visibly damaged or burned and you have advanced soldering skills to replace a surface-mount component. |

## When to Call a Pro

Call a licensed HVAC technician if you are not comfortable working inside live electrical panels, if the EEPROM chip is soldered rather than socketed, or if the code returns after you have reseated the chip and replaced the control board. Bosch commercial and industrial heat pumps often require specialized diagnostic tools and software to verify EEPROM data integrity and perform board programming after replacement. A technician can also access the Bosch Aftermarket Resource Center to confirm the correct part numbers for your exact model and make sure the new board is properly configured to match your compressor and system setup.
