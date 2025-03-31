from display_manager import update_display
from map import update_player_on_map, setup_game_environment
from player_manager import save_player
from utilities import *
import random


def level_two_intro():
    intro_text = """

██╗     ███████╗██╗   ██╗███████╗██╗         ████████╗██╗    ██╗ ██████╗ 
██║     ██╔════╝██║   ██║██╔════╝██║         ╚══██╔══╝██║    ██║██╔═══██╗
██║     █████╗  ██║   ██║█████╗  ██║            ██║   ██║ █╗ ██║██║   ██║
██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║            ██║   ██║███╗██║██║   ██║
███████╗███████╗ ╚████╔╝ ███████╗███████╗       ██║   ╚███╔███╔╝╚██████╔╝
╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝       ╚═╝    ╚══╝╚══╝  ╚═════╝ 

    ──────────────────────────────────
        LEVEL 2: THE BISHOP'S ASCENT 
    ──────────────────────────────────

    The battlefield is no longer a chaotic mess of warriors clashing head-on.  
    It is a game of sight, angles, and precision. You have been chosen for  
    the **Bishop's Path**, a warrior of foresight and deadly accuracy.  

    "Patience and wisdom will guide your blade," whispers the High Priest.

    You are no longer bound to a single step forward. You now move  
    **diagonally across the battlefield**, cutting through enemy lines  
    with speed and grace.

    ⚔️ **New Movement Abilities:**
      * The Bishop moves **one step diagonally** per turn.
      * You must think ahead—your path is limited, but your strategy is key.
      * Enemies lurk in the shadows. Position yourself wisely to survive.

    The path to mastery is not about speed—it is about **seeing what others do not**.  
    Adapt, or be eliminated.

    ➡️ Press ENTER to begin your trial...
    """
    update_display([line.strip() for line in intro_text.splitlines()], status=False)
    input()


def level_two_training():
    training_text = """
    ────────────────
    LEVEL 2 TRAINING 
    ────────────────

    As a **bishop**, your movement is now limited to the color of your starting square.  
    If you begin on a **dark square**, you will always remain on dark squares.  
    If you start on a **light square**, you will always move on light squares.

        ┌───────────────────────────┐
        │   MOVE OPTIONS:           │
        │     * North West   (↖)    │
        │     * North East   (↗)    │
        │     * South West   (↙)    │
        │     * South East   (↘)    │
        └───────────────────────────┘

    ⚔️ **Movement Rules:**
      * You can only travel on **your color** (dark or light).
      * No jumping over obstacles.
      * Capture enemies by stepping onto their position.

    **Training Drill:**
      - Try moving **diagonally** to an empty square of your color.
      - Capture the target dummy placed diagonally from you.
      - Be mindful of the battlefield—some paths may be blocked.

    **The battlefield rewards wisdom over speed.**  
    Master your movement, and you will survive.

    ➡️ Press ENTER to start training...
    """
    update_display(training_text.splitlines(), status=False)
    input()


def spy_mission():
    mission_text = """
    ─────────────────────
    MISSION: FIND THE SPY
    ─────────────────────

    Your mission, brave soldier, is to uncover the traitor among your ranks —the spy. 
    The spy has been planting ambushes all over the land to trap unsuspecting soldiers like you. 
    Your goal is to navigate the battlefield, avoiding traps, and figure out who the spy is. 

    The spy could be anyone. Look for unusual patterns in their movement.

    Here are your instructions:

    1. Move with caution: The land is dangerous, and ambushes lie hidden. 
       Watch your surroundings carefully and move one step at a time.
    2. Spy Indicators: Keep an eye on any strange behavior, like soldiers moving away 
    from their posts or odd paths that don't align with normal patrol routes.
    3. Avoid Ambushes: You may stumble upon traps. If you suspect a trap, don't engage immediately. 
        Look for safer paths and be cautious when moving into enemy territory.
    4. **Find the Spy**: Use your instincts to determine who among your allies may be the spy. 
       They might try to blend in but their actions will give them away.

    !Warning: The spy may also attempt to mislead you by feigning innocence. 

    Once you believe you've identified the spy, report back to your commander. 
    If you're wrong, the enemy might use your mistake against you.

    ➡️ Press ENTER to begin your search for the spy...
    """
    update_display(mission_text.splitlines(), status=False)
    input()


def place_bishop(player, board_start):
    """
    Let the player choose a starting position for their bishop.

    :param player: A dictionary representing the player's attributes.
    :param board_start: A tuple representing the top-left corner of the board.
    :postcondition: Update the player's position and attributes.
    """

    update_display(["Choose your starting position (light or dark square):"])

    while True:
        # Let player choose between light and dark square bishop
        choice = input("Enter 'L' for light square ⬜ or 'D' for dark square ⬛: ").upper().strip()

        if choice not in ['L', 'D']:
            print("Invalid choice. Please enter 'L' or 'D'.")
            continue

        # Determine starting positions based on choice
        if choice == 'L':
            position = (board_start[0] + 7, board_start[1] + 2)  # c1 position
            player["bishop_color"] = "light"
            player["knowledge"].append("Light square bishop - strength on open positions")
        else:
            position = (board_start[0] + 7, board_start[1] + 5)  # f1 position
            player["bishop_color"] = "dark"
            player["knowledge"].append("Dark square bishop - strength in closed positions")

        player["position"] = position
        player["health"] += 10  # Bishop gets health boost
        save_player(player)
        set_pos = ["Bishop placed on " + ("light" if choice == 'L' else "dark") + " square!"]
        update_display(set_pos, save_text=True)
        break


def generate_clues():
    """
    Generate a list of clues for the spy mission.

    :return: List of clues
    """
    suspects = ["The Knight", "The Rook", "The Queen", "The Pawn"]
    locations = ["North Tower", "Eastern Gardens", "Royal Chambers", "Training Grounds"]
    behaviors = ["moving at night", "carrying secret messages", "meeting with enemies", "avoiding certain areas"]

    spy_index = random.randint(0, len(suspects) - 1)
    spy = suspects[spy_index]

    clues = []
    for i in range(len(suspects)):
        if i == spy_index:
            # Genuine clue about the spy
            clue = f"{suspects[i]} was seen {random.choice(behaviors)} near the {random.choice(locations)}."
            clues.append((clue, True))  # True indicates this is a genuine clue
        else:
            # Red herring
            clue = f"{suspects[i]} has been acting suspiciously lately."
            clues.append((clue, False))  # False indicates this is a red herring

    # Add some general clues
    general_clues = [
        (f"Someone has been spotted {random.choice(behaviors)}.", True),
        (f"Unusual activity reported in the {random.choice(locations)}.", True),
        (f"Guards found evidence of betrayal near the {random.choice(locations)}.", True)
    ]

    clues.extend(general_clues)
    random.shuffle(clues)

    return clues, spy


def get_bishop_move_choice():
    """
    Ask the user to choose a valid direction for the bishop from a numbered list.

    :return: A string representing the chosen direction.
    """
    direction_menu = [
        "Choose a direction for the bishop:",
        "1. North-East (↗)",
        "2. North-West (↖)",
        "3. South-East (↘)",
        "4. South-West (↙)"
    ]

    update_display(direction_menu)

    choice = input("Enter a number (1-4): ")

    direction_map = {
        '1': 'north_east',
        '2': 'north_west',
        '3': 'south_east',
        '4': 'south_west'
    }

    return direction_map.get(choice, None)


def discover_clue(player, clues):
    """
    Discover a new clue about the spy.

    :param player: Player dictionary
    :param clues: List of available clues
    :return: Discovered clue or None if no clues left
    """
    if not clues:
        return None

    clue, is_genuine = clues.pop(0)
    player["found_clues"] = player.get("clues", []) + [clue]

    clue_message = [
        "You discovered a clue!",
        clue
    ]

    if random.random() < 0.2 and is_genuine:
        # Add an insight for genuine clues (20% chance)
        clue_message.append("Your intuition tells you this clue seems important.")

    return clue_message


def accuse_spy(suspects, true_spy, player):
    """
    Allow player to accuse who they think is the spy.

    :param suspects: List of suspects
    :param true_spy: The actual spy
    :param player: Player dictionary
    :return: True if correct accusation, False otherwise
    """
    accusation_menu = ["Who do you think is the spy?"]
    for i, suspect in enumerate(suspects, 1):
        accusation_menu.append(f"{i}. {suspect}")

    update_display(accusation_menu)

    while True:
        choice = input(f"Enter a number (1-{len(suspects)}): ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(suspects):
                accused = suspects[index]
                if accused == true_spy:
                    update_display(["You've uncovered the spy! Your mission is a success."])
                    player["reputation"] = player.get("reputation", 0) + 20
                    return True
                else:
                    update_display([
                        f"You wrongly accused {accused}!",
                        f"The true spy was {true_spy}.",
                        "Your reputation has suffered.",

                    ], save_text=True)
                    player["reputation"] = player.get("reputation", 0) - 10
                    return False
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def initialize_level(player):
    level_two_intro()
    level_two_training()
    spy_mission()
    game_map = setup_game_environment()
    board_start = [17, 19]
    place_bishop(player, board_start)
    update_player_on_map(game_map, player["position"])
    clues, true_spy = generate_clues()
    traps = set_traps(game_map, board_start)

    player.update({
        "clues_found": 0,
        "movement_points": 10,
        "clues": clues
    })
    save_player(player)

    return game_map, board_start, clues, true_spy, traps


def handle_random_events(player, clues):
    if random.random() < 0.3 and clues:  # 30% chance to find clue
        clue_message = discover_clue(player, clues)
        if clue_message:
            player["clues_found"] += 1
            update_display(clue_message, save_text=True)
            return

    if random.random() < 0.2:  # 20% chance for random encounter
        event_message = encounter_event(player)
        update_display(["Event: " + event_message], save_text=True)


def handle_accusation(player, true_spy):
    update_display(["You have enough information to make an accusation."], save_text=True)
    accusation_choice = input("Do you want to accuse someone now? (y/n): ").lower()

    if accusation_choice == 'y':
        suspects = ["The Knight", "The Rook", "The Queen", "The Pawn"]
        success = accuse_spy(suspects, true_spy, player)
        return success

    return False


def run_level(player):
    game_map, board_start, clues, true_spy, traps = initialize_level(player)
    max_moves, moves_taken = 20, 0
    player.update({"max_moves": max_moves, "moves_taken": moves_taken})
    save_player(player)

    while (player["moves_taken"] < max_moves and
           player["health"] > 0 and
           player["movement_points"] > 0):

        desired_move = get_bishop_move_choice()
        if not desired_move:
            update_display(["Invalid move for a bishop! Try again."])
            continue

        current_pos = player["position"]
        if not validate_move(board_start, current_pos[0], current_pos[1], desired_move):
            update_display(["Invalid move! Try again."], save_text=True)
            continue

        new_position = move(current_pos[0], current_pos[1], desired_move)
        player["movement_points"] -= 1  # Deduct after check but before actual move
        if player["movement_points"] <= 0:
            update_display([])
            break
        update_player_on_map(game_map, new_position, current_pos)
        player["position"] = new_position

        there_is_trap = check_for_trap(new_position, traps, player)

        if there_is_trap[0]:
            trap_message = there_is_trap[1]
            update_display(trap_message, save_text=True)
            player["moves_taken"] += 1
            save_player(player)
            continue

        handle_random_events(player, clues)
        player["moves_taken"] += 1
        save_player(player)

        if player["clues_found"] >= 3 and random.random() < 0.3:
            if handle_accusation(player, true_spy):
                promote_player(player)
                print_level_completion_message(2)
                return  # Level completed successfully
            max_moves -= 3  # Penalty for wrong accusation_moves -= 3
            player["max_moves"] = max_moves
            save_player(player)

    save_player(player)
    if player["movement_points"] <= 0:
        update_display(["You're out of movement points! Game over."])
    if player["health"] <= 0:
        update_display(["You've died! Game over."])