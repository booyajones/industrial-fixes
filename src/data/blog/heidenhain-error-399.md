---
title: "Heidenhain TNC Error 399 — Causes & Fix"
description: "What Heidenhain TNC Error 399 means, why it happens, and how to fix it step by step."
pubDatetime: 2026-04-22T15:00:00Z
modDatetime: 2026-04-22T15:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - heidenhain
---

## Heidenhain TNC Error 399 — What It Means

Error 399 on Heidenhain TNC controls (TNC 640, TNC 530, TNC 620) indicates an axis error — the control detected a position or velocity discrepancy on one of the controlled axes beyond the allowable tolerance. Heidenhain's digital drive system monitors position feedback continuously; Error 399 fires when the following error (difference between commanded and actual position) exceeds the threshold set in the machine parameters.

[Jump to Fix](#fix)

## Common Causes

- **Mechanical binding or excessive load** — A binding axis guideway, over-tightened ballscrew preload, or heavy cutting load prevents the servo from tracking the commanded path within tolerance.
- **Drive or motor fault** — A degraded servo amplifier or motor reduces available torque, causing following error on demanding moves.
- **Encoder feedback problem** — A damaged Heidenhain linear encoder, angle encoder cable, or dirty encoder scale causes position feedback errors that trigger Error 399.
- **Contaminated linear encoder scale** — Heidenhain linear encoders are sensitive to coolant contamination on the glass scale, which causes erratic position readings.

## Step-by-Step Fix {#fix}

1. **Identify the affected axis** — The TNC display shows which axis generated Error 399. Note it.
2. **Check for mechanical binding** — Move the affected axis by hand (with E-stop engaged if safe). Smooth motion with no rough spots is expected. Any resistance indicates a mechanical issue.
3. **Inspect linear encoder** — Visually inspect the Heidenhain scale and read head for contamination, damage, or debris. Clean the scale with Heidenhain cleaning solution if dirty. Check the read head mounting and gap.
4. **Check encoder cable** — Inspect from the encoder/read head to the control for damage or loose connectors. Heidenhain uses a proprietary EnDat or 1Vpp interface.
5. **Reset and test** — After addressing the root cause, press [CE] to clear the error, re-execute reference return, and run a slow test move through the full axis travel.

## Parts Often Needed

| Part | Notes |
|------|-------|
| [Heidenhain encoder cable](https://www.amazon.com/s?k=Heidenhain%20encoder%20cable&tag=errorcodefixe-20) | Replace if damaged; must match encoder interface type |
| [Encoder read head](https://www.amazon.com/s?k=Encoder%20read%20head&tag=errorcodefixe-20) | Replace if contaminated beyond cleaning |
| [Linear scale cleaning kit](https://www.amazon.com/s?k=Linear%20scale%20cleaning%20kit&tag=errorcodefixe-20) | Heidenhain-approved cleaning solution and lint-free cloth |

## When to Call a Pro

Heidenhain encoder replacement requires precise alignment and gap setting. Heidenhain-trained service engineers handle scale and read head replacement on precision machine tools.
