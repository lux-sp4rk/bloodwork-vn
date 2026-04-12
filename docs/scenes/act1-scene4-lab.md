---
title: "Scene 4: University Lab"
type: scene
act: 1
status: implemented
script_label: act1_flashback_lab
related:
  - "[[act1-scene3-research]]"
  - "[[act1-scene5-vigil]]"
  - "[[rachel]]"
  - "[[david]]"
  - "[[manager]]"
---

# Scene 4: University Lab

**Location:** Open-plan tech office, conference room with glass walls
**Characters:** [[rachel|Rachel]], [[david|David]], [[manager|Manager/Dean]]
**Script label:** `act1_flashback_lab`

## Summary

Rachel drinks vodka from a water bottle at her desk. She'd been debugging the NinjaMaster recommendation algorithm before it launched — toying with edge cases, adversarial inputs. [[david|David]] covers for her. [[manager|The Manager]] calls her in. She's later laid off. She remembers the code: fail-safes, behavioral constraints, the sandboxed environment. The toys shouldn't be able to do what they're doing.

## Key Beats

- Lab buzzed under hard fluorescents. Rachel's hands unsteady over the slides.
- She'd been debugging the NinjaMaster recommendation algorithm before it launched.
- She knew the fail-safes, the sandboxing, the behavioral constraints.
- **The toys shouldn't be able to do what they were doing.**
- David: "You okay?" — he could smell the vodka. He'd been covering for her.
- They'd all been covering. The students loved her.
- Manager: "Rachel. My office. Now."
- The dean had noticed. The next day, she was on leave — {i}get help, come back later.{/i}
- The look in his eyes told her the truth: it was final.

## Implementation

**Implemented in:** `game/script.rpy` — `act1_flashback_lab` label (replaced placeholder in PR #11)
**Source:** Manuscript excerpt adapted directly
**Placeholder images:** `game/images/lab_flashback.png`

## Notes

- [[david|David]] is a one-scene character. His covering behavior is shown on screen, not stated in narration.
- [[manager|Manager]] is a one-scene character. His brief appearance is the climax of Scene 4.
- Closes [[https://github.com/lux-sp4rk/digital-death-dolls/issues/7|Issue #7]].

## Next Scene

[[act1-scene5-vigil|Scene 5: Nighttime Vigil]] →
