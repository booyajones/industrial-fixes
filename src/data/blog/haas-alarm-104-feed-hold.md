---
title: "Haas Alarm 104 Feed Hold — Causes & Fix"
description: "What Haas alarm 104 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T08:00:00Z
modDatetime: 2026-04-22T08:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - haas
---

## Haas Alarm 104 Feed Hold — What It Means

Haas alarm 104 means Feed Hold is active — the machine has been placed in feed hold state and cannot start or continue a program. On Haas VF, ST, and UMC series mills and lathes, the Feed Hold condition is a normal operational state, but alarm 104 appears when the control detects that feed hold is active while a program run is being initiated, or when a feed hold interlock has been engaged by an external device. In most cases this isn't a hardware fault — it's either the Feed Hold button being physically pressed or an M-code or interlock that has put the machine in that state.

[Jump to Fix](#fix)

## Common Causes

- **Feed Hold button physically pressed** — The simplest cause. The yellow Feed Hold button on the operator panel was pressed and not released. The machine waits in this state indefinitely.
- **External feed hold input active** — Haas machines accept an external feed hold signal on the I/O board. If a peripheral device (robot, part loader, fixture clamping circuit) has asserted this input, the machine stays in feed hold.
- **M-code interlock waiting for signal** — An M-code in the program (M0 for optional stop, or a custom M-code) has paused the machine and is waiting for an operator action or external signal.
- **Safety door or interlock switch** — Some Haas configurations use the door interlock as a feed hold source. An open or faulty door switch can assert feed hold continuously.

## Step-by-Step Fix {#fix}

1. **Check the Feed Hold button** — Look at the operator panel. The Feed Hold button LED should be illuminated if it was pressed. If so, press CYCLE START to resume or RESET to clear the program state.
2. **Press RESET** — A single press of the RESET button on the Haas control clears most alarm 104 conditions and returns the machine to idle state.
3. **Check external I/O** — Navigate to the Haas diagnostics screen (Diagnostics > I/O). Look at the Feed Hold input line. If it reads "1" (active), trace the external wiring to find what is asserting the signal.
4. **Check the safety door switch** — Open and close the machine door. If the feed hold condition clears when the door latches, the door switch may be misaligned or failing.
5. **Reset the system** — With feed hold cleared, press CYCLE START to resume the program or return to MDI mode and restart.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Door interlock switch | [Amazon](https://www.amazon.com/s?k=Door+interlock+switch&tag=errorcodefixes-20) \| Replace if door cycling resolves the fault; Haas part numbers vary by machine |
| Feed Hold push button | [Amazon](https://www.amazon.com/s?k=Feed+Hold+push+button&tag=errorcodefixes-20) \| Replace if the button is mechanically stuck in the pressed position |
## When to Call a Pro

If the Haas diagnostics screen shows the Feed Hold input active with no obvious external cause and all field wiring checks clean, a Haas Factory Outlet (HFO) technician can trace the I/O board signal back to the source.
