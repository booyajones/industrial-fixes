---
title: "ABB ACS580 A7AB Fault - Causes & Fix"
description: "ABB ACS580 A7AB (Extension I/O configuration failure) means the installed C-type extension module does not match the drive's configuration or communication is disturbed."
pubDatetime: 2026-05-27T10:34:59Z
modDatetime: 2026-05-27T10:34:59Z
author: "Dana Kowalski"
featured: false
draft: false
tags:
  - vfd
  - abb
money_part: "ABB C-type extension I/O module"
most_likely_cause: "Wrong module type selected in parameters"
---

## What this code means
The A7AB fault on an ABB ACS580 drive indicates an Extension I/O configuration failure. This means the drive has detected a mismatch between the C-type extension module physically installed on the drive and the module type configured in the drive's parameters. It can also appear if communication between the drive and the module has been disturbed by electrical noise or a loose connection.

In practical terms, the drive is reporting that what it expects to see (based on parameter 15.01 Extension module type) does not match what it actually detects (shown in parameter 15.02 Detected extension module). This can happen if no module is installed but the drive is configured for one, if the wrong module type is selected in parameters, or if the module connection is unreliable.

## Common Causes

- **Wrong module type selected in parameters** The drive's parameter 15.01 is set to a different module type than the C-type extension module that is actually installed.
- **No extension module fitted** The drive is configured to expect an extension module but none is physically installed on the unit.
- **Loose or poor module connection** The extension module is not seated correctly or the connector engagement is incomplete, causing intermittent communication.
- **Electrical noise or disturbance** External electrical interference is disrupting the communication link between the drive and the extension module.

## Step-by-Step Fix {#fix}

1. Check parameter 15.02 Detected extension module to see what the drive actually detects is installed on the unit.
2. Compare parameter 15.02 to parameter 15.01 Extension module type and verify they match exactly.
3. Set parameter 15.01 to the correct module type if a module is installed, or set it to 'none' if no extension module is fitted.
4. Inspect the extension module seating and connector engagement, making sure the module is fully seated and the connection is secure.
5. Check for electrical noise sources around the module wiring and drive installation, and eliminate any disturbance sources if present.
6. Cycle power to the drive and restart it so the drive re-reads the module state and confirms the configuration.
7. Replace the extension module or contact ABB service if the fault persists after confirming parameter settings and connections are correct.

## Parts Often Needed

| Part | Notes |
|------|-------|
| ABB C-type extension I/O module | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a7ab-fault-code&k=ABB+C-type+extension+I%2FO+module&tag=errorcodefixes-20) \| Match the exact module type required for your application and verify compatibility with your ACS580 model. |
| Extension module connector/interface assembly | [Amazon](https://www.amazon.com/s?ascsubtag=ecf-abb-acs580-a7ab-fault-code&k=Extension+module+connector%2Finterface+assembly&tag=errorcodefixes-20) \| Only needed if physical damage to the drive-side module interface is found during inspection. |

## When to Call a Pro

Call a qualified technician or ABB service if the fault continues after you have verified that parameter 15.01 matches the installed module (or is set to none if no module is fitted) and you have checked all physical connections. If the fault appeared after a control board change, parameter restore, or module swap and does not clear with a power cycle, the issue may involve a faulty extension module or a problem with the drive's internal module interface that requires diagnostic tools and replacement parts from ABB.
