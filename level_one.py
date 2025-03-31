from utilities import *
from map import *
import player_manager
from display_manager import update_display
import random
import time


def level_one_intro():
    intro_text = """
    
██╗     ███████╗██╗   ██╗███████╗██╗          ██████╗ ███╗   ██╗███████╗
██║     ██╔════╝██║   ██║██╔════╝██║         ██╔═══██╗████╗  ██║██╔════╝
██║     █████╗  ██║   ██║█████╗  ██║         ██║   ██║██╔██╗ ██║█████╗  
██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║         ██║   ██║██║╚██╗██║██╔══╝  
███████╗███████╗ ╚████╔╝ ███████╗███████╗    ╚██████╔╝██║ ╚████║███████╗
╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝     ╚═════╝ ╚═╝  ╚═══╝╚══════╝

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

    * Move wisely. Your life depends on it.
    * Watch out for enemy ambushes.
    * Reach the 8th rank to achieve greatness!

    ➡️ Press ENTER to begin your journey...
    """
    intro_text = intro_text.splitlines()
    update_display(intro_text, status=False)
    input()


def level_one_training():
    training_text = """
    ────────────────────────
    TRAINING: PAWN MOVEMENT
    ────────────────────────

      You are a PAWN. Your movement is limited, 
      but every step forward brings you closer to 
      greatness.

    ┌────────────────────────────┐
    │   MOVE OPTIONS:            │
    │   * Forward North (↑)      │
    │   * Capture Left  (↖)      │
    │   * Capture Right (↗)      │
    └────────────────────────────┘

    You can only move FORWARD unless you are capturing. 
    If an enemy piece is on the left or right diagonal, 
    you can attack!

    IMPORTANT
    - You cannot move backward.
    - You cannot capture straight ahead.
    - Your journey to the 8th rank starts NOW!

    ➡️ Press ENTER to continue...
    """
    training_text = training_text.splitlines()
    update_display(training_text, status=False)
    input()


def get_pawn_direction_choice():
    """
    Ask the user to choose a valid direction for the pawn from a numbered list.

    :return: A string representing the chosen direction.
    """
    direction_menu = [
        "Choose a direction for the pawn:",
        "1. North (Move forward)",
        "2. North-East (Capture right)",
        "3. North-West (Capture left)"
    ]

    update_display(direction_menu)

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
    if column in [4, 11]:
        return "Safe Zone", 5, 10  # Slight skill boost, health +10
    elif column in [5, 10]:  # Near corners (moderate risk)
        return "Moderate Risk", 10, 5  # Moderate skill boost, health +5
    elif column in [6, 9]:  # Middle edge (higher risk)
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
        column = random.randint(4, 11)  # Random file (column)
        location = (25, column)  # Row 25 (2nd rank)
        file_letter = column_to_file(column - 4)
        zone, skill_boost, health_change = assign_position_attributes(column)

        options_menu = [
            f"Your pawn is placed at Rank 2, File {file_letter} ({zone} area).",
            f"- 🛠️ Skill Boost: {skill_boost}",
            f"- ❤️ Health Change: {health_change}",
            "Choose an option:",
            "1️ Keep this position",
            "2️ Re-roll for a new position"
        ]
        update_display(options_menu)

        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == "1":
            player["position"] = location
            player["health"] += health_change
            player["knowledge"].append(f"Started in a {zone} area")
            player_manager.save_player(player)
            break

    print("✅ Final position set!")
    return player


def confirm_move(player, direction):
    """
    Confirm if the player wants to proceed with their move and introduce a random chance of waiting or risk.

    :param player: A dictionary representing the player's attributes.
    :param direction: The direction in which the player wants to move.
    :postcondition: Either allows or prevents movement based on conditions.
    :return: A boolean indicating whether the move is allowed.
    """
    display_text = []
    if direction == "north":
        event = random.randint(1, 5)
        if event == 1:
            update_display(["The path is blocked. You must wait!"], save_text=True)
            return False
        elif event == 2:
            display_text.append("⚠️ Moving forward will remove your protection but bring you closer to greatness!")
        else:
            return True
    elif direction in ["north_west", "north_east"]:
        event = random.randint(1, 5)
        if event == 1:
            update_display(["No piece to capture, safe to move!"], save_text=True)
            return False
        elif event == 2:
            display_text.append("⚠️ The path might put  dangerous, proceed with caution!")
        elif event == 3:
            print("Blocked! You must wait!")
            time.sleep(2)
            return False
        else:
            return True

    options = [
        "Do you want to proceed?",
        "1️ Yes, move ahead!",
        "2️ No, reconsider!"
    ]
    update_display(display_text, save_text=True)
    update_display(options)
    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == "1":
        player["boldness"] += 1
        player_manager.save_player(player)
        return True
    elif choice == "2":
        player["boldness"] -= 1
        player_manager.save_player(player)


def run_level(player):
    level_one_intro()
    level_one_training()
    game_map = setup_game_environment()
    place_pawn(player)
    update_player_on_map(game_map, player["position"], None)
    board_start = (19, 4)

    while player["movement_points"] >= 0:

        if player["position"][0] == board_start[0]:  # Rank 8 reached
            promote_player(player)
            break
        desired_move = get_pawn_direction_choice()
        if not desired_move:
            print("Please enter a valid move!")
            continue
        row = player["position"][0]
        col = player["position"][1]

        if not validate_move(board_start, row, col, desired_move):
            update_display(["Invalid move! Try again."], save_text=True)
            continue

        new_position = move(row, col, desired_move)

        if confirm_move(player, desired_move):
            update_player_on_map(game_map, new_position, player["position"])
            player["position"] = new_position
            player["moves_taken"] += 1
            player["movement_points"] -= 1
            player_manager.save_player(player)
    update_display(["Yay!"])
    print_level_completion_message(1)

