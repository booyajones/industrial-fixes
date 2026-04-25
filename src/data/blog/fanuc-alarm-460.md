---
title: "Fanuc Alarm 460 — Spindle Overload"
description: "Fanuc Alarm 460 means spindle load exceeded the allowable limit. Learn what causes Fanuc spindle overload alarms and how to fix them."
pubDatetime: 2026-04-22T17:00:00Z
modDatetime: 2026-04-22T17:00:00Z
author: "ErrorCodeFixes"
featured: false
draft: false
tags:
  - cnc
  - fanuc
  - spindle
  - overload
---

## Fanuc Alarm 460 — What It Means

**Alarm 460** on a Fanuc CNC means the **spindle load exceeded the permissible limit**. This can happen because of an aggressive cut, dull tooling, a seized spindle component, or a problem in the spindle drive system.

[Jump to Fix](#fix)

## Common Causes

- **Tool is dull or chipped**. Cutting force rises sharply and drives spindle load up.
- **Feed or depth of cut is too aggressive**. The program is demanding more torque than the spindle can safely deliver.
- **Spindle bearings are failing**. Heat and drag increase spindle motor current.
- **Gearbox or belt drive problem**. Mechanical drag upstream of the spindle creates overload.
- **Spindle drive or cooling issue**. An overheated drive can behave unpredictably and trip load alarms.

## Step-by-Step Fix {#fix}

1. **Check the tool first**. Replace dull or damaged tooling before chasing electrical faults.
2. **Reduce feed and depth of cut**. If the alarm disappears, the issue is process load, not machine failure.
3. **Run the spindle unloaded** at several RPMs. If load is high with no tool cutting, the issue is mechanical or electrical.
4. **Listen for bearing noise**. Growling, heat, or vibration points to spindle bearing failure.
5. **Inspect belts or gearbox** if equipped. A seized idler or tight gearbox raises load dramatically.
6. **Check spindle drive cooling**. Dirty filters or failed cooling fans can cause drive overheating and nuisance overload trips.

## Parts Often Needed

| Part | Notes |
|------|-------|
| Spindle bearings | [Amazon](https://www.amazon.com/s?k=Spindle+bearings&tag=errorcodefixes-20) \| Replace if heat or noise is present |
| Toolholder / cutting tool | [Amazon](https://www.amazon.com/s?k=Toolholder+%2F+cutting+tool&tag=errorcodefixes-20) \| Dull tools are the simplest fix |
| Drive cooling fan | [Amazon](https://www.amazon.com/s?k=Drive+cooling+fan&tag=errorcodefixes-20) \| Check spindle drive cabinet airflow |
| Belt set | [Amazon](https://www.amazon.com/s?k=Belt+set&tag=errorcodefixes-20) \| Replace if glazed, cracked, or over-tensioned |
## When to Call a Pro

If spindle load is high with no cutting load, the machine likely needs spindle service, drive diagnostics, or both. Continuing to run it risks spindle damage.

## Related Articles

- [Fanuc 0i-MD Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-0i-md-alarm-codes/)
- [Fanuc 30i/31i/32i Alarm Code Guide — Complete Diagnostic Reference](/posts/fanuc-30i-alarm-codes/)
- [Fanuc Alarm 1 Overtravel — Causes & Fix](/posts/fanuc-alarm-1-overtravel/)
- [Fanuc Alarm 10 Servo Alarm — Causes & Fix](/posts/fanuc-alarm-10-servo-alarm/)
- [Fanuc Alarm 2 — Overtravel Plus Causes & Fix](/posts/fanuc-alarm-2-overtravel/)
