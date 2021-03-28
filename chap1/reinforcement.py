# 1
# Write a short Python function, is_multiple(n, m), that takes two integer values and returns
# True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
from random import choice, randrange


def is_multiple(n, m):
    if n % m == 0:
        return True
    return False


a = is_multiple(20, 3)


# 2
# Write a short Python function, is even(k), that takes an integer value and returns True if k is even,
# and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.
def is_even(k):
    start = 0
    for i in range(1, k + 1, 1):
        if (start == 0):
            start = 1
        else:
            start = 0
    if start == 0:
        return True
    return False


b = is_even(9)


# 3
# Write a short Python function, min_max(data), that takes a sequence of one or more numbers, and returns the smallest
# and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in
# implementing your solution.
def min_max(data):
    smallest = data[0]
    largest = data[1]
    for i in data:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return smallest, largest


c = min_max([2, 3, 4, 1, 6])


# print(c)


# 4 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the
# positive integers smaller than n.
def sum_of_squares(n):
    total = 0
    for i in range(n):
        total = total + (i * i)
    return total


total = sum_of_squares(4)
# print(total)


# 5 Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the
# built-in sum function.
square = sum([k * k for k in range(4)])


# print(square)


# 6 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd
# positive integers smaller than n.
def sum_of_squares_odd(n):
    total = 0
    for i in range(1, n, 2):
        total = total + (i * i)
    return total


# print(sum_of_squares_odd(8))

# 7 Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the
# built-in sum function.
square_odd_comprehension = sum([k * k for k in range(1, 8, 2)])
# print(square_odd_comprehension)


# 8
# Python allows negative integers to be used as indices into a sequence, such as a string.
# If string s has length n, and expression s[k] is used for index −n ≤ k < 0,
# what is the equivalent index j ≥ 0 such that s[j] references the same element?
# ANS : j = n+k (e.g. if hello then index are k = [0, 1, 2, 3, 4] s[-1] = o,
# its positive counterpart is n+k (5 + (-1)) = 4
# str = "hello"
# print(str[5 + (-1)])

# 9
# What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?
# print([i for i in range(50, 90, 10)])

# 10
# What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
# print([k for k in range(8, -10, -2)])

# 11
# Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
# print([2**k for k in range(9)])

# 12 Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence.
# The random module includes a more basic function randrange, with parameterization similar to the built-in range
# function, that return a random choice from the given range. Using only the randrange function, implement your own
# version of the choice function.

def custom_choice(seq):
    random_picker = randrange(0, len(seq))
    return seq[random_picker]


# a = [1, 2, 4, 8, 16, 32, 64, 128, 256]
# print(custom_choice(a))
# print(choice(a))
