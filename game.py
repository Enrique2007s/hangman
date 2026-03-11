from word_service import get_random_word

MAX_ATTEMPTS = 6

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print("\n", display)

def play_game():
    """
    This function contains the main game loop for Hangman.
    It initializes the game state, handles user input,
    and updates the game state based on the user's guesses.
    """
    word = get_word()
    guessed_letters = []

    attempts_left = MAX_ATTEMPTS

    while attempts_left > 0:
        display_word(word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()

        #input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        else:
            print("Good guess!")