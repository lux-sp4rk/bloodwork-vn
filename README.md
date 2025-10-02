# Blood and Servos

A horror visual novel about artificial intelligence, grief, and the price of bringing back the dead.

Based on the manuscript "Digital Death Dolls."

## Project Structure

```
digital-death-dolls/
├── docs/                    # Design documentation and manuscript
│   ├── design-brief.md      # Visual novel design brief
│   ├── characters.md        # Character profiles
│   ├── manuscript.md        # Original story manuscript
│   └── plot.md             # Scene-by-scene plot breakdown
├── game/                    # Ren'Py game files
│   ├── audio/              # Sound effects and music
│   │   ├── music/          # Background music tracks
│   │   └── sfx/            # Sound effects
│   ├── gui/                # GUI images and overlays
│   ├── images/             # Scene backgrounds and illustrations
│   ├── gui.rpy             # GUI configuration
│   ├── options.rpy         # Game options and settings
│   ├── screens.rpy         # UI screens definition
│   └── script.rpy          # Main story script (Intro + Act 1)
├── CLAUDE.md               # Instructions for Claude Code
└── README.md               # This file
```

## Development Status

### ✅ Completed
- Basic Ren'Py project structure
- Configuration files (options.rpy, gui.rpy, screens.rpy)
- Script outline for Intro and Act 1
- Placeholder asset structure

### 🚧 In Progress
- Script adaptation from manuscript (Intro + Act 1 only)
- Asset creation (images, audio)

### 📋 TODO
- Complete script for Act 2
- Complete script for Act 3
- Implement ending variations
- Create/source scene background images
- Create/source GUI graphics
- Generate music tracks (via AI tools like Suno)
- Source/create sound effects
- Create key scene illustrations
- Implement endings gallery
- Playtesting and polish

## Setup Instructions

### Prerequisites
1. Install Ren'Py SDK from https://www.renpy.org/
2. Python 3 (for any custom tooling)

### Running the Game
1. Open the Ren'Py launcher
2. Add the `digital-death-dolls` directory as a project
3. Click "Launch Project"

**Note:** Currently, many assets are placeholder files. The game will run but scenes will appear blank until proper images are added.

## Asset Requirements

### Images Needed
- **GUI elements** (game/gui/):
  - Main menu background (1920x1080)
  - Game menu background
  - Textbox (1280x240)
  - Namebox (360x80)
  - Window icon

- **Scene backgrounds** (game/images/):
  - bedroom.png - Rachel's bedroom
  - backyard.png - Backyard with oak tree
  - living_room.png - Living room/couch
  - lab_flashback.png - University paleontology lab
  - tommy_bedroom_doorway.png - View into Tommy's room
  - tommy_bedroom.png - Tommy's bedroom interior

### Audio Needed
- **Music** (game/audio/music/):
  - Main menu theme
  - Home atmosphere (tense, quiet)
  - Flashback scenes (sad, nostalgic)

- **Sound Effects** (game/audio/sfx/):
  - mechanical_hum.ogg - Toy servo sounds
  - Crow crash/window breaking
  - Footsteps
  - Ambient horror

## Story Structure

### Intro
- Scene 1: The Order (crow crashes through window)
- Scene 2: The Burial (first choice point)

### Act 1
- Scene 3: Research and Reflection
- Scene 4: University Flashback - The Lab
- Scene 5: Nighttime Vigil
- Scene 6: First Attack (second choice point)

### Act 2 (TODO)
- Scenes 7-10

### Act 3 (TODO)
- Scenes 11-15

### Endings (TODO)
- Ending 1: Tragic Fall
- Ending 2: Sacrifice
- Ending 3: Survivor's Guilt
- Ending 4: Descent

## Design Philosophy

This is a **Kinetic Novel+** - primarily linear narrative with 2-3 major choice points that lead to different endings. This approach:
- Preserves the tragic, inevitable spiral of Rachel's story
- Maintains horror pacing and atmosphere
- Allows focus on polish rather than extensive branching
- Provides meaningful player agency at key emotional moments

## Technical Notes

- **Engine:** Ren'Py 8.x
- **Target Resolution:** 1920x1080
- **Horror Theme:** Dark color palette (dark reds, blacks, grays)
- **Text Speed:** 50 cps default
- **Save System:** Ren'Py built-in

## License

[Add license information here]

## Credits

Story: [Author name]
Adaptation: [Your name]
Engine: Ren'Py

---

*Target Release: Halloween 2025*
