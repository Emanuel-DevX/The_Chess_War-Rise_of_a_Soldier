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