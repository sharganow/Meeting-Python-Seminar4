# B.
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import MakePolynomial as Mpl

Mpl.journal


def FillDictJournal(_: None) -> dict:
    while True:
        try:
            data = open(Mpl.journal, 'r')
            fl = data.read()        # fl file list
            if '.' in fl:
                fls = list()
                if '\n' in fl:
                    fls = list(fl.split('\n'))
                else:
                    fls.append(fl)
                    # Одного файла не хватает, нужно его создать
            else:
                # В журнале файлов не обнаружилось
                # их нужно создать
            dictFileEqua = dict()
            data.close()
            break
        except:
            data = open(Mpl.journal, 'a')
            # Здесь нужно реализовать создание файлов с полиномами
            # раз уж даже журнала не было
            data.close()


def GetEquationFromFile(name: str) -> list:
    while True:
        try:
            data = open(name, 'r')
            el = data.read()        # el equation list
            if el.count('='):
                eqs = list()
                if '\n' in el:
                    eqs = list(el.split('\n'))
                else:
                    eqs.append(el)
            else:
                # Полинома нет - нужно создать
            data.close()
            break
        except:
            data = open(name, 'a')
            # здесь тоже можно запустить процесс
            # генерации полинома в файле
            # раз уж даже файла небыло
            # data.write('0 = 0')
            data.close()
    return eqs
