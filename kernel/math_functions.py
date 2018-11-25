import sympy as sp
import sympy.parsing.sympy_parser as ssp
import ast
from sympy.core.basic import *
import scipy.optimize as opt
import scipy
import math

expr = ssp.parse_expr('3*x1*x2 - x1*x2**2 - x1**2*x2')
symbols = list(expr.free_symbols)


x1_diff = sp.diff(expr, symbols[0])
x2_diff = sp.diff(expr, symbols[1])

str = str(symbols).strip('[]')
list_str = str.split(', ')
list_str.sort()
print(list_str)

# crit = sp.solve((x1_diff, x2_diff))
# obj = sp.srepr(expr)
#
#
# for c in crit:
#     x1_x1_diff = sp.diff(x1_diff, x1)
#     x1_x2_diff = sp.diff(x1_diff, x2)
#     x2_x2_diff = sp.diff(x2_diff, x2)
#
#     A = x1_x1_diff.subs({x1:c[x1], x2:c[x2]})
#     B = x1_x2_diff.subs({x1:c[x1], x2:c[x2]})
#     C = x2_x2_diff.subs({x1:c[x1], x2:c[x2]})
#
#     print(A, ' ', B, ' ', C)
#
#     if A*C-B**2 > 0:
#         if A>0:
#             print('Min: ', c)
#         elif A<0:
#             print('Max: ', c)



# print(x1_x1_diff)
# print(x1_x2_diff)
# print(x2_x2_diff)
