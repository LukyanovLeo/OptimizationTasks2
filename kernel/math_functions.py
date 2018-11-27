import sympy as sp
import sympy.parsing.sympy_parser as ssp

from math import *


def unconditional_extremum(str_expr):
    expr = ssp.parse_expr(str_expr)
    symbols = sorted(list(map(str, expr.free_symbols)))

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


def steepest_descent(str_expr, x0=0, y0=0, eps1=0, eps2=0):

    expr = ssp.parse_expr(str_expr)
    symbols = sorted(list(map(str, expr.free_symbols)))

    grad = [sp.diff(expr, s) for s in symbols]
    grad_start_point = [g.subs({symbols[0]:x0, symbols[1]:y0}) for g in grad]
    grad_len = sqrt(sum(map(lambda i: i**2, grad_start_point)))

    while(grad_len>0):

        x1 = ssp.parse_expr('{}-{}*lam'.format(x0, grad_start_point[0]))
        y1 = ssp.parse_expr('{}-{}*lam'.format(y0, grad_start_point[1]))

        new_expr = expr.subs({symbols[0]:x1, symbols[1]:y1})
        lam = sp.Symbol('lam')
        solving = sp.solve(sp.diff(new_expr))
        x0 = x1.subs(lam, float(solving[0]))
        y0 = y1.subs(lam, float(solving[0]))

        grad_start_point = [g.subs({symbols[0]: x0, symbols[1]: y0}) for g in grad]
        grad_len = sqrt(sum(map(lambda i: i ** 2, grad_start_point)))





#steepest_descent('4*(x1-5)**2 + (x2-6)**2', 8, 9)