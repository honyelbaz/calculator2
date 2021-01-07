# the known operators to the calculator

operators = {'+': 1, '*': 2, '/': 2, '^': 3, '~': 6, '%': 4, '!': 6, '@': 5, '$': 5, '&': 5, ')': 99}

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
        # 'e' case -> if it's at the edge of the string that a problem of course "{number1}e+{number2}"
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

    if eq[i] == '-':
        # then it's a sign minus
        if i == len(eq) - 1:
            return False
        if not is_digit(eq[i + 1]):
            return False
        return True
    return False


# --------------------------------------------------------- ranges ----------
# finding ranges of things in the string is important for manipulating it


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


#gets a string
#returns the first index it found of a '-' returns -1 if not found
def find_minus(eq):
    for i in range(len(eq)):
        if is_minus(eq[i]):
            return i
    return -1


def range_of_minuses(eq, i):
    pass