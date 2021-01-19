"""

    :Written by: Hony Elbaz

    this module serves needs of input_output
"""


def get_equation():
    """:returns an equation after all the white spaces are trimmed"""
    equation = ""
    #trt getting a string input from user
    try:
        equation = input()
    except Exception:
        print("input is morally wrong")
    equation = trim_string(equation)
    return equation


def trim_string(equation):
    """trims from the white spaces"""
    return equation.replace(' ', '')\
        .replace('\t', '')\
        .replace('\n', '')
