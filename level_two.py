from utilities import *


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
    update_display([line.strip() for line in intro_text.splitlines()])
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
    update_display(training_text.splitlines())
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
    update_display(mission_text.splitlines())
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
        player_manager.save_player(player)

        update_display([])
        print("✅ Bishop placed on " + ("light" if choice == 'L' else "dark") + " square!")
        time.sleep(2)
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



def run_level(player):
    level_two_intro()
    level_two_training()
    spy_mission()
    game_map = setup_game_environment()
    board_start = [17, 19]
    place_bishop(player, board_start)
    update_player_on_map(game_map, player["position"])
    clues, true_spy = generate_clues()

