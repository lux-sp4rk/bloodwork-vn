# Digital Death Dolls - Design Brief

## Project Overview

**Format**: Kinetic Visual Novel+ (linear narrative with limited branching)
**Engine**: Ren'Py
**Target**: Halloween 2025 release
**Scope**: Text-focused with illustrations, sound effects, and music

## Narrative Approach

### Kinetic Novel+ Structure

The story is primarily linear, following the manuscript closely, with 2-3 major choice points that affect character relationships and lead to different endings. This approach:

- Preserves the tragic, inevitable spiral of Rachel's story
- Maintains horror pacing and atmosphere
- Allows polish on existing manuscript rather than writing 3x content
- Provides meaningful player agency at key emotional moments
- Offers replay value through multiple endings

### Why This Works

1. **Tragedy as Theme**: Rachel's inability to escape her circumstances (addiction, grief, poor decisions) is central to the horror
2. **Controlled Pacing**: Horror requires careful tension building that branching can disrupt
3. **Development Time**: More efficient for Halloween deadline
4. **Emotional Impact**: Players experience Rachel's descent rather than "fixing" her

## Choice Points

### Choice 1: The Burial (Early Game)
**Context**: Tommy discovers Rachel burying the crow in the backyard

**Options**:
- Tell him the truth about the dead bird
- Lie and say she's planting a flower

**Impact**:
- Affects Tommy's trust in Rachel
- Influences dialogue in later scenes
- Sets tone for their relationship

### Choice 2: After First Attack (Mid Game)
**Context**: Ninja has attacked Tommy; he's traumatized and won't sleep

**Options**:
- Give Tommy sedatives (crushed in milk)
- Stay awake with him all night

**Impact**:
- Affects Rachel's condition during later fights
- Changes available options in final confrontation
- Morality/guilt tracking

### Choice 3: Final Confrontation (Late Game)
**Context**: Headless Ninja attacks Rachel on the balcony

**Options**:
- Fight to protect Tommy (struggle, both fall)
- Try to run back inside (fail, both fall differently)
- Sacrifice yourself (push Ninja away, Rachel falls alone)

**Impact**:
- Determines which ending plays
- Tommy's fate
- Emotional resolution

## Endings

### Ending 1: Canon Tragic (Default)
- Rachel and Ninja fall from balcony
- Tommy wakes to sirens
- Sees mother's body below
- **Unlocked by**: Fighting to protect Tommy

### Ending 2: Sacrifice
- Rachel pushes Ninja away but falls alone
- Tommy found unharmed but traumatized
- Authorities puzzle over toy evidence
- **Unlocked by**: Choosing to sacrifice yourself

### Ending 3: Survivor's Guilt
- Rachel survives the fall, critically injured
- Ninja destroyed
- Rachel institutionalized, loses custody of Tommy
- Haunted by whether toys were real
- **Unlocked by**: Choosing to run + staying awake with Tommy (less injured, survives fall)

### Ending 4: Descent (Bad End)
- Rachel sedated Tommy + fights recklessly
- Both die in the confrontation
- Darkest ending
- **Unlocked by**: Sedating Tommy + choosing aggressive fight options

## Technical Implementation

### Engine: Ren'Py
**Features to use**:
- Persistent variables for endings unlocked tracker
- Choice menus with conditional logic
- Audio system (music loops, sound effects)
- Simple image display (backgrounds, illustrations)
- Built-in save/load system

### Visual Assets
**Minimal scope for timeline**:
- Key scene illustrations (5-7 major moments)
- Simple backgrounds (living room, bedroom, lab, backyard)
- No character sprites needed (text-only character presentation)
- Optional: silhouette/abstract imagery for horror effect

### Audio Assets
**Music** (AI-generated via Suno):
- Main menu theme (eerie, melancholic)
- Home atmosphere (tense, quiet)
- Flashback scenes (sad, nostalgic)
- Combat/chase (intense, chaotic)
- Endings (variant themes for each)

**Sound Effects**:
- Crow crash/window breaking
- Toy mechanical sounds (servos, clicking)
- Footsteps
- Breathing/heartbeat
- Fire crackling
- Ambient horror

### UI/UX Considerations
- Dark, minimalist UI fitting horror theme
- Clear choice presentation
- Endings gallery to track completion
- Chapter/scene selection after first playthrough

## Development Priorities

### Phase 1: Core Script
- Adapt manuscript to Ren'Py script format
- Implement choice points and branching logic
- Test all paths to all endings

### Phase 2: Audio
- Generate music tracks
- Source/create sound effects
- Implement audio cues

### Phase 3: Visuals
- Create key illustrations
- Add backgrounds
- Polish UI

### Phase 4: Testing & Polish
- Playtest all routes
- Balance pacing
- Bug fixes
- Final polish

## Scope Management

**Must Have**:
- Complete story adaptation
- All 3-4 endings working
- Basic music and sound effects
- Text presentation

**Nice to Have**:
- Full illustration set
- Advanced UI customization
- Voice acting
- Animated transitions

**Cut if Needed**:
- Character sprites
- Complex visual effects
- Extensive variation in dialogue
