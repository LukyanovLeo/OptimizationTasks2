import sympy as sp
import scipy.optimize as opt
import scipy
import math


x1, x2 = sp.symbols('x1 x2')
expr = 3*x1*x2 - x1*x2**2 - x1**2*x2

x1_diff = sp.diff(expr, x1)
x2_diff = sp.diff(expr, x2)

crit = sp.solve((x1_diff, x2_diff))


for c in crit:
    x1_x1_diff = sp.diff(x1_diff, x1)
    x1_x2_diff = sp.diff(x1_diff, x2)
    x2_x2_diff = sp.diff(x2_diff, x2)

    A = x1_x1_diff.subs({x1:c[x1], x2:c[x2]})
    B = x1_x2_diff.subs({x1:c[x1], x2:c[x2]})
    C = x2_x2_diff.subs({x1:c[x1], x2:c[x2]})

    print(A, ' ', B, ' ', C)

    if A*C-B**2 > 0:
        if A>0:
            print('Min: ', c)
        elif A<0:
            print('Max: ', c)



# print(x1_x1_diff)
# print(x1_x2_diff)
# print(x2_x2_diff)
