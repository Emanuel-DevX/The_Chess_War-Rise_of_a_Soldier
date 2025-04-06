
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
    "False Guide": "Led into ambush! (-15 health & lose 20 gold)",
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
        convo = [f"Elder says: '{test_phrase}'","Your reply: "]
        response = input(f"Elder says: '{test_phrase}'\nYour reply: ").lower()
        convo[1]+= response
        if response == AMHARIC_PHRASES[test_phrase]["reply"]:
            convo.append("Correct! You may proceed.")
        else:
            convo.append("Wrong! In real mission, this would be dangerous.")
        update_display(convo, save_text=True, status=True)


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

    player.update({
        "piece":"rook",
        "position": [5, 15],
        "suspicion": 0,
        "found_clues": [],
        "gold": 100,
        "health": 100,
        "next_task":""
    })
    save_player(player)
    update_display(["" for _ in range(24)])
    clues = generate_clues()
    update_display(["Mission started. Good luck, Agent."])