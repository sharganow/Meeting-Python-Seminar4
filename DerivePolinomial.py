# B.
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import MakePolynomial as Mpl
import Randomizer as Cor
ident_print = 20

# import QuadraticEquation as Qe


def FillDictJournal() -> dict:
    while True:
        try:
            data = open(Mpl.journal, 'r')
            fl = data.read()  # fl file list
            data.close()
            if '.' in fl:
                fls = list()
                if '\n' in fl:
                    fls = list(fl.split('\n'))
                else:
                    # Одного файла не хватает, нужно его создать:
                    Mpl.save_to_file(Mpl.enter_filename(), Mpl.make_polinomial(Mpl.enter_digry_polynom()))
                    continue
            else:
                # В журнале файлов не обнаружилось
                # их нужно создать:
                for _ in range(2):
                    Mpl.save_to_file(Mpl.enter_filename(), Mpl.make_polinomial(Mpl.enter_digry_polynom()))
                continue
            dictFileEquat = dict()
            for f in fls:
                dictFileEquat[f] = GetEquationFromFile(f)
            break
        except:
            # data = open(Mpl.journal, 'a')
            # Здесь нужно реализовать создание файлов с полиномами
            # раз уж даже журнала не было:
            for _ in range(2):
                Mpl.save_to_file(Mpl.enter_filename(), Mpl.make_polinomial(Mpl.enter_digry_polynom()))
            # data.close()
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


def HelpToFindExistFile(short_name: str, source: dict) -> str:
    listSousce = list(source.keys())
    for file in listSousce:
        if short_name in file:
            return file
    else:
        return short_name


def AlignedPrint(start, indent, second) -> None:
    multiple = 0
    indent_str = '\t'  # эквивалентно четырём символам
    multiple = indent // 4 - len(str(start)) // 4
    indent_str *= multiple
    print('{}{}{}'.format(start, indent_str, second))


def MakeChoiceFile(source: dict, choiсe: dict) -> None:
    while True:
        try:
            file = input('Введите имя выбранного файла: ')
            file = HelpToFindExistFile(file, source)
            if file in source:
                choiсe[file] = source.pop(file)
                break
            else:
                print('Файла с таким именем в дирректории нет, требуется повтор')
        except:
            print('Вы делаете что-то не так, соберитесь')
    print('Исходный список файлов:')
    for item in source:
        AlignedPrint(item, ident_print, source[item][0])
    print('Список выбранных файлов:')
    for item in choiсe:
        AlignedPrint(item, ident_print, choiсe[item][0])


def get_dict_odd(item_equ: str) -> list:
    if '*x**' in item_equ:
        item_equ = item_equ.replace('*x**', ' ').split(' ')
        return [item_equ[1], int(item_equ[0])]
    elif item_equ[0] != '-' and item_equ.isnumeric():
        return ['0', int(item_equ)]
    elif item_equ[0] == '-' and item_equ[1:].isnumeric():
        return ['0', int(item_equ)]
    else:
        print('Выражение не соответствует установленному формату')
        return ['0', 0]


def MakeOddsFromEquation(eqtn: str) -> dict:
    oddsf = dict()
    eqtn = eqtn.strip().lower()
    if ' ' in eqtn:
        eqtn = eqtn.replace(' ', '')
    if '=0' in eqtn:
        eqtn = eqtn.replace('=0', '')
    if '+' in eqtn:
        eqtn = eqtn.replace('+', ' ')
    if '-' in eqtn:
        eqtn = eqtn.replace('-', ' -')
    eqtn = eqtn.strip().split(' ')
    lst = list()
    for i in eqtn:
        lst = get_dict_odd(i)
        oddsf[lst[0]] = lst[1]
    return oddsf


def UniteTwoOdds(odd1: dict, odd2: dict) -> dict:
    twoOdds = dict()
    lstOdd1 = list(odd1.keys())
    lstOdd2 = list(odd2.keys())
    for i in lstOdd1:
        if i in lstOdd2:
            twoOdds[i] = odd1.get(i) + odd2.get(i)
            del (lstOdd2[lstOdd2.index(i)])
        else:
            twoOdds[i] = odd1.get(i)
    for i in lstOdd2:
        twoOdds[i] = odd2.get(i)
    return twoOdds


def MakeEquation(odd: dict) -> str:
    newEq = str()
    lstOdd = list(odd.keys())
    lstOdd.sort(reverse=True)    # lstOdd.reverse()
    for i in lstOdd:
        if i != '0':
            if odd.get(i) > 0:
                newEq += ' + ' + str(odd.pop(i)) + '*x**' + i
            elif odd.get(i) < 0:
                newEq += ' ' + str(odd.pop(i)) + '*x**' + i
            else:
                odd.pop(i)
        else:
            if odd.get(i) > 0:
                newEq += ' + ' + str(odd.pop(i)) + ' = 0'
            elif odd.get(i) < 0:
                newEq += ' ' + str(odd.pop(i)) + ' = 0'
            else:
                odd.pop(i)
    newEq = newEq.strip()
    if newEq.startswith('+ '):
        newEq = newEq[2:]
    return newEq


choiсeDct = dict()
dct = FillDictJournal()
for item in dct:
    AlignedPrint(item, ident_print, dct[item][0])
print('\nДля создания нового полинома из списка имеющихся '
      'выберите слагаемые полиномы из списка выше по имени файла\n')
MakeChoiceFile(dct, choiсeDct)
print('\nВыберите второй слагаемый полином из списка\n')
MakeChoiceFile(dct, choiсeDct)
print('По результату сложения двух выбранных полиномов - для нового  ', end='')
fileUnionEquation = Mpl.enter_filename()

lstChDct = list(choiсeDct.keys())
dctEqn1 = MakeOddsFromEquation(choiсeDct.get(lstChDct[0])[0])
dctEqn2 = MakeOddsFromEquation(choiсeDct[lstChDct[1]][0])
untEqn = UniteTwoOdds(dctEqn1, dctEqn2)
newEquation = MakeEquation(untEqn)
Mpl.save_to_file(fileUnionEquation, newEquation)
AlignedPrint(fileUnionEquation, ident_print, newEquation)
