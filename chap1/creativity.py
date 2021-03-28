# C-1.13 Write a pseudo-code description of a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order than they were before,
# and compare this method to an equivalent Python function for doing the same thing.
import copy
import timeit
from random import randint


def reverse_list(list_data):
    reverse_data = []
    for i in range(len(list_data), 0, -1):
        reverse_data.append(i)
    return reverse_data


def reverse_half(list_data):
    length = len(list_data)
    i = 0
    while i < length // 2:
        list_data[i], list_data[length - 1 - i] = list_data[length - 1 - i], list_data[i]
        i += 1
    return list_data


# print(reverse_list([1, 2, 3]))
# print(reversed([1, 2, 3]))

data = [2, 3, 5, 7, 8, 4, 3, 6, 7, 4, 5]


# print(timeit.Timer(lambda: reverse_list(data)).timeit())
# print(timeit.Timer(lambda: reverse_half(data)).timeit())
# print(timeit.Timer(lambda: reversed(data)).timeit())


# C-1.14 Write a short Python function that takes a sequence of integer values and determines if there is a distinct
# pair of numbers in the sequence whose product is odd.
def find_distinct_odd_product(list_data):
    odd_list = []
    for i in range(len(list_data)):
        for j in range(len(list_data)):
            if list_data[i] != list_data[j] and (list_data[i] * list_data[j]) % 2 != 0:
                odd_list.append([list_data[i], list_data[j]])
    return odd_list


# print(find_distinct_odd_product([1, 2, 3, 4, 5]))


# C-1.15 Write a Python function that takes a sequence of numbers and determines if all the numbers are
# different from each other (that is, they are distinct).
def determine_distinct(list_data):
    key_list = {}
    for i in range(len(list_data)):
        if list_data[i] in key_list:
            return False
        key_list[list_data[i]] = True
    return True


# print(determine_distinct([1, 2, 3, 4, 5]))
# print(determine_distinct([1, 2, 3, 4, 4]))

# C-1.16 In our implementation of the scale function (page 25), the body of the loop executes the command data[j] =
# factor. We have discussed that numeric types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance). How is it still possible, then,
# that our implementation of scale changes the actual parameter sent by the caller?
def scale(data, factor):
    for j in range(len(data)):
        data[j] += factor
    return data


data = (1, 2, 3, 4, 5,)
# print(data)
# print(scale(data, 2))
# print(data)

# Since list type is mutable, hence its state can change when you send it as parameter,
# its state gets changed in function as well.


# C-1.17
# (Page 52).  Had we implemented the scale function (page 25) as follows,
# does it work properly?
# def scale(data, factor):
#   for val in data:
#       val = factor
#       Explain why or why not.

# No because we are changing the value of loop variable.

# C-1.18
# Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
n = 1
m = 2
my_list = [(k - 1) * (k + 2) + 2 for k in range(0, 10, n)]
my_list2 = [(n * n) + n for n in range(0, 10)]


# print(my_list)
# print(my_list2)


# C-1.19
# Demonstrate how to use Python’s list comprehension syntax to produce the list [ a , b , c , ..., z ],
# but without having to type all 26 such characters literally.
# print([chr(k) for k in range(97, 123)])

# C-1.20 Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly
# reorders the elements so that each possible order occurs with equal probability. The random module includes a more
# basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using
# only the randint function, implement your own version of the shuffle function.
# print(randint(9, 23))


def my_shuffle(data_list):
    done_keys = []
    temp_list = copy.copy(data_list)
    new_key = 0
    for k in range(len(data_list)):
        new_key = randint(0, len(data_list) - 1)
        # done_keys.append(new_key)
        while True:
            if new_key not in done_keys:
                done_keys.append(new_key)
                break
            else:
                new_key = randint(0, len(data_list) - 1)
        temp_list[k] = data_list[new_key]
    return done_keys, temp_list


# print(my_shuffle([1, 2, 3, 4, 5]))

# Write a Python program that repeatedly reads lines from standard input until an EOFError is raised,
# and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D).

def reverse_input():
    run = True
    arr = []
    while True:
        try:
            arr.append(input(""))
        except EOFError as e:
            break
    # print(arr)
    for element in range(len(arr) - 1, -1, -1):
        print(arr[element])


reverse_input()
