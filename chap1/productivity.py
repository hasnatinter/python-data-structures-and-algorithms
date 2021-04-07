# P-1.29 Write a Python program that outputs all possible strings formed by using the characters c , a , t , d , o ,
# and g exactly once
from random import choices, randint


def recursion(sub_data, string):
    if len(sub_data) == 1:
        print(string)
        # print(''.join(list(map(str, string + sub_data))), end=',')
        return
    else:
        for i in range(len(sub_data)):
            new_subdata = [sub_data[x] for x in range(len(sub_data)) if x != i]  # Make a list with everything but
            # your current item
            print(new_subdata)
            recursion(new_subdata, string + [sub_data[i]])


def all_combos(data):
    assert len(data) > 0, 'You have provided an empty string/array'
    recursion(list(data), [])


# print('Approach 1')
# all_combos('catdog')


# P-1.30 Write a Python program that can take a positive integer greater than 2 as input and write out the number of times
# one must repeatedly divide this number by 2 before getting a value less than 2.

def number_of_times_less_than_2(number):
    if number <= 2:
        return 0
    total = 0
    while number > 2:
        total = total + 1
        number = number / 2
    return total


# print(number_of_times_less_than_2(100))

# P-1.31 Write a Python program that can “make change.” Your program should take two numbers as input, one that is a
# monetary amount charged and the other that is a monetary amount given. It should then return the number of each
# kind of bill and coin to give back as change for the difference between the amount given and the amount charged.
# The values assigned to the bills and coins can be based on the monetary system of any current or former government.
# Try to design your program so that it returns as few bills and coins as possible.

def provide_change(amount_charged, amount_given):
    if amount_charged >= amount_given:
        return 0
    currency = [1, 5, 10, 20, 50, 100]
    change = {}
    remaining = amount_given - amount_charged
    while remaining > 0:
        for i in range(len(currency) - 1, -1, -1):
            if remaining >= currency[i]:
                remaining = remaining - currency[i]
                if currency[i] not in change:
                    change[currency[i]] = 0
                print(change)
                change[currency[i]] = change[currency[i]] + 1
                break
    return change


# print(provide_change(136, 200))

# P-1.32 Write a Python program that can simulate a simple calculator, using the console as the exclusive input and
# output device. That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator,
# like + or =, can be done on a separate line. After each such input, you should output to the Python console what
# would be displayed on your calculator.

def calculator():
    operators = ['+', '-', '*', '/']
    continue_calculating = True
    op1 = False
    op2 = False
    operator = False
    print("Start:")
    while continue_calculating:
        input_from_user = input("")
        try:
            float_val = float(input_from_user)
            if not op1:
                op1 = float_val
            else:
                op2 = float_val
                print(calculate(op1, operator, op2))
                op1 = calculate(op1, operator, op2)
                op2 = 0
        except ValueError as e:
            if input_from_user in operators:
                if not op2:
                    total = calculate(op1, operator, op2)
                    if total:
                        print(total)
                operator = input_from_user

            elif input_from_user == "Exit":
                continue_calculating = False
            elif input_from_user == "Reset":
                print("Start:")
                op1 = op2 = operator = False


def calculate(op1, operator, op2):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2


# calculator()

# A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone
# program that will write out the following sentence one hundred times: “I will never spam my friends again.” Your
# program should number each of the sentences and it should make eight different random-looking typos.
def punishment():
    mistake_list = choices(range(100), weights=None, cum_weights=None, k=8)
    punishment_string = "I will never spam my friends again."
    for i in range(100):
        temp_str = list(punishment_string)
        if i in mistake_list:
            random_index_string = randint(1, len(temp_str) - 1)
            temp = temp_str[random_index_string]
            temp_str[random_index_string] = temp_str[random_index_string - 1]
            temp_str[random_index_string - 1] = temp
        print(str(i + 1) + " " + "".join(temp_str))


# punishment()

def birthday_paradox(n):
    total_found = 0
    for i in range(100):
        birthday_list = []
        for k in range(n):
            rand_val = randint(1, 366)
            if rand_val in birthday_list:
                total_found += 1
                break
            else:
                birthday_list.append(rand_val)
    return total_found


print(birthday_paradox(23))
print(birthday_paradox(5))
print(birthday_paradox(20))
print(birthday_paradox(100))

# Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word
# appears in the list. You need not worry about efficiency at this point, however, as this topic is something that
# will be addressed later in this book.


def count_words():
    total_dict = {}
    sentence = input("")
    word = ""
    for i in range(len(sentence)):
        if sentence[i] == " ":
            if word not in total_dict:
                total_dict[word] = 0
            total_dict[word] += 1
            word = ""
        else:
            word += sentence[i]
    return total_dict


print(count_words())

