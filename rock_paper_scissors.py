from enum import Enum

"""
The game will prompt the player to choose rock, paper, or scissors by typing 'r',
'p', or 's'. The computer will randomly select its choice. The game will then display
both choices using emojis and determine the winner based on the rules.
"""


class Player(Enum):
    PLAYER_1 = 'player 1'
    PLAYER_2 = 'player 2'
    NONE = 'none'


class Choice(Enum):
    ROCK = 'r'
    PAPER = 'p'
    SCISSORS = 's'


def _determine_result(user_choice: Choice, computer_choice: Choice) -> Player:
    if computer_choice == user_choice:
        return Player.NONE
    elif user_choice == Choice.ROCK:
        if computer_choice == Choice.PAPER:
            return Player.PLAYER_2
        elif computer_choice == Choice.SCISSORS:
            return Player.PLAYER_1
    elif user_choice == Choice.PAPER:
        if computer_choice == Choice.ROCK:
            return Player.PLAYER_1
        elif computer_choice == Choice.SCISSORS:
            return Player.PLAYER_2
    elif user_choice == Choice.SCISSORS:
        if computer_choice == Choice.ROCK:
            return Player.PLAYER_2
        elif computer_choice == Choice.PAPER:
            return Player.PLAYER_1


def _prompt_choice(player_number: int) -> Choice:
    """
    Prompts the specified player to input their choice.
    Continues to prompt until a valid input is received.
    """
    while True:
        choice_input = input(
            f"Player {player_number}, choose Rock, Paper, or Scissors (r/p/s): ").lower()
        try:
            choice = Choice(choice_input)
            return choice
        except ValueError:
            print(
                "Invalid input. Please enter 'r' for Rock, 'p' for Paper, or 's' for Scissors.")


def _determine_winner(round_results: dict[str | Player, int]) -> Player:
    """
    Determines the overall winner based on the round results.
    """
    if round_results[Player.PLAYER_1] == round_results[Player.PLAYER_2]:
        return Player.NONE
    elif round_results[Player.PLAYER_1] > round_results[Player.PLAYER_2]:
        return Player.PLAYER_1
    else:
        return Player.PLAYER_2


def _should_game_exit_early(round_results: dict[str | Player, int]):
    """
    Checks if either player has already won two rounds, allowing the game to exit early.
    """
    if round_results[Player.PLAYER_1] == 2 or round_results[Player.PLAYER_2] == 2:
        return True

    return False


def _start_game():
    """
    Starts the Rock, Paper, Scissors game, handling multiple rounds and determining the overall winner.
    """
    round_results = {
        Player.PLAYER_2: 0,
        Player.PLAYER_1: 0,
        Player.NONE: 0
    }

    for i in range(1, 4):
        player_1_choice = _prompt_choice(1)
        player_2_choice = _prompt_choice(2)

        print(f"Player 1 chose {player_1_choice.name}")
        print(f"Player 2 chose {player_2_choice.name}")

        result = _determine_result(player_1_choice, player_2_choice)
        round_results[result] += 1

        print(f"Result of round {i} is {result}")

        if _should_game_exit_early(round_results):
            break

    winner = _determine_winner(round_results)
    print("===========STATS==============")
    print(f"Total player 1 wins: {round_results[Player.PLAYER_1]}")
    print(f"Total player 2 wins: {round_results[Player.PLAYER_2]}")
    print(f"Total tie result is: {round_results[Player.NONE]}")
    print(f"Final Winner: {winner.name}")
    print("==============================")


def _main():
    _start_game()


if __name__ == "__main__":
    _main()
