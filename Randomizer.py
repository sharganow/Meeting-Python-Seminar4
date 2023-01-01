# ЕЩЕ ОДНО НЕОБЯЗАТЕЛЬНОЕ ДЗ - НАПИСАТЬ СВОЙ РАНДОМАЙЗЕР (НЕ ИСПОЛЬЗОВАТЬ БИБЛИОТЕКУ RANDOM)

import textwrap
import time
import math

ident_print = 20


def AlignedPrint(start, indent, second) -> None:
    multiple = 0
    indent_str = '\t'  # эквивалентно четырём символам
    multiple = indent // 4 - len(str(start)) // 4
    indent_str *= multiple
    print('{}{}{}'.format(start, indent_str, second))


def GetNumSigns(value: int) -> int:
    value = value if value > 0 else -value
    gns = 0
    while value > 0:
        value //= 10
        gns += 1
    return gns


def GetRandStr() -> str:
    ter = list(str(time.perf_counter()).split('.'))
    while len(ter[1]) < 7:
        ter[1] += '0'
    # AlignedPrint(ter[0], ident_print, ter[1])
    return ter[1]


def GetRandChar() -> str:
    one_chr = GetRandStr()
    return one_chr[-1]


def GetRandSign(limit: int) -> int:
    getSign = round((int(GetRandChar()) * limit) / 9)
    return limit - 1 if getSign >= limit else getSign


def RandInt(start: int, stop: int) -> int:
    start, stop = (stop, start) if start > stop else (start, stop)
    delta = stop - start
    if delta == 0:
        return start
    numSignDelta = GetNumSigns(delta)
    randStr = GetRandStr()
    while numSignDelta > len(randStr):
        randStr += GetRandChar()
    else:
        randStr = randStr[-numSignDelta:]

    strtLst = list(randStr)
    randLst = list()
    # print(*strtLst)
    while len(strtLst):
        randLst.append(strtLst.pop(GetRandSign(len(strtLst))))
    # strtLst = randLst.copy()
    # strtLst.sort()
    semiRand = int(''.join(randLst))
    limitRand = int('9' * numSignDelta)
    # AlignedPrint(semiRand, ident_print, limitRand)
    # AlignedPrint(strtLst, ident_print, randLst)
    deltaRand = round((delta * semiRand) / limitRand)
    return start + deltaRand


# print(f'Сгенерировано случайное число: {RandInt(100, -100)}')


#
# available_clocks = [
#     ('monotonic', time.monotonic),
#     ('perf_counter', time.perf_counter),
#     ('process_time', time.process_time),
#     ('time', time.time),
# ]
#
# for clock_name, func in available_clocks:
#     info = time.get_clock_info(clock_name)
#     rez = textwrap.dedent(f'''\
#     {clock_name}:
#         adjustable    : {info.adjustable}
#         implementation: {info.implementation}
#         monotonic     : {info.monotonic}
#         resolution    : {info.resolution}
#         current       : {func()}
#     ''')
#     print(rez)
#
# print(time.monotonic())
# print(time.perf_counter())
# print(time.process_time())
# print(time.time())
#
# for _ in range(1000):
#     ter = time.perf_counter()
#     nic = time.monotonic()                  # для генератора случайных чисел не подходит
#     time.sleep(1 / (10000 + _))
#     AlignedPrint(nic, ident_print, ter)
#     # print(type(ter))
