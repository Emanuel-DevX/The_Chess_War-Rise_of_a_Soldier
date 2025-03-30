def create_chess_board():
    """Create an 8x8 chess board pattern"""
    return [["⬜ " if (row + col) % 2 else "⬛ " for col in range(8)] for row in range(8)]


def generate_forest_tiles(excluded_positions):
    """Generate forest tiles while excluding specified positions"""
    vertical_strip = [(row, col) for row in range(20, 30) for col in range(25)]
    adjacent_rectangle = [(row, col) for row in range(0, 5) for col in range(25, 30)]
    all_forest_tiles = vertical_strip + adjacent_rectangle
    return [tile for tile in all_forest_tiles if tile not in excluded_positions]


def generate_fire_tiles(excluded_fire_tiles):
    """Generate fire tiles while excluding specified positions"""
    fire_area = [(row, col) for row in range(23, 30) for col in range(15, 21)]
    return [tile for tile in fire_area if tile not in excluded_fire_tiles]


def generate_level_interior(center_row, center_col, size=8):
    """Generate the interior area of a level"""
    return [
        (row, col)
        for row in range(center_row, center_row + size)
        for col in range(center_col, center_col + size)
    ]


def generate_level_walls(center_row, center_col, size=8):
    """Generate walls surrounding a level"""
    return [
        (row, col)
        for row in range(center_row - 1, center_row + size + 1)
        for col in range(center_col - 1, center_col + size + 1)
        if row == center_row - 1 or row == center_row + size
           or col == center_col - 1 or col == center_col + size
    ]


def initialize_game_map(size=30, default_tile="🌑 "):
    """Create a blank game map with specified dimensions"""
    return [[default_tile for _ in range(size)] for _ in range(size)]


def place_tiles_on_map(game_map, tiles, tile_type):
    """Place tiles of specified type on the game map"""
    for row, col in tiles:
        game_map[row][col] = tile_type


def add_chess_board_labels(game_map, start_row, start_col):
    """Add chess notation labels to the chess board"""
    for rank in range(8):
        game_map[start_row + rank][start_col - 1] = f" {8 - rank} "

    file_labels = [" A ", " B ", " C ", " D ", " E ", " F ", " G ", " H "]
    for file_index in range(8):
        game_map[start_row + 8][start_col + file_index] = file_labels[file_index]


def create_forest_tiles():
    """Create forest tiles with excluded positions"""
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