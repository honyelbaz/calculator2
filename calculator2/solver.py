import validator
import solver_helper
import finder


# def solve(eq):
#     if not validator.is_valid(eq):
#         return None
#     #make haircut for the minuses
#     eq = solver_helper.minuses_haircut(eq)
#     #strip the expression from it's brackets if necessary
#     if solver_helper.needs_to_be_bracket_striped(eq):
#         eq = solver_helper.strip_outer_brackets(eq)
#         if solver_helper.needs_to_be_bracket_striped(eq):
#             raise Exception("unnecessary brackets on an expression: (" + str(eq) + ")")
#     #make a list
#     lst = solver_helper.make_a_list(eq)
#     #(on the list)
#     #if there are expressions (expression is a)
#     i = finder.find_expression(lst)
#     while i != -1:
#         res = solve(lst[i])
#         lst[i] = res
#         i = finder.find_expression(lst)
#     if solver_helper.list_is_valid(lst):
#         pass
#     #while len(lst) > 1 or lst[0] is not an expression
#         #find the strongest operator and operate
#     while len(lst) > 1 or not finder.is_expression(lst[0]):
#         i = finder.find_strongest_operator(lst)
#         if i == -1:
#             solver_helper.list_is_valid(lst)
#             break
#         res = solver_helper.operate(lst, i)
#         if finder.is_middle_operator(lst[i]):
#             if i == 0:
#                 del lst[0]
#                 lst[0] = res
#             elif i == len(lst) - 1:
#                 del lst[-1]
#                 lst[-1] = res
#             else:
#                 del lst[i + 1]
#                 lst[i] = str(res)
#                 del lst[i - 1]
#         elif finder.is_right_operator(lst[i]):
#             if i == 0:
#                 raise Exception("right operator at the left of the string")
#             else:
#                 del lst[i-1]
#                 lst[i-1] = res
#     return lst[0]


#gets a list and makes all the operations
def clear_from_operators(lst):
    i = finder.find_strongest_operator(lst)
    while i != -1:
        if finder.is_operator(lst[i]):
            lst = solver_helper.list_make_operation(lst, i)
        i = finder.find_strongest_operator(lst)
    return lst


def solve(eq):
    if not validator.is_valid(eq):
        return None
    #make haircut for the minuses
    eq = solver_helper.minuses_haircut(eq)
    #strip the expression from it's brackets if necessary
    if solver_helper.needs_to_be_bracket_striped(eq):
        eq = solver_helper.strip_outer_brackets(eq)
        if solver_helper.needs_to_be_bracket_striped(eq):
            raise Exception("unnecessary brackets on an expression: (" + str(eq) + ")")
    #make a list
    lst = solver_helper.make_a_list(eq)
    #(on the list)

    #if there are expressions (expression is a)
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
        raise Exception("something went wrong")
    return lst[0]
