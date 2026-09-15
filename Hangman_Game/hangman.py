import random

WORDS = ["python", "internship", "programming", "developer", "software"]

def choose_word():
    """Selects a word randomly from the predefined list."""
    return random.choice(WORDS)

def display_word(word, guessed_letters):
    """Returns the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def get_valid_guess(guessed_letters):
    """Prompts the user for a valid single alphabetical character guess."""
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter only alphabetical characters.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        else:
            return guess

def play_game():
    """Main game logic for a single round of Hangman."""
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("\n====================================")
    print("          HANGMAN GAME")
    print("====================================")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        
        guessed_display = ", ".join(sorted(guessed_letters)) if guessed_letters else "None"
        print(f"Guessed letters: {guessed_display}\n")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word correctly!")
            print(f"The word was: {word}")
            return True

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"\nGood job! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"\nWord: {display_word(word, guessed_letters)}")
                print("Congratulations! You guessed the word correctly!")
                print(f"The word was: {word}")
                return True
        else:
            print(f"\nSorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    print(f"\nWord: {display_word(word, guessed_letters)}")
    print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
    print("\nGame Over! You've reached the maximum number of incorrect guesses.")
    print(f"The correct word was: {word}")
    return False

def main():
    """Main entry point for the program, handles replay logic."""
    while True:
        play_game()
        replay = input("\nWould you like to play another round? (yes/no): ").lower()
        if replay != 'yes' and replay != 'y':
            print("Thank you for playing the Hangman Game! Goodbye.")
            break

if __name__ == "__main__":
    main()
