"""
Imports
"""
import random
import time
import gspread
from google.oauth2.service_account import Credentials

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

    def play(self):
        """
        Function which checks correct, incorrect or duplicate guesses.
        Displays state based on wrong guesses and dicrements attempts.
        """
        while True:
            self.display_game_state()
            letter_or_word = input("Enter a letter or the whole word: \n")
            if letter_or_word == self.word:
                self.correct_letters = list(self.word)
                self.display_game_state()
                print("You won in", self.wrong_guesses, "guesses! The word was:", self.word)
                break
            if not letter_or_word.isalpha() or len(letter_or_word) != 1:
                print("Error: Please enter a single letter.")
                continue
            if letter_or_word in self.correct_letters + self.incorrect_letters:
                print("Error: Already guessed letter. Please try different letter.")
                continue
            if letter_or_word in self.word:
                self.correct_letters.append(letter_or_word)
                if all([c in self.correct_letters for c in self.word]):
                    self.display_game_state()
                    print("You won! The random word is:", self.word)
                    break
            else:
                self.incorrect_letters.append(letter_or_word)
                self.wrong_guesses += 1
                if self.wrong_guesses >= self.max_wrong_guesses:
                    self.display_game_state()
                    print("You lost :( The word was:", self.word)
                    break

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


if __name__ == "__main__":
    time.sleep(1)
    print("\nWelcome to Hangman World!")
    print("========================")
    time.sleep(1)
    print('''

          +----+
          |   \|
          Ö    |
         /|\   |
          |    |
         / \   |
             =====\n'''
          )
    time.sleep(1)
    while True:
        player_name = input('Enter your name: \n')
        player_name = player_name.strip()
        if len(player_name) == 0 or player_name.isspace():
            print("This is not a valid name!")
            continue
        else:
            break
    time.sleep(1)
    print('\nHello {}. Wish you the best of luck! \n'.format(player_name))
    time.sleep(1)
    print('HANGED or SAVED? Let\'s test your guessing skills =D \n')
    time.sleep(1)
    PLAY_AGAIN = True
    while PLAY_AGAIN:
        game = Hangman(10)
        game.play()
        restart = input('You want to play again ? Y/N   ((EXIT game press ANY key)) \n >>> ')
        PLAY_AGAIN = restart in ['Yes', 'yes', 'Y', 'y']
    print('Thank you for playing =D \n')
