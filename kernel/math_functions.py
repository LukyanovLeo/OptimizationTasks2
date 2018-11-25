import sympy as sp
import sympy.parsing.sympy_parser as ssp
import scipy.optimize as opt
import scipy
import math


expr = ssp.parse_expr('3*x1*x2 - x1*x2**2 - x1**2*x2')
symbols = list(expr.free_symbols)

x1_diff = sp.diff(expr, symbols[0])
x2_diff = sp.diff(expr, symbols[1])

crit = sp.solve((x1_diff, x2_diff))

for c in crit:
    x1_x1_diff = sp.diff(x1_diff, symbols[0])
    x1_x2_diff = sp.diff(x1_diff, symbols[1])
    x2_x2_diff = sp.diff(x2_diff, symbols[1])

    A = x1_x1_diff.subs({symbols[0]:c[symbols[0]], symbols[1]:c[symbols[1]]})
    B = x1_x2_diff.subs({symbols[0]:c[symbols[0]], symbols[1]:c[symbols[1]]})
    C = x2_x2_diff.subs({symbols[0]:c[symbols[0]], symbols[1]:c[symbols[1]]})

    if A*C-B**2 > 0:
        if A>0:
            print('Min: ', c)
        elif A<0:
            print('Max: ', c)