import finder


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
