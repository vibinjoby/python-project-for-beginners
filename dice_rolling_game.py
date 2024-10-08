"""
Write a program that simulates rolling a pair of dice. Each time the program runs, it
should randomly generate two numbers between 1 and 6 (inclusive), representing
the result of each die. The program should then display the results and ask if the
user would like to roll again.
"""

import random


def _roll_dice(num_of_dice: int, dice_counter: int):
    # Generate a tuple of random integers between 1 and 6
    random_num = tuple(random.randint(1, 6) for _ in range(num_of_dice))

    print("You rolled:", random_num)

    user_input = input("Roll the dice again? (y/n): ")

    if user_input.lower() == "y":
        dice_counter += 1
        _roll_dice(num_of_dice, dice_counter)
    else:
        print(f"You have rolled the dice counter {dice_counter} times")


def _main():
    dice_counter = 1
    num_of_dice = input("How many dice do you want to roll?")
    while not num_of_dice.isdigit():  # Validate input
        print("Please enter a valid number.")
        num_of_dice = input("How many dice do you want to roll? ")
    _roll_dice(int(num_of_dice), dice_counter)


if __name__ == "__main__":
    _main()
