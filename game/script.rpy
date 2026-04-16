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

## Addiction / Stress Mechanic
default rachel_stress = 20          # 0-100; crisis at >= 70
default rachel_booze = 1           # bottles remaining — started with 2, crow broke one
default rachel_shots = 15         # 1.5L bottle / 100ml per shot = 15 shots
default rachel_dependency = 0       # 0-100; fog at >=50, shaky at >=75
default rachel_fog = False         # locked dialogue options
default rachel_shaky = False       # harder QTEs
default withdrawal_turns_since_drink = 0  # increments each turn with 0 booze
default withdrawal_active = False  # body failing without supply

## Condition tracking

default rachel_exhaustion = 0
default rachel_sanity = 3
default rachel_health = 0
default tommy_trust = 5

################################################################################
## Start of the Game
################################################################################



################################################################################
## ADDICTION / STRESS SYSTEM
################################################################################

## called after any stress spike. checks threshold and offers drink/cope choice.
label check_stress_crisis:
    ## Buzz check — if enough turns passed without drinking, force crisis
    if withdrawal_turns_since_drink >= 7:
        jump stress_crisis_choice
    if rachel_stress >= 70:
        jump stress_crisis_choice
    ## No crisis, no drink — turn passes, buzz wears off slightly
    if rachel_booze == 0:
        $ withdrawal_turns_since_drink += 1
    return

label stress_crisis_choice:
    ## Withdrawal tick — if out of booze, accumulate withdrawal
    if rachel_booze == 0:
        $ withdrawal_turns_since_drink += 1
        if withdrawal_turns_since_drink >= 7:
            $ withdrawal_active = True

    if withdrawal_active:
        narration """
            Rachel's hands are shaking. The room keeps tilting at the edges.
            Her body is screaming for something that isn't here.
            She's starting to feel feverish. Her vision is going blurry at the edges.
            She knows what's coming next if she doesn't drink soon.
        """
        menu:
            "She needs a drink. Any drink." if rachel_booze > 0:
                jump rachel_takes_drink_critical
            "She has to push through.":
                $ rachel_stress += 20
                $ withdrawal_turns_since_drink += 2
                narration """"
                    She steadies herself. Her vision swims.

                    The toys seem to move in the corner of her eye.
                """
                jump check_stress_crisis
        return

    menu:
        "She needs a drink to get through this." if rachel_booze > 0:
            jump rachel_takes_drink
        "Find another way to cope.":
            jump rachel_cope_attempt

label rachel_takes_drink:
    $ rachel_shots -= 1
    if rachel_shots <= 0:
        $ rachel_booze = 0
    $ rachel_stress -= 40
    $ rachel_dependency += 15
    $ withdrawal_turns_since_drink = 0
    if rachel_dependency >= 50:
        $ rachel_fog = True
    if rachel_dependency >= 75:
        $ rachel_shaky = True
    narration """"
        Rachel poured a drink. The world went soft at the edges.
        She could breathe again.
    """
    jump check_stress_crisis

label rachel_takes_drink_critical:
    $ rachel_shots -= 1
    if rachel_shots <= 0:
        $ rachel_booze = 0
    $ rachel_stress -= 40
    $ rachel_dependency += 15
    $ withdrawal_turns_since_drink = 0
    $ withdrawal_active = False
    if rachel_dependency >= 50:
        $ rachel_fog = True
    if rachel_dependency >= 75:
        $ rachel_shaky = True
    narration """"
        Her hands shook as she poured. She didn't taste it.
        The relief was immediate and chemical and it didn't matter what it cost.
    """
    jump check_stress_crisis

label rachel_cope_attempt:
    ## Cope options - good ones narrow as dependency rises
    if rachel_fog:
        ## Fog state: constructive options gone, only escape options
        menu:
            "Zone out. Disappear into the screen.":
                narration """"
                    She stared at the phone. Then put it down.
                    Easier to disappear than to be seen failing.
                """
                $ rachel_stress -= 5
                $ withdrawal_turns_since_drink += 2
                jump check_stress_crisis
            "Pick a fight with Maya in her head.":
                narration """"
                    She rehearsed every sharp thing she'd never say.
                    The anger was easier than the grief.
                """
                $ rachel_stress -= 5
                $ withdrawal_turns_since_drink += 2
                jump check_stress_crisis
    elif rachel_dependency >= 30:
        ## Mid-dependency: healthy options still there but strained
        menu:
            "Call Maya." if not renpy.seen_label("maya_called_this_session"):
                narration """"
                    She called Maya. The voice on the other end was warm.
                    Maya did not push. That was enough.
                """
                $ rachel_stress -= 15
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Hold Tommy.":
                narration """"
                    She held Tommy. The warmth of a living body.
                    He did not ask questions. She loved him for that.
                """
                $ rachel_stress -= 15
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Breathe. Count. Wait.":
                narration """"
                    She sat down. She breathed. She counted to ten.
                """
                $ rachel_stress -= 10
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
    else:
        ## Low dependency: full menu of constructive options
        menu:
            "Call Maya." if not renpy.seen_label("maya_called_this_session"):
                narration """"
                    She called Maya. The voice on the other end was warm.
                    Just that. Just a warm voice.
                """
                $ rachel_stress -= 20
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Hold Tommy.":
                narration """"
                    She held Tommy until her heartbeat slowed.
                    The warmth of a living body was enough. For now.
                """
                $ rachel_stress -= 20
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Go outside. Get air.":
                narration """"
                    She stepped onto the porch. The air was cool.
                    For a moment, the world was just air and birdsong.
                """
                $ rachel_stress -= 20
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Breathe. Count. Wait.":
                narration """"
                    She sat down. She breathed. She counted to ten.
                    The world held.
                """
                $ rachel_stress -= 15
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisisa living body was enough. For now.
                """
                $ rachel_stress -= 15
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Breathe. Count. Wait.":
                narration """"
                    She sat down. She breathed. She counted to ten.
                    The world held.
                """
                $ rachel_stress -= 15
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis

################################################################################
## STRESS SPIKE MACRO — call with e.g. call checkpoint_add_stress(30)
################################################################################

init python:
    def add_stress(amount):
        renpy.store.rachel_stress = min(100, renpy.store.rachel_stress + amount)
        renpy.jump('check_stress_crisis')


label start:

    scene black
    with fade

    "Blood and Servos"
    "A story about grief, addiction, and the price of bringing back the dead..."

    show screen status_screen

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

    ## Crow breaks one of two bottles — she started with 2, now has 1 (15 shots)
    $ rachel_booze = 1
    $ rachel_shots = 15
    $ renpy.notify("One 1.5L bottle shattered. 15 shots left.")

    narration """
        The crow's body had knocked against the desk on its way in.
        One of the two bottles of vodka she'd kept next to her laptop was in pieces on the floor,
        glass and liquor spreading across the hardwood.




        The other was still standing. Half full. Fifteen shots, maybe.
        She'd counted once. She always knew exactly how much she had.
    """
    nvl clear

    menu:
        "Rachel's nerves are frayed. But she must do something about the crow. What should she do?"

        "Get a drink before burying the crow":
            $ rachel_exhaustion += 1
            $ rachel_sanity += 1
            $ crow_buried = True
            $ rachel_stress += 15
            call check_stress_crisis
            jump act1_the_burial
        "Don't bury the crow. Throw it in the trash":
            $ rachel_stress += 15
            call check_stress_crisis
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

    $ rachel_stress += 15
    call check_stress_crisis

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

    $ rachel_stress += 30
    call check_stress_crisis

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
                $ rachel_stress += 10
                call check_stress_crisis
                r "Just drink this, honey. It'll help you sleep..."
                "Rachel crushed the pills into Tommy's milk, watching him drink it down."

            "Stay awake with him all night":
                $ sedated_tommy = False
                $ stayed_awake = True
                $ rachel_exhaustion += 30
                $ rachel_stress += 10
                call check_stress_crisis
                r "It's okay, baby. Mommy's going to stay right here with you."
                "Rachel settled in for a long, exhausting night..."

    ## End of Act 1
    scene black
    with fade

    "TO BE CONTINUED..."

    return
