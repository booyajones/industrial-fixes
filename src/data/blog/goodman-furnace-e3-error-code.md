---
title: "Goodman Furnace E3 Error Code — Draft Motor Fault"
description: "Goodman E3 error means the induced draft motor failed to prove. Learn how to diagnose the inducer, pressure switch, and condensate drain to fix E3 fast."
pubDatetime: 2026-04-22T18:00:00Z
modDatetime: 2026-04-22T18:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - goodman
  - furnace
  - hvac
  - error-code
  - inducer
---

## Goodman Furnace E3 Error — Draft Motor Fault

**E3 on a Goodman digital-display furnace** means the **induced draft blower failed to prove** — the IFC board energized the inducer motor, waited for the pressure switch to close, and it didn't close within the allowed window.

This error appears on newer Goodman models with digital displays (GMSS96, GCSS96, GMH80 series with updated controls).

## What E3 Is Checking

The startup sequence:
1. IFC energizes inducer motor
2. Inducer spins up, creates negative pressure in the heat exchanger
3. Pressure switch port senses suction, switch closes
4. IFC receives "draft proven" signal, proceeds to ignition

If step 3 or 4 fails, E3 is stored.

## E3 Root Causes

| Cause | Check |
|---|---|
| Condensate drain blocked | Water backed up, blocking switch port |
| Pressure switch hose cracked/off | Trace all small rubber hoses |
| Pressure switch failed | Won't close under suction |
| Inducer motor not spinning | Bad motor, capacitor, or IFC output |
| Blocked flue or intake | No draft pressure builds |
| Cold weather ice blockage | Frozen condensate or flue ice |

## Diagnosis Steps

### Step 1 — Listen at Startup

Turn the thermostat to heat. Within seconds, you should hear the inducer motor spin up (a rushing sound). If you hear nothing:
- Check that the furnace has power
- Check that the inducer motor terminals have 120V (use a multimeter, carefully, with power on)
- If 120V is present and motor doesn't run: bad motor or run capacitor

### Step 2 — Check the Condensate System

High-efficiency Goodman furnaces produce water. The drain pan, trap, and lines must all be clear. Disconnect the drain line at the trap. If water doesn't flow freely, the trap or line is blocked. Clean with warm water or blow it out. Check the pressure switch port on the inducer housing — it should be clear and dry.

### Step 3 — Test the Pressure Switch

With power off, remove one hose from the pressure switch. Apply gentle suction by mouth while measuring continuity across the switch terminals. The switch should close (continuity) under suction. If it doesn't, replace the switch.

Common Goodman pressure switch part numbers:
- B1370135 (single-stage 80% models)
- B13701-35 (90% models — verify on board label)

### Step 4 — Check Flue and Intake

Go outside. Look at both PVC pipes (90%+ efficiency) or metal flue. Debris, bird nests, or ice on the exhaust will immediately cause E3. Clear any obstruction.

### Step 5 — Inducer Motor Testing

If the motor runs but E3 persists, the motor may not be generating enough suction. Use a manometer at the pressure switch port — should read -0.4 to -0.8" WC with motor running. Low readings indicate a worn motor or leaking housing.

## Parts Reference

| Part | Typical Cost |
|---|---|
| Pressure switch (OEM) | $30–70 |
| Pressure switch hose | $5–10 |
| Inducer motor (Goodman OEM) | $150–350 |
| Condensate trap | $15–30 |
| IFC board | $100–280 |

## E3 vs. E1

- **E1** — typically pressure switch stuck open before inducer proves (sequence issue)
- **E3** — draft motor specifically failed to prove during trial

On some Goodman models, these codes can overlap depending on firmware. Always verify with the specific wiring diagram on the inside of the furnace door.

## Quick Reset

After fixing the underlying cause, restore power. The furnace should attempt startup automatically. If E3 clears and returns within one cycle, you have an intermittent issue — suspect condensate backing up in the line during operation, or an inducer motor that's failing under load.
