x = 2

try:
    # print(x/0)
    if not type(x) is str:
        raise TypeError("this is a type error from if statement")
except NameError:
    print("There is something that is not defined")
except Exception as error:
    print(error)
finally:
    print("I will run with or without error")

# try:
#     print(x/0)
# except:
#     print("an error has ocurr!!!")