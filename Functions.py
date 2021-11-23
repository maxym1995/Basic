# def show_progress (how_many, character='*'):
#     print(character*how_many)
#
#
# show_progress(10)
# show_progress(15)
# show_progress(10, '-')
# show_progress(15, '+')

#zad 2 ARGS, KWARGS

# def calculate_paint(efficiency_ltr_per_m2,*space):
#     return sum(space)*efficiency_ltr_per_m2
#
# print(calculate_paint(10,2,5))
#
# def log_it(*args):
#     import os
#     path = r'C:\Users\maxym\Desktop\Python\testowy_doc-kopia.txt'
#     os.path.isfile(path)
#     with open(path,'a') as file:
#         for line in args:
#             file.write(line)
#             file.write(" ")
#         file.write("\n")
#
# log_it('placek','mietek')
# log_it('jestem ten ktory jest essa')

#zad 3

# def double(x):
#     return 2 * x
# def root(x):
#     return x ** 2
# def negative(x):
#     return -x
# def div2(x):
#     return x / 2
# number = 8
# transformations = [double, root, div2, negative]
#
# print('Starting transformations')
# tmp_return_value = number
# for transformation in transformations:
#     tmp_return_value = transformation(tmp_return_value)
#     print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))

#zad 4 funkcja jako argument funkcji
#
# def double(x):
#     return 2 * x
# def square(x):
#     return x ** 2
# def negative(x):
#     return -x
# def div2(x):
#     return x / 2
#
# def generate_values(function, lista):
#     results = []
#     for l in lista:
#         results.append(function(l))
#     return results
#
# lista = list(range(11))
# print(lista)
# print(generate_values(negative,lista))

#ZAD 5 FUNKCJE ZWRACAJACE FUNKCJE

from datetime import datetime


def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]


def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]


def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))
print(end)


def create_function(span):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400

    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(sec)

    exec(source, globals())

    return f


f_minutes = create_function('m')
f_hours = create_function('h')
f_days = create_function('d')

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))