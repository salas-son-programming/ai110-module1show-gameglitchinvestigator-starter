# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, it looked functional, but several parts of the logic behaved incorrectly. The hints were reversed, so when my guess was too high, the game told me to guess higher instead of lower. I also noticed that the secret number behaved inconsistently and that some game state values were not reset properly after starting a new game.

### Bug Reproduction Log

| Input                               | Expected Behavior                             | Actual Behavior                          | Console Output / Error                                            |
| ----------------------------------- | --------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------- |
| Guess larger than secret            | Game should say "Go LOWER!"                   | Game said "Go HIGHER!"                   | No error                                                          |
| Guess smaller than secret           | Game should say "Go HIGHER!"                  | Game said "Go LOWER!"                    | No error                                                          |
| Clicking New Game after winning     | Game should restart normally                  | Game stayed in the won state             | No error                                                          |
| Submitting a guess on some attempts | Guess should be compared to an integer secret | TypeError because secret became a string | TypeError: '>' not supported between instances of 'int' and 'str' |

---

## 2. How did you use AI as a teammate?

I used ChatGPT while working on this project. AI helped me understand the bugs and suggested ways to reorganize the code into `logic_utils.py`. One correct suggestion was fixing the reversed hints in the `check_guess()` function. I verified the fix by running the Streamlit application and checking that the messages matched the guesses.

One incorrect or misleading suggestion involved import issues and file organization. Some suggestions did not immediately solve the problem, so I inspected the code and error messages myself. I learned that I needed to verify every AI suggestion instead of assuming it was correct.

---

## 3. Debugging and testing your fixes

I decided that a bug was fixed only after testing the game manually and running pytest. I created tests for the `check_guess()` function to verify that guesses above the secret returned "Too High" and guesses below the secret returned "Too Low". Running pytest showed that the functions behaved as expected. AI helped me understand how to write the tests and how to interpret some of the error messages.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script every time the user interacts with the page. Session state allows information such as the secret number, score, and number of attempts to persist between reruns. I would explain it to a friend by saying that session state acts like memory for the application, while the rest of the script starts over every time a button is pressed.

---

## 5. Looking ahead: your developer habits

One strategy I want to reuse is fixing one bug at a time and testing after every change. This project showed me that making many changes at once can make debugging harder. Next time I work with AI, I will provide smaller and more focused prompts and verify each suggestion before applying it. This project taught me that AI-generated code should be treated as a starting point rather than something that should automatically be trusted.
