---
title: "Haas Alarm 124 — Causes & Fix"
description: "What Haas Alarm 124 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - cnc
  - haas
money_part: "Tool-present proximity switch"
---

## Haas Alarm 124 — What It Means

Haas Alarm 124 indicates an ATC no-tool condition — the control commanded a tool change but the ATC detected that the designated tool pocket is empty, or the tool wasn't gripped correctly by the ATC arm. The Haas ATC uses a tool-present sensor or pocket occupancy logic to detect whether a tool is in the expected pocket; Alarm 124 fires when that check fails.

[Jump to Fix](#fix)

## Common Causes

- **Tool missing from the programmed pocket** — The T-code in the program called for a tool that isn't loaded in the ATC. Common in setups where tools were changed between programs.
- **Tool seated incorrectly in pocket** — A tool that's partially seated or tilted in its ATC pocket doesn't trigger the pocket sensor correctly.
- **Tool-present sensor failure** — The sensor that detects tool presence in the pocket has failed, reporting empty pockets that actually have tools.
- **Tool table mismatch** — The Haas tool table (tool offsets and pocket assignments) doesn't match the actual tools loaded in the machine.

## Step-by-Step Fix {#fix}

1. **Check the tool table vs. physical carousel** — Compare the tools listed in the Haas tool table/carousel display against the tools actually installed in each pocket. Find any discrepancies.
2. **Verify the called T-number** — Check the program's T-code. Confirm the tool actually exists in the specified pocket.
3. **Inspect the tool pocket** — Look at the pocket that caused Alarm 124. Is the tool fully seated? Correct gripper orientation?
4. **Check the tool-present sensor** — In Haas diagnostics, monitor the pocket sensor input for the affected pocket. Load and unload a tool and confirm the sensor state changes.
5. **Reload the tool and re-attempt** — Fully seat the tool in the pocket, update the tool table if needed, and attempt the tool change again at low speed via MDI.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Tool-present proximity switch | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-124&k=Tool-present+proximity+switch&tag=errorcodefixes-20) \| Replace if not detecting loaded tools |
| Tool holder / pull stud | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-haas-alarm-124&k=Tool+holder+%2F+pull+stud&tag=errorcodefixes-20) \| Inspect if tool won't seat correctly |
## When to Call a Pro

If multiple pockets report Alarm 124 despite tools being loaded, the ATC carousel position calibration or tool detection system needs Haas service diagnosis.

## Related Articles

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 103 — Servo Overload Fix](/posts/haas-alarm-103/)
- [Haas Alarm 104 Feed Hold — Causes & Fix](/posts/haas-alarm-104-feed-hold/)
- [Haas Alarm 105 E-Stop — Causes & Fix](/posts/haas-alarm-105/)

## See Also

- [Haas CNC Alarm 101 — Emergency Stop Active Fix](/posts/haas-alarm-101-emergency-stop/)
- [Haas Alarm 102 — Servo Drive Fault Fix](/posts/haas-alarm-102/)
- [Haas Alarm 122 — ATC Chain Fault](/posts/haas-alarm-122/)
- [Haas Alarm 219 — X-Axis Servo Error Fix](/posts/haas-alarm-219/)
