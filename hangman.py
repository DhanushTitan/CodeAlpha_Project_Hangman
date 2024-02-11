import random

def choose_word():
    words = ["hangman", "python", "programming", "computer", "challenge", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    MAX_INCORRECT_GUESSES = 6
    incorrect_guesses = 0
    guessed_letters = []
    
    word_to_guess = choose_word()
    word_length = len(word_to_guess)
    
    print("Welcome to Hangman!")
    
    while True:
        print("\nWord: ", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess not in word_to_guess:
                incorrect_guesses += 1
                print("Incorrect guess. Attempts remaining:", MAX_INCORRECT_GUESSES - incorrect_guesses)
                
                if incorrect_guesses == MAX_INCORRECT_GUESSES:
                    print("\nSorry, you've run out of attempts. The word was:", word_to_guess)
                    break
            else:
                print("Good guess!")

            if set(guessed_letters) == set(word_to_guess):
                print("\nCongratulations! You've guessed the word:", word_to_guess)
                break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
