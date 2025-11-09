max_attempts = 15  # Max number of wrong guesses allowed

print('Welcome to one of the most popular word guessing games-Hangman\'s wand!')
print(f'The rules are simple: The game is played by two. Player 1 types a '
      f'secret word and player 2 has to guess within {max_attempts} attempts.')

secret_word=input('Player 1,enter a word:')
guessed_letters = []  # To store the correct guesses
wrong_guesses =[] # To store wrong guesses

display_word = '_' * len(secret_word)

# Function to update the display word
def update_display_word():
    global display_word
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])

while True:
    print(f"\nWord to guess: {display_word}")
    print(f"Wrong guesses: {', '.join(wrong_guesses)}")
    print(f"Remaining attempts: {max_attempts - len(wrong_guesses)}")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters or guess in wrong_guesses:
        print("You already guessed that letter.")
        continue

    if guess in secret_word:
        guessed_letters.append(guess)
        update_display_word()
        print(f"Good guess! {guess} is in the word.")
    else:
        wrong_guesses.append(guess)
        print(f"Oops! {guess} is not in the word.")

    if '_' not in display_word:
        print(f"\nCongratulations! You've guessed the word: {secret_word}")
        break

    if len(wrong_guesses) >= max_attempts:
        print(f"\nGame over! The word was: {secret_word}")
        break