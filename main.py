def get_vars(a, b, parts):
    ixes = {'base': [], 'divided': []}
    first_elem = round((b - a) / parts + a, 2)

    ixes['base'].append(first_elem)
    ixes['divided'].append(first_elem-(first_elem/2))
    el = first_elem
    for _ in range(1, parts-1):
        el += first_elem
        ixes['base'].append(round(el, 2))
        ixes['divided'].append(round(el-(first_elem/2), 2))

    ixes['divided'].append(round(b-(first_elem/2), 2))
    return ixes

def eval_function(function, var):
    return round(eval(function.format(var)), 6)

# print(get_vars(0, 1, 10))
def rectangle_first_formula(a, b, _vars, parts, function):
    vars = _vars
    # vars['base'].append(a)
    values = []
    for v in vars['base']:
        values.append(eval_function(function, v))
    values.append(eval_function(function, a))
    return ((b - a) / parts) * sum(values)

def rectangle_second_formula(a, b, _vars, parts, function):
    vars = _vars
    # vars['base'].append(b)
    values = []
    for v in vars['base']:
        values.append(eval_function(function, v))
    values.append(eval_function(function, b))
    return ((b - a) / parts) * sum(values)

def rectangle_third_formula(a, b, _vars, parts, function):
    vars = _vars
    values = []
    for v in vars['divided']:
        values.append(eval_function(function, v))
    return ((b - a) / parts) * sum(values)

def rectangle_trapetion_formula(a, b, _vars, parts, function):
    vars = _vars
    values = []
    for v in vars['base']:
        values.append(eval_function(function, v))
    values.append((eval_function(function, a)+eval_function(function, b))/2)
    return ((b - a) / parts) * sum(values)


def input_vars():
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    function = input('Введите функцию: ')
    parts = int(input('Введите кол-во частей: '))

    return a, b, function, parts

def main():
    a, b, function, parts = input_vars()
    vars = get_vars(a, b, parts)
    print('Формула прямоугольника 1: ', round(rectangle_first_formula(a, b, vars, parts, function), 7))
    print('Формула прямоугольника 1a: ', round(rectangle_second_formula(a, b, vars, parts, function), 7))
    print('Формула прямоугольника 1b: ', round(rectangle_third_formula(a, b, vars, parts, function), 7))
    print('Формула трапеции: ', round(rectangle_trapetion_formula(a, b, vars, parts, function), 7))

main()
