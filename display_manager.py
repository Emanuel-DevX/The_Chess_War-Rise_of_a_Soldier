from colorama import Fore, Style
import re, json, time
from map import setup_game_environment, update_player_on_map
from player_manager import load_player, player_status

FILE_NAME = "display_text.json"


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


def load_display_text():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)  # Returns a list of messages
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# noinspection PyTypeChecker
def save_display_text(messages):
    cleaned_messages = [clean_ansi(msg) for msg in messages]  # Strip ANSI before saving
    with open(FILE_NAME, "w") as file:
        json.dump(cleaned_messages, file, indent=4)


# Append new message and manage length
def update_display_text(new_message, max_len, color=Fore.GREEN, save_text=False, colored=True):
    messages = load_display_text() + [""]

    if save_text and new_message:
        messages = [msg for msg in messages[:] if msg != "=" * 80]
        messages.append("=" * 80)

    if colored:
        colored_messages = [f"{color}{msg}{Style.RESET_ALL}" for msg in new_message]
        messages += colored_messages
    else:
        messages += new_message
    return messages[-max_len:] if len(messages) > max_len else messages


def clean_ansi(text):
    """Remove all ANSI escape sequences from a string."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


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
    print("\n" * 20)
    game_map = setup_game_environment()
    player = load_player()
    if player["position"] != [0, 0]:
        update_player_on_map(game_map, player["position"])
    status_box = make_status_box(player_status())
    status_len = len(status_box)

    left_screen = status_box
    if not status:
        status_len = 0
        left_screen = []

    messages = update_display_text(display_text, 32 - status_len, save_text=save_text, colored=status)
    messages_len = len(messages)
    if save_text:
        clean_msg = [clean_ansi(msg) for msg in messages]
        save_display_text(clean_msg)
    if messages_len + status_len < 30:
        left_screen += ["" for _ in range(30 - (status_len + messages_len))]

    left_screen += messages

    max_rows = max(len(left_screen), len(game_map))

    for row_number in range(max_rows):
        left_part = left_screen[row_number] if row_number < len(left_screen) else ""
        right_part = "".join(game_map[row_number]) if row_number < len(game_map) else ""

        # Get visible length by removing ANSI codes
        visible_length = len(clean_ansi(left_part))
        padding = max(0, 100 - visible_length)

        # Apply padding manually after calculating visible length
        print(f"{left_part}{' ' * padding}{right_part}")
