# 3.
# Задача семинара:
# Имеется выражение-формула квадратного уравнения
# представленная переменной типа String.
# Задача: используя встроенные методы среды и языка Python
# вычленить из переданного выражения коэффициенты квадратного уравнения
# и уже с готовыми исходными данными посчитать корни квадратного уравнения
# и представить результат

equation = '  -4 * X**2 + 28 * x - 49 = 0'


def get_dict_odd(item_equ: str) -> list:
    if item_equ.endswith('x**2'):
        return ['A', item_equ.replace('x**2', '').replace('*', '')]
    elif item_equ.endswith('x'):
        return ['B', item_equ.replace('x', '').replace('*', '')]
    elif item_equ[-1].isdigit():
        return ['C', item_equ]
    else:
        return ['D', -1]


def fined_odds(equ: str) -> dict:
    # odds = {'A': None, 'B': None, 'C': None, 'D': None}
    oddsf = dict()
    equ = equ.strip().lower().replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -').strip().split(' ')
    lst = list()
    for i in equ:
        lst = get_dict_odd(i)
        oddsf[lst[0]] = int(lst[1])
    return oddsf


def calc_quadratic_roots(param: dict) -> dict:
    # odds = dict()
    if param.get('A') is None or param.get('B') is None or param.get('C') is None:
        param['x1'] = 'Корней нет'
        param['x2'] = 'Смотри x1'
    else:
        param['D'] = param['B']**2 - 4*param['A']*param['C']
        if param['D'] >= 0:
            param['x1'] = (-param['B'] - param['D']**0.5)/(2*param['A'])
            param['x2'] = (-param['B'] + param['D'] ** 0.5) / (2 * param['A'])
        else:
            param['x1'] = 'Корней нет'
            param['x2'] = 'Смотри x1'
    return param


def new_equation(param: dict) -> str:
    if param.get('A') is None or param.get('B') is None or param.get('C') is None:
        return 'В формуле есть ошибка'
    else:
        a, b, c = param.get('A'), param.get('B'), param.get('C')
    equat = str(a) + 'X^2'

    if b >= 0:
        equat += ' + ' + str(b) + 'X'
    else:
        equat += ' - ' + str(abs(b)) + 'X'

    if c >= 0:
        equat += ' + ' + str(c) + ' = 0'
    else:
        equat += ' - ' + str(abs(c)) + ' = 0'

    return equat


odds = calc_quadratic_roots(fined_odds(equation))
math_equation = new_equation(odds)
x1, x2 = round(odds.get('x1'), 2), round(odds.get('x2'), 2)
print(f'---\nДля полученой строки {equation} квадратное уравнение может быть представлено следующим образом:\n'
      f'{math_equation}, а корни для данного уравнения x1 = {x1}, x2 = {x2}\n---')


# print(odds, len(odds))
# print(odds.pop('B', None))
# odds = {key: odds[key] for key in odds if key != 'A'}
# print(odds, len(odds))

