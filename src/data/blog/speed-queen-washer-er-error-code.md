---
title: "Speed Queen Washer ER Error Code - Causes & Fix"
description: "ER on a Speed Queen washer requires a second code (OF or CO). ER,OF means overflow or drain issue. ER,CO means control communication fault."
pubDatetime: 2026-05-31T02:58:47Z
modDatetime: 2026-05-31T02:58:47Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - appliance
  - washer
  - speed-queen
money_part: "Water inlet valve"
---

## Speed Queen Washer ER Error Code — What It Means

ER on a Speed Queen washer is not a single universal fault. The meaning depends on the exact model and on whether the display shows a second code such as OF, CO, dS, or another suffix. The two clearly documented combinations are Er,OF and Er,CO. Er,OF means the washer sensed an overflow condition or could not lower the water level within 5 minutes. Er,CO means a communication failure between control electronics, typically between the user interface or main control and the drive board or MCU, or in the wiring between them.

For any technician, the first step is always to identify the exact suffix and the model family, because the diagnostic tree is different for OF versus CO. On some coin-operated or commercial variants, a related ER can involve the coin mechanism rather than the wash system, so model verification matters.

[Jump to Fix](#fix)

## Common Causes

- **Leaking inlet valve (Er,OF)** A faulty water inlet valve allows the tub to keep filling when the washer is off or should be stopped, triggering an overflow condition.
- **Pressure hose problem (Er,OF)** A blockage, loose connection, or air leak in the pressure hose prevents the control from reading water level correctly.
- **Drain restriction or pump problem (Er,OF)** A blocked drain hose, improper standpipe installation, or failing drain pump prevents the machine from lowering water level in time.
- **Loose or damaged wiring harness (Er,CO)** A loose connector, bent pin, or heat-damaged wire between the main control and drive board stops communication between the boards.
- **Drive board or main control board failure (Er,CO)** A failed drive board, inverter, MCU, or main control board loses the ability to communicate with the other control electronics.
- **Power-quality interruption (Er,CO)** An unstable supply, extension cord, or tripped breaker causes the boards to lose sync and throw a communication fault.

## Step-by-Step Fix {#fix}

1. **Unplug the washer** for 60 seconds to clear the fault memory, then plug back in and run a test cycle to see if the code returns and note the exact suffix (OF, CO, or other).
2. **For Er,OF, check the tub** with the washer off and unplugged to see if water is slowly entering on its own, which points to a leaking inlet valve.
3. **Inspect the pressure hose** for blockage, disconnection, or air leaks by tracing the hose from the outer tub air trap to the pressure sensor on the control board.
4. **Check the drain system** by verifying the drain hose is installed at the correct height (consult your model's installation guide), the standpipe is not backing up, and the pump can run freely without restriction.
5. **For Er,CO, confirm stable incoming power** by plugging the washer directly into a wall outlet (no extension cord or power strip) and verifying the breaker has not tripped or the outlet is not loose.
6. **Inspect all wiring harnesses and connectors** between the user interface, main control board, and drive board for looseness, bent pins, corrosion, or heat damage, reseating each connector firmly.
7. **If wiring checks good and the code persists**, isolate the board set by testing or substituting the drive board or MCU first, then the main control or UI board if the fault remains.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Water inlet valve | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-speed-queen-washer-er-error-code&k=Water+inlet+valve&tag=errorcodefixes-20) \| Match the valve model to your washer's exact part number for proper fit and voltage rating. |
| Pressure hose and air trap assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-speed-queen-washer-er-error-code&k=Pressure+hose+and+air+trap+assembly&tag=errorcodefixes-20) \| Order the hose kit specific to your Speed Queen model to make sure correct diameter and length. |
| Drive board or inverter board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-speed-queen-washer-er-error-code&k=Drive+board+or+inverter+board&tag=errorcodefixes-20) \| Verify your model number and board revision before ordering, as these are model-specific and not interchangeable. |
| Main control board or user interface board | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-speed-queen-washer-er-error-code&k=Main+control+board+or+user+interface+board&tag=errorcodefixes-20) \| Confirm the exact board part number from your washer's service label or tech sheet to avoid a mismatch. |

## When to Call a Pro

Call a professional if you see Er,CO and have no experience with control board diagnostics, wiring harness testing, or isolating communication faults between multiple boards. Also call a pro if you see Er,OF and cannot locate the source of the overflow after checking the inlet valve and pressure hose, or if the washer continues to overfill despite replacing the valve. On coin-operated or commercial Speed Queen models, any ER code may involve proprietary control logic or coin-mechanism integration that requires factory training and special tools to diagnose safely.
