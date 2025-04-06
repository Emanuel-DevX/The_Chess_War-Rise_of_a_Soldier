import random
from display_manager import update_display
from player_manager import save_player

# Game Constants
AMHARIC_PHRASES = {
    "selam": {"reply": "selam", "fail_penalty": 30},
    "dehna neh?": {"reply": "dehna", "fail_penalty": 40},
    "Simih manew?": {"reply": "dawit", "fail_penalty": 20},
    "Wedet eyehedk nw?": {"reply": "church", "fail_penalty": 30}
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
    update_display(training_text.splitlines(), status=False)

    # Simulated training
    for _ in range(5):
        test_phrase = random.choice(list(AMHARIC_PHRASES.keys()))
        convo = [f"Elder says: '{test_phrase}'", "Your reply: "]
        response = input(f"Elder says: '{test_phrase}'\nYour reply: ").lower()
        convo[1] += response
        if response == AMHARIC_PHRASES[test_phrase]["reply"]:
            convo.append("Correct! You may proceed.")
        else:
            convo.append("Wrong! In real mission, this would be dangerous.")
        update_display(convo, save_text=True, status=True)



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
        ("oracle", "🧙‍♂️", "A tent filled with scrolls, incense, and riddles.", True),
        ("scorpion trap", "🦂", "You hear a hiss before you feel the sting.", False),
        ("drum circle", "🪘", "You're pulled into a night of hypnotic dancing.", False),
        ("adal market", "🛍️", "Bustling traders shout over each other to sell their wares.", True),
        ("St. George Shrine", "⛪", "A quiet shrine where truths are sworn.", True),
        ("hidden message", "📜", "A cryptic note half-buried under rubble.", True),
        ("shift_locked", "🔒", "A strange symbol etched into stone. It won’t budge.", True),
        ("enemy_king", "🔴", "A guarded location whispered about in rumors.", True),
        ("fake_translator", "🔮", "A translator with shifty eyes and forked tongue.", True),
        ("ambush", "⚔️", "You're surrounded before you can blink.", False),
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
        ("church", "✝️", "An old St. George church with hiding spots beneath the altar.", True),
        ("tea house", None, "Quiet murmurs and sidelong glances. Deals are made here.", False)
    ]

    # Randomly select 25 unique places
    selected_places = random.sample(place_pool, max_places)

    # Generate 25 unique positions in the 8x8 grid starting at (5, 15)
    possible_positions = [(row, col) for row in range(start_row, start_row + grid_size)
                          for col in range(start_col, start_col + grid_size)]
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
        f"Local approaches and says: '{phrase}'",
        "What do you reply?"
    ])

    reply = input("> ").lower()
    if reply != data["reply"]:
        player["suspicion"] += data["fail_penalty"]
        update_display([
            f"Wrong reply! Suspicion +{data['fail_penalty']}%",
        ], save_text=True)
        if player["suspicion"] >= 100:
            update_display([
                "Guards noticed your foreign accent!",
                "⚔️ Queen Yodit's executioners drag you away...",
                "GAME OVER"
            ], save_text=True)
            return False
    return True


def run_level(player):
    level_three_intro()
    level_three_training()
    adal_places = generate_adal_places()

    player.update({
        "piece": "rook",
        "position": [5, 15],
        "suspicion": 0,
        "found_clues": [],
        "gold": 100,
        "health": 100,
        "next_task": ""
    })
    save_player(player)
    update_display(["" for _ in range(24)])
    clues = generate_clues()
    update_display(["Mission started. Good luck, Agent."])