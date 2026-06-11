---
title: "Haas Alarm 125 Tool Carousel Fault — Causes & Fix"
description: "What Haas Alarm 125 tool carousel fault means, why it trips, and how to diagnose and fix it step by step."
pubDatetime: 2026-04-22T13:00:00Z
modDatetime: 2026-04-22T13:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - haas
money_part: "Carousel proximity switch"
---

## Haas Alarm 125 Tool Carousel Fault — What It Means

Haas **Alarm 125** indicates a **tool carousel fault**. On Haas mills with an umbrella-style or side-mount tool changer, this means the carousel did not reach the commanded pocket position, or the control did not receive the correct position confirmation from the carousel sensors. The tool changer stops mid-sequence to prevent a crash between the spindle, tool pocket, and changer arm. Alarm 125 usually points to a sensor, motor, or obstruction problem inside the carousel assembly.

[Jump to Fix](#fix)

## Common Causes

- **Carousel pocket obstruction** — A tool holder sitting crooked, a loose retention knob, or packed chips in the pocket prevents smooth carousel indexing.
- **Failed carousel motor or gearbox** — The carousel drive motor can stall or the gearbox can bind, preventing the pocket from reaching the commanded position.
- **Bad proximity switch or position sensor** — The carousel relies on sensors to confirm home and pocket positions. A failed prox switch triggers Alarm 125 even if the mechanism moved correctly.
- **Low air pressure** — Some carousel functions depend on shop air. Low incoming pressure can prevent full tool release or clamp action, stopping the sequence.

## Step-by-Step Fix {#fix}

1. **Inspect the carousel pockets** — Put the machine in a safe state, open the tool changer area, and check every pocket for chips, damaged holders, or a tool sitting too low or too high in the pocket.
2. **Run ATC recovery** — Use the Haas ATC RECOVERY screen to move the changer slowly back to a known safe position. This helps identify where the carousel is hanging up.
3. **Check carousel sensors** — Locate the carousel home and pocket position sensors. Verify sensor LED lights change state when the carousel moves past the target position.
4. **Test carousel motor movement** — Command a slow carousel rotation in recovery mode. If the motor hums, stalls, or moves unevenly, inspect the motor coupling and gearbox.
5. **Reset the system** — Restore normal air pressure, clear the obstruction or failed part, then press RESET and run a dry tool change cycle with no program loaded to confirm Alarm 125 is cleared.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Carousel proximity switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-125-carousel-fault&k=Carousel+proximity+switch&tag=errorcodefixes-20) \| Replace if the LED state does not change at the expected position |
| Carousel motor or gearbox | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-125-carousel-fault&k=Carousel+motor+or+gearbox&tag=errorcodefixes-20) \| Replace when the carousel stalls or rotates unevenly |
| Tool holder / pull stud | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-125-carousel-fault&k=Tool+holder+%2F+pull+stud&tag=errorcodefixes-20) \| Replace if a damaged holder is hanging in the pocket |
## When to Call a Pro

If the carousel is mechanically jammed and ATC recovery cannot return it to home, stop there. Forcing the changer can bend the arm or damage the carousel plate. Haas Factory Outlet service is the right move in that situation.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)

## See Also

- [Haas Alarm 124 — Causes & Fix](/posts/haas-alarm-124/)
- [Haas CNC Alarm Codes — Complete Guide (100-Series and Up)](/posts/haas-alarm-codes/)
- [Haas Alarm 126 — ATC Door Fault](/posts/haas-alarm-126/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
