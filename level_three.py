"""
level_three.py – Level 3: The Rook's Shadow Campaign

Implements the third level of the Chess War RPG.

Handles:
- Level intro and cultural training
- Map generation and task progression
- Event handling (oracle, shrine, traps, battle)
- Main game loop via run_level()

Uses colorama for styled output and depends on display_manager, player_manager, and utilities.
"""
from colorama import Fore, Style
from display_manager import update_display
from player_manager import save_player
from utilities import *
from itertools import product
import random, time

# Game Constants
# noinspection SpellCheckingInspection
AMHARIC_PHRASES = {
    "selam": {"reply": "selam", "fail_penalty": 20},
    "dehna neh?": {"reply": "dehna", "fail_penalty": 20},
    "Simih manew?": {"reply": "dawit", "fail_penalty": 5},
    "Wedet eyehedk nw?": {"reply": "church", "fail_penalty": 5}
}


# noinspection SpellCheckingInspection
def level_three_intro():
    intro_text = f"""
██████╗ ██╗  ██╗██╗   ██╗███╗   ███╗███████╗     ██████╗ █████╗ ██╗     ██╗     
██╔══██╗╚██╗██╔╝██║   ██║████╗ ████║██╔════╝    ██╔════╝██╔══██╗██║     ██║     
███████║ ╚███╔╝ ██║   ██║██╔████╔██║███████╗    ██║     ███████║██║     ██║     
██╔══██║ ██╔██╗ ██║   ██║██║╚██╔╝██║╚════██║    ██║     ██╔══██║██║     ██║     
██║  ██║██╔╝ ██╗╚██████╔╝██║ ╚═╝ ██║███████║    ╚██████╗██║  ██║███████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝
{Fore.LIGHTYELLOW_EX}
    ───────────────────────────────────────────
    .   LEVEL 3: THE ROOK'S SHADOW CAMPAIGN   .
    ───────────────────────────────────────────
{Style.RESET_ALL}                                                                                

    The year is 1896. You are Agent "Tower", a royal spy embedded in the breakaway 
    territory of Adal. Once part of the great Axum kingdom, this land was 
    torn away by King Menelik's own cousin and his ruthless queen, Yodit.

    "Remember three rules," your handler whispers as you cross the border:

    1. Move like the rook - straight lines only
    2. When they greet you, answer *exactly* as locals do
    3. Trust no translator until they swear by St. George

    Your mission:
    - Infiltrate the capital
    - Decipher the king's whereabouts
    - Choose: strike alone or signal the imperial army

    One misstep, and Queen Yodit's executioners will make you wish 
    you'd never been born.

    ➡️ Press ENTER to begin your mission...
    """
    update_display([line.strip() for line in intro_text.splitlines()], status=False)
    input()


# noinspection SpellCheckingInspection
def level_three_training():
    training_text = f"""
    ────────────────────────
    FIELD TRAINING: ESSENTIALS
    ────────────────────────

    █ MOVEMENT
    Unlike peasants who wander, you move with purpose:
    {Fore.LIGHTMAGENTA_EX}↑ North    ↓ South    ← West    → East{Style.RESET_ALL}

    █ CULTURAL TRAINING
    Adal locals will test you. Memorize these:
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    When they say:                               You reply:
    "selam" (Greetings)                         {Fore.LIGHTCYAN_EX}"selam"{Style.RESET_ALL}
    "dehna neh?" (How are you?)                 {Fore.LIGHTCYAN_EX}"dehna" (fine){Style.RESET_ALL}
    "Simih manew?" (What is your name?)         {Fore.LIGHTCYAN_EX}"Dawit" (A common name){Style.RESET_ALL}
    "Wedet eyehedk nw?" (Where are you headed?) {Fore.LIGHTCYAN_EX}"Church" (Obviously..){Style.RESET_ALL}
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    
    This is the last time you will get the translations beware!
    You will be dressed in {Fore.LIGHTYELLOW_EX}yellow{Fore.LIGHTYELLOW_EX} to easily blend in with the locals.
    
    █ SUSPICION METER
    Every wrong answer increases suspicion.
    At 100%, the royal guard arrests you.

    █ PROVE YOURSELF
     Answer the elder's greeting correctly
    """
    update_display(training_text.splitlines(), save_text=True, status=False)

    # Simulated training
    for _ in range(2):
        test_phrase = random.choice(list(AMHARIC_PHRASES.keys()))
        convo = ["", f"Elder says: '{test_phrase}'", "Your reply: "]
        response = input(f"Elder says: '{test_phrase}'\nYour reply: ").lower()
        convo[1] += response
        if response == AMHARIC_PHRASES[test_phrase]["reply"]:
            convo.append("Correct! You may proceed.")
        else:
            convo.append("Wrong! In real mission, this would be dangerous.")
        update_display(convo)


def generate_adal_places():
    """
    Generate a randomized 8x8 map segment starting at (5, 15) with 25 unique places.
    Each place has a unique position and a data dictionary containing:
      - name
      - emoji symbol (optional)
      - description
      - hidden (True if player needs context to reveal it)
    """

    # Starting grid size
    start_row, start_col = 5, 15
    grid_size = 8
    max_places = 25

    # Pool of possible places
    place_pool = [
        ("oracle", "🧙‍♂️ ", "A tent filled with scrolls, incense, and riddles.", True),
        ("scorpion trap", "🦂 ", "You hear a hiss before you feel the sting.", False),
        ("drum circle", "🪘 ", "You're pulled into a night of hypnotic dancing.", False),
        ("adal market", "🛍️ ", "Bustling traders shout over each other to sell their wares.", True),
        ("St. George Shrine", "⛪ ", "A quiet shrine where truths are sworn.", True),
        ("hidden message", "📜 ", "A cryptic note half-buried under rubble.", False),
        ("shift_locked", "🔒 ", "A strange symbol etched into stone. It won’t budge.", True),
        ("enemy_king", "🔴 ", "A guarded location whispered about in rumors.", True),
        ("fake_translator", "🔮 ", "A translator with shifty eyes and forked tongue.", True),
        ("ambush", "⚔️ ", "You're surrounded before you can blink.", False),
        ("wandering villager", None, "A local asks where you're from and watches closely.", False),
        ("suspicious camp", None, "Tents that look too perfect. Something's off.", True),
        ("abandoned hut", None, "A crumbling shelter. Might hold clues.", True),
        ("ravine edge", None, "A steep drop. You hear echoes below.", False),
        ("goat pen", None, "A noisy pen full of goats. Smells awful.", False),
        ("guard post", None, "Adal soldiers patrol lazily here.", True),
        ("ancient stone", None, "A weathered stone with inscriptions.", True),
        ("storyteller", None, "An old man shares riddles for gold.", False),
        ("well", None, "You peer into the dark water. Something gleams.", True),
        ("spice stall", None, "The smell of cumin and cardamom overwhelms you.", False),
        ("carved idol", None, "A statue worn smooth by time and belief.", True),
        ("drunken bard", None, "He sings loudly, but his lyrics carry warnings.", False),
        ("children’s game", None, "They chant a rhyme... is it a clue?", False),
        ("church", "✝️ ", "An old St. George church with hiding spots beneath the altar.", True),
        ("tea house", None, "Quiet murmurs and sidelong glances. Deals are made here.", False)
    ]

    # Randomly select 25 unique places
    selected_places = random.sample(place_pool, max_places)

    # Generate 25 unique positions in the 8x8 grid starting at (5, 15)]
    possible_positions = list(product(
        range(start_row, start_row + grid_size),
        range(start_col, start_col + grid_size)
    ))
    possible_positions.pop()
    place_positions = random.sample(possible_positions, max_places)

    # Combine positions with places into final dictionary
    place_dict = {}
    for pos, (name, symbol, desc, hidden) in zip(place_positions, selected_places):
        place_dict[pos] = {
            "name": name,
            "symbol": symbol,
            "description": desc,
            "hidden": hidden,
        }

    return place_dict


def update_player_visible_places(player, adal_map):
    """
    Update the player's 'visible_places' dictionary with all non-hidden
    map locations that have a symbol (emoji).

    :param player: dict – Player's current data
    :param adal_map: dict – Adal map with positions and place data
    """
    task = player.get("next_task")
    progress = player.get("progress", {})

    # Task-to-place mapping for dynamic reveals
    task_visibility_map = {
        "Go to the market to find a translator": "adal market",
        "Realize it was fake and seek the shrine": "St. George Shrine",
        "Goto the oracle to find the shift key": "oracle",
        "Decrypt the message at the church": "St. George Shrine",
        "Locate the enemy king": "enemy_king",
        "Lead the final strike️": "enemy_king"
    }

    # Unlock task-relevant place if hidden
    if task in task_visibility_map:
        target_place = task_visibility_map[task]
        for position, place in adal_map.items():
            if place["name"] == target_place and place.get("hidden"):
                adal_map[position]["hidden"] = False

    if task not in ["Goto the oracle to find the shift key", "Find the hidden message"]:
        for position, place in adal_map.items():
            if place["name"] == "oracle" and progress.get("translated_but_encrypted") is False:
                place["hidden"] = True
                place["symbol"] = None

            elif place["name"] == "hidden message":
                place["hidden"] = True
                place["symbol"] = None

    player["visible places"] = {}

    for position, place in adal_map.items():
        if place["symbol"] and not place["hidden"]:
            player["visible places"][place["name"]] = {
                "position": position,
                "symbol": place["symbol"],
            }


# noinspection SpellCheckingInspection
def handle_villager_encounter(player):
    """Random cultural challenge"""
    phrase, data = random.choice(list(AMHARIC_PHRASES.items()))

    options = {"1": "selam", "2": "dawit", "3": "church", "4": "dehna"}
    options_menu = [
        f"{Fore.LIGHTBLUE_EX}Local approaches and says:{Style.RESET_ALL} '{phrase}'",
        "What do you reply?",
        f"{Fore.LIGHTBLUE_EX}1. Selam    2. Dawit   3. Church    4. Dehna{Style.RESET_ALL}"
    ]
    update_display(options_menu, save_text=True)

    reply = options.get(input("> ").strip(), "")
    update_display([reply], save_text=True)
    if reply != data["reply"]:
        player["suspicion"] += data["fail_penalty"]
        update_display([
            f"{Fore.RED}Wrong reply! Suspicion +{data['fail_penalty']}%{Style.RESET_ALL}",
        ], save_text=True)
        if player["suspicion"] >= 100:
            display_text = [
                "Guards noticed your foreign accent!",
                "⚔️ Queen Yodit's executioners drag you away...",
                "GAME OVER"
            ]
            display_text = [f"{Fore.RED + line + Style.RESET_ALL}" for line in display_text[:]]
            update_display(display_text, save_text=True)
            return False
    return True


def get_player_movement_choice():
    """
    Prompt the user to select a movement direction from a numbered menu.

    :postcondition: Display the direction menu using update_display()
    :postcondition: Return None if invalid input is provided
    :return: A string representing the chosen direction ('north', 'west', 'east', 'south') or None if invalid choice.
    """
    direction_menu = [
        "Choose a direction:",
        f"{Fore.LIGHTMAGENTA_EX}1. ↑ North    2. ↓ South   3.  ← West    4. → East{Style.RESET_ALL}"
    ]

    update_display(direction_menu)

    choice = input("> ")

    direction_map = {
        '1': 'north',
        '2': 'south',
        '3': 'west',
        '4': 'east'
    }

    return direction_map.get(choice, None)


def generate_tasks():
    """
    Yield a sequence of mission tasks for the player in order.

    :postcondition: Returns a generator yielding tasks in fixed storyline sequence.
    :yield: String representing the next task in the storyline.

    >>> tasks = generate_tasks()
    >>> next(tasks)
    'Find the hidden message'
    >>> next(tasks)
    'Go to the market to find a translator'
    >>> next(tasks)
    'Realize it was fake and seek the shrine'
    >>> next(tasks)
    'Goto the oracle to find the shift key'
    """
    yield "Find the hidden message"
    yield "Go to the market to find a translator"
    yield "Realize it was fake and seek the shrine"
    yield "Goto the oracle to find the shift key"
    yield "Decrypt the message at the church"
    yield "Locate the enemy king"
    yield "Lead the final strike️"


# noinspection SpellCheckingInspection
def handle_shrine_task(player, tasks):
    """
    Handle the player's interaction inside the church/shrine, based on their current quest progress.

    :param player: dict – The player's current state, including 'next_task' and 'progress'.
    :param tasks: iterator – A generator or list iterator of upcoming task strings.
    :precondition: player must include 'next_task' and optionally a 'progress' dict.
    :postcondition: If the player prays (option "1"), a peaceful message is shown.
    """
    progress = player.setdefault("progress", {})
    current_task = player.get("next_task")

    update_display([
        "✝️ You enter the quiet church.",
        "A priest approaches: 'How may I help you, child?'",
        "1. To pray",
        "2. To speak with the priest"
    ])
    choice = input("> ").strip()

    if choice == "1":
        update_display([f"{Fore.GREEN}You kneel quietly in prayer.{Style.RESET_ALL}"], save_text=True)
        time.sleep(0.3)
        return

    if choice == "2":
        if (current_task == "Realize it was fake and seek the shrine"
                and progress.get("found_message") and progress.get("scammed")):
            update_display([
                "'Ah, let me see this message... hmm.'",
                "'This is in Ge'ez. Let me translate... wait, this message is encrypted!'",
                f"{Fore.LIGHTBLUE_EX}'I swear by St. George, {Style.RESET_ALL}"
                f"I shall keep this safe here at the shrine until you return with the key.' "
            ], save_text=True)
            progress["message_saved"] = True
            progress["translated_but_encrypted"] = True
            player["next_task"] = next(tasks)

        elif (current_task == "Decrypt the message at the church" and progress.get("cipher_shift") == 3 and
              progress.get("message_saved")):
            update_display([
                "'Ah, you have the key? Good.'",
                f"'Decoding now... {Fore.RED}The king{Style.RESET_ALL} is being hidden in the mountain temple, "
                f"guarded by {Fore.RED}Queen Yodit{Style.RESET_ALL}.'"
            ], save_text=True)
            progress["king_location_known"] = True
            player["next_task"] = next(tasks)

        else:
            update_display(["'Come back when you're ready.'"], save_text=True)
    else:
        update_display(["You leave the church."], save_text=True)


def handle_market_task(player, tasks):
    """
    Handle player interactions at the Adal Market.

    :param player: dict – The player's current state, including 'gold', 'health', 'progress', and 'next_task'.
    :param tasks: iterator – A generator or list iterator of upcoming task strings.

    :precondition: player must have 'gold', 'health', and optionally 'progress' and 'position'.
    :postcondition: Update player's gold and health if medicine is purchased.
    :postcondition: Update player's progress and next_task if translator interaction occurs.
    :postcondition: May change player["position"] if scammed.
    """
    progress = player.setdefault("progress", {})

    update_display([
        "🛍️ You're at the bustling Adal Market.",
        "1. Buy medicine (20 gold, +30 health)",
        "2. Ask about a translator"
    ])
    choice = input("> ").strip()

    if choice == "1":
        if player["gold"] >= 20:
            player["gold"] -= 20
            player["health"] = min(player["health"] + 30, 100)
            update_display([f"{Fore.GREEN}You bought herbs and regained +30 health.{Style.RESET_ALL}"],
                           save_text=True)
        else:
            update_display(["Not enough gold!"], save_text=True)

    elif choice == "2":
        if not progress.get("scammed"):
            progress["scammed"] = True
            update_display([
                "A shady merchant whispers: 'By the river, you’ll find him.'",
                f"You rush there... only to find a fisherman. {Fore.RED}You've been tricked!{Style.RESET_ALL}"
            ], save_text=True)
            player["next_task"] = next(tasks)
            player["position"] = [12, 22]  #place the player to simulate uncontrolled move
        elif progress.get("scammed") and not progress.get("true_translation"):
            progress["true_translation"] = True
            update_display([
                f"'The real one swears by St. George,' a kind woman says."
                f"{Fore.LIGHTBLUE_EX} 'Seek the shrine.{Style.RESET_ALL}'"
            ], save_text=True)
        else:
            update_display(["You've already found the true translator."], save_text=True)


def handle_message_task(player, tasks):
    """
    Handle the player's discovery of the hidden message and update task progression.

    :param player: dict – The player's current state, including 'progress' and 'next_task'.
    :param tasks: iterator – A generator or list iterator of upcoming task strings.

    :precondition: player must include a mutable dictionary with 'progress' and 'next_task'.
    :postcondition: Add 'found_message' = True to player["progress"].
    :postcondition: Set the player's next task using next(tasks).
    :postcondition: Call update_display() to describe the event to the player.
    """
    progress = player.setdefault("progress", {})
    update_display([
        "You find the hidden message scrawled on old parchment.",
        "But it's written in a language you don't understand...",
        f"{Fore.LIGHTBLUE_EX}You will need to go to the market to find a translator.{Style.RESET_ALL}"
    ], save_text=True)

    progress["found_message"] = True
    player["next_task"] = next(tasks)


def handle_oracle_task(player, tasks):
    """
    Handle the player's interaction with the Oracle, involving a riddle challenge.

    :param player: dict – Player state, including 'progress' and 'next_task'.
    :param tasks: iterator – A generator or list iterator of remaining tasks.

    :precondition: player["next_task"] must be either "Goto the oracle to find the shift key"
                   or "Solve the oracle's puzzle" for the riddle to be asked.
    :postcondition: Set progress["cipher_shift"] = 3 and advance player["next_task"] if puzzle solved correctly.
    """
    progress = player.setdefault("progress", {})
    current_task = player.get("next_task")

    if current_task in ["Goto the oracle to find the shift key", "Solve the oracle's puzzle"]:
        update_display([
            "🧙‍♂️ The Oracle greets you: 'Answer me this:'",
            "'What walks on four legs in the morning, two at noon, and three in the evening?'"
        ], save_text=False)
        answer = input("> ").strip().lower()
        if "man" in answer:
            update_display(["'Correct. The cipher shift is 3. Use it wisely.'"], save_text=True)
            progress["cipher_shift"] = 3
            player["next_task"] = next(tasks)
        else:
            update_display(["'Come back when you have the answer.'"], save_text=True)


# noinspection SpellCheckingInspection
def handle_final_battle(player, tasks):
    """
    Handle the final confrontation with Queen Yodit.

    :param player: dict – Player state including health, status, and next_task.
    :param tasks: iterator – A generator or list iterator of any remaining tasks.

    :precondition: player must contain 'health' and 'status'.
    :postcondition: Display a narrative sequence based on the player's choice.
    :postcondition: Set player['status'] to 'defeated' if the player chooses a solo attack.
    :postcondition: Set player['health'] to 0 if the player chooses a solo attack.
    :postcondition: Set player['status'] to 'victorious' if the player chooses to call for reinforcements.
    :postcondition: Reduce player['health'] to a minimum of 10 if the player chooses to call for reinforcements.
    :postcondition: Update player['next_task'] to the next task from the generator or a fallback message.
    """
    update_display([
        "You approach the enemy king's hiding place.",
        f"{Fore.RED}Queen Yodit{Style.RESET_ALL} stands guard, sword drawn.",
        "What will you do?",
        "1. Attempt a solo attack",
        "2. Return and inform your king"
    ], save_text=True)
    choice = input("> ").strip()

    if choice == "1":
        fight_scene = [
            f"{Fore.RED}You break into the palace alone, blade at your side...{Style.RESET_ALL}",
            f"{Fore.LIGHTGREEN_EX}A guard lunges—you parry, spin, and cut him down.{Style.RESET_ALL}",
            f"{Fore.RED}You press deeper through the halls... breathing heavy... bleeding...{Style.RESET_ALL}",
            f"{Fore.RED}In the king's chamber—Queen Yodit awaits, sword glinting in candlelight.{Style.RESET_ALL}",
            f"{Fore.RED}'You're brave,' she hisses, 'but foolish.'{Style.RESET_ALL}",
            f"{Fore.LIGHTGREEN_EX}You clash—steel against steel! You land a deep gash on her shoulder!{Style.RESET_ALL}",
            f"{Fore.RED}But more guards arrive. You fight... and fall beneath their blades.{Style.RESET_ALL}",
            f"{Fore.RED}🩸 Your body lies still. Your mission ends in tragedy.{Style.RESET_ALL}",
            f"{Fore.RED}GAME OVER.{Style.RESET_ALL}"
        ]

        for scene in fight_scene:
            update_display([scene], save_text=True)
            time.sleep(2)

        player["status"] = "defeated"
        player["health"] = 0
        player["next_task"] = next(tasks, "No more task, Defeated!")

    else:
        fight_scene = [
            f"You send the signal. Moments later, chaos erupts at the palace gates!",
            f"{Fore.GREEN}You and a small strike team storm the rear! Swords drawn, eyes blazing!{Style.RESET_ALL}",
            f"{Fore.GREEN}In the throne room, Queen Yodit stands her ground. She charges!{Style.RESET_ALL}",
            f"{Fore.RED}You block her strike—but not fast enough. "
            f"Blood sprays from your arm! (-30 health){Style.RESET_ALL}",
            f"{Fore.GREEN}The pain fuels your fury—you riposte and slash her thigh! She stumbles!{Style.RESET_ALL}",
            f"{Fore.GREEN}Your team surrounds the king. He drops his blade. The room falls silent...{Style.RESET_ALL}",
            f"{Fore.GREEN}The enemy king is captured. Queen Yodit lies defeated.{Style.RESET_ALL}",
            f"{Fore.GREEN}You fought hard—and won. Adal is free once more!{Style.RESET_ALL}",
            f"{Fore.GREEN}VICTORY!{Style.RESET_ALL}"
        ]
        for scene in fight_scene:
            update_display([scene], save_text=True)
            time.sleep(2)
        player["status"] = "victorious"
        player["health"] = max(10, player["health"] - 30)
        player["next_task"] = next(tasks, "No more task, Victorious!")


def handle_trap(player):
    """
    Handle trap events triggered when the player steps on certain marked map locations.

    :param player: dict – The player's current state, including 'position', 'health', 'gold', and 'visible places'.

    :precondition: player must include a valid 'position' and 'visible places' mapping names to coordinates.
    :postcondition: Identify the place name at the player's current position.
    :postcondition: Reduce player['health'] by 15 if the trap is a scorpion.
    :postcondition: Reduce player['health'] by 10 and player['gold'] by 15 if the trap is an ambush.
    :postcondition: Display immersive text and trigger drum beats if the trap is a drum circle.
    :postcondition: Print musical beats randomly if the drum circle is triggered.
    :postcondition: Display an escape message once the player exits the drum circle.
    """
    place_name = ""
    current_pos = player["position"]
    for name, data in player["visible places"].items():
        if data["position"] == current_pos:
            place_name = name
            break

    if place_name == "scorpion trap":
        player["health"] = max(player["health"] - 15, 0)
        update_display([
            "A scorpion leaps out from a crack!",
            f"{Fore.RED}It stings you before you can react. -15 health.{Style.RESET_ALL}"
        ], save_text=True)

    elif place_name == "ambush":
        player["health"] = max(player["health"] - 10, 0)
        player["gold"] = max(player["gold"] - 15, 0)
        update_display([
            f"{Fore.RED}⚔️ You’re ambushed by enemy scouts!{Style.RESET_ALL}",
            f"{Fore.RED}-10 health, -15 gold.{Style.RESET_ALL}"
        ], save_text=True)

    elif place_name == "drum circle":
        update_display([
            "You're pulled into a hypnotic drum circle!",
            f"{Fore.LIGHTYELLOW_EX}You can’t leave... you must dance until sunrise.{Style.RESET_ALL}"
        ], save_text=True)
        time.sleep(0.2)
        beats = ["BOOM", "TAK", "DUM", "BOOM-BOOM"]
        for _ in range(6):
            print(f"🎶 {random.choice(beats)}")
            time.sleep(random.uniform(0.4, 0.8))
        escape_text = ["You finally escape as the sun rises. You're tired, but unharmed."]
        update_display(escape_text, save_text=True)


def handle_tasks(player, adal_places, tasks):
    """
    Determine and trigger the appropriate event handler based on the player's current position.

    :param player: dict – The player's current state including 'position' and 'progress'.
    :param adal_places: dict – The game map with positions mapped to place data.
    :param tasks: A generator of upcoming tasks.

    :precondition: player must include a valid 'position' matching a key in adal_places.
    :postcondition: Identify the current place name based on the player's position.
    :postcondition: Call the corresponding handler function if the place has a story event.
    :postcondition: Pass only the player to trap handlers like drum circle or ambush.
    :postcondition: Pass both player and tasks to non-trap story handlers.
    :postcondition: Display a default message if the place has no associated handler.
    """
    current_pos = player["position"]
    place_data = adal_places[current_pos]
    place_name = place_data["name"]

    # Dictionary of places mapped to their handler functions
    place_handlers = {
        "adal market": handle_market_task,
        "St. George Shrine": handle_shrine_task,
        "oracle": handle_oracle_task,
        "hidden message": handle_message_task,
        "enemy_king": handle_final_battle,
        "drum circle": handle_trap,
        "scorpion trap": handle_trap,
        "ambush": handle_trap
    }

    # Use the correct function, or default to nothing
    handler = place_handlers.get(place_name)

    if handler:
        if handler == handle_trap:
            handler(player)
        else:
            handler(player, tasks)
    else:
        update_display([f"You're at {place_name}. There's nothing story-related here yet."])


def initialize_level_three(player):
    """
    Initialize the player's stats and environment for Level 3: The Rook's Shadow Campaign.

    :param player: dict – The player's data structure to be initialized and updated.
    :precondition: player must be a dictionary ready to be initialized for Level 3.
    :postcondition: Set player attributes including piece, position, suspicion, health, and gold.
    :postcondition: Display the level intro and training sequence to the player.
    :postcondition: Generate the Adal map and identify locations with villagers.
    :postcondition: Initialize the player's task sequence and set the first task.
    :postcondition: Update visible places based on the player's state and current task.
    :postcondition: Save the player's state and display a mission start message.
    :return: Tuple (adal_places, villagers, tasks)
    """
    player.update({
        "piece": "rook",
        "position": [12, 22],
        "suspicion": 0,
        "found_clues": [],
        "gold": 100,
        "health": 100,
        "status": None
    })
    level_three_intro()
    level_three_training()

    adal_places = generate_adal_places()
    villagers = {location for location, data in adal_places.items() if data["symbol"] is None}
    tasks = generate_tasks()
    player["next_task"] = next(tasks)
    update_player_visible_places(player, adal_places)

    save_player(player)
    update_display([""] * 30 + ["Mission started. Good luck, Agent."], save_text=True)
    update_display([f"Your next task is to {Fore.LIGHTBLUE_EX}{player['next_task']}{Style.RESET_ALL}"],
                   save_text=True)

    return adal_places, villagers, tasks


def run_level(player):
    """
    Run the main game loop for Level 3: The Rook's Shadow Campaign.

    :param player: dict – The player's data structure, updated as the level progresses.
    :precondition: player must include fields such as 'position', 'health', 'suspicion', and 'next_task'.
    :postcondition: Initialize the level and assign starting values using initialize_level_three().
    :postcondition: Continuously prompt the player for movement until the king is found or the player fails.
    :postcondition: Update player position and trigger tasks or villager encounters based on map content.
    :postcondition: Call appropriate task handlers when standing on visible story-related places.
    :postcondition: Save player state after key actions and update visible locations.
    :postcondition: Display final player status and return updated player data after game loop ends.
    :return: Updated player dictionary after level completion or failure.
    """
    board_start = (5, 15)
    found_king = False
    adal_places, villagers, tasks = initialize_level_three(player)

    save_player(player)
    update_display([f"Your next task is to {Fore.LIGHTYELLOW_EX}"
                    f"{player['next_task']}{Style.RESET_ALL}"], save_text=True)

    while not found_king and player["health"] > 0 and player["suspicion"] < 100:
        save_player(player)
        desired_move = get_player_movement_choice()
        if not desired_move:
            update_display(["Invalid move! Try again."])
            continue

        pos_x, pos_y = player["position"]
        if not validate_move(board_start, pos_x, pos_y, desired_move):
            update_display([f"{Fore.RED}Invalid move! Try again.{Style.RESET_ALL}"], save_text=True)
            continue

        new_pos = move(pos_x, pos_y, desired_move)
        player["position"] = new_pos
        save_player(player)
        place_name = "nothing"
        description = ""
        save_text = False

        if new_pos in adal_places and not adal_places[new_pos]["hidden"]:
            place_name, description = adal_places[new_pos]["name"], adal_places[new_pos]["description"]
            save_text = True
        update_display([f"There is {place_name} here.", f"{description}"], save_text=save_text)
        if new_pos in villagers:
            if handle_villager_encounter(player):
                continue
            break

        if any(place["position"] == new_pos for place in player["visible places"].values()):
            handle_tasks(player, adal_places, tasks)

            if player["status"] == "victorious":
                adal_places[new_pos]["hidden"] = True
                adal_places[new_pos]["symbol"] = None
                found_king = True
            save_player(player)
            update_player_visible_places(player, adal_places)

    save_player(player)
    update_display([str(player["status"])], save_text=True)
    return player
