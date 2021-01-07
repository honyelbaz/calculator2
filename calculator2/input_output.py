import re

#function that asks the user for string input and returns it


def get_equation():
    s = input()
    s = re.sub('[\s\t]', '', s)
    return s


#print the result
def print_result(res):
    print(res)
