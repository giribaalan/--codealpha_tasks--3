import random

def hangman():
    # Predefined list of words
    words = ["PYTHON", "JAVASCRIPT", "COMPUTER", "PROGRAMMING", "DEVELOPER"]
    
    # Randomly select a word
    secret_word = random.choice(words)
    word_length = len(secret_word)
    
    # Game variables
    guessed_word = ["_"] * word_length
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("=" * 50)
    print("🎮 WELCOME TO HANGMAN GAME! 🎮")
    print("=" * 50)
    print(f"\nThe word has {word_length} letters.")
    print("You have 6 incorrect guesses allowed.\n")
    
    # Main game loop
    while incorrect_guesses < max_incorrect and "_" in guessed_word:
        # Display current progress
        print("\n" + "-" * 50)
        print(f"Current word: {' '.join(guessed_word)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print("-" * 50)
        
        # Get player's guess
        guess = input("Guess a letter: ").upper().strip()
        
        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single letter (A-Z).")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue
        
        # Add to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is in the word
        if guess in secret_word:
            print(f"✅ Good guess! '{guess}' is in the word!")
            # Update the guessed word
            for i in range(word_length):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry, '{guess}' is NOT in the word.")
            print(f"💀 Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
    
    # Game over - show result
    print("\n" + "=" * 50)
    if "_" not in guessed_word:
        print(f"🎉 CONGRATULATIONS! YOU WON! 🎉")
        print(f"The word was: {secret_word}")
        print(f"🎯 You guessed it with {incorrect_guesses} mistake(s)!")
    else:
        print(f"💀 GAME OVER! YOU LOST! 💀")
        print(f"The word was: {secret_word}")
        print(f"Better luck next time!")
    print("=" * 50)

# Run the game
if __name__ == "__main__":
    hangman()