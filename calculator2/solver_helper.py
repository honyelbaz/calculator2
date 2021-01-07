
import finder


"""make a number """


def float_number_from_range(eq, start, finish):
    return float(substring_from_range(eq, start, finish))


def number_from_index(eq, i):
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
#i don't mean to treat the minus sign as an operator but as a sign so i will find them
# and terminate them >:)


#this method gets the string.  it finds all the minuses that are duplicated in a row and cut
#them to be one minus or one plus
#this method needs a next method to complete it (attach a plus to a minus)
def minuses_haircut(eq):
    pass


def attach_pluses_to_minuses(eq):
    pass
