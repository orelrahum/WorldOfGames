# Created by : Orel Rahum
import time
from random import randint
from Auxiliary_functions import *
from currency_converter import CurrencyConverter

color_list = {"white": '\033[0m', "red": '\033[31m', "green": '\033[32m', "orange": '\033[33m', "blue": '\033[34m',
              "purple": '\033[35m', "bold": '\033[1m', "end": '\033[0m'}

##################################################################################################

difficulty_list_range = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}


def get_money_interval(random_number):
    return CurrencyConverter().convert(random_number, 'USD', 'ILS')


get_money_interval(5)


def get_guess_from_user(random_number):
    return input_number(f"Please guess how much {random_number}$ in ILS : ")


def play(difficulty):
    print(f"{color_list.get('blue')}{color_list.get('bold')}Welcome to Currency Roulette Game{color_list.get('end')}\n")
    time.sleep(1)
    difficulty_range = difficulty_list_range.get(difficulty)
    print(f"your difficulty_range is {difficulty_range}  ")
    random_number = randint(1, 100)
    get_money_number = get_money_interval(random_number)
    get_guess_from_user_number = get_guess_from_user(random_number)
    time.sleep(1)
    if (get_money_number - difficulty_range) < get_guess_from_user_number < (get_money_number + difficulty_range):
        print(
            f"{color_list.get('green')}{color_list.get('bold')}You Win!!!\n{random_number}$ is {get_money_number} in ILS{color_list.get('end')}")
        return
    print(f"{color_list.get('red')}You Lose :\n{random_number}$ is {get_money_number} in ILS{color_list.get('end')}")
