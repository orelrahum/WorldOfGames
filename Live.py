# Created by : Orel Rahum
from Auxiliary_functions import *


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG)." \
           "Here you can find many cool games to play."


def load_game():
    print("Please choose a game to play:\n" \
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n" \
          "2. Guess Game - guess a number and see if you chose like the computer\n" \
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    choice = input_number_with_range("Please choose game from 1 to 3:", 1, 3)
    print("")
    difficulty = input_number_with_range("Please choose game difficulty from 1 to 5:",1,5)


load_game()
