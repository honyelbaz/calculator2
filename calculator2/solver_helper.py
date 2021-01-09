
import finder
#-----------------------------------------------validations--------------------

"""make a number """


def float_number_from_range(eq, start, finish):
    return float(substring_from_range(eq, start, finish))


def float_number_from_index(eq, i):
    if not finder.is_part_of_number(eq, i):
        raise Exception("index not in a number")

    start, finish = finder.range_of_number(eq, i)
    return float_number_from_range(eq, start, finish)


""" make a substring """


def substring_from_range(eq, start, finish):
    s = ""
    #the range given is exact which means that the finish needs to go up one because it wont be hit
    for i in range(start, finish + 1):
        s += eq[i]
    return s


""" adjust the string as i would like it to be """

#-----------------------------------------------minuses--------------------


#this method gets the string.  it finds all the minuses that are duplicated in a row and cut
#them to be one minus or one plus
def minuses_haircut(eq):
    #find the index where needs to be changed index = -1 if there are none
    index = finder.find_minus_that_is_part_of_streak(eq)

    #while there is where to change
    while index != -1:
        #the range of minuses that needs to be converted to one ore plus
        start, finish = finder.range_of_minuses(eq, index)
        #split the strings to assemble together something else
        s1, s2, s3 = split_to_3_strings_by_range(eq, start, finish)
        # if the amount is even it needs to be a plus else it needs to be a minus
        if len(s2) % 2 == 0:
            if start == 0 or finish == len(eq) - 1:
                eq = s1 + s3
            elif eq[start - 1] == '(':
                eq = s1 + s3
            elif (not finder.is_digit(eq[start - 1])) and (not(eq[start - 1] == ')'))\
                    and finder.is_middle_operator(eq[start - 1]):
                eq = s1 + s3
            else:
                eq = s1 + "+" + s3
        else:
            eq = s1 + "-" + s3
        index = finder.find_minus_that_is_part_of_streak(eq)
    return eq


#----------------------------------------------- list --------------------

#
def list_is_valid(lst):
    #the list is not valid if expression and numbers are in a  row with not operators between theme
    for i in range(len(lst)):
        if finder.is_number(lst[i]) or finder.is_expression(lst[i]):
            if i == 0 or i == len(lst) - 1:
                pass
            elif finder.is_number(lst[i + 1]) or finder.is_expression(lst[i + 1]):
                raise Exception("numbers and expressions are one after another with not operator between")
            elif finder.is_number(lst[i - 1]) or finder.is_expression(lst[i - 1]):
                raise Exception("numbers and expressions are one after another with not operator between")


#
#makes a list of meaningful members of the string into list (operands, operators, expressions)
def make_a_list(eq):
    #itarating the string and appending all the members of the equation into a string
    #it helps me to know which minus is an operand an which is a sign
    lst = []

    i = 0
    while i < len(eq):
        if finder.is_known_operator(eq[i]):
            lst.append(str(eq[i]))

        elif finder.is_part_of_number(eq, i):
            start, finish = finder.range_of_number(eq, i)
            lst.append(str(float_number_from_range(eq, start, finish)))
            i = finish

        elif eq[i] == '(':
            finish = finder.find_closer_for_opener(eq, i)
            s = substring_from_range(eq, i, finish)
            lst.append(s)
            i = finish
        else:
            raise Exception("a none valid char encountered")

        i += 1
    return lst


#
def list_make_operation(lst, i):
    if not finder.is_operator(lst[i]):
        raise Exception("not an operator")
    res = operate(lst, i)
    op = lst[i]
    lst[i] = str(res)
    if finder.is_minus(op) and i == 0:
        del lst[0 + 1]
    elif finder.is_middle_operator(op):
        if finder.is_minus(lst[i + 1]):
            del lst[i + 1]
            del lst[i + 1]
            del lst[i - 1]
        else:
            del lst[i + 1]
            del lst[i - 1]
    elif finder.is_right_operator(op):
        del lst[i - 1]
    return lst


#----------------------------------------------- string manipulations --------------------


#gets a string and a range
#return 3 strings that are the split of the original string by range
def split_to_3_strings_by_range(s, start, finish):
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


#
#
def strip_outer_brackets(eq):
    if not (eq[0] == '(' and eq[len(eq) - 1] == ')'):
        raise Exception("no brackets to strip")
    eq = split_to_3_strings_by_range(eq, 1, len(eq) - 2)[1]
    return eq


#
def needs_to_be_bracket_striped(eq):
    if eq[0] == '(':
        closer = finder.find_closer_for_opener(eq, 0)
        return closer == len(eq) - 1
    return False

#----------------------------------------------- operations --------------------


def factorial(num):

    if num < 0:
        raise Exception("factorial on negative number is wrong")
    if num % 1 != 0:
        raise Exception("factorial on none complete number is wrong")
    if num <= 1:
        return 1
    return num * factorial(num - 1)


def operate(lst, i):
    if finder.is_middle_operator(lst[i]):
        return operate_middle(lst, i)
    if finder.is_right_operator(lst[i]):
        return operate_right(lst, i)


def operate_middle(lst, i):
    if not finder.is_operator(lst[i]):
        raise Exception("not an operator")
    if i == len(lst) - 1:
        raise Exception("the operator " + str(lst[i]) + " is at the right edge of an expression")
    if finder.is_minus(lst[i]):
        if i == 0:
            if not finder.is_number(lst[i + 1]):
                raise Exception("the operator " + str(lst[i]) + " is not before a number")
            else:
                return get_result(0, float(lst[i + 1]), '-')
        elif not finder.is_number(lst[i - 1]):
            if not finder.is_number(lst[i + 1]):
                raise Exception("the operator " + str(lst[i]) + " is not before a number")
            else:
                return get_result(0, float(lst[i + 1]), '-')

    if i == 0:
        raise Exception("the operator " + str(lst[i]) + " is at the left edge of an expression")

    if finder.is_number(str(lst[i + 1])) and finder.is_number(str(lst[i - 1])):
        return get_result(float(lst[i - 1]), float(lst[i + 1]), lst[i])
    elif finder.is_number(str(lst[i - 1])) and finder.is_minus(str(lst[i + 1])):
        return get_result(float(lst[i - 1]), float(operate_middle(lst, i + 1)), lst[i])
    raise Exception("the operator " + str(lst[i]) + " is not in between two number")


def operate_right(lst, i):
    if not finder.is_operator(lst[i]):
        raise Exception("not an operator")
    if i == 0:
        raise Exception("the operator " + str(lst[i]) + " is at the left edge of an expression")
    if finder.is_number(lst[i - 1]):
        return get_result(float(lst[i - 1]), None, lst[i])
    raise Exception("the operator " + str(lst[i]) + " is not to the right of a number")


def get_result(num1, num2, op):
    # operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '~': 6, '%': 4, '!': 6, '@': 5, '$': 5, '&': 5, ')':99}
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '^':
        return num1 ** num2
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
    else:
        return None


