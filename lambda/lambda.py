sqr = lambda num: num * num
# print(sqr(12))

sum = lambda a, b: a + b
# print(sum(5,2))

def funcbuilder(x):
    return lambda num: num + x

add_ten = funcbuilder(10)
add_twenty = funcbuilder(20)

# print(add_ten(5))
# print(add_twenty(5))

######################################
# Higher order function

# Convert this string list into int nums list
nums = ["1","2","3"]
intNums = map(int, nums)
# print(nums)
# print(list(intNums))

# Square of each number
nums = [1,2,4,3,5,6]
spr = list(map(lambda x: x * x, nums))
# print(spr)


# filter functions
# filter even numbers
oddnums = list(filter(lambda n: n % 2 != 0, nums))
# print(oddnums)

# clacualate the chars in list function

names = ['zohair', 'ahmed', 'sheikh', 'de']

def char_counts(l):
    list_lenth = len(l)
    i = 0
    c = 0
    while i < list_lenth:
        c = c + len(l[i])
        i = i + 1
    print(c)

# char_counts(names)

# clacualate the chars in list using reduce
from functools import reduce

char_in_names = reduce(lambda a,b: a + len(b),names,0)
print(char_in_names)