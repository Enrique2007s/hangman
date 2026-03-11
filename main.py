from game import play_game

def main():
    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print("You have 6 incorrect guesses before you lose.")
    print("Good luck!")
    print("--------------------------------")
    play_game()

if __name__ == "__main__":
    main()