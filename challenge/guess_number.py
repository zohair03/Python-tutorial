from random import choice

x = True
game_count = 0
win_count = 0

def win_percent(total_game, win_game):
    return (win_game/total_game)*100


def guess_number_logic(num1, num2, name):
    global game_count
    global win_count
    game_count += 1

    if num1 == num2:
        win_count += 1
        print(f"\n{name} wins!! 🙌 Pyton choose {num1}")
        print(f"\nWin percent: {win_percent(game_count,win_count):.2f} | Won Game: {win_count} | Total Game: {game_count}\n")
    else:
        print(f"\nPyton wins!! 🐍 Pyton choose {num1}")
        print(f"\nWin percent: {win_percent(game_count,win_count):.2f} | Won Game: {win_count} | Total Game: {game_count}\n")


def play_guess_number_game(player_name):
    global x

    while x:
        print("-------------------------------------------")
        print("Choose number from 1,2 and 3 👇\n")

        python_num = choice("123")
        player_num = input(f"Choose your number: ")

        if str(player_num) == "1" or str(player_num) == "2" or str(player_num) == "3":
            guess_number_logic(python_num, player_num, player_name)
        else:
            print("\nPlease enter 1,2 or 3 🙄\n")
            continue

        quit = input("Y to playagain \nX to Quit\n")
        if quit.lower() == "x":
            x = False
            print(f"Thanks for Playing {player_name}🙏")
        else:
            continue

if __name__ == "__main__":
    play_guess_number_game()