users = ['zohair', 'ahmed', 'sheikh']

data = ['zohair', 22, True]

print('ahmed' in data)
print(users[2])
print(users.index('sheikh'))
print(users[0:2])
print(users[0:])
print(users[0:1])

print(len(data))

data.append('developer')
print(data)

data += ['AI/ML Engineer']
print(data)

data.extend(["python", "Mern stack"])
print(data)

data.insert(0,"Male")
print(data)

data[2:2] = ["Ahmed"]
print(data)

data.remove('Ahmed')
print(data)

# del data[3]
# print(data)

# del data - this deletes data list fully

# data.clear() - this emptys the list


# How to Sort the list in python

users.sort() # - sorts alfabeticaly # - not supported between instances of 'int' and 'str'
print(users) 

nums = [1, 2, 3, 4, 5, 75]
nums.reverse() # - this reverse the list [75, 5, 4, 3, 2, 1]
print(nums)

nums.sort(reverse=True) # - this makes the list desend order
print(nums)

print(sorted(nums, reverse=True)) # - this sorted funtion sorts the list without changing the orignal list. the orignal list nums stays the same.
print(nums)


# How to copy any list
mycopy = nums.copy()
numscopy = list(nums)
mynums = nums[:]


# Tuples - immutables

newtuple = (1, 2, 3, 4)
anothertuple = tuple((32, 46, 12, 89))

print(newtuple)
print(anothertuple)