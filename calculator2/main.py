import solver
import input_output as io


#get input from user
eq = io.get_equation()
res = None
#while input != "stop"
while eq.lower() != "stop":
    #solve the input
    try:
        res = solver.solve(eq)
    except Exception as e:
        #print reason why it's unsolvable
        if e.args[0] == "maximum recursion depth exceeded in comparison":
            print("the result is too large for calculating")
        else:
            print(e)

    #if solved
    if res is not None:
        if res == "inf":
            print("the result is too large for calculating")
        #print the result
        else:
            print(res)
    res = None

    #get input from user
    eq = io.get_equation()
