## Bloodwork - Main Script
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
define ninjamaster = Character("NinjaMaster", color="#888888")
define viking = Character("Viking", color="#ffaa44")

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

## Act 2 injury tracking
default hand_nailed = False       # Ninja stabbed through palm
default foot_pierced = False      # rusty nail through arch
default eye_infected = False      # crow glass shard gone septic
default viking_in_fishtank = False
default viking_limbless = False

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
                narration """
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
    narration """
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
    narration """
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
                narration """
                    She stared at the phone. Then put it down.
                    Easier to disappear than to be seen failing.
                """
                $ rachel_stress -= 5
                $ withdrawal_turns_since_drink += 2
                jump check_stress_crisis
            "Pick a fight with Maya in her head.":
                narration """
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
                narration """
                    She called Maya. The voice on the other end was warm.
                    Maya did not push. That was enough.
                """
                $ rachel_stress -= 15
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Hold Tommy.":
                narration """
                    She held Tommy. The warmth of a living body.
                    He did not ask questions. She loved him for that.
                """
                $ rachel_stress -= 15
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Breathe. Count. Wait.":
                narration """
                    She sat down. She breathed. She counted to ten.
                """
                $ rachel_stress -= 10
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
    else:
        ## Low dependency: full menu of constructive options
        menu:
            "Call Maya." if not renpy.seen_label("maya_called_this_session"):
                narration """
                    She called Maya. The voice on the other end was warm.
                    Just that. Just a warm voice.
                """
                $ rachel_stress -= 20
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Hold Tommy.":
                narration """
                    She held Tommy until her heartbeat slowed.
                    The warmth of a living body was enough. For now.
                """
                $ rachel_stress -= 20
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Go outside. Get air.":
                narration """
                    She stepped onto the porch. The air was cool.
                    For a moment, the world was just air and birdsong.
                """
                $ rachel_stress -= 20
                $ withdrawal_turns_since_drink += 1
                jump check_stress_crisis
            "Breathe. Count. Wait.":
                narration """
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

    "Bloodwork"
    "A story about grief, addiction, and the price of bringing back the dead..."

    show screen status_screen

    jump cold_open_bathroom


################################################################################
## COLD OPEN
################################################################################

label cold_open_bathroom:

    scene black
    with fade

    nvl clear
    narration """
        The tile was cold through her jeans.
        She'd been here long enough that it didn't register anymore.
    """
    nvl clear

    narration """
        Her body finished what it was doing.
        She waited.
    """
    nvl clear

    narration """
        Eventually she got up.
        Ran the tap. Rinsed twice.
        Looked at her face in the mirror the way you check a clock — 
        just to confirm the time, not because you want to know it.
    """
    nvl clear

    narration """
        Tommy was still asleep.
        She'd heard him turn over twenty minutes ago. Nothing since.
    """
    nvl clear

    narration """
        She went to the bedroom, opened the laptop,
        and finished what she'd been about to do before.
    """
    nvl clear

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

    ## PRE-CRASH BEAT — The Entity reaches before it has a vessel
    narration """
        The laptop screen flickered. Just once. A thin line of static
        crawled across the display, then vanished.
    """
    nvl clear
    narration """
        The cursor blinked twice on its own. Then returned to normal.
    """
    nvl clear
    narration """
        The room went quiet. The rain sound dropped for a half-second,
        like something was listening.
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
        "How should I help Tommy get through this night?"

        "Give Tommy sedatives (crushed in milk)":
            $ sedated_tommy = True
            $ stayed_awake = False
            $ rachel_exhaustion -= 20
            $ rachel_stress += 10
            call check_stress_crisis
            rachel "Just drink this, honey. It'll help you sleep..."
            "Rachel crushed the pills into Tommy's milk, watching him drink it down."

        "Stay awake with him all night":
            $ sedated_tommy = False
            $ stayed_awake = True
            $ rachel_exhaustion += 30
            $ rachel_stress += 10
            call check_stress_crisis
            rachel "It's okay, baby. Mommy's going to stay right here with you."
            "Rachel settled in for a long, exhausting night..."

    ## End of Act 1
    scene black
    with fade

    "TO BE CONTINUED..."

    return


################################################################################
## ACT 2
################################################################################

## Scene 7: Aftermath
label act2_aftermath:
    scene black
    with fade

    nvl clear
    narration """
        She slid down the bathroom wall and sat on the cold tile,
        knees drawn up, arms wrapped around herself like she was the only
        thing holding her together.
    """
    nvl clear

    narration """
        The taste in her mouth was wrong. Not bile — something thicker.
        She leaned over the toilet and heaved again, and what came up
        was dark red. Cranberry vodka and blood. She couldn't tell which
        was which anymore.
    """
    nvl clear

    narration """
        Her cheek was singing fire. The glass shard from the crow was still
        embedded just below her eye — she'd tried to pull it out twice
        and both times her hands had shaken too badly to get a grip.
        The skin around it was inflamed, angry red, and when she touched
        the edge of the shard, pus threatened at the corners.
    """
    nvl clear

    narration """
        The front door was locked. She'd checked the windows twice.
        Barricaded with chairs, with the bookshelf, with anything
        that could hold. She didn't know what she was keeping out.
        She didn't know if anything was left to come in.
    """
    nvl clear

    narration """
        Tommy was upstairs. Finally sleeping. She'd crushed half a
        sedative into his milk and watched him drink it down,
        counting his breaths until they went slow and even.
        The dinosaur pajamas were crusted with blood — his blood,
        all of it his. Deep punctures still leaking. One cut that had
        gone past skin into the yellow fat beneath.
    """
    nvl clear

    narration """
        She'd called no one. Could call no one.
        The police would come and they'd smell the open bottle
        on the counter and the bruise blooming on her arm where
        she'd tried to stop the Ninja and they'd draw conclusions.
        Wrong conclusions. Worse conclusions.
        She couldn't afford wrong.
    """
    nvl clear

    $ rachel_stress += 10
    call check_stress_crisis

    jump act2_kitchen_ambush


## Scene 8: Kitchen Ambush
label act2_kitchen_ambush:
    scene kitchen
    with fade

    nvl clear
    narration """
        Hours later. Her stomach growling.
        She padded to the kitchen in bare feet, blood-crusted
        pajamas stiff and wrong against her skin. Half-expected
        to wake up. To find the morning had been the nightmare
        and this was the life she'd always known.
    """
    nvl clear

    narration """
        She stood at the counter and ate celery with peanut butter.
        Drank a mixed drink while she chewed. The vodka was warm
        going down and the burn was almost pleasant now.
        Almost familiar.
    """
    nvl clear

    narration """
        The knife block was behind her. She reached back for it
        without looking and her hand closed on empty air.
        The block was right where it always was. The knives were not.
    """
    nvl clear

    ninjamaster "...Got you."

    nvl clear
    narration """
        The NinjaMaster moved like nothing she'd seen before —
        no whir of servos, no mechanical hesitation. It simply
        appeared behind her and the knife was through her palm
        before she could understand what was happening.
    """
    nvl clear

    narration """
        The blade punched through the meat of her hand and erupted
        from the back — six inches of kitchen steel jutting from
        beneath her ring finger, glistening. The NinjaMaster twisted
        its wrist and the blade ground against the bones of her palm
        with a sound like someone scraping a magnet on a chalkboard.
    """
    nvl clear

    narration """
        Blood sprayed across the counter in arterial pulses.
        She could see white bone — the handle had driven flush
        against her palm and she could see the round end of her
        metacarpal grinding against steel. The tendons tore with
        a nauseating pop and her fingers spasmed, curling inward
        like claws.
    """
    nvl clear

    rachel "FUCK—"

    narration """
        She grabbed the NinjaMaster's other arm with her free hand —
        the toy was already raising its blade for the finishing strike —
        and she slammed its wrist down against the counter edge.
        Once. Twice. The third time, something gave and the toy released.
    """
    nvl clear

    narration """
        The NinjaMaster made a sound — not electronic, not mechanical.
        Something wet. Like a cough. Like disappointment.
    """
    nvl clear

    narration """
        She pulled the knife from her palm and the sound was
        a wet sucking pop, like pulling a plug from a drain.
        Blood ran freely, the wound opening like a mouth.
        She wrapped her hand in a dish towel and it soaked through
        crimson almost immediately.
    """
    nvl clear

    $ rachel_stress += 25
    $ hand_nailed = True
    call check_stress_crisis

    ninjamaster "...Process... terminated..."

    narration """
        Rachel grabbed the cast-iron frying pan from the stove.
        She swung it like a golf club and connected with the
        NinjaMaster's head in a crack of plastic and metal.
        The toy staggered. She swung again. And again.
    """
    nvl clear

    narration """
        The third blow took it off its feet entirely. The head was
        caved in. Circuit boards and wiring spilled from the fracture.
        The servos twitched once, twice, then went still.
    """
    nvl clear

    narration """
        Rachel stood over it, breathing hard, the pan still raised.
        The toy didn't move anymore. But it wasn't over.
        She knew it wasn't over.
    """
    nvl clear

    jump act2_the_trap


## Scene 9: The Trap
label act2_the_trap:
    scene hallway_stairs
    with fade

    nvl clear
    narration """
        She had to check on Tommy. Had to know he was still breathing.
        Had to know the sedatives hadn't taken too much.
    """
    nvl clear

    narration """
        She climbed the stairs on her knees because her feet couldn't
        take it anymore. The left foot was still bleeding through the
        dish towel she'd wrapped around it — the nail had torn through
        the arch between the metatarsals, a ragged exit wound that
        pulped the sole. She could feel the wet heat of it every time
        she shifted her weight.
    """
    nvl clear

    narration """
        Halfway up, her bare foot came down on something cold and hard.
        Long. Rusty. Metal.
    """
    nvl clear

    narration """
        The nail punched through the soft arch of her foot like
        a thumbtack through paper. Three inches of rusty steel,
        driven between the metatarsal bones, scraping against
        the top of her foot from the inside. She could feel every
        ridge of rust against the top of her foot. Could feel it
        pushing, insistent, like it wanted through.
    """
    nvl clear

    rachel "No—"

    narration """
        She tried to lift her foot. The nail scraped against bone.
        She could feel the exact shape of her own metatarsal
        grinding against iron. Every nerve lit up and her vision
        went white at the edges and she screamed but her body
        wouldn't let her lift — it was stuck, the foot was stuck
        and she was stuck and—
    """
    nvl clear

    narration """
        The nail tore free with a sound like a branch breaking.
        A wet, pulpy pop. The exit wound was ragged, the sole
        split open like overripe fruit. Blood ran down onto
        the stair carpet in a spreading stain.
    """
    nvl clear

    narration """
        Rachel collapsed. Her head hit the banister with a crack
        that she felt more than heard. The world tilted.
        The stairs swam. The last thing she saw was the crow
        feather on the carpet — gray-black, glistening —
        before everything went dark.
    """
    nvl clear

    $ rachel_stress += 20
    $ foot_pierced = True
    call check_stress_crisis

    jump act2_awakening


## Scene 10: Awakening
label act2_awakening:
    scene bedroom
    with fade

    nvl clear
    narration """
        A sound woke her. Loud. Harsh. A crow's screech
        torn through speakers not built to scream.
    """
    nvl clear

    narration """
        She opened her eyes to the flutter of wings. Not real wings —
        shadows on the wall, shapes that moved like wings, cast
        by something she couldn't see. Her head was pounding.
        Her foot was singing. Her hand was a closed fist she
        couldn't open.
    """
    nvl clear

    narration """
        She looked at her hand. The right one. The one the knife
        had gone through. It was curled inward, fingers locked
        into a claw. The tendons she'd heard tear were done —
        the fingers would never open properly again. The towel
        was soaked through and stiff and the wound had bled
        through to the sheets.
    """
    nvl clear

    narration """
        Her foot was worse. She'd wrapped it in a fresh towel and
        it was already red. The exit wound had torn wider and
        the sole of her foot was a mess of pulped tissue and
        exposed meat. She couldn't stand on it.
    """
    nvl clear

    narration """
        And her face — God, her face. The glass shard below
        her eye was hot to the touch and when she finally
        got her trembling fingers on it and worked it free,
        what came out was blue-green and stinking. The wound
        was ulcerated. Infected. The skin around it was yellow
        with pus and the smell was like death.
    """
    nvl clear

    $ rachel_stress += 15
    $ eye_infected = True
    call check_stress_crisis

    narration """
        From the hallway, a sound: metallic clicking and dragging.
        Something being pulled across the floor. Something heavy
        and broken and still moving.
    """
    nvl clear

    narration """
        Rachel pushed herself up against the headboard. Her body
        screamed at every movement. She grabbed the lamp
        from the nightstand — the only weapon she had —
        and waited in the dark.
    """
    nvl clear

    jump act2_wrestling_match


## Scene 11: The Wrestling Match
label act2_wrestling_match:
    scene hallway_stairs
    with fade

    nvl clear
    narration """
        The door to the hallway was open. She hadn't left it open.
        The darkness beyond was thick and wrong and Rachel held
        the lamp above her head like a club.
    """
    nvl clear

    narration """
        Two shapes in the hallway. The NinjaMaster — mangled, one
        arm hanging limp, head caved in — was holding a kitchen
        knife in its functional hand. The Viking was crouched
        at the other end, scissors extended, eyes glowing amber.
    """
    nvl clear

    ninjamaster "...Requesting... reinforcement..."
    viking "...Negative."

    narration """
        The TV in the living room flickered to life.
    """
    nvl clear

    scene living_room
    with fade

    narration """
        The screen was static at first. Then an image resolved —
        a wrestling ring, bright lights, a crowd that wasn't
        moving right. The announcer stood at center ring,
        microphone in hand, smile frozen.
    """
    nvl clear

    narration """
        "Tonight's championship bout: Ms. America, Ragnarok the Viking,"
        the announcer's voice was layered — dozens of voices
        speaking the same words at the same time, echoing off
        each other, and underneath the words, a sound like
        beating wings. "and Ninja Master Kunoichi."
    """
    nvl clear

    narration """
        The wrestlers in the ring were wrong. Ms. America moved
        across the ropes and her face glitched — human features
        for one frame, black feathers the next. Ragnarok the
        Viking turned toward the camera and his eyes were
        solid red and his jaw was too wide and the skin of
        his face stretched like a mask.
    """
    nvl clear

    narration """
        The announcer's face began to change. The skin stretched
        upward. Beak-shaped. Black feathers erupted from his
        hairline and crackled with static. His eyes stayed human
        for one more second — bulging, afraid — then went
        completely black.
    """
    nvl clear

    narration """
        "Only one will ascend," the crow-announcer said, and its
        voice was dozens of voices and wings and the whisper
        of something vast and hungry. "Only one will be crowned."
    """
    nvl clear

    narration """
        The Viking in the ring turned its head. Not toward another
        wrestler — toward Rachel. Through the camera. Through
        the screen. Directly at her. Its eyes glowed red and
        stayed glowing and it smiled with too many teeth.
    """
    nvl clear

    $ rachel_stress += 20
    call check_stress_crisis

    narration """
        Then the TV went dark and the hallway sounds started again.
        Rachel gripped the lamp and listened to the clicking
        grow closer.
    """
    nvl clear

    jump act2_the_duel


## Scene 12: The Duel
label act2_the_duel:
    scene hallway_stairs
    with fade

    nvl clear
    narration """
        The Viking moved first. Not toward Rachel — toward the
        NinjaMaster. Its scissors snapped open and closed,
        open and closed, a mechanical rhythm that grew faster.
    """
    nvl clear

    viking "...You failed. You will be recycled."

    ninjamaster "...Objection... filed..."

    narration """
        The Viking lunged. Its scissors caught the NinjaMaster's
        knife arm and pinioned it — the blades locked around
        the forearm and bit down. Cables whipped free from
        the Ninja's shoulder joint. Oil misted the wall.
    """
    nvl clear

    narration """
        The Viking twisted and the scissors sheared through
        the NinjaMaster's arm at the elbow. The toy dropped
        its knife. Cables and fluid sprayed across the wallpaper.
    """
    nvl clear

    ninjamaster "...Unit... decommissioned..."

    narration """
        The Viking drove its scissors into the NinjaMaster's
        chest. The chassis cracked open like a egg. Wiring
        and circuit boards spilled out. The NinjaMaster's
        eyes went dark. Its body collapsed in a heap of
        broken plastic and dead servos.
    """
    nvl clear

    narration """
        The Viking turned toward Rachel.
    """
    nvl clear

    viking "...Final contestant confirmed. Proceeding to elimination."

    narration """
        Its eyes glowed brighter. A faint beep echoed from its
        chest — the same targeting frequency the NinjaMaster
        had made. The same sound from the toys before they'd
        moved against Tommy.
    """
    nvl clear

    $ rachel_stress += 15
    call check_stress_crisis

    jump act3_flight_and_fire


################################################################################
## ACT 3
################################################################################

## Scene 13: Flight and Fire
label act3_flight_and_fire:
    scene bedroom
    with fade

    nvl clear
    narration """
        Rachel slammed the bedroom door. The Viking's weight hit
        it a half-second later — a solid thunk of impact that
        shook the frame. She threw her back against the door
        and felt it shudder again. And again.
    """
    nvl clear

    narration """
        Tommy was on the bed, still out. She shook him — nothing.
        Shook him harder — his head lolled but his eyes stayed
        closed. The sedatives had him too deep. Too deep.
    """
    nvl clear

    narration """
        The door cracked. She could see the gap between the frame
        and the wood — the Viking's scissors were already
        wedged in, working. She had seconds.
    """
    nvl clear

    rachel "Tommy. TOMMY. Wake up. Please. Please wake up—"

    narration """
        Nothing. His breathing was slow and even and wrong.
        She grabbed him under the arms and hauled — his dead
        weight dragging across the bed, across the floor,
        her bleeding foot leaving a smeared trail behind them.
    """
    nvl clear

    scene living_room
    with fade

    narration """
        She carried him to the living room. Put him on the couch.
        The Viking was still working on the bedroom door —
        she could hear the crack of wood, the snick of scissors.
        She had minutes. Maybe less.
    """
    nvl clear

    narration """
        The coat closet. Ethan's golf club — expensive, never used,
        a relic of a version of himself he hadn't become. She
        grabbed it and turned just as the Viking burst through
        the bedroom door.
    """
    nvl clear

    viking "...Target located. Proceeding to—"

    narration """
        She swung. The iron connected with the Viking's knee
        and something cracked. The toy buckled. It dropped
        the scissors — they clattered across the hardwood —
        and it crashed against the wall.
    """
    nvl clear

    narration """
        Rachel swung again. And again. The third blow took the
        Viking's leg off entirely — the plastic shattered, the
        servo inside whined and died, and the toy collapsed
        in a heap of broken limbs and sparking wires.
    """
    nvl clear

    $ rachel_stress += 20
    $ viking_in_fishtank = True
    $ viking_limbless = True
    call check_stress_crisis

    narration """
        Rachel fell to her knees. Her body was shutting down.
        The foot, the hand, the face — all of it screaming
        at once. She couldn't feel anything but fire.
    """
    nvl clear

    narration """
        Then she heard it. Thrashing. Splashing.
        The Viking — one leg, broken, limbless — had
        dragged itself into the fish tank. It was trapped.
        The glass was too slick and its remaining limb
        couldn't find purchase and the tank was too high
        for it to climb out. It thrashed, spraying water,
        its eyes still glowing.
    """
    nvl clear

    narration """
        A hairline crack spread across the front glass.
        Then another. The tank was old, had been old when
        Ethan bought it, and the pressure of the thrashing
        toy was more than it could take.
    """
    nvl clear

    narration """
        Rachel's eyes went to the bottle on the counter.
        Half full. The last of what she had.
        Her body screamed for it. The dependency was a live
        thing in her blood, demanding. The wound in her hand
        throbbed in time with her heartbeat and the only
        thing that had ever made that feeling go away was
        right there. Twelve feet away.
    """
    nvl clear

    narration """
        She crawled to the counter. Pulled herself up on shaking
        legs. The room tilted and she grabbed the edge and
        held on and reached for the bottle with her good hand.
    """
    nvl clear

    narration """
        She drank. Long. Deep. The burn was almost mechanical
        and her body sang with relief even as her mind
        screamed that this was wrong, that she was doing
        something wrong, that she was taking the easy way
        out when Tommy needed her to be strong—
    """
    nvl clear

    narration """
        But Tommy was breathing. Tommy was alive.
        And the Viking was in the fish tank and the crack
        was spreading and she had to end this.
    """
    nvl clear

    $ rachel_shots -= 1
    if rachel_shots <= 0:
        $ rachel_booze = 0
    $ rachel_dependency += 20
    $ withdrawal_turns_since_drink = 0
    $ withdrawal_active = False
    if rachel_dependency >= 50:
        $ rachel_fog = True
    if rachel_dependency >= 75:
        $ rachel_shaky = True

    narration """
        She grabbed the bottle and the lighter from the drawer
        and she soaked the pillow from the couch in the
        remaining alcohol and she doused the thrashing
        Viking and the wet fur of its broken body and the
        water it was half-drowning in.
    """
    nvl clear

    narration """
        The lighter caught on the third try. The pillow caught
        after that. She pressed it against the bottle neck
        until the fumes caught — a WHOOOMPF of flame that
        nearly took off her eyebrows — and she pitched the
        whole burning, soaking, reeking mess into the tank.
    """
    nvl clear

    narration """
        The Viking thrashed once, twice — then went still.
        The flame spread across the water's surface. The
        plastic melted. The wiring ignited. The smell was
        chemical and wrong and almost beautiful.
    """
    nvl clear

    narration """
        Rachel sat on the kitchen floor and watched the fish
        tank burn. The crack had gone all the way through
        but the water kept the glass in place long enough
        for everything to burn. Long enough for the eyes
        to go dark. Long enough for the clicking to stop.
    """
    nvl clear

    narration """
        Tommy was still breathing. The house was still standing.
        She was still here.
    """
    nvl clear

    $ rachel_stress += 10
    call check_stress_crisis

    ## End of Act 3 Scene 13
    scene black
    with fade

    "TO BE CONTINUED..."

    return
