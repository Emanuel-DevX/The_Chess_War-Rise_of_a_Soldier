from utilities import *
import random


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


def assign_position_attributes(column):
    """
    Assign attributes based on the column (file) position.

    :param column: The column (file) index (0-7).
    :return: A tuple containing skill boost and health adjustment.
    """
    if column in [0, 7]:
        return "Safe Zone", 5, 10  # Slight skill boost, health +10
    elif column in [1, 6]:  # Near corners (moderate risk)
        return "Moderate Risk", 10, 5  # Moderate skill boost, health +5
    elif column in [2, 5]:  # Middle edge (higher risk)
        return "Risky", 15, 0  # More skill boost, no health change
    else:  # Columns 3 and 4 (most dangerous but rewarding)
        return "High Risk", 20, -5  # High skill boost, health -5


def place_pawn(player):
    """
    Randomly place the pawn on the 2nd rank (row 6) and allows the user to choose whether to keep it.

    :param player: A dictionary representing the player's attributes.
    :postcondition: Update the player's position, health, and knowledge based on the chosen location.
    """
    while True:
        column = random.randint(0, 7)  # Random file (column)
        location = (6, column)  # Row 6 (2nd rank)
        file_letter = column_to_file(column)
        zone, skill_boost, health_change = assign_position_attributes(column)

        print(f"\nYour pawn is placed at Rank 2, File {file_letter} ({zone} area).")
        print(f"- 🛠️ Skill Boost: {skill_boost}\n- ❤️ Health Change: {health_change}")

        print("\nChoose an option:")
        print("1️ Keep this position")
        print("2️ Re-roll for a new position")

        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == "1":
            player["position"] = location
            player["health"] += health_change
            player["knowledge"].append(f"Started in a {zone} area")
            break

    print("✅ Final position set!")
    return player


def run_level(player):
    level_one_intro()
    level_one_training()
    place_pawn(player)
    while True:
        print_map(8, 8, player["position"])
        desired_move = get_pawn_direction_choice()
        if not desired_move:
            print("Please enter a valid move!")
            continue
        row = player["position"][0]
        col = player["position"][1]

        new_position = move(8, row, col, desired_move)
        player["position"] = new_position



