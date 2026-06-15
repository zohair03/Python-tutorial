# value = 1

# while loops:

# while value <= 10:
#     print(value)
#     value += 1

# while value <= 10:
#     if value == 5:
#         value += 1
#         continue
#     print(value)
#     value += 1

# for loops:

# names = ['zohair', 'ahmed', 'shaikh']

# for name in names:
#     print(name)

# for x in 'zohair':
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(5,101,5):
#     print(x)

for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")