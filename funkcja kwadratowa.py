

str_a = int(input('podaj a'))
str_b = int(input('podaj b'))
str_c = int(input('podaj c'))

if str_a == 0:
    print('to nie jest rownanie kwadratowe')
else:
    delta = (str_b**2) - (4*(str_a*str_c))
    if delta < 0:
        print('brak rozwiazan')

    elif delta == 0:
        x0 = -str_b/2*str_a
        print(f'miejsce zerowe wynosi {x0}')

    elif delta > 0:
        x1 = ((-str_b) - (delta**0.5)) / (2*str_a)
        x2 = ((-str_b) + (delta**0.5)) / (2*str_a)
        print(f'miejca zerowe {x1} oraz  {x2}')
