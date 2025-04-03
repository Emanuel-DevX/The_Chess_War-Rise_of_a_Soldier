from level_two import level_two_intro
from unittest import TestCase
from unittest.mock import patch


class TestLevelTwoIntro(TestCase):

    @patch("builtins.input", return_value="")
    @patch("level_two.update_display")
    def test_level_two_intro(self, mock_update_display, mock_input):
        level_two_intro()

        # Ensure update_display is called with correctly formatted text
        expected_text = [line.strip() for line in """

██╗     ███████╗██╗   ██╗███████╗██╗         ████████╗██╗    ██╗ ██████╗ 
██║     ██╔════╝██║   ██║██╔════╝██║         ╚══██╔══╝██║    ██║██╔═══██╗
██║     █████╗  ██║   ██║█████╗  ██║            ██║   ██║ █╗ ██║██║   ██║
██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║            ██║   ██║███╗██║██║   ██║
███████╗███████╗ ╚████╔╝ ███████╗███████╗       ██║   ╚███╔███╔╝╚██████╔╝
╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝       ╚═╝    ╚══╝╚══╝  ╚═════╝ 

    ──────────────────────────────────
        LEVEL 2: THE BISHOP'S ASCENT 
    ──────────────────────────────────

    The battlefield is no longer a chaotic mess of warriors clashing head-on.  
    It is a game of sight, angles, and precision. You have been chosen for  
    the **Bishop's Path**, a warrior of foresight and deadly accuracy.  

    "Patience and wisdom will guide your blade," whispers the High Priest.

    You are no longer bound to a single step forward. You now move  
    **diagonally across the battlefield**, cutting through enemy lines  
    with speed and grace.

    ⚔️ **New Movement Abilities:**
      * The Bishop moves **one step diagonally** per turn.
      * You must think ahead—your path is limited, but your strategy is key.
      * Enemies lurk in the shadows. Position yourself wisely to survive.

    The path to mastery is not about speed—it is about **seeing what others do not**.  
    Adapt, or be eliminated.

    ➡️ Press ENTER to begin your trial...
    """.splitlines()]

        mock_update_display.assert_called_once_with(expected_text, status=False)

        mock_input.assert_called_once()
