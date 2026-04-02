# AGENTS.md - Digital Death Dolls

## Project Intent

Ren'Py-based horror/thriller Kinetic Novel+ about AI toys ("Blood and Servos").

## Stack & Tooling

| Layer     | Technology | Notes |
| --------- | ---------- | ----- |
| Engine    | Ren'Py 8.x | 1920x1080 resolution [game/options.rpy:13](game/options.rpy:13) |
| Scripting | Ren'Py DSL | Main script at [game/script.rpy:1](game/script.rpy:1) |
| UI/GUI    | Ren'Py GUI | Custom config at [game/gui.rpy:15](game/gui.rpy:15) |

**Non-obvious:** Dark horror aesthetic (blacks, dark reds, grays). Target Release: Halloween 2025.

## Essential Commands

```bash
# Run/Launch (External)
# Use Ren'Py Launcher to add project and "Launch Project"
```

## Git Workflow

**Standard PR-first. No direct push to main.**

```bash
# Branch naming
feature/scene-123-description
```

## Key Patterns

| Pattern           | Location                                |
| ----------------- | --------------------------------------- |
| Story Script      | [game/script.rpy:1](game/script.rpy:1)  |
| UI Screens        | [game/screens.rpy:1](game/screens.rpy:1)|
| Game Config       | [game/options.rpy:13](game/options.rpy:13)|

## Quick References

- Design Brief: [docs/design-brief.md](docs/design-brief.md)
- Plot Breakdown: [docs/plot.md](docs/plot.md)
- Characters: [docs/characters.md](docs/characters.md)
- Manuscript: [docs/manuscript.md](docs/manuscript.md)

## Constraints

- Resolution: 1920x1080
- Theme: Dark horror (blacks, dark reds, grays)
