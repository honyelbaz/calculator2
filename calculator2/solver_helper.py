
import finder
#-----------------------------------------------validations--------------------


def is_valid(eq):
    # 
    pass


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


ss = (make_a_list(minuses_haircut("----235-003635235-5334!*---235--235^(--23)--33---")))
print(ss)
print(finder.find_strongest_operator(ss))
