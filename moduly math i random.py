import math

mala_pizza_r = 0.22
srednia_pizza_r = 0.27
duza_pizza_r = 0.38

mala_pizza_price = 11.50
srednia_pizza_price = 15.60
duza_pizza_price = 22.00

mala_area = math.pi * mala_pizza_r ** 2
srednia_area = math.pi * srednia_pizza_r ** 2
duza_area = math.pi * duza_pizza_r ** 2

print('mala', mala_pizza_r, mala_pizza_price, mala_area)
print('srednia', srednia_pizza_r, srednia_pizza_price, srednia_area)
print('duza', duza_pizza_r, duza_pizza_price, duza_area)
print('')
print('mala', mala_pizza_price / mala_area)
print('srednia', srednia_pizza_price / srednia_area)
print('duza', duza_pizza_price / duza_area)
print('')

# modul random

import random

nr1 = random.randint(1,100)
nr2 = random.randint(1,100)
counter = 1
print("numer 1 to {} a numer 2 {} to ".format(nr1,nr2))

while nr1 != nr2:
    counter += 1
    nr2 = random.randint(1,100)
    print('Przy probie {} wylosowano liczbe {}'.format(counter,nr2))

# grupy na MS

import random
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
numer_grupy = 0

for n in range (len(countries)):
    if n % 4 == 0:
        numer_grupy += 1
        print('-----------GRUPA {}------------'.format(numer_grupy))
    print(countries[n])

#zadanie z rzutem kostka

print('-----------RZUCANIE KOSTKA ------------')

import random

min = 1
max = 6
dice = random.randint(1,6)

if dice == 1:
    print('   ')
    print(' o ')
    print('   ')
elif dice == 2:
    print('  o')
    print('   ')
    print('o  ')
elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')

print('----------------------')

#RZUT 5 KOSTKAMI

dices = []

for d in range (5):
    dice = random.randint(1,6)
    dices.append(dice)

dices.sort()
print(dices)