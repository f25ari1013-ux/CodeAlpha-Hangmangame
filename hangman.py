import random

def hangman():
    print("🎮 Welcome to Hangman Game!")
    print("You have 6 incorrect guesses allowed.\n")

    # Predefined word list
    words = ["apple", "mango", "grape", "peach", "lemon"]
    
    # Random word selection
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    while wrong_guesses < max_wrong:
        display_word = ""

        # Display guessed letters
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)

        # Win condition
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word:", word)
            return

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct guess! ✅\n")
        else:
            guessed_letters.append(guess)
            wrong_guesses += 1
            print("Wrong guess! ❌ Attempts left:", max_wrong - wrong_guesses, "\n")

    print("😢 Game Over! The word was:", word)


# Run the game
hangman()