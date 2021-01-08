# the known operators to the calculator

operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '~': 6, '%': 4, '!': 6, '@': 5, '$': 5, '&': 5}

# --------------------------------------------------------- recognizers ----------
# because in order to find stuff you need to recognize stuff :)

"""    numbers    """


# is a char a digit
def is_digit(c):
    return '0' <= c <= '9'


# is char a dot
def is_dot(c):
    return c == '.'


# is a char minus
def is_minus(c):
    return c == '-'


#gets a char and returns True if the char is part of a streak with itself
def is_part_of_streak(eq, i):
    if len(eq) == 1:
        return False
    if i == 0:
        return eq[i + 1] == eq[i]
    if i == len(eq) - 1:
        return eq[i - 1] == eq[i]
    return eq[i] == eq[i - 1] or eq[i] == eq[i + 1]


# a number that is not in the form of "e+" example: 5e+7 which is converted to 50000000
def is_part_of_simple_number(c):
    # easy , if it's a digit or a dot
    if is_digit(c):
        return True
    if is_dot(c):
        return True


# gets a string and index and return is it a part of a number
# if this string encounters a minus-
# it assumes that all the duplicated minuses has been cut to one minus by another function
def is_part_of_number(eq, i):
    # if char a digit than it must be part of a number
    # if char is a dot then it must a part of a number
    # if the combination "{number}e+{number}" accrues
    if is_part_of_simple_number(eq[i]):
        return True

    #if the number is big enough and a float python will represent it in the format of {number1}e+{number2}
    # which means {number1} * 10^{number2}
    if eq[i] == 'e':
        # 'e' case -> if it's at the edge of the string that's a problem of course "{number1}e+{number2}"
        # i of 'e' is greater then 0 and less then len(eq) - 2 is good
        if i == 0 or i >= len(eq) - 2:
            return False
        if eq[i + 1] != '+':
            return False
        if not is_part_of_simple_number(eq[i + 2]):
            return False
        if not is_part_of_simple_number(eq[i - 1]):
            return False
        return True

    if eq[i] == '+':
        if i <= 1 or i == len(eq) - 1:
            return False
        if eq[i - 1] != 'e':
            return False
        if not is_part_of_simple_number(eq[i - 2]):
            return False
        if not is_part_of_simple_number(eq[i + 1]):
            return False
        return True
    return False


"""operators"""


#
def strength_of_operator(c):
    if not is_known_operator(c):
        raise Exception("char is not a known operator")
    return operators[c]


# if it's in the dictionary of operators it is known
def is_known_operator(c):
    return c in operators


#
#
def kind_of_operator(c):
    if not is_known_operator(c):
        raise Exception("char is not a known operator")

    #operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '~': 6, '%': 4, '!': 6, '@': 5, '$': 5, '&': 5}

    if c == '+' or c == '-' or c == '*' or c == '/' or c == '^' or c == '%' or c == '@' or c == '$' or c == '&':
        return "mid"
    elif c == '~' or c == '!':
        return "right"
    #no no operator is "left" operator yet but still it needs to be respected
    elif True:
        return "left"


def is_middle_operator(c):
    return kind_of_operator(c) == "mid"


def is_right_operator(c):
    return kind_of_operator(c) == "right"

# --------------------------------------------------------- ranges ----------
# finding ranges of things in the string is important for manipulating it


#gets an index of a minus and a string
#returns the range of the streak of minuses
def range_of_minuses(eq, i):
    if eq[i] != '-':
        raise Exception("char is not a minus")

    start = i
    finish = i
    while start >= 0 and eq[start] == '-':
        start -= 1
    start += 1

    while finish < len(eq) and eq[finish] == '-':
        finish += 1
    finish -= 1

    return start, finish


# gets the string and index and return a tuple of the range of number (start, end)
def range_of_number(eq, i):
    if not is_part_of_number(eq, i):
        raise Exception("the index is not in a number")
    start = i
    finish = i

    # go left
    while start >= 0 and is_part_of_number(eq, start):
        start -= 1
    start += 1

    # go right
    while finish < len(eq) and is_part_of_number(eq, finish):
        finish += 1
    finish -= 1

    return start, finish

# --------------------------------------------------------- find chars ----------
#finding specific chars or kinds of chars


"""minus"""


#gets a string
#returns the first index it found of a '-' returns -1 if not found
def find_minus(eq):
    for i in range(len(eq)):
        if is_minus(eq[i]):
            return i
    return -1


#returns the index of a minus streak
def find_minus_that_is_part_of_streak(eq):
    for i in range(len(eq)):
        if is_minus(eq[i]) and is_part_of_streak(eq, i):
            return i
    return -1


"""bracket"""


#gets a string and opener bracket index
#returns the index of the matching closer bracket for it
def find_closer_for_opener(eq, i):
    if eq[i] != '(':
        raise Exception("char not a opener bracket")

    #finding the matching closer bracket is not so obvious
    #its not he first closer bracket encountered but rather
    #the first one encounter after all the openers have found their pair
    #so every time we see an opener we add it to the unmatched openers and remove it when we find a match

    unmatched_openers_count = 0

    while i < len(eq):

        if eq[i] == '(':
            unmatched_openers_count += 1
        if eq[i] == ')':
            #if the unmatched_openers_count is 1 it means that the closer bracket matching is found
            if unmatched_openers_count == 1:
                return i
            unmatched_openers_count -= 1

        i += 1
    raise Exception("closer bracket not found, something is wrong")


# --------------------------------------------------------- list ----------
"""
important to notice that this section is about a list and not about a string 

"""

"""operators"""


#gets a list
#returns the index of the strongest operator if none found returns -1
def find_strongest_operator(lst):
    maxi = 0
    maxs = 0
    for i in range(len(lst)):
        if is_known_operator(lst[i]):
            if strength_of_operator(lst[i]) > maxs:
                maxi = i
                maxs = strength_of_operator(lst[i])
    return maxi
