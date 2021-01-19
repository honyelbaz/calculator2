"""

    :Written by: Hony Elbaz

    this module helps the solver module to
    get results and manipulate strings and lists
"""


import finder

#   make a number   #


def float_number_from_range(equation, start, finish):
    """

    :param equation: A string of the equation
    :param start: start index of a number
    :param finish: finish index of a number
    :return: return the number
    """
    return float(substring_from_range(equation, start, finish))


def float_number_from_index(equation, index_of_number_char):
    """

    :param equation: A string of the equation
    :param index_of_number_char: Index of a char that is part of a number
    :return: the number
    """
    if not finder.is_part_of_number(equation, index_of_number_char):
        raise Exception("index not in a number")

    #find the range of the number and call the function
    # that returns the number from the range
    start, finish = finder.range_of_number(equation, index_of_number_char)
    return float_number_from_range(equation, start, finish)


""" make a substring """


def substring_from_range(equation, start, finish):
    """gets a string and a range and returns a
    substring from that range"""
    s = ""
    # the range given is exact which means that the finish needs to
    # go up one because it wont be hit
    for i in range(start, finish + 1):
        s += equation[i]
    return s


""" adjust the string as i would like it to be """


# -----------------------------------------------minuses-----------------------


def minuses_haircut(equation):
    """  this method gets the string.
         it finds all the minuses that are duplicated
         in a row and cut them to be one minus or one plus or none
         :returns: the new string
"""
    # find the index where needs to be changed index = -1 if there are none
    index_of_minuses_in_row \
        = finder.find_minus_that_is_part_of_streak(equation)

    # while there is where to change
    while index_of_minuses_in_row != -1:
        # the range of minuses that needs to be converted to one or plus
        start, finish = finder.range_of_minuses(
                                                equation,
                                                index_of_minuses_in_row)
        # split the strings to assemble together something else
        s1, s2, s3 = split_to_3_strings_by_range(equation, start, finish)
        # if the amount is even it needs to be a plus else it needs
        # to be a minus
        if len(s2) % 2 == 0:
            if start == 0 or finish == len(equation) - 1:
                equation = s1 + s3
            elif equation[start - 1] == '(':
                equation = s1 + s3
            elif (not finder.is_digit(equation[start - 1])) \
                    and (not (equation[start - 1] == ')')) \
                    and finder.is_middle_operator(equation[start - 1]):
                equation = s1 + s3
            elif finder.is_known_operator(equation[start - 1]) \
                    and finder.is_known_operator(equation[finish + 1]) \
                    and not \
                    (finder.is_right_operator(equation[start - 1])
                     and finder.is_right_operator(equation[finish + 1])):
                equation = s1 + s3
            else:
                equation = s1 + "+" + s3
        else:
            equation = s1 + "-" + s3
        index_of_minuses_in_row \
            = finder.find_minus_that_is_part_of_streak(equation)
    return equation


# ----------------------------------------------- list ------------------------


def list_is_valid(equation_list):
    """

    :param equation_list: The list of the equation
    :return: Is the list valid
    """
    # the list is not valid if expression and numbers are in a  row with not
    # operators between theme
    for i in range(len(equation_list)):
        if finder.is_number(equation_list[i]) or finder.is_expression(equation_list[i]):
            if i == 0 or i == len(equation_list) - 1:
                pass
            elif finder.is_number(equation_list[i + 1]) \
                    or finder.is_expression(equation_list[i + 1]):
                raise Exception("numbers and expressions are one"
                                " after another with not operator between")
            elif finder.is_number(equation_list[i - 1]) \
                    or finder.is_expression(equation_list[i - 1]):
                raise Exception("numbers and expressions are one"
                                " after another with not operator between")


def make_a_list(equation):
    """
    # makes a list of meaningful members of the string into list
    # (operands, operators, expressions)

    :param equation: string to make list from
    :return: the list of course
    """
    # iterating the string and appending all the members of the equation into
    # a string it helps me to know which minus is an operand an which is a sign
    lst = []

    i = 0
    while i < len(equation):
        if finder.is_known_operator(equation[i]):
            lst.append(str(equation[i]))

        elif finder.is_part_of_number(equation, i):
            start, finish = finder.range_of_number(equation, i)
            lst.append(str(float_number_from_range(equation, start, finish)))
            i = finish

        elif equation[i] == '(':
            finish = finder.find_closer_for_opener(equation, i)
            s = substring_from_range(equation, i, finish)
            lst.append(s)
            i = finish
        else:
            raise Exception("a none valid char encountered")

        i += 1
    return lst


def list_make_operation(equation_list, index_of_element):
    """
    This method is very good.
    it gets a result for operator and numbers and finds out
    where to place and what nodes to delete

    :param equation_list: The list of the equation
    :param index_of_element: the index of the operator
    :return: the new list after the result is paced correctly
    """
    if not finder.is_operator(equation_list[index_of_element]):
        raise Exception("not an operator")
    res = operate(equation_list, index_of_element)
    op = equation_list[index_of_element]
    equation_list[index_of_element] = str(res)
    if finder.is_minus(op) and index_of_element == 0:
        del equation_list[0 + 1]
    elif finder.is_middle_operator(op):
        if finder.is_minus(equation_list[index_of_element + 1]):
            del equation_list[index_of_element + 1]
            del equation_list[index_of_element + 1]
            del equation_list[index_of_element - 1]
        else:
            del equation_list[index_of_element + 1]
            del equation_list[index_of_element - 1]
    elif finder.is_right_operator(op):
        del equation_list[index_of_element - 1]

    elif finder.is_left_operator(op):
        if finder.is_minus(equation_list[index_of_element + 1]):
            del equation_list[index_of_element + 1]
            del equation_list[index_of_element + 1]
        else:
            del equation_list[index_of_element + 1]

    return equation_list


# ---------------------------------- string manipulations ---------------------


def split_to_3_strings_by_range(s, start, finish):
    """ # gets a string and a range
        # return 3 strings that are the split of the original string by range
"""
    s1 = ""
    s2 = ""
    s3 = ""
    for i in range(len(s)):
        if i < start:
            s1 += s[i]
        elif start <= i <= finish:
            s2 += s[i]
        else:
            s3 += s[i]
    return s1, s2, s3


def strip_outer_brackets(equation_string):
    """gets a string covered with brackets
    and return new string without the brackets"""
    if not (equation_string[0] == '('
            and equation_string[len(equation_string) - 1] == ')'):
        raise Exception("no brackets to strip")

    equation_string \
        = split_to_3_strings_by_range(
                                        equation_string,
                                        1, len(equation_string) - 2)[1]
    return equation_string


def needs_to_be_bracket_striped(equation):
    """checks if is needs to be bracket striped
    :returns True or False"""
    if equation[0] == '(':
        closer = finder.find_closer_for_opener(equation, 0)
        return closer == len(equation) - 1
    return False


# ----------------------------------------------- operations ------------------


def factorial(num):
    """not mush to say
    :returns the factorial of a number"""
    if num < 0:
        raise Exception("factorial on negative number is wrong")
    if num % 1 != 0:
        raise Exception("factorial on none complete number is wrong")
    if num <= 1:
        return 1
    return num * factorial(num - 1)


def operate(list_equation, index_of_operator):
    """

    :param list_equation: the equation
    :param index_of_operator:
    :return: the result of the operation
    """
    res = None
    if finder.is_middle_operator(list_equation[index_of_operator]):
        res = operate_middle(list_equation, index_of_operator)
    if finder.is_right_operator(list_equation[index_of_operator]):
        res = operate_right(list_equation, index_of_operator)
    if finder.is_left_operator(list_equation[index_of_operator]):
        res = operate_left(list_equation, index_of_operator)

    if res == float("inf"):
        raise Exception("the result is too large for calculating")
    return res


def operate_middle(list_equation, index_of_operator):
    """
    Assumes the operator is a middle operator

    :param list_equation: the equation
    :param index_of_operator:
    :return: the result of the operation
    """
    if not finder.is_operator(list_equation[index_of_operator]):
        raise Exception("not an operator")
    if index_of_operator == len(list_equation) - 1:
        raise Exception("the operator "
                        + str(list_equation[index_of_operator])
                        + " is at the right edge of an expression")

    # minus is a special case because it's not always a middle operator
    # some times it's ok for it too be at the left edge of the equation
    if finder.is_minus(list_equation[index_of_operator]):
        if index_of_operator == 0:
            if not finder.is_number(list_equation[index_of_operator + 1]):
                raise Exception("the operator "
                                + str(list_equation[index_of_operator])
                                + " is not before a number"
                                )
            else:
                return get_result(
                    0,
                    float(list_equation[index_of_operator + 1]),
                    '-'
                )

        elif not finder.is_number(list_equation[index_of_operator - 1]):
            if not finder.is_number(list_equation[index_of_operator + 1]):
                raise Exception(
                    "the operator "
                    + str(list_equation[index_of_operator])
                    + " is not before a number")
            else:
                return get_result(
                    0,
                    float(list_equation[index_of_operator + 1]),
                    '-'
                )

    if index_of_operator == 0:
        raise Exception("the operator " + str(list_equation[index_of_operator])
                        + " is at the left edge of an expression")

    if finder.is_number(str(list_equation[index_of_operator + 1])) \
            and finder.is_number(str(list_equation[index_of_operator - 1])):

        return get_result(float(list_equation[index_of_operator - 1]),
                          float(list_equation[index_of_operator + 1]),
                          list_equation[index_of_operator])

    elif finder.is_number(str(list_equation[index_of_operator - 1])) \
            and finder.is_minus(str(list_equation[index_of_operator + 1])):

        return get_result(float(list_equation[index_of_operator - 1]),
                          float(operate_middle(list_equation,
                                               index_of_operator + 1)),
                          list_equation[index_of_operator])

    raise Exception("the operator " + str(list_equation[index_of_operator]) +
                    " is not in between two number")


def operate_left(list_equation, index_of_operator):
    """
    Assumes the operator is a left operator

    :param list_equation: the equation
    :param index_of_operator:
    :return: the result of the operation
    """

    if not finder.is_operator(list_equation[index_of_operator]):
        raise Exception("not an operator")
    if index_of_operator == len(list_equation) - 1:
        raise Exception(
            "the operator " + str(list_equation[index_of_operator])
                            + " is at the right edge of an expression")
    if finder.is_number(list_equation[index_of_operator + 1]):
        return get_result(
            float(list_equation[index_of_operator + 1]),
            None,
            list_equation[index_of_operator]
        )
    elif finder.is_minus(list_equation[index_of_operator + 1]):
        return get_result(
                          operate_middle(list_equation, index_of_operator + 1),
                          None,
                          list_equation[index_of_operator]
                          )

    raise Exception("the operator "
                    + str(list_equation[index_of_operator])
                    + " is not to t he left of a number")


def operate_right(list_equation, index_of_operator):
    """
    Assumes the operator is a right operator

    :param list_equation: the equation
    :param index_of_operator:
    :return: the result of the operation
    """

    if not finder.is_operator(list_equation[index_of_operator]):
        raise Exception("not an operator")
    if index_of_operator == 0:
        raise Exception("the operator "
                        + str(list_equation[index_of_operator])
                        + " is at the left edge of an expression")
    if finder.is_number(list_equation[index_of_operator - 1]):
        return get_result(float(list_equation[index_of_operator - 1]),
                          None,
                          list_equation[index_of_operator]
                          )
    raise Exception("the operator " + str(list_equation[index_of_operator])
                    + " is not to the right of a number")


def get_result(num1, num2, op):
    """
    :param num2: number 2
    :param num1: number 1
    :parameter:s
    :param op: is the operator

    if op is middle operator
        num1 is the left and num2 is the right

    if op is right or left operator
        num1 is the only operator because only one needed


    :return: returns the result of the operation
    """
    try:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '^':
            res = num1 ** num2
            if isinstance(res, complex):
                raise Exception("does not support complex numbers")
            return res
        elif op == '@':
            return (num1 + num2) / 2
        elif op == '$':
            return max(num1, num2)
        elif op == '&':
            return min(num1, num2)
        elif op == '%':
            return num1 % num2
        elif op == '/':
            return num1 / num2
        elif op == '!':
            return factorial(num1)
        elif op == '~':
            return -1 * num1
        elif op == '|':
            return -1 * num1
        elif op == 'z':
            return num1 + 1
        else:
            return None
    except OverflowError:
        raise Exception("the result is too large for calculating")
    except RecursionError:
        raise Exception("the result is too large for calculating")
