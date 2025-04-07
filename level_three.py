import random


from display_manager import update_display
from player_manager import save_player
from utilities import *
from colorama import Fore, Style

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
    training_text = """
    ────────────────────────
    FIELD TRAINING: ESSENTIALS
    ────────────────────────

    █ MOVEMENT
    Unlike peasants who wander, you move with purpose:
    ↑ North    ↓ South    ← West    → East

    █ CULTURAL TRAINING
    Adal locals will test you. Memorize these:
    When they say:                                You reply:
    "selam" (Greetings)                              "selam"
    "dehna neh?" (How are you?)                      "dehna" (fine)
    "Simih manew?" (What is your name?)              "Dawit" (A common name)
    "Wedet eyehedk nw?" (Where are you headed?)      "Church" (Obviously..)
    
    This is the last time you will get the translations beware!
    You will be dressed in yellow to easily blend in with the locals.
    
    █ SUSPICION METER
    Every wrong answer increases suspicion.
    At 100%, the royal guard arrests you.

    █ PROVE YOURSELF
     Answer the elder's greeting correctly
    """
    update_display(training_text.splitlines(),save_text=True, status=False)

    # Simulated training
    for _ in range(5):
        test_phrase = random.choice(list(AMHARIC_PHRASES.keys()))
        convo = ["",f"Elder says: '{test_phrase}'", "Your reply: "]
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
        ("adal market", "🛍 ️", "Bustling traders shout over each other to sell their wares.", True),
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
    Initializes the player's 'visible_places' dictionary with all non-hidden
    map locations that have a symbol (emoji).

    :param player: dict – Player's current data
    :param adal_map: dict – Adal map with positions and place data
    """
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
    update_display([
        f"{Fore.LIGHTBLUE_EX}Local approaches and says:{Style.RESET_ALL} '{phrase}'",
        "What do you reply?"
    ], save_text=True)

    reply = input("> ").lower()
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
        "1. ↑ North    2. ↓ South   3.  ← West    4. → East"
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
    yield "Go to the translator"
    yield "Realize it was fake and seek the shrine"
    yield "Goto the oracle to find the shift key"
    yield "Solve the oracle's puzzle"
    yield "Decrypt the message at the church"
    yield "Locate the enemy king"
    yield "Lead the final strike️"


def handle_tasks(player, adal_places):
    current_pos = player["position"]

    # Confirm this is a valid place on the map
    if current_pos not in adal_places:
        update_display(["You're wandering... there's nothing here."])
        return

    place_data = adal_places[current_pos]
    place_name = place_data["name"]

    # Dictionary of places mapped to their handler functions
    place_handlers = {
        "adal market": handle_market_task,
        "fake_translator": handle_translator_task,
        "St. George Shrine": handle_church_task,
        "church": handle_shrine_task,
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
        handler(player, adal_places)
    else:
        update_display([f"You're at {place_name}. There's nothing story-related here yet."])


def run_level(player):
    level_three_intro()
    level_three_training()
    adal_places = generate_adal_places()
    villagers = {location for location, data in adal_places.items() if data["symbol"] is None}


    update_player_visible_places(player, adal_places)



    player.update({
        "piece": "rook",
        "position": [12, 22],
        "suspicion": 0,
        "found_clues": [],
        "gold": 100,
        "health": 100,
        "next_task": ""
    })
    board_start = (5,15)
    save_player(player)
    start_mission_text = ["" for _ in range(30)]
    start_mission_text.append("Mission started. Good luck, Agent.")
    update_display(start_mission_text, save_text=True)
    clues = generate_clues()

    player["tasks"] = generate_tasks()

    found_king = False
    player["next_task"] = next(player["tasks"])
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

        if new_pos in adal_places and not adal_places[new_pos]["hidden"]:
                place_name, description = adal_places[new_pos]["name"], adal_places[new_pos]["description"]
        update_display([f"There is {place_name} here.", f"{description}"], save_text=True)
        if new_pos in villagers:
            if handle_villager_encounter(player):
                continue
            break

        if any(place["position"] == new_pos for place in player["visible places"].values()):
            handle_tasks(player, adal_places)

    # update_display([f"{adal_places}"], save_text=True, status=True)

    save_player(player)
