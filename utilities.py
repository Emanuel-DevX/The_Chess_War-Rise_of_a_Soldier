import random
import time

import player_manager
from map import setup_game_environment, update_player_on_map
from player_manager import save_player


def print_map(rows, column, player_loc):
    """
    Display a visual representation of the game map with walls and the player's position.

    :param rows: An integer representing the number of rows in the game map.
    :param column: An integer representing the number of columns in the game map.
    :param player_loc: A tuple (x, y) representing the player's current location.
    :precondition: rows must be a non-negative integer.
    :precondition: column must be a non-negative integer.
    :precondition: player_loc must be a tuple of two integers, where both are within the range of (0, rows-1) and
                   (0, column-1) respectively.
    :postcondition: Display a visual representation of the game map with walls around the edge and the player's
                    position marked with a blue circle.

    >>> # print_map(2, 2, (1, 1)) will print the following map.
    >>> # 🏛️ 🏛️ 🏛️ 🏛️
    >>> # 🏛️       🏛️
    >>> # 🏛️    🔵 🏛️
    >>> # 🏛 🏛️ 🏛️ 🏛️
    """
    rows += 1
    column += 1
    my_map = "\n"

    for row in range(-1, rows):
        for col in range(-1, column):
            if row == -1 or col == -1 or row == rows - 1 or col == rows - 1:
                my_map += "⛩ "
            else:
                if player_loc == (row, col):
                    my_map += "🔵 "
                else:
                    my_map += "   "
        my_map += "\n"
    print(my_map)


def validate_move(board_start, row, col, direction):
    """
    Validate if the character's proposed move stays within the boundaries of the board.

    :param board_size: An integer representing the size of the square board (board is board_size x board_size).
    :param row: An integer representing the character's current row position.
    :param col: An integer representing the character's current column position.
    :param direction: A string representing the proposed movement direction, which can be:
                      'north', 'south', 'east', 'west', 'north_east', 'north_west',
                      'south_east', or 'south_west'.
    :precondition: board_size must be a positive integer.
    :precondition: row and col must be integers between 0 and board_size - 1 (inclusive).
    :precondition: direction must be one of the allowed direction strings ('north', 'south',
                   'east', 'west', 'north_east', 'north_west', 'south_east', 'south_west').
    :postcondition: Validate if the proposed move stays within the board boundaries.
    :return: True if the proposed move stays within the board boundaries, False otherwise.

    >>> validate_move(8, 7, 3, 'north')
    True
    >>> validate_move(8, 7, 3, 'south')
    False
    >>> validate_move(8, 0, 0, 'north')
    False
    >>> validate_move(8, 0, 0, 'west')
    False
    >>> validate_move(8, 4, 4, 'north_east')
    True
    >>> validate_move(8, 0, 7, 'north_west')
    False
    >>> validate_move(8, 6, 6, 'south_east')
    True
    >>> validate_move(8, 1, 1, 'south_west')
    True
    """
    board_start_row = board_start[0]
    board_start_col = board_start[1]
    if direction == 'north' and row > board_start_row:
        return True
    elif direction == 'south' and row < board_start_row + 8:
        return True
    elif direction == 'east' and col < board_start_col + 8:
        return True
    elif direction == 'west' and col > board_start_row:
        return True
    elif direction == 'north_east' and row > board_start_row and col < board_start_col + 7:
        return True
    elif direction == 'north_west' and row > board_start_row and col > board_start_col:
        return True
    elif direction == 'south_east' and row < board_start_row + 7 and col < board_start_col + 7:
        return True
    elif direction == 'south_west' and row < board_start_row + 7 and col > board_start_col:
        return True

    return False


def move(board_size, row, col, direction):
    """
    Move the character on the board according to the desired direction, if valid.

    :param board_size: An integer representing the size of the square board (board is board_size x board_size).
    :param row: An integer representing the character's current row position.
    :param col: An integer representing the character's current column position.
    :param direction: A string representing the proposed movement direction, which can be:
                      'north', 'south', 'east', 'west', 'north_east', 'north_west',
                      'south_east', or 'south_west'.
    :precondition: board_size must be a positive integer.
    :precondition: row and col must be integers between 0 and board_size - 1 (inclusive).
    :precondition: direction must be one of the allowed direction strings ('north', 'south',
                   'east', 'west', 'north_east', 'north_west', 'south_east', 'south_west').
    :postcondition: If the move is valid, the character is moved in the specified direction.
                    If the move is invalid, the character remains in the current position.
    :return: A tuple (new_row, new_col) representing the character's new position.

    >>> move(8, 7, 3, 'north')
    (6, 3)
    >>> move(8, 0, 0, 'west')
    (0, 0)
    >>> move(8, 4, 4, 'north_east')
    (3, 5)
    >>> move(8, 1, 1, 'south_west')
    (2, 0)
    """
    if validate_move(board_size, row, col, direction):
        if direction == 'north':
            row -= 1
        elif direction == 'south':
            row += 1
        elif direction == 'east':
            col += 1
        elif direction == 'west':
            col -= 1
        elif direction == 'north_east':
            row -= 1
            col += 1
        elif direction == 'north_west':
            row -= 1
            col -= 1
        elif direction == 'south_east':
            row += 1
            col += 1
        elif direction == 'south_west':
            row += 1
            col -= 1
    return row, col


def column_to_file(column):
    """
    Convert column index (0-7) to chess file (A-H).

    :param column: A positive integer between 0 and 7 (inclusive).
    :precondition: column must be a positive integer between 0 and 7 (inclusive).
    :postcondition: Convert the column to its equivalent chess file correctly.
    :return: A single letter character representing the file (column position) on a chess board.

    >>> column_to_file(3)
    'D'
    >>> column_to_file(1)
    'B'
    """
    return chr(65 + column)


def check_ambush(player):
    """
    Check if the player encounters an ambush based on their boldness level.

    :param player: A dictionary representing the player's attributes.
    :postcondition: Reduces health if an ambush occurs.
    """
    if player["boldness"] > 3 and random.random() < (player["boldness"] * 0.1):
        damage = random.randint(20, 40)
        player["health"] -= damage
        print(f"💀 Ambush! You lost {damage} health points!")
    else:
        print("🛡️ No ambush this time.")


def promote_player(player):
    """
    Promote the player.

    :param player: A dictionary representing the player's attributes.
    :postcondition: Update the player's piece, skills, and completed challenges.
    """
    if player["piece"] == "pawn":
        player["piece"] = "bishop"
        player["position"] = [0,0]
        player["gold"] += 20
        player["knowledge"].append("Master of Diagonal Warfare")
        player["completed_challenges"].append("Level 1 Completed")
        print("🔱 Your pawn has been promoted to a Bishop!")
    elif player["piece"] == "bishop":
        player["piece"] = "rook"
        player["gold"] += 30
        player["knowledge"].append("Master of Straight-Line Power")
        player["completed_challenges"].append("Level 2 Completed")
        print("🏰 Your Bishop has been promoted to a Rook!")
    elif player["piece"] == "rook":
        player["piece"] = "overlord"
        player["gold"] += 50
        player["knowledge"].append("Overlord - Imposes dominance without being a King.")
        player["completed_challenges"].append("Level 3 Completed")
        print("👑 The Rook, now Overlord, enforces its rule from the Obsidian Tower!")


def print_level_completion_message(level):
    """
    Print a congratulatory message when a player completes a level.

    :param level: The level that was completed.
    """
    messages = {
        1: "🎉 Congratulations! You have completed Level 1! Your journey as a Bishop begins.",
        2: "🎉 Well done! Level 2 completed! The power of the Rook is now yours.",
        3: "👑 Magnificent! You have reached the pinnacle as an Overlord! Rule wisely."
    }
    print(messages.get(level, "🎉 Congratulations on your achievement!"))

def print_game_map(game_map):
    """Print the game map with row numbers"""

    for row_number, row in enumerate(game_map):
        print(f"{row_number:>100}", end="")
        print("".join(row))

def update_display(display_text):

    print("\n"*50)
    game_map = setup_game_environment()
    player = player_manager.load_player()
    if player["position"] != [0,0]:
        update_player_on_map(game_map, player["position"])
    player_h = player["health"]
    player_g = player["gold"]
    health_msg = f"""
                ┌─────────────┐
                │❤️HEALTH: {player_h:03d}│
                │  💰GOLD: {player_g:03d}│
                └─────────────┘"""

    game_map += [line.strip() for line in health_msg.splitlines()]
    my_text = []
    display_len = len(display_text)
    if display_len < 30:
        my_text += ["" for _ in range(30 - display_len)]
    for line in display_text:
        my_text.append(line.strip())
    my_text += ["" for _ in range(10)]

    for row_number, row in enumerate(game_map):
        print(f"{my_text[row_number]:<100}", end="")
        print("".join(row))



def set_traps(game_map, board_start, num_traps=5):
    """
    Set hidden traps on the board.

    :param game_map: Current game map
    :param board_start: Board starting position
    :param num_traps: Number of traps to place
    :return: List of trap positions
    """
    traps = []
    for _ in range(num_traps):
        while True:
            row = random.randint(board_start[0], board_start[0] + 7)
            col = random.randint(board_start[1], board_start[1] + 7)

            if game_map[row][col] == ' ' and (row, col) not in traps:
                traps.append((row, col))
                break

    return traps


def loading_screen():
    load_msg = """

    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗       
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝       
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗      
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║      
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝

    """
    print(load_msg)
    for _ in range(90):
        print("██", end="")
        time.sleep(0.1)