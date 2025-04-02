"""
Display Manager

Handles all game visuals in a two-panel layout:
- Left panel: Status box and game messages
- Right panel: Game map

Key Features:
- Dynamic text boxes with automatic sizing
- ANSI color code support and cleaning
- Message history saving/loading
- Screen clearing and formatted printing

Usage:
1. update_display() - Main display refresh
2. make_status_box() - Create bordered status panels
3. clean_ansi() - Remove color codes for saving
4. *_display_text() - Manage message history
"""
from colorama import Fore, Style
import re, json, time
from map import setup_game_environment, update_player_on_map
from player_manager import load_player, player_status

FILE_NAME = "display_text.json"


def loading_screen():
    """
    Display a loading screen with a delayed effect.
    """
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
    """
    Load and return display messages from JSON file.

    :postcondition: Attempt to read and parse JSON file
    :postcondition: Return empty list if file missing or invalid
    :return: List of message strings if successful, empty list otherwise
    """
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)  # Returns a list of messages
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# noinspection PyTypeChecker
def save_display_text(messages):
    """
    Save display messages to JSON file after cleaning ANSI codes.

    :param messages: List of message strings to save.
    :precondition: Messages must be strings (may contain ANSI codes).
    :postcondition: ANSI codes removed from all messages.
    :postcondition: Messages saved to JSON file with 4-space indentation.
    """
    cleaned_messages = [clean_ansi(msg) for msg in messages]  # Strip ANSI before saving
    with open(FILE_NAME, "w") as file:
        json.dump(cleaned_messages, file, indent=4)


# Append new message and manage length
def update_display_text(new_message, max_len, color=Fore.GREEN, save_text=False, colored=True):
    """
    Update and format display messages with optional coloring and saving.

    :param new_message: Message or list of messages to add.
    :param max_len: Maximum number of messages to retain.
    :param color: ANSI color code (default: Fore.GREEN).
    :param save_text: Whether to save with separator (default: False).
    :param colored: Whether to apply coloring (default: True).
    :precondition: new_message must be string or list of strings.
    :precondition: max_len must be positive integer.
    :postcondition: Load existing messages.
    :postcondition: Add separator if save_text enabled.
    :postcondition: Apply coloring if enabled.
    :postcondition: Truncate to max_len messages if needed.
    :return: List of formatted messages.
    """
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
    """Remove all ANSI escape sequences from a string.

    :param text: String potentially containing ANSI codes
    :precondition: Input must be a string
    :postcondition: All ANSI escape sequences removed
    :return: Cleaned string without ANSI codes

    >>> clean_ansi("\033[31mRed Text\033[0m")
    'Red Text'
    >>> clean_ansi("Normal \x1B[1mBold\x1B[0m Text")
    'Normal Bold Text'
    >>> clean_ansi("No codes here")
    'No codes here'
    >>> clean_ansi("\x1B[38;2;255;0;0mComplex\x1B[0m")
    'Complex'"""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def make_status_box(status_message):
    """
    Create a bordered text box around status messages.

    :param status_message: List of strings to display in the box.
    :precondition: status_message must be a non-empty list of strings.
    :postcondition: Calculate maximum line length for box width.
    :postcondition: Format all lines to equal width.
    :postcondition: Add Unicode border characters around content.
    :return: List of strings forming the complete text box.
    """
    # Find max length for dynamic box size
    max_length = max(len(line) for line in status_message)
    border_top = "┌" + "─" * (max_length + 2) + "┐"
    border_bottom = "└" + "─" * (max_length + 2) + "┘"

    # Format each line to fit the box
    formatted_lines = [f"│ {line.ljust(max_length)} │" for line in status_message]

    box = [border_top] + formatted_lines + [border_bottom]
    return box


def update_display(display_text, save_text=False, status=True):
    """
    Update and print the game display with map and status information.

    :param display_text: Text or list of text lines to display.
    :param save_text: Whether to save the display text (default: False).
    :param status: Whether to show player status (default: True).
    :precondition: display_text must be string or list of strings.
    :postcondition: Clear the screen (20 newlines).
    :postcondition: Load game map and player data.
    :postcondition: Generate status box if enabled.
    :postcondition: Format and truncate display text.
    :postcondition: Save text if requested (with ANSI codes cleaned).
    :postcondition: Print formatted two-column display (left: messages/status, right: map).
    """
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
