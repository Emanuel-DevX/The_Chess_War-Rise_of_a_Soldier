import json
from map import setup_game_environment, update_player_on_map
from player_manager import load_player, player_status


FILE_NAME = "display_text.json"
MAX_LINES = 30

def load_display_text():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)  # Returns a list of messages
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# noinspection PyTypeChecker
def save_display_text(messages):
    with open(FILE_NAME, "w") as file:
        json.dump(messages, file, indent=4)

# Append new message and manage length
def update_display_text(new_message, max_len):

    messages = load_display_text()
    messages += new_message
    # Trim the list if it exceeds MAX_LINES
    if len(messages) > max_len:
        messages = messages[-max_len:]  # Keep only the last MAX_LINES messages
    return messages




def make_status_box(status_message):
    # Find max length for dynamic box size
    max_length = max(len(line) for line in status_message)
    border_top = "┌" + "─" * (max_length + 2) + "┐"
    border_bottom = "└" + "─" * (max_length + 2) + "┘"


    # Format each line to fit the box
    formatted_lines = [f"│ {line.ljust(max_length)} │" for line in status_message]

    box = [border_top] + formatted_lines + [border_bottom]
    return box


def update_display(display_text, save_text=False, status=True):

    print("\n"*10)
    game_map = setup_game_environment()
    player = load_player()
    if player["position"] != [0,0]:
        update_player_on_map(game_map, player["position"])
    status_box = make_status_box(player_status())
    status_len = len(status_box)

    left_screen = status_box
    if not status:
        status_len = 0
        left_screen = []

    messages = update_display_text(display_text, 32 - status_len)
    messages_len = len(messages)
    if save_text:
        save_display_text(messages)
    if messages_len + status_len < 30:
        left_screen += ["" for _ in range(30 - (status_len + messages_len))]

    left_screen += messages

    max_rows = max(len(left_screen), len(game_map))

    for row_number in range(max_rows):
        left_part = left_screen[row_number] if row_number < len(left_screen) else ""
        right_part = "".join(game_map[row_number]) if row_number < len(game_map) else ""
        print(f"{left_part:<100}{right_part}")
