#Question 1
my_list = [2, 3, 6]

result = 1

for item in my_list:
    result *= item

print(result)


#Question 2

my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sorted(my_list, key=lambda x: x[-1])

print(sorted_list)

#Question 3

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

result = {}

# Add the values of d1 to the result dictionary
for key, value in d1.items():
    result[key] = value

# Add the values of d2 to the result dictionary, summing the values if the key already exists
for key, value in d2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)

#Question 4


n = int(input("Enter a number: "))

result = {}

for i in range(1, n+1):
    result[i] = i * i
    # Enter a number: 8


print(result)

#Question 5

lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

result = sorted(lst, key=lambda x: float(x[1]), reverse=True)

print(result)

#Question 6

# Creating a set
s = {0, 1, 2, 3, 4}
print(s)
# Output: {0, 1, 2, 3, 4}

# Creating an empty set
s = set()
print(s)
# Output: set()

# Initializing a set with elements
s = set([1, 2, 3, 2, 1])
print(s)
# Output: {1, 2, 3}


# Iterating over a set
s = {0, 1, 2, 3, 4}
for elem in s:
    print(elem)
# Output:
# 0
# 1
# 2
# 3
# 4



# Adding and removing items from a set
s = {1, 2, 3}
s.add(4)
print(s)
# Output: {1, 2, 3, 4}

s.remove(2)
print(s)
# Output: {1, 3, 4}











