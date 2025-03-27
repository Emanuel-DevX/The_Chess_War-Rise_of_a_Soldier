def level_one_intro():
    intro_text = """
    ───────────────────────────────────────
       ⚔️  LEVEL 1: PAWN'S JOURNEY  ⚔️
    ───────────────────────────────────────

    The battlefield is a chaotic mess of broken weapons, fallen soldiers, and 
    the distant sound of war drums. You, a mere pawn, stand among the ranks, 
    gripping your sword tightly. The enemy lines stretch before you, but 
    beyond them lies a chance for greatness.

    "Keep moving forward! No turning back!" yells your commander.

    Your mission is simple: Reach the enemy's last row and earn your promotion.

    However, the battlefield is dangerous. Enemy pawns will try to stop you, 
    and the terrain itself is full of obstacles.

    🔹 Move wisely. Your life depends on it. 
    🔹 Watch out for enemy ambushes. 
    🔹 Reach the 8th rank to achieve greatness!

    ➡️ Press ENTER to begin your journey...
    """
    print(intro_text)
    input()


def level_one_training():
    training_text = """
    ─────────────────────────────────────────────
             🏰 TRAINING: PAWN MOVEMENT 🏰
    ─────────────────────────────────────────────

             You are a PAWN. Your movement is limited, 
             but every step forward brings you closer to 
             greatness.

        ┌────────────────────────────┐
        │   MOVE OPTIONS:            │
        │   🔹 Forward (↑)           │
        │   🔹 Capture Left (↖)      │
        │   🔹 Capture Right (↗)     │
        └────────────────────────────┘

         8 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
         7 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
         6 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
         5 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
         4 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
         3 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
         2 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
         1 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
           A  B  C  D  E  F  G  H

    You can only move FORWARD unless you are capturing. 
    If an enemy piece is on the left or right diagonal, 
    you can attack!

    ❗ IMPORTANT ❗
    - You cannot move backward.
    - You cannot capture straight ahead.
    - Your journey to the 8th rank starts NOW!

    ➡️ Press ENTER to continue...
    """
    print(training_text)
    input()


def run_level(player):
    level_one_intro()
    level_one_training()


run_level(0)
