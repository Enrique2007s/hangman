import random
import requests
"""
Done this way, as APIs are not my strong point,
and I want to make sure the game is functional,
even if the API fails. Also, this part is credited to ChatGPT,
as I had a lot of trouble with the API section using Google Cloud
and it helped me figure out how to handle errors and use a
fallback word list.I also added a timeout to the API request
to prevent the game from staying put if the API is unresponsive.
"""
API_URL = "https://random-word-api.herokuapp.com/word?number=1"

def get_word():
     
    try:
        response = requests.get(API_URL, timeout=5)

        if response.status_code == 200:
            word = response.json()[0]
            return word.lower()

    except requests.RequestException:
            print("Error fetching word from API. Using a fallback word.")
        
    return get_local_word()

def get_local_word():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()

    return random.choice(words)