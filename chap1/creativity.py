# C-1.13 Write a pseudo-code description of a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order than they were before,
# and compare this method to an equivalent Python function for doing the same thing.
import copy
import timeit
from math import sqrt
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

# C-1.21
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


# reverse_input()

# C-1.22
# Write a short Python program that takes two arrays a and b of length n storing int values, and returns the dot
# product of a and b. That is, it returns an array c of length n such that c[i] = a[i]·b[i], for i = 0,...,n−1.


def dot_product(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c


# print(dot_product([1, 2, 3, 4, 5], [10, 11, 22, 33, 44, 55]))

# C-1.23
# Give an example of a Python code fragment that attempts to write an element to a list based on an index that may
# be out of bounds. If that index is out of bounds, the program should catch the exception that results,
# and print the following error message: “Don’t try buffer overflow attacks in Python!”


def out_of_bound_array(arr):
    try:
        arr[len(arr) + 1] = 1
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")


# out_of_bound_array([1])

# C-1.24
# Write a short Python function that counts the number of vowels in a given character string.


def count_vowels(my_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0
    for i in range(len(my_str)):
        if str.lower(my_str[i]) in vowels:
            total += 1
    return total


# print(count_vowels('abcdefghiIE'))


# C-1.25

# Write a short Python function that takes a strings, representing a sentence, and returns a copy of the string with
# all punctuation removed. For exam- ple, if given the string "Let s try, Mike.", this function would return "Lets
# try Mike".

def remove_punctuation(my_str):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', ' ']
    new_str = ""
    for i in range(len(my_str)):
        if str.lower(my_str[i]) in chars:
            new_str += my_str[i]
    return new_str


# print(remove_punctuation("Let's try, Mike."))


# C-1.26 Write a short program that takes as input three integers, a, b, and c, from the console and determines if
# they can be used in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”

def arithmetic_formula(a, b, c):
    if a + b == c:
        print("a+b=c")
    if a == (b - c):
        print("a=b-c")
    if (a * b) == c:
        print("a*b=c")


# aVal = int(input("Enter a:"))
# bVal = int(input("Enter b:"))
# cVal = int(input("Enter c:"))
# arithmetic_formula(aVal, bVal, cVal)


# C-1.27 In Section 1.8, we provided three different implementations of a generator that computes factors of a given
# integer. The third of those implementations, from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports factors in increasing order,
# while maintaining its general performance advantages.

def factors_improve(factor_of):
    k = 1
    while k * k < factor_of:
        if factor_of % k == 0:
            yield k
        k = k + 1
    while k > 0:
        if factor_of % k == 0:
            yield factor_of // k
        k = k - 1
    if k * k == factor_of:
        yield k


# for values in factors_improve(81):
#     print(values)


# The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is de- fined as ­ppp p v = v1 +v2 +···+vn. For the
# special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector.
# For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of √42 +
# 32 = √16 + 9 = √25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.

def norm(v, p=False):
    if not p:
        a = v[0] ** 2
        b = v[1] ** 2
        total = sqrt(a + b)
        return total
    else:
        total = 0
        for i in range(len(v)):
            total += v[i] ** p
        for i in range(p - 1):
            total = sqrt(total)
        return total


# print(norm([1, 2, 3, 4], 3))
