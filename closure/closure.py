def arcade(player, coins):
    def game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print(player + " has " + str(coins) + " coins left")
        elif coins == 1:
            print(player + " has " + str(coins) + " coin left")
        else:
            print(player + " is out of coins")
    return game

zohair = arcade("zohair", 3)
john = arcade("john", 3)

zohair()
zohair()
zohair()
zohair()

john()
john()