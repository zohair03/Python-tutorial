import random

tg = ["rock", "scissors", "paper"]
com_tg = tg[random.randint(0,2)]

print("******** Rock Papaer Scissors Game *******\n")
user_tg = input("Enter your thing:")

if user_tg == tg[0] or user_tg == tg[1] or user_tg == tg[2]:
    if user_tg == com_tg:
        print("Tie for " + user_tg + " and " + com_tg)
    elif user_tg == tg[0] and com_tg == tg[2]:
        print("Computer wins!!")
        print("Computer's thing: " + com_tg)
    elif user_tg == tg[1] and com_tg == tg[0]:
        print("Computer wins!!")
        print("Computer's thing: " + com_tg)
    elif user_tg == tg[2] and com_tg == tg[1]:
        print("Computer wins!!")
        print("Computer's thing: " + com_tg)
    # elif user_tg == tg[2] and com_tg == tg[0]:
    #     print("You wins!!")
    #     print("Computer's thing: " + com_tg)
    # elif user_tg == tg[0] and com_tg == tg[1]:
    #     print("You wins!!")
    #     print("Computer's thing: " + com_tg)
    # elif user_tg == tg[1] and com_tg == tg[2]:
    #     print("You wins!!")
    #     print("Computer's thing: " + com_tg)
    else:
        print("🙌 You wins!!")
        print("Computer's thing: " + com_tg)
else:
    print("Please enter valid things like rock, paper & scissors")



