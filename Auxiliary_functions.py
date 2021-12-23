# Created by : Orel Rahum
# This file has Auxiliary functions for my project

def input_number(text):
    while True:
        try:
            number = int(input(text))
        except ValueError:
            print("Not an integer! Please enter an integer.\n")
        else:
            break

    return number


def input_number_with_range(text, start, end):
    while True:
        try:
            number = int(input(text))
            assert start <= number <= end
        except ValueError:
            print("Not an integer! Please enter an integer.\n")
        except AssertionError:
            print(f"Please enter an integer between {start} and {end}\n")
        else:
            break

    return number
