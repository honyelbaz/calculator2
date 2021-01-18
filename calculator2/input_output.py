
#function that asks the user for string input and returns it


def get_equation():
    s = ""
    try:
        s = input()
    except Exception:
        print("input is morally wrong")
    s = trim_string(s)
    return s


#print the result
def print_result(res):
    print(res)


def trim_string(s):
    return s.replace(' ', '')\
        .replace('\t', '')\
        .replace('\n', '')
