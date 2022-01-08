# Created by : Orel Rahum
import os
import time

import Games.GuessGame
from Auxiliary_functions import *
from Games.GuessGame import play
from Games.MemoryGame import play
from Games.CurrencyRouletteGame import play


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG)." \
           "Here you can find many cool games to play.\n"


def load_game():
    continue_game = 'Y'
    while continue_game == 'Y' or continue_game == 'y':
        print("Please choose a game to play:")
        time.sleep(1)
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        time.sleep(1)
        print("2. Guess Game - guess a number and see if you chose like the computer")
        time.sleep(1)
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
        time.sleep(1)
        choice = input_number_with_range("Please choose game from 1 to 3: ", 1, 3)
        print("")

        difficulty = input_number_with_range("Please choose game difficulty from 1 to 5: ", 1, 5)

        games_list = {1: f'Games.MemoryGame.play({difficulty})', 2: f'Games.GuessGame.play({difficulty})',
                      3: f'Games.CurrencyRouletteGame.play({difficulty})'}
        os.system('cls' if os.name == 'nt' else 'clear')
        exec(games_list.get(choice))
        time.sleep(0.5)
        continue_game = input("\nDo You Want to play again (Y/n) ")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
