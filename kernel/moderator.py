from math_functions import *


def select_operation(descriptor, params=""):
    if descriptor == 1:
        unconditional_extremum(params)
    elif descriptor == 2:
        steepest_descent(params)
    elif descriptor == 3:
        lagrange(params)
    elif descriptor == 4:
        simplex_alg()
    elif descriptor == 2:
        pass
    elif descriptor == 2:
        pass