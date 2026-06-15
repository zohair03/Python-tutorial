def hello_world():
    print("Hello World")

# hello_world()

def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2

# total = sum(3, 3)
# print(total)


# multi arguments funtions:

def multi_args(*names):
    print(names)
    print(type(names))

multi_args("Zohair", "Ahmed", "Shaikh")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Dave", last="Gray")