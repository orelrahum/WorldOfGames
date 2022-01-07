# Created by : Orel Rahum
import os
import time
from random import randint
from Auxiliary_functions import *

color_list = {"white": '\033[0m', "red": '\033[31m', "green": '\033[32m', "orange": '\033[33m', "blue": '\033[34m',
              "purple": '\033[35m', "bold": '\033[1m', "end": '\033[0m'}

##################################################################################################

difficulty_list_number = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
difficulty_list_guess = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}


def generate_number(difficulty_number):
    return randint(1, difficulty_number)


def get_guess_from_user(difficulty_number):
    return input_number_with_range(f"Please guess a Number between 1 to {difficulty_number} : ", 1, difficulty_number)


def compare_results(secret_number, guess_from_user):
    if secret_number == guess_from_user:
        return True
    elif secret_number < guess_from_user:
        print(
            f"The secret number is {color_list.get('orange')}{color_list.get('bold')}smaller{color_list.get('end')} from {guess_from_user} \n")
        return False
    elif secret_number > guess_from_user:
        print(
            f"The secret number is {color_list.get('purple')}{color_list.get('bold')} bigger{color_list.get('end')} from {guess_from_user} \n")
        return False


def play(difficulty):
    print(f"{color_list.get('blue')}{color_list.get('bold')}Welcome to Guess Game{color_list.get('end')}")
    time.sleep(1)
    difficulty_number = difficulty_list_number.get(difficulty)
    difficulty_guess_times = difficulty_list_guess.get(difficulty)
    secret_number = generate_number(difficulty_number)
    print(f"\nYou have {difficulty_guess_times} to try guess  \n")
    time.sleep(1)
    for index in range(1, difficulty_guess_times + 1):
        time.sleep(0.5)
        print(f"{index}/{difficulty_guess_times} tries")
        guess_from_user = get_guess_from_user(difficulty_number)
        time.sleep(0.5)
        game_status = compare_results(secret_number, guess_from_user)
        if game_status:
            print(f"{color_list.get('green')}{color_list.get('bold')}You Win!!!{color_list.get('end')}")
            return
    print(f"{color_list.get('red')}You Lose :\nthe secret number is {secret_number}{color_list.get('end')}")
