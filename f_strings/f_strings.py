# import ref string doc: https://www.w3schools.com/python/python_string_formatting.asp


person = "Zohair"
coins = 3

# message = f"{person.upper()} has {2*4} coins left"
# print(message)

num = 10
# print(f"2.25 times {num} is {2.25*num:.2f}")

for x in range(1, 11):
    print(f"{x} is multiple by 2.25 is {x * 2.25:.2f}")


person = "Dave"
coins = 3

#################
# Concatenating strings

print("\n" + person + " has " + str(coins) + " coins left.")

#################
# Previous %s formatting

message = "\n%s has %s coins left." % (person, coins)
print(message)

#################
# Previous string.format() method

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person
)
print(message)

player = {'person': 'Dave', 'coins': 3}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)

##################
# f-Strings! This is the way.

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

message = f"\n{player['person']} has {2 * 5} coins left."
print(message)

##################
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")