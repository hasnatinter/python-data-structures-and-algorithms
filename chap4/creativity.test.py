from creativity import *

# 1- Maximum Element
sampleList1 = [2, 5, 6, 9, 1, 3]
assert maximum_element(sampleList1, 6) == 9

sampleList1 = [2, 5, 6, 9, 1, 10]
assert maximum_element(sampleList1, 6) == 10

sampleList1 = [10, 5, 6, 9, 1, 3]
assert maximum_element(sampleList1, 6) == 10

# 6- Harmonic Number
assert round(harmonic_number(9), 5) == 2.82897
assert round(harmonic_number(0), 5) == 0

# 7- String to Number
assert string_to_integer("13591", 5) == 13591
assert string_to_integer("0", 1) == 0
assert string_to_integer("0000", 4) == 0
assert string_to_integer("0001", 4) == 1
assert string_to_integer("00010", 5) == 10

# 8- Isabel Sum
assert isabel_sum([1, 2, 3, 4], 4) == 10
assert isabel_sum([1, 2, 3, 4, 5, 6, 7, 8], 8) == 36
