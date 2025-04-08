# 🌟 The Chess War: Rise of a Soldier

## 🏛️ Overview
_The Chess War: Rise of a Soldier_ is a turn-based RPG-strategy game built with Python. Inspired by Ethiopian legends and the structure of chess, the player advances through levels assuming roles of chess pieces—starting as a pawn and rising through the ranks.

In **Level 3: The Rook's Shadow Campaign**, the player is "Agent Tower," a spy embedded in the territory of Adal during a time of rebellion. To succeed, the player must:
- Solve linguistic and cultural puzzles
- Decipher an encrypted message
- Make strategic choices to infiltrate and capture the enemy king
- Either face death in solo combat or victory through teamwork

This game showcases multiple elements of clean, modular Python development.

## 👷 Developer
**Emanuel Fisha Molla**

 Github: [@Emanuel-DevX](https://github.com/Emanuel-DevX)

**Student Number**: A01411440


## ⚙️ Technical Requirements Breakdown
### 🧪 Python Requirement Coverage

| Requirement Element          | Where to Find It (File:Line)                | Code Snippet / Summary                                                                      |
|-----------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------|
| (a) Immutable structures (tuples) | `map.py:112`                                | `return (row, col)` in `generate_level_interior()` – fast coord logic                       |
| (b) Mutable structures (lists/dicts) | `level_three.py:172`                        | `player["visible places"] = {}` – updated player vision dictionary                          |
| (c) Exception handling       | `player_manager.py:55`                      | `except (FileNotFoundError, json.JSONDecodeError):` – failover loading                      |
| (d) Scoped variables         | `level_three.py:33`                         | `intro_text = f"""..."""` scoped inside a function                                          |
| (e) Decomposition into functions | `level_three.py handle_tasks():589`         | `def handle_tasks(...)` – manages modular event triggers                                    |
| (f) Simple, flat code        | `game.py:24-48`                             | Main game loop uses linear logic with minimal nesting                                       |
| (g) List/dict comprehensions| `map.py:49`                                 | `[tile for tile in fire_area if tile not in excluded]`                                      |
| (h) Selection using if-statements | `level_three.py:623`                        | `if handler:` dispatch pattern in `handle_tasks()`                                          |
| (i) Repetition via loops     | `level_three.py run_level() :694`           | `while not found_king and player["health"] > 0 and player["suspicion"] <100:`               |
| (j) Membership operator usage| `map.py:65`                                 | `if tile not in excluded` – filter logic                                                    |
| (k) `range()` function usage | `map.py intialize_game_map():135`           | `for row in range(...)` in grid generator                                                   |
| (l) `itertools` usage        | `level_three.py generate_adal_places():165` | `from itertools import product ` for grid sampling                                          |
| (m) `random` module usage    | `level_three.py:170`                        | `random.sample(...)`, `random.choice(...)` – efficient place gen                            |
| (n) Function annotations     | `map.py:122`                                | `-> list[list[str]]` intialize_game_map() function header                                   |
| (o) Doctests and/or unit tests| `tests/`, `utilities.py:78`                 | Unittests packaged for each module and Doctests inside each funciton that can be doctested; |
| (p) Formatted output         | `display_manager.py:205`                    | `f"│{color_pre} {line.ljust(max_length)}{color_reset} │"` – output with color               |

## 📅 Running the Game

> ⚠️ **Recommended:** Run the game in **PyCharm’s terminal** with a minimum window size of **200×80 characters** to ensure full UI and display features work correctly.

```bash
python3 game.py
```

## 🌐 Dependencies
Install requirements:
```bash
pip install -r requirements.txt
```

## ✈️ Levels
| Level | Title | Summary |
|-------|-------|---------|
| Level 1 | **Pawn's Journey** | Escape through a battlefield to reach enemy lines and earn your promotion. Master forward movement and basic survival. |
| Level 2 | **The Bishop's Eye** | Investigate a spy by moving diagonally on bishop-colored tiles, uncovering clues in sequence. |
| Level 3 | **The Rook's Shadow Campaign** | Infiltrate enemy territory as a spy. Translate languages, survive traps, and decode encrypted messages to locate the enemy king. |


## 🔧 Technologies
- Python 3.13+
- Colorama for terminal color
- Doctest & Unittest for testing
---

> _"The war of logic and loyalty begins on the chessboard of destiny."_

