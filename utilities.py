import random


def validate_move(board_start, row, col, direction):
    """
    Validate if the character's proposed move stays within the boundaries of the current board segment.

    :param board_start: A tuple (start_row, start_col) representing the top-left corner of the current 8x8 board segment.
    :param row: An integer representing the character's current row position within the segment.
    :param col: An integer representing the character's current column position within the segment.
    :param direction: A string representing the proposed movement direction, which can be:
                      'north', 'south', 'east', 'west', 'north_east', 'north_west',
                      'south_east', or 'south_west'.
    :precondition: board_start must be a tuple of two non-negative integers.
    :precondition: row and col must be integers between 0 and 7 (inclusive).
    :precondition: direction must be one of the allowed direction strings.
    :return: True if the proposed move stays within the current 8x8 segment, False otherwise.

    >>> validate_move((0, 0), 7, 3, 'north')  # From bottom edge moving north
    True
    >>> validate_move((0, 0), 7, 3, 'south')  # From bottom edge moving south (would exit segment)
    False
    >>> validate_move((0, 0), 0, 0, 'north')  # From top-left corner moving north
    False
    >>> validate_move((0, 0), 0, 0, 'west')    # From top-left corner moving west
    False
    >>> validate_move((0, 0), 4, 4, 'north_east')  # Valid diagonal move
    True
    >>> validate_move((0, 0), 0, 7, 'north_west')  # From top-right corner moving NW
    False
    >>> validate_move((0, 0), 6, 6, 'south_east')   # Valid SE move
    True
    >>> validate_move((0, 0), 1, 1, 'south_west')   # Valid SW move
    True
    """
    board_start_row = board_start[0]
    board_start_col = board_start[1]
    if direction == 'north' and row > board_start_row:
        return True
    elif direction == 'south' and row < board_start_row + 7:
        return True
    elif direction == 'east' and col < board_start_col + 7:
        return True
    elif direction == 'west' and col > board_start_col:
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


def move(row, col, direction):
    """
    Move the character on the board according to the desired direction, if valid.

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

    >>> move(7, 3, 'north')
    (6, 3)
    >>> move(0, 0, 'east')
    (0, 1)
    >>> move(4, 4, 'north_east')
    (3, 5)
    >>> move(1, 1, 'south_west')
    (2, 0)
    """
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


def print_level_completion_message(level):
    """
    Print a congratulatory message when a player completes a level.

    :param level: The level that was completed.
    """
    messages = {
        1: ("🎉 Congratulations! You have completed Level 1! Your journey as a Bishop begins."
            "🔱 Your pawn has been promoted to a Bishop!"),
        2: ("🎉 Well done! Level 2 completed! The power of the Rook is now yours."
            "🏰 Your Bishop has been promoted to a Rook!"),
        3: ("👑 Magnificent! You have reached the pinnacle as an Overlord! Rule wisely."
            "👑 The Rook, now Overlord, enforces its rule from the Obsidian Tower!")
    }
    print(messages.get(level, "🎉 Congratulations on your achievement!"))


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

            if game_map[row][col].strip() == '' and (row, col) not in traps:
                traps.append((row, col))
                break

    return traps


def check_for_trap(position, traps, player):
    """
    Check if the player stepped on a trap.

    :param position: Current position
    :param traps: List of trap positions
    :param player: Player dictionary
    :return: True if trap triggered, False otherwise
    """
    if position in traps:
        damage = random.randint(5, 15)
        player["health"] -= damage

        trap_message = [
            "⚠️ YOU TRIGGERED A TRAP! ⚠️",
            f"You take {damage} damage.",
            f"Remaining health: {player['health']}"
        ]

        # Add to player knowledge
        player["knowledge"].append("Discovered trap location")

        return True, trap_message
    return False,


def encounter_event(player):
    """
    Random encounter event while moving.

    :param player: Player dictionary
    :return: Event message
    """
    events = [
        "You found a hidden passage! +5 movement points.",
        "You sense a trap nearby. Proceed with caution.",
        "You spot enemy movement in the distance.",
        "You find signs of recent activity.",
        "The path ahead looks clear."
    ]

    event = random.choice(events)

    if "movement points" in event:
        player["movement_points"] = player.get("movement_points", 0) + 5

    return event

