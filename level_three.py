
import random
from display_manager import update_display

# Game Constants
AMHARIC_PHRASES = {
    "selam": {"reply": "selam", "fail_penalty": 30},
    "dehna neh?": {"reply": "dehna", "fail_penalty": 40},
    "Simih manew?": {"reply": "dawit", "fail_penalty": 50},
    "Wedet eyehedk nw?": {"reply": "church", "fail_penalty": 60}
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

    Test your movement by reaching the marked square.

    █ CULTURAL TRAINING
    Adal locals will test you. Memorize these:
    When they say:                                   You reply:
    "selam" (Greetings)                                 "selam"
    "dehna neh?" (How are you?)                         "dehna"
    "Simih manew?" (What is your name?)                 "Dawit"
    "Wedet eyehedk nw?" (Where are you headed?)         "Church"
    
    This is the last time you will get the translations beware!
    █ SUSPICION METER
    Every wrong answer increases suspicion.
    At 100%, the royal guard arrests you.

    █ PROVE YOURSELF
    1. Move east twice to the checkpoint
    2. Answer the elder's greeting correctly
    """
    update_display(training_text.splitlines(), status=False)

    # Simulated training
    for _ in range(4):
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
    """Creates progressive clues with red herrings"""
    return [
        {"id": 1, "text": "ገብረ በ 3 ማዕረግ ወደ ሰሜን በር", "type": "amharic", "is_scam": True},
        {"id": 2, "text": "The king moves like the horse but hides like the pawn", "type": "hint"},
        {"id": 3, "text": "VHQG LV WKH NHB", "type": "caesar", "shift": 3},
        {"id": 4, "text": "Find the woman who sings of St. George", "type": "oracle_loc"},
        {"id": 5, "text": "Gate combination: animal, plant, stone", "type": "oracle_key"}
    ]


def run_level(player):
    level_three_intro()
    level_three_training()