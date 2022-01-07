# Created by : Orel Rahum
import time
from random import randint
from Auxiliary_functions import *

color_list = {"white": '\033[0m', "red": '\033[31m', "green": '\033[32m', "orange": '\033[33m', "blue": '\033[34m',
              "purple": '\033[35m', "bold": '\033[1m', "end": '\033[0m'}

##################################################################################################
# converter difficulty levels
difficulty_list_amount = {1: 3, 2: 4, 3: 5, 4: 6, 5: 7}
difficulty_list_time = {1: 0.7, 2: 1, 3: 1.2, 4: 1.5, 5: 2}


# this function generate sequence Depending on the level

def generate_sequence(difficulty):
    generate_sequence_list = list(range(difficulty))
    for index in range(0, difficulty):
        generate_sequence_list[index] = randint(1, 101)
    return generate_sequence_list


# this function get list from user
def get_list_from_user(difficulty):
    user_sequence_list = list(range(difficulty))
    print(f"Need to memory {difficulty} numbers :")
    time.sleep(1)
    for index in range(0, difficulty):
        user_sequence_list[index] = input_number_with_range(
            f"{index + 1}/{difficulty} index. Please Enter number between 1 to 101 : ", 1, 101)
    return user_sequence_list


# this function compare between user list to generate list
def is_list_equal(generate_sequence_list, user_sequence_list):
    for index in generate_sequence_list:
        if generate_sequence_list != user_sequence_list:
            return False
    return True


# this function is to run MemoryGame
def play(difficulty):
    # Print Title
    time.sleep(1)
    print(f"{color_list.get('blue')}{color_list.get('bold')}Welcome to Memory Game{color_list.get('end')}\n")
    # Get difficulty by converter difficulty
    difficulty_number = difficulty_list_amount.get(difficulty)
    difficulty_time = difficulty_list_time.get(difficulty)
    generate_sequence_list = generate_sequence(difficulty_number)

    # Print generate sequence list for X time (depend on difficulty)
    print(generate_sequence_list, end="")
    time.sleep(difficulty_time)
    print('\r', end='')
    print("", end='')
    time.sleep(1)
    # Got from user sequence list
    user_sequence_list = get_list_from_user(difficulty_number)

    # compare between user_list to generate_list
    game_status = is_list_equal(generate_sequence_list, user_sequence_list)
    if game_status:
        print(f"{color_list.get('green')}You Wine :\nthe list was {generate_sequence_list}{color_list.get('end')}")
    else:
        print(f"{color_list.get('red')}You Lose :\nthe list was {generate_sequence_list}{color_list.get('end')}")
