"""
Module for managing player data in JSON format.
Handles loading, saving, and updating player information.
"""
import json


def initialize_player():
    """
    Create and save a new player dictionary with default starting values.

    :postcondition: Creates dictionary with all required player attributes.
    :postcondition: Saves player data using save_player().
    :return: Dictionary containing initialized player data.
    """
    player = {
        "health": 30,
        "gold": 25,
        "boldness": 0,
        "movement_points": 50,
        "moves_taken": 0,
        "clues_found": 0,

        "piece": "pawn",
        "position": [0, 0],
        "inventory": [],
        "knowledge": [],
        "completed_challenges": [],
    }
    save_player(player)
    return player


# noinspection PyTypeChecker
def save_player(player_dict):
    """
    Save player data to a JSON file.

    :param player_dict: Dictionary containing player data to save.
    :precondition: player_dict must be JSON-serializable.
    :postcondition: Data saved to 'player.json' with 4-space indentation.
    """
    with open('player.json', 'w') as file:
        json.dump(player_dict, file, indent=4)


def load_player():
    """
    Load player data from JSON file or initialize new player if file doesn't exist.

    :postcondition: Attempt to load player.json file.
    :postcondition: Initialize new player if file missing or invalid.
    :return: Dictionary containing player data.
    """
    try:
        with open('player.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Creating new player data...")
        return initialize_player()


def promote_player(player):
    """
    Promote the player.

    :param player: A dictionary representing the player's attributes.
    :postcondition: Update the player's piece, skills, and completed challenges.

    >>> test_player = {'piece': 'pawn', 'position': [1,1], 'gold': 0, 'knowledge': [], 'completed_challenges': []}
    >>> expected = {'piece': 'bishop', 'position': [0,0], 'gold': 20, 'knowledge': ['Master of Diagonal Warfare'],\
        'completed_challenges': ['Level 1 Completed']}
    >>> promote_player(test_player)
    >>> test_player == expected
    True
    """
    if player["piece"] == "pawn":
        player["piece"] = "bishop"
        player["position"] = [0, 0]
        player["gold"] += 20
        player["knowledge"].append("Master of Diagonal Warfare")
        player["completed_challenges"].append("Level 1 Completed")
    elif player["piece"] == "bishop":
        player["piece"] = "rook"
        player["gold"] += 30
        player["knowledge"].append("Master of Straight-Line Power")
        player["completed_challenges"].append("Level 2 Completed")
        player["position"] = [0, 0]

    elif player["piece"] == "rook":
        player["piece"] = "overlord"
        player["gold"] += 50
        player["knowledge"].append("Overlord - Imposes dominance without being a King.")
        player["completed_challenges"].append("Level 3 Completed")


def player_status():
    """
    Generate current player status summary for display.

    :postcondition: Loads current player data.
    :postcondition: Compiles key status information.
    :postcondition: Returns formatted status lines.
    :return: List of strings containing player status information.
    """
    player = load_player()  # Assuming this function loads player data

    player_hl = player["health"]
    player_gd = player["gold"]
    clues_found = player.get("clues_found", 0)
    clues = player.get("clues", [])
    total_clues = len(clues) + clues_found
    max_moves = player.get("max_moves", 50)
    goals = {
        "pawn": "Reach the 8th rank without being captured.",
        "bishop": "Find the spy while avoiding traps!",
        "rook": "Spy in enemy territory to uncover the king's location."
    }

    if player["piece"] == "rook":
        status_message = [
            f"Health: {player_hl}",
            f"Gold: {player_gd}",
            f"Total suspicion: {player['suspicion']}%",
            f"Next task: {player["next_task"]}",
            f"Your goal: {goals[player['piece']]}"
        ]
        return status_message

    status_message = [
        f"Health: {player_hl}",
        f"Gold: {player_gd}",
        f"Clues found: {clues_found}/{total_clues}",
        f"Movement points: {player['movement_points']}",
        f"Moves taken: {player['moves_taken']}/{max_moves}",
        f"Your goal: {goals[player['piece']]}"
    ]

    return status_message
