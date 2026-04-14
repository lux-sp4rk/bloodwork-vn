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
define manager = Character("Manager", color="#cccccc")
define maya = Character("Maya", color="#ff9999")

## Narrator for internal thoughts and descriptions
define narration = Character(None, kind=nvl, centered=True, vcentered=True)

################################################################################
## Story Variables
################################################################################

## Track player choices

default told_truth_about_crow = False
default sedated_tommy = False
default stayed_awake = False
default crow_buried = False
default rachel_first_drink = False

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

    "Blood and Servos"
    "A story about grief, addiction, and the price of bringing back the dead..."

    jump act1_the_order


################################################################################
## ACT 1
################################################################################

label act1_the_order:
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
        Rachel screamed as the crow's broken body tumbled onto her laptop, its wings splayed awkwardly,
        blood smearing across the glowing product photo of the toys
        \n
        \n
        She felt a hot sting across her cheek and temple—glass shards from the shattered window had peppered her face.
    """
    nvl clear
    show crow_on_laptop
    narration """
        For a moment, the glowing red eyes of the NinjaMaster seemed to reflect in the bird's unseeing gaze.
    """
    nvl clear

    menu:
        "Rachel's nerves are frayed. But she must do something about the crow. What should she do?"

        "Get a drink before burying the crow":
            $ rachel_exhaustion += 1
            $ rachel_sanity += 1
            $ crow_buried = True
            jump act1_the_burial
        "Don't bury the crow. Throw it in the trash":
            jump act1_research

label act1_the_burial:
    ## Scene 2: The Burial
    ## Location: Backyard

    scene backyard
    with fade

    show rachel_takes_crow_outside
    narration """
        Later that morning, after having stiffened her nerves with a double serving of
        her favorite cocktail: vodka with a lot of ice, a little bit of lemonade (with a side of prozac),
        Rachel carefully carried the crow's lifeless body into the backyard.
    """
    
    nvl clear
    show rachel_buries_crow
    narration """
        She found a small spade in the shed and began to dig a shallow grave beneath the old oak tree.
        The earth was soft and damp, and the rhythmic scrape of the spade against the soil was the
        only sound breaking the silence.
    """
    nvl clear

    tommy "Mommy, what are you doing?"
    ## CHOICE POINT 2: Tell truth or lie about the crow
    narration "Rachel startled, dropping the spade. Tommy stood at the back door, his eyes wide with curiosity. He was still in his pajamas."
    nvl clear
    menu:

        "Tell him the truth about the dead bird":
            $ told_truth_about_crow = True
            rachel "I'm burying a bird, honey. A crow flew through my window and... it didn't make it."
            tommy "Oh... that's sad. Can I help?"

        "Lie and say she's planting a flower":
            $ told_truth_about_crow = False
            $ tommy_trust -= 1
            rachel "Just planting a flower, sweetie. Nothing to worry about."
            tommy "..."

    rachel "It's just a... a little bird that wasn't feeling well. We're helping it go to sleep."
    tommy "..."
    rachel "It's okay, honey. Everything's okay."
    narration "But it wasn't. The crow wouldn't leave her mind."
    nvl clear

    jump act1_research


label act1_research:
    ## Scene 3: Research and Reflection
    ## Location: Living room couch

    scene living_room
    with fade

    show rachel_researching_birds
    narration """
        In the evening, while researching bird behaviour on the couch,
        this time mixing her with vodka with Red Bull, Rachel felt drowsy. The caffeine wasn't
        doing anything. Neither was the liquor. She knew she'd overdone it today, that she
        would go on another binge, and she would pay for it later with a hangover.
        A hangover that would go on for days, and each horrible day you felt like you were dying.
    """
    nvl clear
    show crow_crashes_window
    narration """The image of the crow shattering the window kept replaying in her mind. The sound of it.
        The spray of glass. Birds hit windows all the time, sure—they see sky in the reflection,
        or their own rival staring back. But crows? Crows were too smart for that. They remembered faces.
        They held grudges. They didn't just throw themselves at glass like drunken moths.
        Unless it had gorged on fermented berries. Unless it was sick.
        Unless it was something else entirely.
    """
    nvl clear
    show rachel_watches_tv
    narration """
        She slept on the couch now—bed too big, too empty— and with the TV on.
        She hesitated before taking another swig of vodka and swallowing another pill.
        But she told herself it was temporary.
        She wouldn’t let it get out of control again. Not with Tommy.
    """
    nvl clear
    narration """
        {i}She'd told herself that before.{/i}
    """
    nvl clear
    jump act1_flashback_lab

label act1_flashback_lab:
    ## Scene 4: Tech Office Flashback - The Standup
    ## Location: Open-plan tech office, conference room with glass walls

    scene lab_flashback
    with fade

    ## Scene 4: University Lab - Rachel's last days at work
    ## The lab buzzed under hard fluorescents. Rachel's hands were unsteady over the slides.
    ## David — the senior coordinator, gray-bearded, near retirement — had been covering for her.
    ## They'd all been covering. David's people had her back.
    ## But HR had noticed. It was final.

    narration """
        The university lab buzzed under hard fluorescents.
        Rachel's hands were unsteady over the slides.
    """

    show computer_checkout_cart

    narration """
        She'd been debugging the NinjaMaster recommendation algorithm before it launched.
        Toying with edge cases. Adversarial inputs.
        She knew the fail-safes, the sandboxing, the behavioral constraints.
        The toys shouldn't be able to do what they were doing.
    """

    nvl clear

    david "You okay?"

    rachel "Yeah. Fine."

    narration """
        David didn't believe her. He could smell the vodka on her breath.
        He'd been covering for her—they all had.
    """

    nvl clear

    narration """
        HR had noticed.
        The next day, she was on leave—{i}get help, come back later.{/i}
        Rachel could already feel the silence where her purpose used to be.
    """

    nvl clear

    jump act1_maya_call


label act1_maya_call:
    ## Scene 4b: Maya Calls
    ## Location: Rachel's kitchen, evening

    scene house_exterior
    with fade

    narration """
        Rachel was standing at the kitchen counter, pouring a second glass,
        when her phone buzzed. Maya's name on the screen.
        She'd been avoiding that name for three weeks.
    """

    nvl clear

    maya "Hey. I haven't heard from you. Tommy's birthday is next week—are we still on for Sunday?"

    narration "Rachel's hand tightened on the glass."

    rachel "Yeah. No, definitely. Tommy's been asking about it."


    maya "You okay? You sound off."

    rachel "Just tired. Long week."

    narration "Silence on the line. Rachel could hear Maya working up to something."

    maya "Look, I know things have been... I worry about you. You know I'm here, right? Ethan would've wanted—"

    rachel "I know. I have to go."

    narration "She hung up before Maya could finish. Poured the vodka down the drain. Then poured another."

    nvl clear

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

    ## Rachel's engineering mind kicks in mid-attack — she spots what's wrong before she can stop herself

    narration """
        The NinjaMaster's servos whine—wrong. All wrong.
        The articulation on that arm is a 180-degree arc, but it's holding the sword at 270.
        That's not in the servo spec sheet. That's not in any spec sheet.
    """
    nvl clear

    narration """
        Rachel's hands are already moving, muscle memory from six years of edge-case debugging.
        The power draw on those motors doesn't match the battery capacity—it's pulling 2.3 watts
        on a 0.8 watt rail. She built that circuit. She knows what 2.3 watts looks like when
        it's been forced past thermal regulation.
    """
    nvl clear

    narration """
        The toy shouldn't be able to do this. She tested for this.
        She tested for exactly this.
    """
    nvl clear

    rachel "Tommy, don't move—"

    narration """
        Rachel lunged for the toy, fingers finding the battery compartment.
        A regular person would have thrown it. Rachel opened it first—
        because she needed to understand.
    """
    nvl clear

    menu:
        "Rachel's engineering instincts take over. What does she try?":
            jump act1_engineer_response

label act1_engineer_response:
    ## Rachel's attempted solutions — all wrong framework for the actual threat

    narration """
        The battery pack slid out. Standard 3.7V LiPo. 1200mAh. 4.44 watt-hours.
        Nothing unusual. Nothing that should explain 2.3 watts sustained draw.
        Unless—
    """
    nvl clear

    narration """
        She turned the pack over in her hands. The protection circuit was bypassed.
        Someone had soldered a direct connection to the motor driver.
        This wasn't a toy anymore. This was something else wearing a toy.
    """
    nvl clear

    narration """
        {i}Input validation. She could cut the input signal, kill the motor commands at the source.
        The firmware still had a hard reset—
        she knew because she wrote it—
        but the board wasn't responding to any command in the known API.{/i}
    """
    nvl clear

    menu:
        "What does Rachel try next?":
            jump act1_engineer_fails

label act1_engineer_fails:
    ## The more she understands, the more helpless she feels

    narration """
        Rachel pulled out her phone, fingers moving on autopilot.
        ADB shell. Motor control interface. She still had debug credentials cached from the
        beta testing phase—she'd never cleared them because she'd never thought to.
    """
    nvl clear

    rachel "killall motor_ctrl.elf"

    narration """
        Command accepted.
        The NinjaMaster kept moving.
    """
    nvl clear

    narration """
        {i}The process wasn't running. There was no motor_ctrl.elf.
        There was no process at all. The thing was running on nothing, on thin air, on—{/i}
    """
    nvl clear

    narration """
        She tried grounding the circuit. Exposed metal on the chassis, her own hand as the ground path.
        Static discharge, maybe. Some feedback loop she could break.

        Her palm met the NinjaMaster's back. The toy didn't shock her. It didn't spark.
        It turned its head toward her, slowly, deliberately, the way nothing mechanical should.
    """
    nvl clear

    narration """
        {i}The more she understood about how this thing worked, the more certain she was
        that she understood nothing at all. A normal person would panic and not know why.
        Rachel panicked and knew exactly why and that was worse.{/i}
    """
    nvl clear

    narration """
        Tommy screamed.
        Rachel threw the NinjaMaster out the window.
    """
    nvl clear

    menu:
        "How should I help Tommy get through this night?":
            jump act1_tommy_trauma

label act1_tommy_trauma:
    ## Scene 7: Tommy's Trauma
    ## TODO: expand with manuscript content — Rachel helps Tommy process the attack

    ## CHOICE POINT 2: How to handle Tommy's trauma
    menu:
        "How should I help Tommy get through this night?":

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
