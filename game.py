"""
The Chess War: Rise of a Soldier
Main Game Loop
"""
import time

import level_one
import level_three
import level_two
import player_manager
from display_manager import loading_screen

PLAYER_FILE = "player.json"
DISPLAY_FILE = "display_text.json"


def clean_files(only_display=False):
    """Clean player and display JSON files."""
    open(DISPLAY_FILE, "w").close()
    if not only_display:
        open(PLAYER_FILE, "w").close()


def run_game():
    """
    Full game run with loop, cleanup, and replay prompt
    """
    while True:

        clean_files()
        player = player_manager.load_player()

        loading_screen()
        level_one.run_level(player)
        time.sleep(5)
        clean_files(only_display=True)
        level2_result = level_two.run_level(player)
        time.sleep(5)
        clean_files(only_display=True)
        if level2_result:
            level_three.run_level(player)

        clean_files()
        print("\n🎮 Game Over. Would you like to play again? (y/n)")
        if input("> ").strip().lower() != "y":
            print("👋 Thanks for playing! Goodbye.")
            break


def main():
    """
    Drive the program.
    """
    try:
        run_game()
    except KeyboardInterrupt:
        print("\n\n⚠️ Game interrupted by user. Cleaning up...")
        clean_files()
        print("🧼 Cleanup complete. Exiting...")


if __name__ == "__main__":
    main()
