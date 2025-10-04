## Blood and Servos - Main Script
## Based on "Digital Death Dolls" manuscript
##
## This is a kinetic visual novel with limited branching choices
## leading to different endings based on player decisions.

################################################################################
## Character Definitions
################################################################################

define rachel = Character("Rachel", color="#c8c8ff")
define tommy = Character("Tommy", color="#ffcc99")
define david = Character("David", color="#99ccff")
define dean = Character("Dean", color="#cccccc")

## Narrator for internal thoughts and descriptions
define narration = Character(None, kind=nvl)

################################################################################
## Story Variables
################################################################################

## Track player choices

default told_truth_about_crow = False

default sedated_tommy = False

default stayed_awake = False

## Condition tracking

default rachel_exhaustion = 0
default rachel_sanity = 3
default rachel_health = 0
default tommy_trust = 5

################################################################################
## Start of the Game
################################################################################

label start:

    scene black
    with fade

    "A story about grief, addiction, and the price of bringing back the dead..."

    ## TODO: Add opening narration and atmosphere setting

    jump scene_the_order


################################################################################
## INTRO
################################################################################

label scene_the_order:
    ## Scene 1: The Order
    ## Location: Rachel's bedroom
    scene house_exterior
    play sound "audio/sfx/rainstorm.ogg" loop volume 0.6

    with fade
    pause 2
    show bedroom_interior_rachel
    pause 3
    show computer_checkout_cart
    narration """
        Rachel clicked 'Place Order' on the NinjaMaster 9000 and its companion opponent, Viking Warrior.
        Tommy would finally have the AI battle toys he'd been begging for.
    """
    narration """
        She was about to close the website
        when the confirmation email dinged in her inbox.
    """
    nvl clear
    show crow_crashes_window
    narration """
        At that exact moment, a crow struck her bedroom window, glass exploding inward.
    """
    nvl clear
    show rachel_laptop_screaming
    narration """
        Rachel screamed as the crow's broken body tumbled onto her laptop, its wings splayed awkwardly, blood smearing across the glowing product photo of the toys. She felt a hot sting across her cheek and temple—glass shards from the shattered window had peppered her face.
    """
    nvl clear
    show crow_on_laptop
    narration """
        For a moment, the glowing red eyes of the NinjaMaster seemed to reflect in the bird's unseeing gaze.
    """
    jump scene_the_burial

label scene_the_burial:
    ## Scene 2: The Burial
    ## Location: Backyard

    scene backyard
    with fade

    ## TODO: Adapt manuscript content here
    ## - Rachel buries the crow
    ## - Tommy discovers her

    "Placeholder: Rachel digs in the backyard..."

    ## CHOICE POINT 1: Tell truth or lie about the crow
    menu:
        tommy "Mom? What are you doing?"

        "Tell him the truth about the dead bird":
            $ told_truth_about_crow = True
            $ tommy_trust += 10
            rachel "I'm burying a bird, honey. A crow flew through my window and... it didn't make it."
            tommy "Oh... that's sad. Can I help?"

        "Lie and say she's planting a flower":
            $ told_truth_about_crow = False
            $ tommy_trust -= 10
            rachel "Just planting a flower, sweetie. Nothing to worry about."
            tommy "But it doesn't look like a flower..."

    jump act1_research


################################################################################
## ACT 1
################################################################################

label act1_research:
    ## Scene 3: Research and Reflection
    ## Location: Living room couch

    scene living_room
    with fade

    ## TODO: Adapt manuscript content here
    ## - Rachel drinks vodka and Red Bull
    ## - Researches bird behavior
    ## - Wine glass with "Nevermore Sober!!"
    ## - Reflects on addiction

    "Placeholder: Rachel drinks and researches..."

    jump act1_flashback_lab


label act1_flashback_lab:
    ## Scene 4: University Flashback - The Lab
    ## Location: University paleontology lab

    scene lab_flashback
    with fade

    ## TODO: Adapt manuscript content here
    ## - Rachel drinking at work
    ## - David and students cover for her
    ## - Dean's visit
    ## - Put on leave

    "Placeholder: Flashback to the university lab..."

    jump act1_nighttime_vigil


label act1_nighttime_vigil:
    ## Scene 5: Nighttime Vigil
    ## Location: Tommy's doorway

    scene tommy_bedroom_doorway
    with fade

    ## TODO: Adapt manuscript content here
    ## - Rachel watches Tommy sleep
    ## - Reminisces about Ethan's death
    ## - Reflects on bulimia and substance abuse
    ## - Says "Addict" aloud

    "Placeholder: Rachel watches Tommy sleep..."

    jump act1_first_attack


label act1_first_attack:
    ## Scene 6: First Attack
    ## Location: Tommy's bedroom, night

    scene tommy_bedroom
    with fade

    play sound "audio/sfx/mechanical_hum.ogg"

    ## TODO: Adapt manuscript content here
    ## - Mechanical hum
    ## - Wine glass tips over
    ## - Tommy screams
    ## - Ninja attacks with plastic sword
    ## - Rachel throws toy out window

    "Placeholder: The Ninja attacks Tommy..."

    ## CHOICE POINT 2: How to handle Tommy's trauma
    menu:
        "How should I help Tommy get through this night?"

        "Give Tommy sedatives (crushed in milk)":
            $ sedated_tommy = True
            $ stayed_awake = False
            $ rachel_exhaustion -= 20
            r "Just drink this, honey. It'll help you sleep..."
            "Rachel crushed the pills into Tommy's milk, watching him drink it down."

        "Stay awake with him all night":
            $ sedated_tommy = False
            $ stayed_awake = True
            $ rachel_exhaustion += 30
            r "It's okay, baby. Mommy's going to stay right here with you."
            "Rachel settled in for a long, exhausting night..."

    ## End of Act 1
    scene black
    with fade

    "TO BE CONTINUED..."

    return
