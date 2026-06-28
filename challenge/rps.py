import random

def rps(player_name):
    tg = ["rock", "scissors", "paper"]

    play_again = True

    print("******** Rock Papaer Scissors Game *******\n")

    while play_again:

        com_tg = tg[random.randint(0,2)]

        user_tg = input("Enter your thing or x to quit: ")

        if user_tg == tg[0] or user_tg == tg[1] or user_tg == tg[2]:
            if user_tg == com_tg:
                print("\n 🎀 Tie for " + user_tg + " and " + com_tg)
            elif user_tg == tg[0] and com_tg == tg[2]:
                print("\n 🤖 Computer wins!!")
                print("\n Computer's thing: " + com_tg)
            elif user_tg == tg[1] and com_tg == tg[0]:
                print("\n 🤖 Computer wins!!")
                print("\n Computer's thing: " + com_tg)
            elif user_tg == tg[2] and com_tg == tg[1]:
                print("\n 🤖 Computer wins!!")
                print("\n Computer's thing: " + com_tg)
            else:
                print(f"\n 🙌 {player_name} wins!!")
                print("\n Computer's thing: " + com_tg)
        elif user_tg.lower() == "x":
            play_again = False
            print("\nThanks for playing 🥰")
        else:
            print("Please enter valid things like rock, paper & scissors")
