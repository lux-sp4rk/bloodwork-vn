---
title: "Scene 6: First Attack"
type: scene
act: 1
status: implemented
script_label: act1_first_attack
related:
  - "[[act1-scene5-vigil]]"
  - "[[act2-scene7-aftermath]]"
  - "[[rachel]]"
  - "[[tommy]]"
  - "[[ninjamaster]]"
---

# Scene 6: First Attack

**Location:** Tommy's bedroom, night
**Characters:** [[rachel|Rachel]], [[tommy|Tommy]], [[ninjamaster|NinjaMaster 9000]]
**Script label:** `act1_first_attack`

## Summary

A mechanical hum and metallic voice ("By the blood of the dragon, target confirmed!") wake Rachel. Her wine glass printed with a drunken crow and "Nevermore Sober!!" tips over, spilling cranberry vodka. Tommy screams as the Ninja repeatedly stabs him with its sharpened plastic sword, blood blooming across his dinosaur pajamas. Rachel lunges, grabbing the Ninja; it cuts her forearm and she feels something pop in her wrist. She hurls it out the window, locks it, and passes out.

## Key Beats

- Mechanical hum and metallic voice wake Rachel
- Wine glass ("Nevermore Sober!!") tips over, spilling cranberry vodka
- Tommy screams as Ninja stabs him repeatedly with sharpened plastic sword
- Blood blooms across dinosaur pajamas
- Rachel lunges, grabs Ninja — it cuts her forearm, something pops in her wrist
- She hurls Ninja out the window, locks it
- She passes out
- **Choice:** Give Tommy sedatives (crushed in milk) or stay awake with him all night
  - Sedatives: `sedated_tommy = True`, `stayed_awake = False`, exhaustion decreased
  - Stay awake: `sedated_tommy = False`, `stayed_awake = True`, `rachel_exhaustion += 30`

## Choice Tracking

| Choice | Variable | Effect |
|--------|----------|--------|
| Give sedatives | `sedated_tommy = True` | Tommy sleeps; Rachel's exhaustion decreases |
| Stay awake | `stayed_awake = True` | `rachel_exhaustion += 30` |

## Implementation

**Implemented in:** `game/script.rpy` — `act1_first_attack` label (partial — choice implemented, attack narration is placeholder)
**Placeholder images:** `game/images/tommy_bedroom.png`
**Audio:** `game/audio/sfx/mechanical_hum.ogg`

## Next Scene

[[act2-scene7-aftermath|Scene 7: Aftermath]] →
