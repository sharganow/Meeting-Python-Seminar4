# A.
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def enter_filename() -> str:
    while True:
        try:
            file_name = input('Задайте имя файла для хранения полинома: ')
            file_name.lower()
            lst = file_name.split('.')
            if lst[0].isalnum():
                if len(lst) == 1:
                    file_name += '.pln'
                else:
                    file_name = lst[0] + '.pln'
                break
            else:
                print('Имя файла содержит недопустимые символы')
                continue
        except:
            print('Повторите попытку')
    return file_name


def enter_digry_polynom() -> int:
    while True:
        try:
            degree = int(input('Введите старшую степень создаваемого полинома: '))
            break
        except:
            print('Вводимое значение должно быть целым числом')
    return degree


def make_polinomial(dgr: int) -> str:
    import random
    strng = ''
    cnt_plnml = 0
    for d in range(dgr, -1, -1):
        k = random.randint(-100, 100)
        if k:
            if d:
                strng += f' {k}*x**{d} '
                cnt_plnml += 1
            else:
                if cnt_plnml:
                    strng += f' {k} = 0'
                else:
                    strng += ' 0 = 0'
                    # print('Исключение 1')
        else:
            if not d:
                if cnt_plnml:
                    strng += '= 0'
                    # print('Исключение 2')
                else:
                    strng += '0 = 0'
                    # print('Исключение 3')
    return strng.replace(' 1*x', ' x').replace('-1*x', '-x').strip().replace('  -', ' - ').replace('  ', ' + ')


def save_to_file(name: str, polinom: str) -> None:
    while True:
        try:
            data = open(name, 'r')
            old = data.read()
            if len(old):
                old += '\n'
            data.close()
            break
        except:
            data = open(name, 'a')
            data.close()
    with open(name, 'w') as data:
        data.write(old + polinom)


save_to_file(enter_filename(), make_polinomial(enter_digry_polynom()))
# print(make_polinomial(enter_digry_polynom()))
