import argparse
from guess_number import play_guess_number_game
from rps import rps


parser = argparse.ArgumentParser(
    description="This is a Arcade Menu."
)
parser.add_argument(
    "-n", "--name", metavar="name", required=True, help="Enter your name to start the Arcade ex: -n Name"
)
args = parser.parse_args()


def arcade(player_name):
    x = True
    while x:
        print(f"Welcome to Arcade {player_name}. Enter 1, 2 or X to quit\n")
        print("1 for Guess Number\n")
        print("2 for RPS\n")
        player_input = input()

        if player_input == "1" or player_input == "2":
            if player_input == "1":
                play_guess_number_game(player_name)
                continue
            else:
                rps(player_name)
                continue
        elif player_input.lower() == "x":
            x = False
            break
        else:
            print("Plese enter valid number\n")
            continue

arcade(args.name)