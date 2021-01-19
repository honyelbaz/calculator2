"""

    :Written by: Hony Elbaz

    this module has the solving methods
"""

import validator
import solver_helper
import finder


def clear_from_operators(equation_list):
    """

    :param equation_list: The list of the equation
    :return: the list after all the operations has been made on it
    """
    i = finder.find_strongest_operator(equation_list)
    #find an operator until not found and operate it
    while i != -1:
        if finder.is_operator(equation_list[i]):
            equation_list = solver_helper.list_make_operation(equation_list, i)
        i = finder.find_strongest_operator(equation_list)
    return equation_list


def solve(equation):
    """
    The solving method. this is a somewhat recursive method.
    The method finds al the between brackets expression and solves them
    with recursive call (as if they where equations themselves),
    then solves the equation itself.

    This method the only solving method that should be called
    in the main file

    *This method needs to be covered with try and catch

    :param equation: The string, The Equation
    :return: the result to the equation
    :exception: Exceptions of validity of the equation
    """

    if not validator.is_valid(equation):
        raise Invalid("not valid")
    #make haircut for the minuses
    equation = solver_helper.minuses_haircut(equation)
    #strip the expression from it's brackets if necessary
    # if an expression needs to be striped twice then it's
    # invalid equation
    if solver_helper.needs_to_be_bracket_striped(equation):
        equation = solver_helper.strip_outer_brackets(equation)
        if solver_helper.needs_to_be_bracket_striped(equation):
            raise Exception("unnecessary brackets on an expression: (" +
                            str(equation) + ")")
    #make a list
    lst = solver_helper.make_a_list(equation)
    #(on the list)

    # while there are expressions, solve them
    # (expression is an equation in between brackets)

    i = finder.find_expression(lst)
    while i != -1:
        res = solve(lst[i])
        lst[i] = res
        i = finder.find_expression(lst)

    if solver_helper.list_is_valid(lst):
        pass
    #while len(lst) > 1 or lst[0] is not an expression
        #find the strongest operator and operate
    lst = clear_from_operators(lst)
    if solver_helper.list_is_valid(lst):
        pass
    if len(lst) > 1:
        raise Exception("an operator is missing between two expressions")
    return lst[0]


class Invalid(Exception):
    """A class for differing "invalidity" Exceptions"""
    pass
