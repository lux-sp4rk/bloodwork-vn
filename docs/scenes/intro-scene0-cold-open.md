# Scene 0: Cold Open — Bathroom

**Label:** `cold_open_bathroom`  
**Location:** Bathroom  
**Characters:** Rachel (alone)  
**Feeds into:** `act1_the_order` (Scene 1)  
**Status:** Implemented

---

## Purpose

Establishes alcoholism as a *physical fact* before any sympathy context exists. The player sees the body first, the reasons never.

Structurally mirrors the ending: Rachel starts on a bathroom floor; she ends on pavement. The story is bracketed by her body failing her.

The transition — bathroom floor → mundane consumer purchase — does heavy lifting. The horror isn't just the toys. It's that she's normalized this completely.

---

## Tone

**Flat affect.** This is maintenance, not a moment. She doesn't cry at the mirror. She doesn't monologue about why. The narration should read like a checklist, not a confession.

Compare to **Scene 7** (Act 2 bathroom), where she vomits red bile after the Ninja attack — that scene is body crisis, fear, isolation. The cold open is routine. Different registers.

---

## Key Beats

1. Rachel on the bathroom floor, back against the tub
2. No internal monologue about *why* — no grief, no Ethan, nothing
3. She waits it out. Gets up. Rinses her mouth at the sink.
4. Looks at herself in the mirror briefly. Not melodramatic.
5. Goes to bedroom. Opens laptop. Orders the toys.
6. Hard cut to crow hitting window — Scene 1 picks up from confirmation email ding.

---

## Prose

```
The tile was cold through her jeans.
She'd been here long enough that it didn't register anymore.

Her body finished what it was doing.
She waited.

Eventually she got up.
Ran the tap. Rinsed twice.
Looked at her face in the mirror the way you check a clock —
just to confirm the time, not because you want to know it.

Tommy was still asleep.
She'd heard him turn over twenty minutes ago. Nothing since.

She went to the bedroom, opened the laptop,
and finished what she'd been about to do before.
```

---

## Audio

Silence or near-silence. No music. Distant ambient optional — fridge hum, traffic. The absence of the horror soundtrack is part of the point.

---

## Visual Asset

**TODO:** `game/images/bathroom_floor.png` — dark, cold tile, low angle. No blood (that's Scene 7). Just the room.

Currently falls back to `scene black` until asset is available.

---

## Changes

- `game/script.rpy`: New `cold_open_bathroom` label; `start` now jumps here instead of directly to `act1_the_order`
- `docs/plot.md`: Scene 0 added before Scene 1 in Intro section
