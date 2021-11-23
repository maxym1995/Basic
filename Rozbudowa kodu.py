# #Zad 1
# ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
#          'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
#
# tuplets = [(a,b) for a in ports for b in ports ]
# print(tuplets)
# print(len(tuplets))
#
# tuplets1 = [(a,b) for a in ports for b in ports if a != b]
# print(tuplets1)
# print(len(tuplets1))
#
# tuplets2 = [(a,b) for a in ports for b in ports if a > b]
# print(tuplets2)
# print(len(tuplets2))
#
# #zad 2 generator
#
# gen = ((a,b) for a in ports for b in ports if a > b)
#
# counter = 0
#
# for g in gen:
#     print(g)
#     counter = counter + 1
# print(counter)
#
# # ZAD 4 eval
# import math
# argument_list = []
# for i in range(0,100):
#     argument_list.append(i/10)
# print(argument_list)
# formula = input('podaj wzor')
# for x in argument_list:
#     result = eval(formula)
#     print(result)
#
# # np wzor : 2*x lub 3*x+5**3


# zad 3 EXEC

# import os
# files = os.getcwd()
# exec1 = 'exec1.py'
# exec2 = 'exec2.py'
# exec1_path = os.path.join(files,exec1)
# exec2_path = os.path.join(files,exec2)
# list = [exec1_path,exec2_path]
# print(list)
#
# for l in list:
#     with open(l,'r') as file:
#         source = file.read()
#         exec(source)


# zad 4 complie:

import math
import time

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []

for i in range(1000000):
    argument_list.append(i / 10)

for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    print("Calculation time: {}".format(stop - start))

#COMPLIED VERSION

for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))

    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()

    print("Calculation time: {}".format(stop - start))

