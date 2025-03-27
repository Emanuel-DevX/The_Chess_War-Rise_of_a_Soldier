from utilities import *


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
        │   🔹 Forward North (↑)     │
        │   🔹 Capture Left  (↖)     │
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


def get_pawn_direction_choice():
    """
    Ask the user to choose a valid direction for the pawn from a numbered list.

    :return: A string representing the chosen direction.
    """
    print("Choose a direction for the pawn:")
    print("1. North (Move forward)")
    print("2. North-East (Capture right)")
    print("3. North-West (Capture left)")

    choice = input("Enter a number (1-3): ")

    direction_map = {
        '1': 'north',
        '2': 'north_east',
        '3': 'north_west'
    }

    return direction_map.get(choice, None)  # Return None if invalid input


def run_level(player):
    level_one_intro()
    level_one_training()
    while True:
        print_map(8, 8, player["position"])
        desired_move = get_pawn_direction_choice()
        if not desired_move:
            print("Please enter a valid move!")
            continue
        row = player["position"][0]
        col = player["position"][1]

        new_position = move(8, row, col, desired_move)
        print(new_position)
        player["position"] = new_position


player = {
    "health": 100,
    "piece": "pawn",
    "position": (6,2),
    "inventory": [],
    "knowledge": [],
    "completed_challenges": [],
}
run_level(player)
