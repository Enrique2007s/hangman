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