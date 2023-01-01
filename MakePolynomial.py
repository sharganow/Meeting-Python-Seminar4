# A.
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

# P.S. данную задачу я дополнил фукцией ведения журнала сформированных файлов для облегчения поиска последних
#       Файл с функциями используется как библиотека для второй задачи, для проверки этой задачи нужно разком-
#       ментировать последнюю строку №123

journal = 'journal.pln'


def enter_filename() -> str:
    while True:
        try:
            file_name = input('Задайте имя файла для хранения полинома: ')
            file_name = file_name.lower()
            lst = file_name.split('.')
            if lst[0].isalnum():
                if len(lst) == 1:
                    file_name += '.pln'
                else:
                    file_name = lst[0] + '.pln'
                if file_name == journal:
                    print(f'Имя {file_name} занято, используйте иное')
                    continue
                else:
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
            degree = abs(degree)
            break
        except:
            print('Вводимое значение должно быть целым числом')
    return degree


def make_polinomial(dgr: int) -> str:
    import Randomizer as Cor
    strng = ''
    cnt_plnml = 0
    for d in range(dgr, -1, -1):
        k = Cor.RandInt(-100, 100)
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
    addFileNameToJournal(name)


def addFileNameToJournal(name: str) -> None:
    while True:
        try:
            data = open(journal, 'r')
            dt = data.read()
            if name in dt:
                data.close()
                return
            old = list()
            if '\n' in dt:
                old = list(dt.split('\n'))
            else:
                old.append(dt)
            data.close()
            break
        except:
            data = open(journal, 'a')
            data.write(name)
            data.close()
    with open(journal, 'w') as data:
        old.append(name)
        new = old[0]
        for i in range(1, len(old), 1):
            new += '\n' + old[i]
        data.write(new)


# save_to_file(enter_filename(), make_polinomial(enter_digry_polynom()))
