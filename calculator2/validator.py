import finder


#gets a string after the white characters has been cleared
#returns True if it's valid two start solving else returns False and prints
# reason why not valid
def is_valid(eq):
    # not valid if...
    # no numbers or empty
    # if the amount of left brackets is not equal to the amount of
    # right brackets
    # if two dot are one after another or a dot is not in middle of a number
    # a number can be presented like 45e+4 but it's invalid if the user
    # gives 23e+32e+23

    msg = ""
    if len(eq) == 0:
        print("empty input. ")
        return False

    if len(eq) > 10000:
        print("Don't you think the size of this equation is absurd?!")
        return False

    number_found = False
    left_bracket_counter = 0
    right_bracket_counter = 0

    i = 0
    while i < len(eq):
        if finder.is_digit(eq[i]):
            number_found = True
        elif eq[i] == '(':
            left_bracket_counter += 1
            if finder.find_closer_for_opener(eq, i) == -1:
                msg += "some brackets are not correctly ordered. "
        elif eq[i] == ')':
            right_bracket_counter += 1
        elif finder.is_dot(eq[i]):
            if not check_if_dot_in_suitable_place(eq, i):
                print("dot not in suitable place. ")
                return False
        elif eq[i] == 'e':
            if not check_if_e_plus_in_suitable_place(eq, i):
                msg += "the streak of e+ is not used correctly. "
        elif not finder.is_known_operator(eq[i]):
            print("invalid character found. \'" + str(eq[i]) + "\'")
            return False
        i += 1

    if not number_found:
        msg += "no number found in the equation. "
    if left_bracket_counter != right_bracket_counter:
        msg += "amount of left brackets is not equal to the amount of right brackets. "

    if msg == "":
        return True
    else:
        print(msg)
        return False


#enter:gets string and index of a dot
#exit:returns true if the dot is in suitable place, else false
def check_if_dot_in_suitable_place(eq, i):
    if not finder.is_dot(eq[i]):
        raise Exception("char is not a dot")

    #if it's at the edge it's obviously not ok
    if i == 0:
        return False
    if i == len(eq) - 1:
        return False
    #next to another dot is not ok
    if finder.is_dot(eq[i + 1]) or finder.is_dot(eq[i - 1]):
        return False
    #needs to be between two digits
    if not(finder.is_digit(eq[i + 1]) and finder.is_digit(eq[i - 1])):
        return False

    #checking a situation like this: "152.485.44444"
    dot_counter = 0
    start, finish = finder.range_of_number(eq, i)
    for j in range(start, finish):
        if finder.is_dot(eq[j]):
            dot_counter += 1
    if dot_counter > 1:
        return False

    return True


#
def check_if_e_plus_in_suitable_place(eq, i):
    if not (eq[i] == 'e' or eq[i] == '+'):
        raise Exception("char is not a dot")

    if not finder.is_part_of_number(eq, i):
        return False
    start, finish = finder.range_of_number(eq, i)

    counter = 0
    for i in range(start, finish):
        if eq[i] == 'e':
            counter += 1
    if counter > 1:
        return False
    return True
