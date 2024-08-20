import string


# ---- Question: 9 ----
# Write a short recursive Python function that finds the minimum and maximum values in a
# sequence without using any loops.
def sequence_max_min(s: list, i: int = 0) -> dict[str, int]:
    if i == len(s) - 2:
        mn = min(s[i], s[i + 1])
        mx = max(s[i], s[i + 1])
        return {'min': mn, 'max': mx}
    result = sequence_max_min(s, i + 1)
    mn = min(s[i], result['min'])
    mx = max(s[i], result['max'])
    return {'min': mn, 'max': mx}


# ---- Question: 10 ----
# Describe a recursive algorithm to compute the integer part of the base-two
# logarithm of n using only addition and integer division.
def base_two(n: int, t: int = 0) -> int:
    if n < 2:
        return 0
    return 1 + base_two(n // 2, t + 1)


# --- Question: 11 ----
# Describe an efficient recursive function for solving the element uniqueness problem,
# which runs in time that is at most O(n2) in the worst case without using sorting.
def has_unique_elements(s: list, n: int = 0) -> bool:
    if n == len(s):
        return True
    for i in range(n + 1, len(s)):
        if s[n] == s[i]:
            return False
    return has_unique_elements(s, n + 1)


# ---- Question: 12 ----
# Give a recursive algorithm to compute the product of two positive integers, m and n,
# using only addition and subtraction
def product_two_integers(m: int, n: int, t: int = 1) -> int:
    if n == t:
        return m
    return m + product_two_integers(m, n, t + 1)


# ---- Question: 14 ----
# In the Towers of Hanoi puzzle, we are given a platform with three pegs,a, b, and c,
# sticking out of it. On peg a is a stack of n disks, each larger than the next, so that the smallest is on the top
# and the largest is on the bottom. The puzzle is to move all the disks from peg a to peg c, moving one disk at a
# time, so that we never place a larger disk on top of 'a' smaller one. See Figure 4.15 for an example of the case n =
# 4. Describe a recursive algorithm for solving the Towers of Hanoi puzzle for arbitrary n. (Hint: Consider first the
# sub-problem of moving all but the nth disk from peg 'a' to another peg using the third as “temporary storage.”)

def tower(n: int, s: dict, source: str, temp: str, destination) -> None:
    if n == 1:
        upper_disk = s[source].pop()
        s[destination].append(upper_disk)
        return
    tower(n - 1, s, source, destination, temp)
    upper_disk = s[source].pop()
    s[destination].append(upper_disk)
    tower(n - 1, s, temp, source, destination)


# ---- Question 15 ----
# Write a recursive function that will output all the subsets of a set of n
# elements (without repeating any subsets).
def subsets2(s: list, res: list, subset: list, index: int) -> list:
    if index == len(s):
        res.append(list(subset))
        return res

    subset.append(s[index])
    subsets(s, res, subset, index + 1)
    subset.pop()
    subsets(s, res, subset, index + 1)
    return res


def subsets(s: list, sub = [], l = [], i = 0) -> list:
    if i == len(s):
        sub.append(l)
        return sub
    temp_list = list(l)
    temp_list.append(s[i])
    subsets(s, sub, temp_list, i + 1)
    subsets(s, sub, l, i + 1)
    return sub


# ---- Question 16 ----
# Write a short recursive Python function that takes a character string s and outputs its reverse.
# For example, the reverse of "pots&pans" would be "snap&stop".
def reverse_string(s: string, index: int = 0) -> string:
    if s == "":
        return ""
    if index >= len(s) - 1:
        return s[index]
    return reverse_string(s, index + 1) + s[index]


# ---- Question 17 ----
# Write a short recursive Python function that determines if a string s is a palindrome,
# that is, it is equal to its reverse. For example, racecar and
# gohangasalamiimalasagnahog are palindromes.
def is_palindrome(s: string, index: int = 0) -> bool:
    if index == len(s) // 2:
        return True
    if s[index] != s[-index - 1]:
        return False
    if not is_palindrome(s, index + 1):
        return False
    return True


# ---- Question 18 ----
# Use recursion to write a Python function for determining if a string s has more vowels than consonants.
def has_more_vowels(s: string, index: int = 0) -> int or bool:
    vowels = "aeiou"
    if index == len(s) - 1:
        if index == 0:
            return s[index] in vowels
        return 1 if s[index] in vowels else -1
    total = 1 if s[index] in vowels else -1
    total = total + has_more_vowels(s, index + 1)
    if index == 0:
        return total > 0
    return total


# ---- Question 19 ----
# Write a short recursive Python function that rearranges a sequence of integer values
# so that all the even values appear before all the odd values.
def sort_even_odds(s: list, index: int = 0, even_count: int = 0, sorted_list: list = []) -> list:
    if index == 0:
        sorted_list = []
    if index >= len(s):
        return []
    if s[index] % 2 == 0:
        sorted_list.append(0)
        for i in range(len(sorted_list) - 1, even_count, - 1):
            sorted_list[i] = sorted_list[i - 1]
        sorted_list[even_count] = s[index]
        even_count = even_count + 1
    else:
        sorted_list.append(s[index])
    sort_even_odds(s, index + 1, even_count, sorted_list)
    return sorted_list


# ---- Question 20 ----
# Given an unsorted sequence, S, of integers and an integer k,
# describe a recursive algorithm for rearranging the elements in S
# so that all elements less than or equal to k come before any elements larger than k.
# What is the running time of your algorithm on a sequence of n values?


# The running time of algorithm is O(n)
def sort_before_k(s: list, k: int, index: int = 0, last_index: int = 0) -> list:
    if s[index] <= k:
        temp = s[last_index]
        s[last_index] = s[index]
        s[index] = temp
        last_index += 1
    if index < len(s) - 1:
        sort_before_k(s, k, index + 1, last_index)
    return s


# ---- Question 21 ----
# Suppose you are given an n-element sequence, S, containing distinct integers
# that are listed in increasing order. Given a number k,
# describe a recursive algorithm to find two integers in S that sum to k, if such a pair exists.
# What is the running time of your algorithm?

# The running time of algorithm is O(n)
def sum_to_k(s: list, k: int, start_index: int = 0, end_index: int = -1) -> list:
    # Base case
    if end_index == -1:
        end_index = len(s) - 1
    # End base case

    result = []
    if start_index == end_index:
        return []
    if s[start_index] + s[end_index] == k:
        result = [s[start_index], s[end_index]]
        return result
    if s[start_index] + s[end_index] < k:
        result = sum_to_k(s, k, start_index + 1, end_index)
    if s[start_index] + s[end_index] > k:
        result = sum_to_k(s, k, start_index, end_index - 1)
    return result


# ---- Question 22 ----
# Develop a non-recursive implementation of the version of power from Code Fragment 4.12 that uses repeated squaring.
def non_recursive_square(x: int, n: int) -> int:
    total = 1
    while n > 0:
        if n % 2 == 0:
            x = x * x
            n = n // 2
        else:
            total = total * x
            n = n - 1
    return total
