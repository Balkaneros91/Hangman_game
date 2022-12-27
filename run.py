import gspread
from google.oauth2.service_account import Credentials
import random
import time

words = ['mouse', 'house', 'love', 'mississippi', 'europe', 'asia', 'hangman', 'game', 'animal', 'flower', 'river', 'yoghurt', 'seed', 'random', 'lipstick', 'surname', 'playground', 'python', 'software', 'object', 'programming', 'seaside', 'city', 'continent', 'life', 'positive', 'school', 'return', 'spanish', 'loyal', 'rude', 'mother', 'siblings', 'ocean', 'atlantis', 'americano', 'aircraft', 'holidays', 'vacation', 'institute', 'care', 'health', 'human', 'booking']

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_game')

result = SHEET.worksheet('result')
data = result.get_all_values()
# print(data)

class Hangman:
    """
    Hangman class
    """
    def __init__(self, max_wrong_guesses):
        """
        Method initializing Hangman object with attr and sets more attr's
        Set random word for game.
        """
        self.max_wrong_guesses = max_wrong_guesses

        self.word = random.choice(words)

        self.correct_letters = []
        self.incorrect_letters = []
        self.wrong_guesses = 0

# game = Hangman(6)
# print(game.word)

    def display_game_state(self):
        """
        Game's visually displayed stages.
        """
        hangman_stages = [

            """
            +-------
            |/    
            |
            |
            |
            |
          =====
            """,
            """
            +-------+
            |/      
            |
            |
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |
            |
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |       I
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I\\
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I\\
            |       o
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I\\
            |       o
            |      / 
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I\\
            |       o
            |      / \\
          =====
            """,
            """
            +-------+
            |/      |
            |       X
            |      /I\\
            |       o
            |      / \\
          =====
            """            
        ]

        print(hangman_stages[self.wrong_guesses])
        print("Word: " + " ".join([c if c in self.correct_letters else "_" for c in self.word]))
        print("Incorrectly guessed words:\n", self.incorrect_letters)
        print("Wrong guesses:", self.wrong_guesses, "/10")
