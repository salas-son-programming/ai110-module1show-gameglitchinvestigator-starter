# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The purpose of this project was to debug and repair an AI-generated number guessing game built with Streamlit. The original version contained several logic and state-management bugs that made the game difficult to play correctly.

### Bugs Found

* The higher/lower hints were reversed.
* The secret number was sometimes converted into a string, causing type errors.
* Starting a new game after winning did not correctly reset the game state.
* The Hard difficulty range was not harder than Normal mode.

### Fixes Applied

* Refactored game logic into `logic_utils.py`.
* Corrected the hint messages in `check_guess()`.
* Fixed the secret number type issue.
* Reset the game status correctly when starting a new game.
* Added automated tests for the game logic and verified them with pytest.




## 📸 Demo Walkthrough

<!-- Describe your fixed game in numbered steps so a reader can follow along without watching a video: -->

1. User enters a guess of 40.
2. Game returns "Too Low".
3. User enters 70.
4. Game returns "Too High".
5. Score updates after each guess.
6. User guesses correctly.
7. The game displays the final score and balloons.

<!-- **Screenshot** *(optional)*: Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```text
pytest
========================= 3 passed in 0.XXs =========================
```



