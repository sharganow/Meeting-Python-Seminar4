# B.
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import MakePolynomial as Mpl

# import QuadraticEquation as Qe


def FillDictJournal() -> dict:
    while True:
        try:
            data = open(Mpl.journal, 'r')
            fl = data.read()  # fl file list
            if '.' in fl:
                fls = list()
                if '\n' in fl:
                    fls = list(fl.split('\n'))
                else:
                    fls.append(fl)
                    # Одного файла не хватает, нужно его создать:
                    Mpl.save_to_file(Mpl.enter_filename(), Mpl.make_polinomial(Mpl.enter_digry_polynom()))
            else:
                # В журнале файлов не обнаружилось
                # их нужно создать:
                for _ in range(2):
                    Mpl.save_to_file(Mpl.enter_filename(), Mpl.make_polinomial(Mpl.enter_digry_polynom()))
            dictFileEquat = dict()
            for f in fls:
                dictFileEquat[f] = GetEquationFromFile(f)
            data.close()
            break
        except:
            data = open(Mpl.journal, 'a')
            # Здесь нужно реализовать создание файлов с полиномами
            # раз уж даже журнала не было:
            for _ in range(2):
                Mpl.save_to_file(Mpl.enter_filename(), Mpl.make_polinomial(Mpl.enter_digry_polynom()))
            data.close()
    return dictFileEquat


def GetEquationFromFile(name: str) -> list:
    while True:
        try:
            data = open(name, 'r')
            el = data.read()  # el equation list
            if el.count('='):
                eqs = list()
                if '\n' in el:
                    eqs = list(el.split('\n'))
                else:
                    eqs.append(el)
            else:
                # Полинома нет - нужно создать
                data.close()
                eqs.append(Mpl.make_polinomial(Mpl.enter_digry_polynom()))
                with open(name, 'w') as data:
                    data.write(eqs[0])
                data = open(name, 'r')
            data.close()
            break
        except:
            data = open(name, 'a')
            # здесь тоже можно запустить процесс
            # генерации полинома в файле
            # раз уж даже файла небыло
            # data.write('0 = 0')
            data.write(Mpl.make_polinomial(Mpl.enter_digry_polynom()))
            data.close()
    return eqs


def MakeChoiceFile(source: dict, choiсe: dict) -> None:
    while True:
        try:
            file = input('Введите имя выбранного файла: ')
            if file in source:
                choiсe[file] = source.pop(file)
                break
            else:
                print('Фала с таким именем в дирректории нет, требуется повтор')
        except:
            print('Вы делаете что-то не так, соберитесь')
    print('Исходный список файлов:')
    for item in source:
        print('{}\t\t\t{}'.format(item, source[item][0]))
    print('Список выбранных файлов:')
    for item in choiсe:
        print('{}\t\t\t{}'.format(item, choiсe[item][0]))


choiсeDct = dict()
dct = FillDictJournal()
for item in dct:
    print('{}\t\t\t{}'.format(item, dct[item][0]))
print('\nДля создания нового полинома из списка имеющихся '
      'выберите слагаемые полиномы из списка выше по имени файла\n')
MakeChoiceFile(dct, choiсeDct)
print('\nВыберите второй слагаемый полином из списка\n')
MakeChoiceFile(dct, choiсeDct)
