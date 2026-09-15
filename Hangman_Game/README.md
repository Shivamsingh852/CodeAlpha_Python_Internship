# Hangman Game

## Objective
A simple but professional text-based Hangman game built in Python where the player guesses a randomly selected word one letter at a time. The game runs completely in the console without external libraries.

## Features
* Predefined list of 5 words randomly selected per game.
* Allows players to guess one letter at a time.
* Displays the current progress of the hidden word (using underscores).
* Keeps track of and displays already guessed letters.
* Validates user input (single letters only, prevents repeated guesses).
* Includes a max limit of 6 incorrect guesses before the game is lost.
* Displays a clear winning or losing message, revealing the word upon loss.
* Option to play another round after a game concludes.

## Technologies Used
* **Python 3**: Core language.
* **Standard Library**: Used `random` module to select words.

## Python Concepts Used
* **Modules**: `import random`
* **Lists**: Storing words and ASCII art frames.
* **Strings**: Formatting, manipulating, and checking characters.
* **Loops**: `while` loops for the core game loop and input prompts, `for` loops for word display.
* **Conditionals**: `if-elif-else` structures to handle guesses and game logic.
* **Functions**: Modularizing the code (`choose_word()`, `display_word()`, `get_valid_guess()`, `play_game()`, `main()`).
* **Sets**: To keep track of unique guessed letters (`set()`).
* **Input/Output**: `input()` for reading guesses, `print()` for console updates.
* **Input Validation**: Ensuring user enters only valid alphabetical characters.

## Project Structure
```text
Hangman_Game/
│
├── hangman.py          # Main Python script containing game logic
├── README.md           # Project documentation
└── requirements.txt    # Project dependencies
```

## How the Game Works
1. The game initializes and randomly selects a word from the predefined list.
2. The user is presented with a series of underscores representing the unknown letters.
3. The user inputs a letter guess.
4. The system validates the input (checking if it's a single alphabetic character and hasn't been guessed before).
5. If the guess is correct, the letter replaces the corresponding underscores in the displayed word.
6. If the guess is incorrect, the number of incorrect guesses increments, and a new part of the hangman is drawn.
7. Steps 3-6 repeat until the word is completely guessed (Win) or 6 incorrect guesses are made (Loss).
8. The final result is displayed, and the user is prompted to play again.

## Installation/Setup Instructions
Since this project uses only Python's standard library, there is no need to install external packages or configure a virtual environment.

1. Ensure you have **Python 3.x** installed on your system. You can check by running `python --version` in your terminal.
2. Clone the repository or download the project files to your local machine.

## How to Run the Program
1. Open your terminal or command prompt.
2. Navigate to the directory containing the project:
   ```bash
   cd path/to/Hangman_Game
   ```
3. Run the Python script:
   ```bash
   python hangman.py
   ```

## Example Output
```text
====================================
          HANGMAN GAME
====================================

       +---+
           |
           |
           |
          ===
    
Word: _ _ _ _ _ _
Incorrect guesses: 0/6
Guessed letters: None

Enter a letter: p

Good job! 'p' is in the word.

       +---+
           |
           |
           |
          ===
    
Word: p _ _ _ _ _
Incorrect guesses: 0/6
Guessed letters: p

Enter a letter:
```

## Future Enhancements
* Read words from an external text file to increase the word pool dynamically.
* Implement a scoring system that carries over across multiple rounds.
* Add difficulty levels (e.g., fewer guesses, longer words).
* Add a graphical user interface (GUI) using Tkinter or Pygame.

## Author
* Developed during the CodeAlpha Internship program.
