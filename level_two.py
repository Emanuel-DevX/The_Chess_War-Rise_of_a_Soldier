def level_two_intro():
    intro_text = """
    ───────────────────────────────────────
       🔥 LEVEL 2: THE BISHOP'S ASCENT 🔥
    ───────────────────────────────────────

    The battlefield is no longer a chaotic mess of warriors clashing head-on.  
    It is a game of sight, angles, and precision. You have been chosen for  
    the **Bishop's Path**, a warrior of foresight and deadly accuracy.  

    "Patience and wisdom will guide your blade," whispers the High Priest.

    You are no longer bound to a single step forward. You now move  
    **diagonally across the battlefield**, cutting through enemy lines  
    with speed and grace.

    ⚔️ **New Movement Abilities:**
      🔹 The Bishop moves **one step diagonally** per turn.
      🔹 You must think ahead—your path is limited, but your strategy is key.
      🔹 Enemies lurk in the shadows. Position yourself wisely to survive.

    The path to mastery is not about speed—it is about **seeing what others do not**.  
    Adapt, or be eliminated.

    ➡️ Press ENTER to begin your trial...
    """
    print(intro_text)
    input()


def level_two_training():
    training_text = """
    ────────────────────────────────────────────
              🏹 LEVEL 2 TRAINING 🏹
    ────────────────────────────────────────────

    As a **bishop**, your movement is now limited to the color of your starting square.  
    If you begin on a **dark square**, you will always remain on dark squares.  
    If you start on a **light square**, you will always move on light squares.
    
        ┌────────────────────────────┐
        │   MOVE OPTIONS:            │
        │     🔹 North West   (↖)    │
        │     🔹 North East   (↗)    │
        │     🔹 South West   (↙)    │
        │     🔹 South East   (↘)    │
        └────────────────────────────┘

         8 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
         7 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
         6 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
         5 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
         4 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
         3 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
         2 ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ 
         1 ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ ⬛ ⬜ 
           A  B  C  D  E  F  G  H
    
    
    ⚔️ **Movement Rules:**
      🔹 You can only travel on **your color** (dark or light).
      🔹 No jumping over obstacles.
      🔹 Capture enemies by stepping onto their position.

    📜 **Training Drill:**
      - Try moving **diagonally** to an empty square of your color.
      - Capture the target dummy placed diagonally from you.
      - Be mindful of the battlefield—some paths may be blocked.

    **The battlefield rewards wisdom over speed.**  
    Master your movement, and you will survive.

    ➡️ Press ENTER to start training...
    """
    print(training_text)
    input()


level_two_intro()
level_two_training()
