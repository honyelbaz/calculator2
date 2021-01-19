"""

    :Written by: Hony Elbaz

    this module serves all the needs of finding indexes,
    ranges and recognizing them.
"""

# dictionary of the known operators to the calculator
# the known operators are separated in a way that can differ them
# and also menage them fairly easily

left_operators = {'~': 6}

middle_operators = {'+': 1,
                    '-': 1,
                    '*': 2,
                    '/': 2,
                    '^': 3,
                    '%': 4,
                    '@': 5,
                    '$': 5,
                    '&': 5}

right_operators = {'!': 6}

""" 
-----------------------------------------
----------------------------------------- recognizers ----------
-----------------------------------------       

# because in order to find stuff you need to recognize stuff :)                       
"""


#   numbers     #


def is_digit(character):
    """Is a char a digit"""
    return '0' <= character <= '9'


def is_dot(character):
    """Is char a dot"""
    return character == '.'


def is_minus(character):
    """Is a char minus"""
    return character == '-'


def is_part_of_streak(equation, index_of_char):
    """

    :param equation: The string of the equation
    :param index_of_char: Index of a char in the string
    :return: True if the char is part of a string with itself
                           else, false
    """
    if len(equation) == 1:
        return False

    # look left and right and check if the same character is there
    if index_of_char == 0:
        return equation[index_of_char + 1] == equation[index_of_char]
    if index_of_char == len(equation) - 1:
        return equation[index_of_char - 1] == equation[index_of_char]

    return equation[index_of_char] == equation[index_of_char - 1] \
           or equation[index_of_char] == equation[index_of_char + 1]


def is_part_of_simple_number(character):
    """
    a number that is not in the form of "e+" example:
    5e+7 which is converted to 50000000

    this function is helper of "is_part_of_number"

    :param character:
    :return: True if the char is part of a simple number
                  else, false

    """
    # easy , if it's a digit or a dot it's part of
    # a simple number
    if is_digit(character) \
            or is_dot(character):
        return True

    return False


def is_part_of_number(equation, index_of_char):
    """
    This function assumes that all the duplicated minuses has been cut
    to one minus by another function

    :param equation: The string of the equation
    :param index_of_char: Index of a char in the string
    :return: True if the char is part of any kind of
    presentation of a number.
                  else, false
    """

    # if char a digit than it must be part of a number
    # if char is a dot then it must a part of a number
    # if the combination "{number}e+{number}" accrues
    if is_part_of_simple_number(equation[index_of_char]):
        return True

    # if the number is big enough and a float python will represent it in the
    # format of {number1}e+{number2}
    # which means {number1} * 10^{number2}
    if equation[index_of_char] == 'e':
        # 'e' case -> if it's at the edge of the string that's a problem of
        # course "{number1}e+{number2}"
        # i of 'e' is greater then 0 and less then len(eq) - 2 is good
        if index_of_char == 0 or index_of_char >= len(equation) - 2:
            return False
        if equation[index_of_char + 1] != '+':
            return False
        if not is_part_of_simple_number(equation[index_of_char + 2]):
            return False
        if not is_part_of_simple_number(equation[index_of_char - 1]):
            return False
        return True

    if equation[index_of_char] == '+':
        if index_of_char <= 1 or index_of_char == len(equation) - 1:
            return False
        if equation[index_of_char - 1] != 'e':
            return False
        if not is_part_of_simple_number(equation[index_of_char - 2]):
            return False
        if not is_part_of_simple_number(equation[index_of_char + 1]):
            return False
        return True
    return False


#   operators   #


def strength_of_operator(operator):
    """

    :param operator: A character that's suppose to be an operator
    :return: an integer, the strength of the operator
            (relatively to the other operators)
    """
    if not is_known_operator(operator):
        raise Exception("char is not a known operator")

    # check what kind of operator it is to know what dictionary to
    # look for it's strength
    if is_left_operator(operator):
        return left_operators[operator]
    elif is_right_operator(operator):
        return right_operators[operator]
    elif is_middle_operator(operator):
        return middle_operators[operator]


def is_known_operator(operator):
    """If it's in any dictionary of operators it's known"""
    return operator in right_operators \
           or operator in middle_operators \
           or operator in left_operators


def is_middle_operator(operator):
    """If it's the kind of operator in between two numbers"""
    return operator in middle_operators


def is_right_operator(operator):
    """If it's the kind of operator to the right of a number"""
    return operator in right_operators


def is_left_operator(operator):
    """If it's the kind of operator to the left of a number"""
    return operator in left_operators


"""
 these functions gets a string which is the element of the list
 and return True if it's one of them
"""


def is_number(element_of_list):
    msg = ""
    try:
        float(element_of_list)
    except Exception as e:
        msg = e
    return msg == ""


def is_expression(element_of_list):
    if is_number(element_of_list) or is_operator(element_of_list):
        return False
    return element_of_list[0] == '(' \
        and element_of_list[len(element_of_list) - 1] == ')'


def is_operator(element_of_list):
    if len(element_of_list) > 1:
        return False
    return is_known_operator(element_of_list)


""" 
-----------------------------------------
----------------------------------------- ranges ----------
-----------------------------------------       

# finding ranges of things in the string is important for
 manipulating it
"""


def range_of_minuses(equation, index_of_minus):
    """

    :param equation: A string representing the equation
    :param index_of_minus: An index of char that's suppose to be a minus
    :return: A tuple of two indexes , start of the range and the end
    of the range
    """
    if equation[index_of_minus] != '-':
        raise Exception("char is not a minus")

    start = index_of_minus
    finish = index_of_minus
    #go left
    while start >= 0 and equation[start] == '-':
        start -= 1
    start += 1

    #go right
    while finish < len(equation) and equation[finish] == '-':
        finish += 1
    finish -= 1

    return start, finish


def range_of_number(equation, index_of_number_char):
    """

    :param equation: A string representing the equation
    :param index_of_number_char: An index of char that's suppose to be
    part of a number
    :return: A tuple of two indexes , start of the range and the end
    of the range
    """
    if not is_part_of_number(equation, index_of_number_char):
        raise Exception("the index is not in a number")
    start = index_of_number_char
    finish = index_of_number_char

    # go left
    while start >= 0 and is_part_of_number(equation, start):
        start -= 1
    start += 1

    # go right
    while finish < len(equation) and is_part_of_number(equation, finish):
        finish += 1
    finish -= 1

    return start, finish


""" 
-----------------------------------------
----------------------------------------- find chars ----------
-----------------------------------------       

# finding specific chars or kinds of chars
"""


"""minus"""


def find_minus(equation):
    """

    :param equation: A string
    :return: the first index it found of a '-' returns -1 if not found
    """
    for i in range(len(equation)):
        if is_minus(equation[i]):
            return i
    return -1


def find_minus_that_is_part_of_streak(equation):
    """returns the index of a minus streak"""
    for i in range(len(equation)):
        if is_minus(equation[i]) and is_part_of_streak(equation, i):
            return i
    return -1


"""bracket"""


def find_closer_for_opener(equation, index_of_opener_bracket):
    """

    :param equation: A string
    :param index_of_opener_bracket: opener bracket index
    :return: the index of the matching closer bracket for it
            -1 if not found
    """
    if equation[index_of_opener_bracket] != '(':
        raise Exception("char not a opener bracket")

    # finding the matching closer bracket is not so obvious
    # its not he first closer bracket encountered but rather
    # the first one encounter after all the openers have found their pair
    # so every time we see an opener we add it to the unmatched openers and
    # remove it when we find a match

    unmatched_openers_count = 0

    while index_of_opener_bracket < len(equation):

        if equation[index_of_opener_bracket] == '(':
            unmatched_openers_count += 1
        if equation[index_of_opener_bracket] == ')':
            # if the unmatched_openers_count is 1 it means that the closer
            # bracket matching is found
            if unmatched_openers_count == 1:
                return index_of_opener_bracket
            unmatched_openers_count -= 1

        index_of_opener_bracket += 1
    return -1


"""operators"""

# --------------------------------------------------------- list ----------
"""
important to notice that this section is about a list and not about a string 

"""

"""operators"""


def find_strongest_operator(equation_list):
    """

    :param equation_list: The equation after it has been broken apart
            to be a list
    :return: the index of the strongest operator if none found returns -1
    """
    max_index = -1
    max_strength = 0
    for i in range(len(equation_list)):
        if is_known_operator(equation_list[i]):
            if strength_of_operator(equation_list[i]) > max_strength:
                max_index = i
                max_strength = strength_of_operator(equation_list[i])

    if is_left_operator(equation_list[max_index]):
        max_index = find_most_right_lefty(equation_list, max_index)
    return max_index


def find_most_right_lefty(equation_list, index_of_left_operator):
    """although the operator is the first strongest found
    but it might be that it's not his turn to be operated.
    in fact it's the most right one's concat to it"""

    # in case of a left operator. if it's the strongest then the
    # real strongest operator is the lefty operator which is most right
    if not equation_list[index_of_left_operator] in left_operators:
        raise Exception("not a left operator")
    original_operator = equation_list[index_of_left_operator]

    while index_of_left_operator < len(equation_list) \
            and (equation_list[index_of_left_operator] in left_operators
                 and
                 strength_of_operator(original_operator)
                 == strength_of_operator(
                equation_list[index_of_left_operator])) \
            or is_minus(equation_list[index_of_left_operator]):
        index_of_left_operator += 1

    while equation_list[index_of_left_operator] != original_operator:
        index_of_left_operator -= 1
    return index_of_left_operator


def find_expression(equation_list):
    """find an expression that is between a number"""
    for i in range(len(equation_list)):
        if is_expression(equation_list[i]):
            return i
    return -1
