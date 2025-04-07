from player_manager import load_player
from colorama import Fore, Style

def create_chess_board():
    """
    Generate a 8x8 chess board pattern with alternating squares.

    :postcondition: Create a perfect chess board pattern
    :return: List of lists representing the board (8 rows x 8 columns)

    >>> board = create_chess_board()
    >>> len(board)
    8
    >>> board[0][0]  # Top-left corner
    '⬛ '
    >>> board[0][1]
    '⬜ '
    >>> board[7][7]  # Bottom-right corner
    '⬛ '
    """
    return [["⬜ " if (row + col) % 2 else "⬛ " for col in range(8)] for row in range(8)]


def generate_forest_tiles(excluded_positions):
    """
    Generate list of forest tile coordinates excluding specified positions.

    :param excluded_positions: List of (row, col) tuples to exclude.
    :postcondition: Creates vertical strip (rows 20-29, cols 0-24).
    :postcondition: Creates adjacent rectangle (rows 0-4, cols 25-29).
    :postcondition: Filters out excluded positions.
    :return: List of (row, col) tuples representing forest tiles.

    >>> generate_forest_tiles([])[:3]  # First few tiles
    [(20, 0), (20, 1), (20, 2)]
    >>> len(generate_forest_tiles([]))  # Total tiles without exclusions
    275
    >>> len(generate_forest_tiles([(20, 0), (21, 1)])) #275 - 2   2 positions excluded
    273
    """
    vertical_strip = [(row, col) for row in range(20, 30) for col in range(25)]
    adjacent_rectangle = [(row, col) for row in range(0, 5) for col in range(25, 30)]
    all_forest_tiles = vertical_strip + adjacent_rectangle
    return [tile for tile in all_forest_tiles if tile not in excluded_positions]


def generate_fire_tiles(excluded_fire_tiles):
    """
    Generate coordinates for fire hazard tiles excluding specified positions.

    :param excluded_fire_tiles: List of (row, col) tuples to exclude from fire zone.
    :postcondition: Create rectangular fire zone (rows 23-29, columns 15-20).
    :postcondition: Filter out all excluded positions.
    :return: List of (row, col) tuples representing active fire tiles.

    >>> fire_tiles = generate_fire_tiles([])
    >>> len(fire_tiles)  # 7 rows x 6 columns
    42
    >>> (23, 15) in fire_tiles  # Top-left corner
    True
    >>> (29, 20) in fire_tiles  # Bottom-right corner
    True
    """
    fire_area = [(row, col) for row in range(23, 30) for col in range(15, 21)]
    return [tile for tile in fire_area if tile not in excluded_fire_tiles]


def generate_level_interior(center_row, center_col, size=8):
    """
    Generate the interior area of a level

    :param center_row: An integer representing the starting row of the level interior.
    :param center_col: An integer representing the starting column of the level interior.
    :param size: The size of the square level interior (default is 8).
    :return: List of (row, col) tuples representing the level interior.


    >>> interior = generate_level_interior(10, 10)
    >>> len(interior)  # 8 rows x 8 columns
    64
    >>> (10, 10) in interior  # Top-left corner
    True
    >>> (17, 17) in interior  # Bottom-right corner
    True
    """
    return [
        (row, col)
        for row in range(center_row, center_row + size)
        for col in range(center_col, center_col + size)
    ]


def generate_level_walls(center_row, center_col, size=8):
    """
    Generate walls surrounding a level.

    :param center_row: An integer representing the starting row of the level interior.
    :param center_col: An integer representing the starting column of the level interior.
    :param size: The size of the square level interior (default is 8).
    :return: List of (row, col) tuples representing the wall tiles.

    >>> walls = generate_level_walls(10, 10)
    >>> len(walls)  # 10x10 outer boundary - 8x8 inner space
    36
    >>> (9, 9) in walls  # Top-left corner of wall
    True
    >>> (18, 18) in walls  # Bottom-right corner of wall
    True
    >>> (10, 10) in walls  # Interior tile, should not be in walls
    False
    """
    return [
        (row, col)
        for row in range(center_row - 1, center_row + size + 1)
        for col in range(center_col - 1, center_col + size + 1)
        if row == center_row - 1 or row == center_row + size
           or col == center_col - 1 or col == center_col + size
    ]


def initialize_game_map(size=30, default_tile="🌑 "):
    """
    Create a blank game map with specified dimensions.

    :param size: The size of the square game map (default is 30x30).
    :param default_tile: The default tile representation for the map.
    :return: A 2D list representing the game map.

    >>> game_map = initialize_game_map(5, '#')
    >>> len(game_map)  # 5 rows
    5
    >>> len(game_map[0])  # 5 columns
    5
    >>> game_map[0][0] == "#"  # Check default tile
    True
    """
    return [[default_tile for _ in range(size)] for _ in range(size)]


def place_tiles_on_map(game_map, tiles, tile_type):
    """Place tiles of specified type on the game map.

    :param game_map: The game map represented as a 2D list.
    :param tiles: A list of (row, col) tuples where the tile should be placed.
    :param tile_type: The tile representation to place on the map.
    :postcondition: Modifies game_map in place by updating specified positions with tile_type.

    >>> test_map = initialize_game_map(5, "⬜")
    >>> place_tiles_on_map(test_map, [(1, 1), (2, 2)], "🔥")
    >>> test_map[1][1] == "🔥"
    True
    >>> test_map[2][2] == "🔥"
    True
    >>> test_map[0][0] == "⬜"  # Unchanged tile
    True
    """
    for row, col in tiles:
        game_map[row][col] = tile_type


def add_chess_board_labels(game_map, start_row, start_col):
    """
    Add chess notation labels to the chess board.

    :param game_map: The game map represented as a 2D list.
    :param start_row: The starting row for the chess board labels.
    :param start_col: The starting column for the chess board labels.
    :postcondition: Update game_map in place with chess rank and file labels.

    >>> test_map = initialize_game_map(10, "⬜")
    >>> add_chess_board_labels(test_map, 1, 1)
    >>> test_map[1][0] == " 8 "  # Rank 8 label
    True
    >>> test_map[9][1] == " A "  # File A label
    True
    """
    for rank in range(8):
        game_map[start_row + rank][start_col - 1] = f" {8 - rank} "

    file_labels = [" A ", " B ", " C ", " D ", " E ", " F ", " G ", " H "]
    for file_index in range(8):
        game_map[start_row + 8][start_col + file_index] = file_labels[file_index]


def create_forest_tiles():
    """
    Create forest tiles with excluded positions.

    :return: List of (row, col) tuples representing forest tiles.
    """
    excluded_forest_positions = {
        (4, 25), (3, 25), (4, 26),
        (4, 27), (3, 26), (2, 25), (20, 0), (29, 24)
    }
    return generate_forest_tiles(excluded_forest_positions)


def create_fire_tiles():
    """Create fire tiles with excluded positions"""
    excluded_fire_positions = [(29, 15), (29, 16), (28, 15), (27, 15), (29, 17)]
    return generate_fire_tiles(excluded_fire_positions)


def create_level_interiors():
    """Generate all level interior areas"""
    return (
            generate_level_interior(19, 4) +
            generate_level_interior(17, 19) +
            generate_level_interior(5, 15)
    )


def create_level_walls():
    """Generate all level walls"""
    return (
            generate_level_walls(19, 4) +
            generate_level_walls(17, 19) +
            generate_level_walls(5, 15)
    )


def place_chess_board(game_map, start_row=2, start_col=2):
    """
    Place chess board on the game map.

    :param game_map: The game map represented as a 2D list.
    :param start_row: The starting row for the chess board (default is 2).
    :param start_col: The starting column for the chess board (default is 2).
    :postcondition: Modifies game_map in place by inserting a 8x8 chess board.
    """
    chess_board = create_chess_board()
    for row_offset in range(8):
        for col_offset in range(8):
            game_map[start_row + row_offset][start_col + col_offset] = chess_board[row_offset][col_offset]
    add_chess_board_labels(game_map, start_row, start_col)


def print_game_map(game_map):
    """Print the game map with row numbers"""
    for row_number, row in enumerate(game_map):
        print(f"{row_number:>100}", end="")
        print("".join(row))


def update_player_on_map(game_map, new_position, old_position=None):
    game_map[new_position[0]][new_position[1]] = "👤 "
    if old_position:
        game_map[old_position[0]][old_position[1]] = "   "


def add_extra_places():
    pass

def setup_game_environment(rook_map=False):
    game_map = initialize_game_map()

    place_tiles_on_map(game_map, create_forest_tiles(), "🌲 ")
    place_tiles_on_map(game_map, create_fire_tiles(), "🔥 ")

    place_tiles_on_map(game_map, create_level_interiors(), "   ")
    place_tiles_on_map(game_map, create_level_walls(), "🏛️ ")

    place_chess_board(game_map)
    if rook_map:
        add_extra_places()

    return game_map

def get_adal_map():
    player = load_player()
    player_pos_x, player_pos_y = player["position"]
    visible_places = player["visible places"]
    adal_map = setup_game_environment()
    adal_map[player_pos_x][player_pos_y] = "🟡 "


    for _, data in visible_places.items():
        location = data["position"]
        loc_x, loc_y = location
        adal_map[loc_x][loc_y] = data["symbol"]

    return adal_map



