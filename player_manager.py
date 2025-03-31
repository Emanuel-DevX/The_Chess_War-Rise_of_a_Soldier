"""
Module for managing player data in JSON format.
Handles loading, saving, and updating player information.
"""
import json


def initialize_player():
    """Create a new player with default values."""
    player = {
        "health": 100,
        "gold":25,
        "boldness": 0,
        "movement_points": 50,
        "moves_taken": 0,
        "clues_found":0,

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
    with open('player.json', 'w') as file:
        json.dump(player_dict, file, indent=4)


def load_player():
    """Load player data from JSON file."""
    try:
        with open('player.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Creating new player data...")
        return initialize_player()

def update_player_attribute(key, value):
    """Update a specific player attribute."""
    player = load_player()
    player[key] = value
    save_player(player)
    return player

def add_to_inventory(item):
    """Add an item to player's inventory."""
    player = load_player()
    player["inventory"].append(item)
    save_player(player)
    return player

def add_knowledge(info):
    """Add information to player's knowledge."""
    player = load_player()
    player["knowledge"].append(info)
    save_player(player)
    return player


def player_status():
    player = load_player()  # Assuming this function loads player data

    player_hl = player["health"]
    player_gd = player["gold"]
    clues_found = player.get("clues_found", 0)
    clues = player.get("clues", [])
    total_clues = len(clues) + clues_found
    max_moves = player.get("max_moves", 50)

    status_message = [
        f"Health: {player_hl}",
        f"Gold: {player_gd}",
        f"Clues found: {clues_found}/{total_clues}",
        f"Movement points: {player['movement_points']}",
        f"Moves taken: {player['moves_taken']}/{max_moves}",
        "Your goal: Find the spy while avoiding traps!"
    ]

    return status_message
