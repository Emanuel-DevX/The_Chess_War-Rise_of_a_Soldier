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
    >>> # 🏛️ 🏛️ 🏛️ 🏛️
    """
    rows += 1
    column += 1
    my_map = "\n"

    for row in range(-1, rows):
        for col in range(-1, column):
            if row == -1 or col == -1 or row == rows - 1 or col == rows - 1:
                my_map += "🏛️ "
            else:
                if player_loc == (row, col):
                    my_map += "🔵 "
                else:
                    my_map += "   "
        my_map += "\n"
    print(my_map)


def validate_move(board_size, row, col, direction):
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
    :postcondition: Returns True if the proposed move stays within the board boundaries, False otherwise.

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
    if direction == 'north' and row > 0:
        return True
    elif direction == 'south' and row < board_size - 1:
        return True
    elif direction == 'east' and col < board_size - 1:
        return True
    elif direction == 'west' and col > 0:
        return True
    elif direction == 'north_east' and row > 0 and col < board_size - 1:
        return True
    elif direction == 'north_west' and row > 0 and col > 0:
        return True
    elif direction == 'south_east' and row < board_size - 1 and col < board_size - 1:
        return True
    elif direction == 'south_west' and row < board_size - 1 and col > 0:
        return True

    return False
