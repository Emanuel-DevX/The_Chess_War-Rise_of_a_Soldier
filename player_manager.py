"""
Module for managing player data in JSON format.
Handles loading, saving, and updating player information.
"""
import json


def initialize_player():
    """Create a new player with default values."""
    player = {
        "health": 100,
        "boldness": 0,
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