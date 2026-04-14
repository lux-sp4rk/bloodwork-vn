---
title: "Scene 2: The Burial"
type: scene
act: 1
status: implemented
script_label: act1_the_burial
related:
  - "[[act1-scene1-order]]"
  - "[[act1-scene3-research]]"
  - "[[rachel]]"
  - "[[tommy]]"
---

# Scene 2: The Burial

**Location:** Backyard
**Characters:** [[rachel|Rachel]], [[tommy|Tommy]]
**Script label:** `act1_the_burial`

## Summary

The next morning, after drinking vodka with ice and lemonade (with a side of Prozac), Rachel buries the crow under the oak tree. Tommy discovers her and she lies about planting a flower. The choice of whether to tell Tommy the truth about the crow affects his trust. The crow incident haunts her thoughts.

## Key Beats

- Rachel stiffened her nerves with a double vodka lemonade (with side of Prozac) before going outside
- Finds small spade in shed, digs shallow grave beneath old oak tree
- Rhythmic scrape of spade against damp earth — the only sound breaking the silence
- Tommy discovers her: "Mommy, what are you doing?"
- **Choice:** Tell Tommy the truth, or lie about planting a flower
  - Truth: Tommy asks to help; `told_truth_about_crow = True`
  - Lie: Tommy goes quiet; `tommys_trust -= 1`
- Rachel: "It's just a little bird that wasn't feeling well. We're helping it go to sleep."
- "But it wasn't. The crow wouldn't leave her mind."

## Choice Tracking

| Choice | Variable | Effect |
|--------|----------|--------|
| Bury crow in yard (not trash) | `crow_buried = True` | Set in Scene 1 |
| Tell Tommy the truth | `told_truth_about_crow = True` | Tommy trust maintained |
| Lie to Tommy | `told_truth_about_crow = False` | `tommys_trust -= 1` |

## Implementation

**Implemented in:** `game/script.rpy` — `act1_the_burial` label
**Placeholder images:** `game/images/backyard.png`, `game/images/rachel_takes_crow_outside.png`, `game/images/rachel_buries_crow.png`

## Next Scene

[[act1-scene3-research|Research and Reflection]] →
