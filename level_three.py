import time
from xml.sax.saxutils import escape

from colorama import Fore, Style

from display_manager import update_display
from player_manager import save_player
from utilities import *

# Game Constants
AMHARIC_PHRASES = {
    "selam": {"reply": "selam", "fail_penalty": 20},
    "dehna neh?": {"reply": "dehna", "fail_penalty": 20},
    "Simih manew?": {"reply": "dawit", "fail_penalty": 5},
    "Wedet eyehedk nw?": {"reply": "church", "fail_penalty": 5}
}

TRAP_TYPES = {
    "Scorpion": "A venomous sting! (-25 health)",
    "Ambush": "Led into ambush! (-15 health & lose 20 gold)",
    "Drum Circle": "Forced to dance until sunrise! (Skip 2 turns)"
}


def level_three_intro():
    intro_text = f"""

██████╗ ██╗  ██╗██╗   ██╗███╗   ███╗███████╗     ██████╗ █████╗ ██╗     ██╗     
██╔══██╗╚██╗██╔╝██║   ██║████╗ ████║██╔════╝    ██╔════╝██╔══██╗██║     ██║     
███████║ ╚███╔╝ ██║   ██║██╔████╔██║███████╗    ██║     ███████║██║     ██║     
██╔══██║ ██╔██╗ ██║   ██║██║╚██╔╝██║╚════██║    ██║     ██╔══██║██║     ██║     
██║  ██║██╔╝ ██╗╚██████╔╝██║ ╚═╝ ██║███████║    ╚██████╗██║  ██║███████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                

    ───────────────────────────────────────────
        LEVEL 3: THE ROOK'S SHADOW CAMPAIGN
    ───────────────────────────────────────────

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


def level_three_training():
    training_text = f"""
    ────────────────────────
    FIELD TRAINING: ESSENTIALS
    ────────────────────────

    █ MOVEMENT
    Unlike peasants who wander, you move with purpose:
    ↑ North    ↓ South    ← West    → East

    █ CULTURAL TRAINING
    Adal locals will test you. Memorize these:
    {Fore.LIGHTCYAN_EX}
    When they say:                                You reply:
    "selam" (Greetings)                              "selam"
    "dehna neh?" (How are you?)                      "dehna" (fine)
    "Simih manew?" (What is your name?)              "Dawit" (A common name)
    "Wedet eyehedk nw?" (Where are you headed?)      "Church" (Obviously..){Style.RESET_ALL}
    
    This is the last time you will get the translations beware!
    You will be dressed in yellow to easily blend in with the locals.
    
    █ SUSPICION METER
    Every wrong answer increases suspicion.
    At 100%, the royal guard arrests you.

    █ PROVE YOURSELF
     Answer the elder's greeting correctly
    """
    update_display(training_text.splitlines(), save_text=True, status=False)

    # Simulated training
    for _ in range(5):
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

    # Generate 25 unique positions in the 8x8 grid starting at (5, 15)
    possible_positions = [(row, col) for row in range(start_row, start_row + grid_size)
                          for col in range(start_col, start_col + grid_size)]
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
            if place["name"] == "oracle" and  progress.get("translated_but_encrypted") is False:
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


def generate_clues():
    """Create progressive clues with red herrings"""
    return [
        {"id": 1, "text": "ገብረ በ 3 ማዕረግ ወደ ሰሜን በር", "type": "amharic", },
        {"id": 2, "text": "The king moves like the horse but hides like the pawn", "is_scam": True, "type": "hint"},
        {"id": 3, "text": "VHQG LV WKH NHB", "type": "caesar", "shift": 3},
        {"id": 4, "text": "Find the woman who sings of St. George", "type": "oracle_loc"},
        {"id": 5, "text": "Gate combination: animal, plant, stone", "type": "oracle_key"}
    ]


def handle_villager_encounter(player):
    """Random cultural challenge"""
    phrase, data = random.choice(list(AMHARIC_PHRASES.items()))

    options = {"1": "selam", "2":"dawit", "3":"church", "4":"dehna"}
    options_menu = [
        f"{Fore.LIGHTBLUE_EX}Local approaches and says:{Style.RESET_ALL} '{phrase}'",
        "What do you reply?",
        f"{Fore.LIGHTBLUE_EX}1. Selam    2. Dawit   3. Church    4. Dehna{Style.RESET_ALL}"
    ]
    update_display(options_menu, save_text=True)

    reply = options.get(input("> ").strip(),"")
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
    :return: A string representing the chosen direction ('north', 'west',
             'east', 'south') or None if invalid choice.
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
    yield "Find the hidden message"
    yield "Go to the market to find a translator"
    yield "Realize it was fake and seek the shrine"
    yield "Goto the oracle to find the shift key"
    yield "Decrypt the message at the church"
    yield "Locate the enemy king"
    yield "Lead the final strike️"


def handle_shrine_task(player, tasks):
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
        update_display([f"{Fore.GREEN}You kneel quietly in prayer.{Style.RESET_ALL}"])
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
                "'Decoding now... The king is being hidden in the mountain temple, guarded by Queen Yodit.'"
            ])
            progress["king_location_known"] = True
            player["current_task"] = next(tasks)

        else:
            update_display(["'Come back when you're ready.'"])
    else:
        update_display(["You leave the church."])


def handle_market_task(player, tasks):
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
    progress = player.setdefault("progress", {})
    update_display([
        "You find the hidden message scrawled on old parchment.",
        "But it's written in a language you don't understand...",
        f"{Fore.LIGHTBLUE_EX}You will need to go to the market to find a translator.{Style.RESET_ALL}"
    ], save_text=True)

    progress["found_message"] = True
    player["next_task"] = next(tasks)


def handle_oracle_task(player, tasks):
    progress = player.setdefault("progress", {})
    current_task = player.get("current_task")

    if current_task in ["Goto the oracle to find the shift key", "Solve the oracle's puzzle"]:
        update_display([
            "🧙‍♂️ The Oracle greets you: 'Answer me this:'",
            "'What walks on four legs in the morning, two at noon, and three in the evening?'"
        ])
        answer = input("> ").strip().lower()
        if "man" in answer:
            update_display(["'Correct. The cipher shift is 3. Use it wisely.'"])
            progress["cipher_shift"] = 3
            player["current_task"] = next(player["task_gen"])
        else:
            update_display(["'Come back when you have the answer.'"])


def handle_final_battle(player, tasks):
    update_display([
        "🔴 You approach the enemy king's hiding place.",
        "Queen Yodit stands guard, sword drawn.",
        "What will you do?",
        "1. Attempt a solo attack",
        "2. Return and inform your king"
    ])
    choice = input("> ").strip()

    if choice == "1":
        update_display([
            "⚔️ You charge forward, facing Queen Yodit in a fierce duel...",
            "You fight valiantly... but she strikes you down.",
            "🩸 Your mission ends in tragedy."
        ])
        player["status"] = "defeated"

    elif choice == "2":
        update_display([
            "🏇 You return to your king with the message.",
            "Reinforcements arrive. Together, you battle Queen Yodit.",
            "After a brutal fight, she falls. The king is captured. 🎯",
            "Victory is yours!"
        ])
        player["status"] = "victorious"

    else:
        update_display(["You hesitate, and the moment passes."])


def handle_trap(player):
    place_name =""

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
        ])

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


def run_level(player):
    player.update({
        "piece": "rook",
        "position": [12, 22],
        "suspicion": 0,
        "found_clues": [],
        "gold": 100,
        "health": 100,
    })
    level_three_intro()
    level_three_training()
    adal_places = generate_adal_places()
    villagers = {location for location, data in adal_places.items() if data["symbol"] is None}
    tasks = generate_tasks()
    player["next_task"] = next(tasks)
    update_player_visible_places(player, adal_places)


    board_start = (5, 15)
    save_player(player)
    start_mission_text = ["" for _ in range(30)]
    start_mission_text.append("Mission started. Good luck, Agent.")
    update_display(start_mission_text, save_text=True)
    generate_clues()

    found_king = False
    save_player(player)
    update_display([f"Your next task is to {player['next_task']}"])

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
            save_player(player)
            update_player_visible_places(player, adal_places)


    save_player(player)
