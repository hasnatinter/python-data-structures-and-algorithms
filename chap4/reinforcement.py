#  ---- Question: 1 ----
# Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements.
# What is your running time and space usage?
def maximum_element(s: list, n: int) -> int:
    if n == 0:
        return s[n]
    return max(s[n - 1], maximum_element(s, n - 1))

# Both running time and space usage are O(n)

#  ---- Question: 2 ----
# Draw the recursion trace for the computation of power(2,5),
# using the traditional function implemented in Code Fragment 4.11.

# The function is
def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    return x * power(x, n - 1)


# the recursion trace for power(2,5)
# -- 2*16 = 32 -- > power(2,5) -- 2*8 = 16 -- > power(2,4) -- 2*4 = 8 -- >
# power(2,3) -- 2*2 = 4 -- > power(2,2) -- 2*1 = 2 -- > power(2,1) -- 1 -- > power(2,0)

#  ---- Question: 3 ----
# Draw the recursion trace for the computation of power(2,18),
# using the repeated squaring algorithm, as implemented in Code Fragment 4.12.

# The function is
def improved_power(x: int, n: int) -> int:
    if n == 0:
        return 1
    half = n // 2
    p = improved_power(x, half) * improved_power(x, half)
    if n % 2 != 0:
        p = p * 2
    return p

# the recursion trace for improved_power(2,18) -- 512 * 512 = 262144 -- > improved_power(2,18) -- 16*16 *2 = 512 -- >
# improved_power(2,9) -- 4*4 = 16 -- > improved_power(2,4) -- 2*2 = 4 -- > improved_power(2,2) -- 1*1 * 2 = 2 -- >
# improved_power(2,1) -- 1 -- > improved_power(2,0)


#  ---- Question: 4 ----
# Draw the recursion trace for the execution of function reverse(S, 0, 5)
# (Code Fragment 4.10) on S = [4, 3, 6, 2, 6].

# The function is
def reverse(s: list, start: int, stop: int) -> None:
    if start < stop - 1:
        s[start], s[stop - 1] = s[stop - 1], s[start]
        reverse(s, start + 1, stop - 1)

# the recursion trace for reverse([4, 3, 6, 2, 6])
# -- [6, 2, 6, 3, 4] -- > reverse (s, 0, 5) -- [4, 2, 6, 3, 6] -- > reverse (s, 1, 4)
# -- [4, 3, 6, 2, 6] -- > reverse (s, 2, 3)

#  ---- Question: 5 ----
# Draw the recursion tract for function PuzzleSolve(3,S,U) (Code Fragment 4.14), where S is empty and U = {a, b, c, d}.

# The function is, note I have added an extra parameter pattern to match for testing
def puzzle_solve(n: int, s: list, u: list, pattern: str) -> None or bool:
    a = 0
    for e in u:
        s.append(e)
        u.remove(e)
        if n == 1:
            pattern_to_match = "".join(s)
            if pattern == pattern_to_match:
                print("Solution found " + pattern_to_match)
                return "Solution found " + pattern_to_match
        else:
            puzzle_solve(n - 1, s, u, pattern)
        s.pop()
        u.insert(a, e)
        a = a + 1

# The recursion trace for puzzle_solve(3, [], ["a", "b", "c", "d"]), (without extra parameter pattern)
# -- puzzle_solve(3, [], ["a", "b", "c", "d"]) --> puzzle_solve(2, ["a"], ["b", "c", "d"])
#   -- Check for abc --> puzzle_solve(1, ["a", "b"], ["c", "d"]) -- Check for abd --> puzzle_solve(1, ["a", "b"], ["d", "c"])
#   -- Check for acb --> puzzle_solve(1, ["a", "c"], ["b", "d"]) -- Check for acd --> puzzle_solve(1, ["a", "c"], ["d", "b"])
#   -- Check for adb --> puzzle_solve(1, ["a", "d"], ["b", "c"]) -- Check for adc --> puzzle_solve(1, ["a", "d"], ["c", "b"])
# -- puzzle_solve(2, ["b"], ["a", "c", "d"])
#   -- Check for bac --> puzzle_solve(1, ["b", "a"], ["c", "d"]) -- Check for bad --> puzzle_solve(1, ["b", "a"], ["d", "c"])
#   -- Check for bca --> puzzle_solve(1, ["b", "c"], ["a", "d"]) -- Check for bcd --> puzzle_solve(1, ["b", "c"], ["d", "a"])
#   -- Check for bda --> puzzle_solve(1, ["b", "d"], ["a", "c"]) -- Check for bdc --> puzzle_solve(1, ["b", "d"], ["c", "a"])
# -- puzzle_solve(2, ["c"], ["a", "b", "d"])
#   -- Check for cab --> puzzle_solve(1, ["c", "a"], ["b", "d"]) -- Check for cad --> puzzle_solve(1, ["c", "a"], ["d", "b"])
#   -- Check for cba --> puzzle_solve(1, ["c", "b"], ["a", "d"]) -- Check for cbd --> puzzle_solve(1, ["c", "b"], ["d", "a"])
#   -- Check for cda --> puzzle_solve(1, ["c", "d"], ["a", "b"]) -- Check for cdb --> puzzle_solve(1, ["c", "d"], ["b", "a"])
# -- puzzle_solve(2, ["d"], ["a", "b", "c"])
#   -- Check for dab --> puzzle_solve(1, ["d", "a"], ["b", "c"]) -- Check for dac --> puzzle_solve(1, ["d", "a"], ["c", "b"])
#   -- Check for dba --> puzzle_solve(1, ["d", "b"], ["a", "c"]) -- Check for dbc --> puzzle_solve(1, ["d", "b"], ["c", "a"])
#   -- Check for dca --> puzzle_solve(1, ["d", "c"], ["a", "b"]) -- Check for dcb --> puzzle_solve(1, ["d", "c"], ["b", "a"])

#  ---- Question: 6 ----
# Describe a recursive function for computing the nth Harmonic number, Hn = ∑n 1/i.
def harmonic_number(n: int) -> float:
    if n == 0:
        return 0
    return 1 / n + harmonic_number(n - 1)


#  ---- Question: 7 ----
# Describe a recursive function for converting a string of digits into the
# integer it represents. For example, "13531" represents the integer 13,531.
def string_to_integer(s: str, n: int) -> int:
    int_to_str_mapping = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
    if s[-n] not in int_to_str_mapping:
        raise ValueError(s[-n] + " is not valid")
    if n == 1:
        return int_to_str_mapping[s[-n]]

    # Here we will get the number to plus by using power, so e.g. we want "561" and current we have 61
    # to add another 500, first get pow(10, 2) = 100, then multiply that 5, (5*100) + 61 = 561

    # Also we use s[-n], so we get the nth number of str, e.g. s[-5] = "1"
    multiple = int_to_str_mapping[s[-n]] * pow(10, n - 1)
    return multiple + string_to_integer(s, n - 1)


#  ---- Question: 8 ----
# Isabel has an interesting way of summing up the values in a sequence A of n integers,
# where n is a power of two.
# She creates a new sequence B of half the size of A and sets B[i] = A[2i]+A[2i+1], for i = 0,1,...,
# (n/2)−1. If B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and repeats the process.
# What is the running time of her algorithm?
def isabel_sum(s: list, n: int) -> list:
    if len(s) == 1:
        return s[0]
    temp_list = [i for i in range(n // 2)]
    for i in range(0, (n // 2)):
        temp_list[i] = s[(2 * i)] + s[(2 * i) + 1]
    s = temp_list
    return isabel_sum(s, n // 2)
