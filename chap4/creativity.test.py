from creativity import *

# 9- Max and Min from sequence
s = [1, 5, 9]
assert sequence_max_min(s) == {'min': 1, 'max': 9}
s = [9, 5, 9]
assert sequence_max_min(s) == {'min': 5, 'max': 9}
s = [1, 1, 1, 1]
assert sequence_max_min(s) == {'min': 1, 'max': 1}
s = [9, 3, 7, 4, 1, 0]
assert sequence_max_min(s) == {'min': 0, 'max': 9}

# 10- Base2 of integer
assert base_two(8) == 3
assert base_two(9) == 3
assert base_two(100) == 6
assert base_two(1) == 0

# 11- Element uniques
s = [1, 2, 7, 4, 6, 1]
assert has_unique_elements(s) == False
s = [1, 2, 3, 4, 6, 1]
assert has_unique_elements(s) == False
s = [1, 2, 3, 4, 6, 7]
assert has_unique_elements(s) == True

# 12- Product of two integers
assert product_two_integers(2, 3) == 6
assert product_two_integers(2, 30) == 60
assert product_two_integers(3, 3) == 9
assert product_two_integers(10, 1) == 10

# 14- Tower of Hanoi
s = {'source': [4, 3, 2, 1], 'temp': [], 'destination': []}
tower(4, s, 'source', 'temp', 'destination')
assert s['destination'] == [4, 3, 2, 1]
s = {'source': [3, 2, 1], 'temp': [], 'destination': []}
tower(3, s, 'source', 'temp', 'destination')
assert s['destination'] == [3, 2, 1]
s = {'source': [1], 'temp': [], 'destination': []}
tower(1, s, 'source', 'temp', 'destination')
assert s['destination'] == [1]

# 15- Subsets
res = subsets([1, 2, 3])
assert res == [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
res = subsets([1], [], [], 0)
assert res == [[1], []]
res = subsets([], [], [], 0)
assert res == [[]]

# 16- Reverse string
assert reverse_string('pots&pans') == 'snap&stop'
assert reverse_string('a') == 'a'
assert reverse_string('') == ''
assert reverse_string(' abcd ') == ' dcba '

# 17- Palindrome
assert is_palindrome("racecar") == True
assert is_palindrome("gohangasalamiimalasagnahog") == True
assert is_palindrome("abba") == True
assert is_palindrome("acba") == False
assert is_palindrome("racecat") == False
assert is_palindrome("a") == True


# 18- Vowels
assert has_more_vowels("sabeo") == True
assert has_more_vowels("sabep") == False
assert has_more_vowels("aapp") == False
assert has_more_vowels("a") == True
assert has_more_vowels("p") == False

# 19- Sort even odds
assert sort_even_odds([1, 2, 3, 4, 5]) == [2, 4, 1, 3, 5]
assert sort_even_odds([1, 2, 3, 4, 5, 6]) == [2, 4, 6, 1, 3, 5]
assert sort_even_odds([1, 3, 5]) == [1, 3, 5]
assert sort_even_odds([2, 4, 6]) == [2, 4, 6]
assert sort_even_odds([]) == []
assert sort_even_odds([2]) == [2]
assert sort_even_odds([1]) == [1]
assert sort_even_odds([2, 1]) == [2, 1]

# 20- Sort before k
assert sort_before_k([1, 4, 10, 6, 8, 9, 3], 7) == [1, 4, 6, 3, 8, 9, 10]
assert sort_before_k([1, 3], 2) == [1, 3]
assert sort_before_k([3, 1], 2) == [1, 3]
assert sort_before_k([1, 2], 3) == [1, 2]
assert sort_before_k([3, 2], 1) == [3, 2]
assert sort_before_k([10, 1, 2, 3, 4, 5, 6, 11], 7) == [1, 2, 3, 4, 5, 6, 10, 11]
assert sort_before_k([1, 9, 8, 2], 7) == [1, 2, 8, 9]

# 21- Sum to k
assert (sum_to_k([1, 3, 4, 6, 8, 9, 10], 7)) == [1, 6]
assert (sum_to_k([1, 3, 4, 6, 8, 9, 10], 19)) == [9, 10]
assert (sum_to_k([1, 2, 3], 4)) == [1, 3]
assert (sum_to_k([1, 2, 3], 3)) == [1, 2]
assert (sum_to_k([1, 3, 4], 6)) == []
assert (sum_to_k([1, 3, 4], 5)) == [1, 4]

# 22- Non recursive squares
assert (non_recursive_square(2, 2)) == 4
assert (non_recursive_square(2, 3)) == 8
assert (non_recursive_square(2, 4)) == 16
assert (non_recursive_square(2, 5)) == 32
assert (non_recursive_square(2, 6)) == 64
assert (non_recursive_square(2, 7)) == 128
assert (non_recursive_square(2, 8)) == 256
assert (non_recursive_square(2, 9)) == 512
assert (non_recursive_square(7, 2)) == 49
assert (non_recursive_square(7, 1)) == 7
assert (non_recursive_square(3, 4)) == 81
assert (non_recursive_square(1, 1)) == 1
