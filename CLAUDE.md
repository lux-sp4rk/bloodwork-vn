# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Ren'Py visual novel game project based on the horror/thriller story "Digital Death Dolls" (working title: "Blood and Servos"). The game is a Kinetic Novel+ - primarily linear narrative with 2-3 major choice points leading to multiple endings.

**Target Release:** Halloween 2025

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
│   ├── gui/                # GUI images and overlays
│   ├── images/             # Scene backgrounds and illustrations
│   ├── gui.rpy             # GUI configuration
│   ├── options.rpy         # Game options and settings
│   ├── screens.rpy         # UI screens definition
│   └── script.rpy          # Main story script
└── .vscode/                # VS Code configuration
```

## Working with This Project

### Ren'Py Script Files (.rpy)
- **Primary script:** `game/script.rpy` - Main story implementation (currently Intro + Act 1)
- **Configuration:** `game/options.rpy` - Game title, version, resolution settings
- **GUI:** `game/gui.rpy` - Visual styling and theme customization
- **Screens:** `game/screens.rpy` - UI screen definitions

### Documentation Files
- **Design brief:** `docs/design-brief.md` - Overall game design and structure
- **Plot breakdown:** `docs/plot.md` - Scene-by-scene adaptation from manuscript
- **Characters:** `docs/characters.md` - Character profiles and relationships
- **Original manuscript:** `docs/manuscript.md` - Source material for adaptation

### Assets
- **Images:** Located in `game/images/` (backgrounds) and `game/gui/` (UI elements)
- **Audio:** Music in `game/audio/music/`, SFX in `game/audio/sfx/`
- Many assets are currently placeholders awaiting proper implementation

## Development Status

**Completed:** Basic Ren'Py project structure, configuration files, Intro + Act 1 script outline

**In Progress:** Script adaptation from manuscript, asset creation

**TODO:** Act 2 & 3 scripts, endings implementation, full asset creation

## Technical Notes

- **Engine:** Ren'Py 8.x
- **Language:** Ren'Py script language (Python-based)
- **Resolution:** 1920x1080
- **Theme:** Dark horror aesthetic (blacks, dark reds, grays)
- **Save System:** Ren'Py built-in
- **Running:** Open Ren'Py launcher, add project directory, click "Launch Project"

## Content Type

This is a horror visual novel about AI-powered toys that malfunction and attack the protagonist and her son. The story explores themes of grief, addiction, and the consequences of bringing back the dead.
