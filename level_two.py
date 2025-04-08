"""
Level Two: Bishop's Spy Hunt

Control a bishop piece to:
- Move diagonally across the board
- Find hidden clues
- Avoid traps
- Identify the spy before time runs out

Features:
- 20 turns max
- Random clue discoveries
- Traps that reduce health
- Accusation mechanic at 3+ clues
"""
from display_manager import update_display
from map import update_player_on_map, setup_game_environment
from player_manager import save_player, promote_player
from utilities import *
from colorama import Fore, Style
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
    training_text = f"""
    ────────────────
    LEVEL 2 TRAINING 
    ────────────────

    As a **bishop**, your movement is now limited to the color of your starting square.  
    If you begin on a **dark square**, you will always remain on dark squares.  
    If you start on a **light square**, you will always move on light squares.
        {Fore.LIGHTYELLOW_EX}
        ┌───────────────────────────┐
        │   MOVE OPTIONS:           │
        │     * North West   (↖)    │
        │     * North East   (↗)    │
        │     * South West   (↙)    │
        │     * South East   (↘)    │
        └───────────────────────────┘
        {Style.RESET_ALL}
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
    :precondition: Ensure player is a mutable dictionary with required keys.
    :precondition: Ensure board_start is a valid coordinate tuple (row, col).
    :postcondition: Update player's position, health, bishop_color, and knowledge based on choice
    :postcondition: Update the player's position and attributes.
    """

    update_display(["Choose your starting position (light or dark square):"])

    while True:
        # Let player choose between light and dark square bishop
        choice = input("Enter 'L' for light square ⬜ or 'D' for dark square ⬛: ").upper().strip()

        if choice not in ['L', 'D']:
            update_display([f"{Fore.RED}Invalid choice.{Style.RESET_ALL} Please enter 'L' or 'D'."],
                           save_text=True)
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
    Generate random clues about the spy's identity, including genuine clues and red herrings.

    :postcondition: Create a shuffled list of clues where some are genuine and some are red herrings.
    :postcondition: Guarantee at least one genuine clue about the actual spy.
    :postcondition: Include additional general clues that may be helpful.
    :return: A tuple containing (list of (clue, is_genuine) tuples, actual_spy_identity)
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
    Prompt the user to select a bishop movement direction from a numbered menu.

    :postcondition: Display the direction menu using update_display()
    :postcondition: Return None if invalid input is provided
    :return: A string representing the chosen direction ('north_east', 'north_west',
             'south_east', 'south_west') or None if invalid choice.
    """
    direction_menu = [
        "Choose a direction for the bishop:",

        f"{Fore.LIGHTMAGENTA_EX}"
        f"1. North-West (↖)",
        "2. North-East (↗)",
        "3. South-West (↙)"
        f"4. South-East (↘)"
        f"{Style.RESET_ALL}",
    ]

    update_display(direction_menu)

    choice = input("Enter a number (1-4): ")

    direction_map = {
        '2': 'north_east',
        '1': 'north_west',
        '4': 'south_east',
        '3': 'south_west'
    }

    return direction_map.get(choice, None)


def discover_clue(player, clues):
    """
    Discover and reveal a clue from the available clues list.

    :param player: A dictionary containing player information including found_clues.
    :param clues: A list of tuples containing (clue_text, is_genuine) pairs.
    :precondition: Ensure player is a mutable dictionary.
    :precondition: Ensure clues is a mutable list of (str, bool) tuples.
    :postcondition: Remove the first clue from the clues list if available.
    :postcondition: Add discovered clue to player's found_clues list.
    :postcondition: Display clue with possible intuition hint for genuine clues.
    :return: A list of strings representing the clue message or None if no clues left.
    """
    if not clues:
        return None

    clue, is_genuine = clues.pop(0)
    player["found_clues"] = player.get("clues", []) + [clue]

    clue_message = [
        "You discovered a clue!",
        Fore.BLUE + clue + Style.RESET_ALL
    ]

    if random.random() < 0.4 and is_genuine:
        # Add an insight for genuine clues (40% chance)
        clue_message.append(f"{Fore.GREEN}Your intuition tells you this clue seems important.{Style.RESET_ALL}")

    return clue_message


def accuse_spy(suspects, true_spy, player):
    """
    Handle player's accusation of who they believe is the spy.

    :param suspects: A list of strings representing possible suspects.
    :param true_spy: A string representing the actual spy's identity.
    :param player: A dictionary containing player's reputation information.
    :precondition: suspects must be a non-empty list of strings.
    :precondition: Ensure true_spy exists in suspects list.
    :precondition: Ensure player is a mutable dictionary.
    :postcondition: Display accusation menu using update_display().
    :postcondition: Modify player's reputation based on accusation correctness.
    :postcondition: Display outcome message using update_display().
    :return: True if accusation correct, False otherwise.
    """
    accusation_menu = ["Who do you think is the spy?"]
    for index, suspect in enumerate(suspects, 1):
        accusation_menu.append(f"{Fore.LIGHTYELLOW_EX}{index}. {suspect}{Style.RESET_ALL}")

    update_display(accusation_menu, save_text=True)

    while True:
        choice = input(f"Enter a number (1-{len(suspects)}): ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(suspects):
                accused = suspects[index]
                if accused == true_spy:
                    update_display(["You've uncovered the spy! Your mission is a success."], save_text=True)
                    player["reputation"] = player.get("reputation", 0) + 20
                    return True
                else:
                    update_display([
                        f"You wrongly accused {accused}!",
                        f"The true spy was {Fore.RED}{true_spy}{Style.RESET_ALL}.",
                        "Your reputation has suffered.",
                        f"You must find {true_spy} before you run out of moves.",

                    ], save_text=True)
                    player["reputation"] = player.get("reputation", 0) - 10
                    return False
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def initialize_level(player):
    """
    Initialize all components for level two gameplay.

    :param player: A dictionary containing player information to be updated.
    :precondition: Ensure player is a mutable dictionary with required keys.
    :postcondition: Execute level two introduction and training sequences.
    :postcondition: Start spy mission narrative.
    :postcondition: Set up game map environment.
    :postcondition: Place bishop on board and update map display.
    :postcondition: Generate spy clues and traps.
    :postcondition: Update player with level-specific attributes.
    :postcondition: Save updated player state.
    :return: Tuple containing (game_map, board_start, clues, true_spy, traps)
    """
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
        "movement_points": 15,
        "clues": clues
    })
    save_player(player)

    return game_map, board_start, clues, true_spy, traps


def handle_random_events(player, clues):
    """
    Handle random events that may occur during player's turn.

    :param player: A dictionary containing player information including clues_found
    :param clues: A list of available clues to discover
    :precondition: Ensure player is a mutable dictionary with 'clues_found' key
    :precondition: Ensure clues is a mutable list of clue tuples
    :postcondition: May discover and display a clue with 30% probability
    :postcondition: Update player's clues_found count if clue discovered
    :postcondition: Display clue message if one is found
    """
    if random.random() < 0.4 and clues:  # 40% chance to find clue
        clue_message = discover_clue(player, clues)
        if clue_message:
            player["clues_found"] += 1
            update_display(clue_message, save_text=True)
            return

    if random.random() < 0.3:  # 30% chance for random encounter
        event_message = encounter_event(player)
        update_display(["Event: " + event_message], save_text=True)


def handle_accusation(player, true_spy):
    """
    Prompt player to make spy accusation if they choose to.

    :param player: A dictionary containing player's reputation information.
    :param true_spy: A string representing the actual spy's identity.
    :precondition: Ensure player is a mutable dictionary.
    :precondition: Ensure true_spy is a valid suspect string.
    :postcondition: Display accusation prompt to player.
    :postcondition: If player chooses to accuse, execute accusation process.
    :postcondition: Modify player's reputation based on accusation outcome.
    :return: True if player makes correct accusation, False otherwise.
    """
    msg = [f"{Fore.LIGHTYELLOW_EX}You have enough information to make an accusation.{Style.RESET_ALL}"]
    update_display(msg, save_text=True)
    accusation_choice = input("Do you want to accuse someone now? (y/n): ").lower()

    if accusation_choice == 'y':
        suspects = ["The Knight", "The Rook", "The Queen", "The Pawn"]
        success = accuse_spy(suspects, true_spy, player)
        return success

    return False


def run_level(player):
    """
    Execute main game loop for level two gameplay.

    :param player: A dictionary containing player state information.
    :precondition: Ensure player dictionary contains required keys (health, position, etc.).
    :postcondition: Initialize level components and player state.
    :postcondition: Process player moves until game ending conditions met.
    :postcondition: Handle traps, random events, and accusation opportunities.
    :postcondition: Update player state and display throughout gameplay.
    :postcondition: Save player progress after each move.
    """
    game_map, board_start, clues, true_spy, traps = initialize_level(player)
    max_moves, moves_taken = 20, 0
    player.update({"max_moves": max_moves, "moves_taken": moves_taken})
    save_player(player)

    while (player["moves_taken"] < max_moves and
           player["health"] > 0 and
           player["movement_points"] > 0):

        desired_move = get_bishop_move_choice()
        if not desired_move:
            update_display(["Invalid move for a bishop! Try again."], game_map=game_map)
            continue

        current_pos = player["position"]
        if not validate_move(board_start, current_pos[0], current_pos[1], desired_move):
            update_display([f"{Fore.RED}Invalid move! Try again.{Style.RESET_ALL}"], save_text=True)
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
            update_player_on_map(game_map, new_position, current_pos)
            update_display(trap_message, save_text=True)
            player["moves_taken"] += 1
            save_player(player)
            continue

        handle_random_events(player, clues)
        player["moves_taken"] += 1
        save_player(player)

        if player["clues_found"] >= 3:
            if handle_accusation(player, true_spy):
                promote_player(player)
                print_level_completion_message(2)
                return True  # Level completed successfully
            max_moves -= 3  # Penalty for wrong accusation_moves -= 3
            player["max_moves"] = max_moves
            save_player(player)

    save_player(player)
    if player["movement_points"] <= 0:
        update_display([f"{Fore.RED}You're out of movement points! Game over.{Style.RESET_ALL}"])
    if player["health"] <= 0:
        update_display([f"{Fore.RED}You've died! Game over.{Style.RESET_ALL}"])
    return False