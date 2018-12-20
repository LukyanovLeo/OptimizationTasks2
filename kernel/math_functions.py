import re
import sympy as sp
import sympy.parsing.sympy_parser as ssp
from sympy.printing.repr import srepr
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


def steepest_descent(str_expr, x0=0, y0=0, eps_x=0.0, eps_y=0.0):
    expr = ssp.parse_expr(str_expr)
    symbols = sorted(list(map(str, expr.free_symbols)))

    grad = [sp.diff(expr, s) for s in symbols]
    grad_start_point = [g.subs({symbols[0]:x0, symbols[1]:y0}) for g in grad]
    grad_len = sqrt(sum(map(lambda i: i**2, grad_start_point)))

    x0_pre = 0.0
    y0_pre = 0.0
    while(grad_len>0):
        x1 = ssp.parse_expr('{}-{}*lam'.format(x0, grad_start_point[0]))
        y1 = ssp.parse_expr('{}-{}*lam'.format(y0, grad_start_point[1]))

        new_expr = expr.subs({symbols[0]:x1, symbols[1]:y1})
        lam = sp.Symbol('lam')
        solving = sp.solve(sp.diff(new_expr))
        x0 = x1.subs(lam, float(solving[0]))
        y0 = y1.subs(lam, float(solving[0]))

        if abs(x0_pre) - x0 < eps_x and abs(y0_pre - y0) < eps_y:
            print(round(x0), round(y0))
            break
        grad_start_point = [g.subs({symbols[0]: x0, symbols[1]: y0}) for g in grad]
        grad_len = sqrt(sum(map(lambda i: i ** 2, grad_start_point)))
        x0_pre = x0
        y0_pre = y0
        print(x0, y0, 'solv:', )


def lagrange(params, x0=0, y0=0):
    # парсим и вводим новые переменные
    list_params = params.split('|')
    expr = ssp.parse_expr(list_params[0])
    symbols = sorted(list(map(str, expr.free_symbols)))
    lam1, lam2 = sp.symbols('lam1, lam2')

    # Сохраняем отдельно ограничения
    restrictions = list()

    # сохраняем значения ограничений
    restriction_answers = list()
    for i in range(1, len(list_params)):
        if '>=' in list_params[i]:
            restrictions.append(list_params[i][:list_params[i].find('>=')].strip())
            restriction_answers.append(list_params[i][list_params[i].find('>=') + 2:].strip())
        if '<=' in list_params[i]:
            restrictions.append(list_params[i][:list_params[i].find('<=')].strip())
            restriction_answers.append(list_params[i][list_params[i].find('<=') + 2:].strip())

    # формируем функцию Лагранжа
    lagr = ssp.parse_expr('{}+lam1*({}-{})+lam2*({}-{})'.format(expr, restrictions[0], restriction_answers[0],
                                                                restrictions[1], restriction_answers[1]))
    # формируем систему уравнений от частных производных по функции Лагранжа
    x1_diff = sp.diff(lagr, symbols[0])
    x2_diff = sp.diff(lagr, symbols[1])
    lam1_diff = sp.diff(lagr, lam1)
    lam2_diff = sp.diff(lagr, lam2)

    # решаем систему уравнений

    solving = sp.solve([x1_diff, x2_diff, lam1_diff, lam2_diff], [symbols[0], symbols[1], lam1, lam2])[0]
    print(solving)
    # чисто чтобы побыстрее считать (4)
    lam2_value = lagr.subs({symbols[0]:solving[0], symbols[1]:solving[1], lam1:solving[2], lam2:solving[3]})

    # ищем точку с решением
    new_lagr = lagr.subs({lam1:-5, lam2:4})
    x1_diff = sp.diff(new_lagr, symbols[0])
    x2_diff = sp.diff(new_lagr, symbols[1])

    # ищем вторые производные
    x1_x1_diff = sp.diff(x1_diff, symbols[0])
    x1_x2_diff = sp.diff(x1_diff, symbols[1])
    x2_x2_diff = sp.diff(x2_diff, symbols[1])

    # ищем значения в найденной точке (0, 0)
    A = x1_x1_diff.subs({symbols[0]: 0, symbols[1]: 2})
    B = x1_x2_diff.subs({symbols[0]: 0, symbols[1]: 2})
    C = x2_x2_diff.subs({symbols[0]: 0, symbols[1]: 2})

    hessian = [[A, B],[B, C]]
    if A > 0:
        print(solving[0], solving[1])











def simplex_alg(params=None, args_number=1):
    list_expr = params.split('|')
    target_expr = ssp.parse_expr(list_expr[0])
    symbols = sorted(list(map(str, target_expr.free_symbols)))

    counter = 0
    basis = list()
    matrix = list()
    basis_coeffs = list()

    for i in range (0, len(list_expr)):
        if i != 0:
            counter += 1
            # добавляем базисные переменные
            new_symbol = 'x' + str(counter - 1 + len(list_expr))
            symbols.append(new_symbol)
            basis_coeffs.append(new_symbol)
            # убираем знаки равенств
            list_expr[i] = list_expr[i].replace('>=', '-').replace('<=', '-')
            list_expr[i] = ssp.parse_expr('{}+{}'.format(list_expr[i], symbols[-1]))
            basis_member = int(re.search('-?\d+', re.findall("Integer\(-?\d+\)", srepr(list_expr[i]))[-1]).group(0))
            if (basis_member < 0):
                basis_member = basis_member * -1
                list_expr[i] = list_expr[i] * -1
            basis.append(basis_member)
        else:
            list_expr[i] = ssp.parse_expr(format(list_expr[i]))
            basis.append(0)
            basis_coeffs.append(nan)

    # делаем матрицу коэффициентов (базисы хранятся отдельно)
    for expr in list_expr:
        expr_coeffs = list()
        for symbol in symbols:
            expr_coeffs.append(expr.coeff(symbol))

        matrix.append(expr_coeffs)
    # ф-ла Таккера
    matrix[0] = [m*-1 for m in matrix[0]]

    #### решаем симплекс-метод
    # (matrix[0][0] > 0 or matrix[0][1] > 0) and ('x1' not in basis_coeffs or 'x2' not in basis_coeffs)
    for k in range(1, 3):
        # 1. ищем столбец с минимальным значением целевой функции
        key_column = 0
        for i in range(0, args_number):
            if matrix[0][i] > key_column:
                key_column = matrix[0][i]

        # запоминаем номер ключевого столбца
        key_string = 0
        for i in range(1, len(basis)):
            if matrix[i][key_column] != 0 and basis[i]/matrix[i][key_column] < basis[key_string]/matrix[i][key_column]:
                key_string = i

        print(key_string, key_column)
        # ключевой элемент
        key_elem = matrix[key_string][key_column]
        # 2. Строим новую матрицу
        # делим
        matrix[key_string] = [m/key_elem for m in matrix[key_string]]
        basis[key_string] = basis[key_string]/key_elem
        basis_coeffs[key_string] = symbols[key_column]

        new_matrix = list(list())
        for i in range(len(matrix)):
            new_matrix_str = list()
            for j in range(len(matrix[i])):
                if i == key_string:
                    new_matrix_str.append(matrix[i][j])
                else:
                    new_matrix_str.append(matrix[i][j] - matrix[key_string][j] * matrix[i][key_column])
            new_matrix.append(new_matrix_str)

        matrix = new_matrix
        print(matrix)



#unconditional_extremum('3*x1*x2 - x1*x2**2 - x1**2*x2')

#lagrange('2*x1**2+x2**2 | x1**2+x2**2<=4 | 4*x1**2+x2**2>=4')
lagrange('x1**2+x2**2 | x1**2+x2**2<=16 | x1+x2>=4', 0, 4)


#steepest_descent('4*(x1-5)**2 + (x2-6)**2', 8, 9, 0.1, 0.1)
# steepest_descent('x1**3-x1*x2+x2**2-2*x1+3*x2-4', 0, 0)
#simplex_alg('3*x1+50*x2 | 200*x1+150*x2>=-200 | 14*x1+4*x2<=14', 2)

# expr.args