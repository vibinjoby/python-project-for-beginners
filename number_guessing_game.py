import random
from typing import Optional

"""
Write a program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number. The program should give
hints if the guess is too high or too low.

Allow the user to specify the minimum and maximum values for the number
range before the game starts. This gives the player more control over the
difficulty level.
• Implement a feature that limits the number of guesses a player can make. If
the player runs out of attempts, the game should end, and the correct number
should be revealed.
• Add a feature that keeps track of the fewest attempts it took to guess the
number correctly. The program should display this "best score" at the end of
each game.
"""

def _number_guess(best_score: Optional[int]) -> Optional[int]:
    attempts = 1
    max_attempts = 5
    min_number = int(input("Min number: "))
    max_number = int(input("Max number: "))
    
    random_number = random.randint(min_number, max_number)
    
    while attempts <= max_attempts:
        input_number = int(input(f"Guess the number (between {min_number} and {max_number}): "))

        if input_number == random_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts")
            if best_score is None or attempts < best_score:
                best_score = attempts
                print(f"New best score: {best_score}")
            else:
                print(f"Best score remains: {best_score}")
            break
        elif input_number < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        attempts += 1
    
    if attempts > max_attempts:
        print(f"You've run out of attempts... The correct number was {random_number}")
    
    return best_score

def _main():
    best_score: Optional[int] = None
    while True:
        best_score = _number_guess(best_score)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    _main()
