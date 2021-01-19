import solver
import input_output as io

# get input from user
eq = io.get_equation()
res = None
# while input != "stop"
while eq.lower() != "stop":
    # solve the input
    try:
        res = solver.solve(eq)
    except solver.Invalid as e:
        pass    # the validity check function already prints the reason.
                # no need to print "invalid" if the reason is printed
    except Exception as e:
        # print reason why it's unsolvable
        print(e)

    # if solved
    if res is not None:
        print(res)
    res = None

    # get input from user
    eq = io.get_equation()
