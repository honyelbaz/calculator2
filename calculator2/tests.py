import solver
import input_output as io


def test_empty():
    #set up the equation and the result
    eq = ""
    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "not valid"


def test_eq1():
    #set up the equation and the result
    eq = "5235^2-7 * 22%(3!+45-7 * (44$2@12))"
    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "27406086.0"


def test_eq2():
    #set up the equation and the result
    eq = "((8*(8+79*(8))-0)-0)"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "5120.0"


def test_eq3():
    #set up the equation and the result
    eq = "24%12^2-7*9&(2+3-4+6$22--8--~9+8!)"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "-63.0"


def test_eq4():
    #set up the equation and the result
    eq = "----(8--8)$5+2%456+99*~(6+6)+2^(-(1+1))"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "-1169.75"


def test_eq5():
    #set up the equation and the result
    eq = "0!+-1*2/3^4%5&6$7@~8"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "-1.0"


def test_eq6():
    #set up the equation and the result
    eq = "---6&22%(2+6-5)^2-2&21$221@0"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "-110.5"


def test_eq7():
    #set up the equation and the result
    eq = "----~4+67 * 2-4522/221+(2&23 * 22%3^2)-7*2@4"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "90.53846153846155"


def test_eq8():
    #set up the equation and the result
    eq = "((2+4-~6^2-4+2)/(2+3^2/5&2@56)+76+~-4!)"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "86.14925373134328"


def test_eq9():
    #set up the equation and the result
    eq = "005* 2^2&2-7&88+224@26-(43-44+66&2----45*(321&2))"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "47.0"


def test_eq10():
    #set up the equation and the result
    eq = "7&8*22^3!-7^3+((22%2 * 7)+3$5^3&~7)"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "793658985.0000128"


def test_eq11():
    #set up the equation and the result
    eq = "14$5%2&4+4+4-7.7+(5*3$2)!"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "1307674368000.3"


def test_eq12():
    #set up the equation and the result
    eq = "~((88/23*2.2)^3&(5!+---6^3))"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "-1.5239066784713154e-89"


def test_eq13():
    #set up the equation and the result
    eq = "6^6^6-345"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "1.0314424798490537e+28"


def test_eq14():
    #set up the equation and the result
    eq = "999999^99999"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "the result is too large for calculating"


def test_eq15():
    #set up the equation and the result
    eq = "34344!"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "the result is too large for calculating"


def test_eq16():
    #set up the equation and the result
    eq = "1!+8-(90)"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "-81.0"


def test_eq17():
    #set up the equation and the result
    eq = "1!+2@3$4%5^6&7*~8-(90)"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "-32857.0"


def test_eq18():
    #set up the equation and the result
    eq = "~~~----~-~---~--~~~~~----~-~-~2323"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "2323.0"


def test_eq19():
    #set up the equation and the result
    eq = "34e+66"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "3.4e+67"


def test_eq20():
    #set up the equation and the result
    eq = "~--~5"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "5.0"


def test_syntax1():
    #set up the equation and the result
    eq = "7.7.7+5.1.1"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "not valid"


def test_syntax2():
    #set up the equation and the result
    eq = "7.7.7+5.1.1"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "not valid"


def test_syntax3():
    #set up the equation and the result
    eq = "5+a"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "not valid"


def test_syntax4():
    #set up the equation and the result
    eq = "45(6)6+4"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "numbers and expressions are one after another with" \
                  " not operator between"


def test_syntax5():
    #set up the equation and the result
    eq = "(5+9"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "not valid"


def test_syntax6():
    #set up the equation and the result
    eq = "*5+9"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "the operator * is at the left edge of an expression"


def test_syntax7():
    #set up the equation and the result
    eq = "\t"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "not valid"


def test_syntax8():
    #set up the equation and the result
    eq = "\n"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "not valid"


def test_syntax9():
    #set up the equation and the result
    eq = "((4325))"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "unnecessary brackets on an expression: ((4325))"


def test_math_error1():
    #set up the equation and the result
    eq = "4/0"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "float division by zero"


def test_math_error2():
    #set up the equation and the result
    eq = "0.5!"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "factorial on none complete number is wrong"


def test_math_error3():
    #set up the equation and the result
    eq = "~4^0.5+2"

    #try solving the equation
    try:
        res = solver.solve(io.trim_string(eq))
    except Exception as e:
        res = e.args[0]
    #assert the result
    assert res == "does not support complex numbers"
