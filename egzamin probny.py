# zad 1
import random


def pierwsza_litera(zdanie):
    zdanie = zdanie.split(" ")

    result = []
    for z in range(len(zdanie)):
        a = zdanie[z].upper()
        string = a[0]
        result.append(string)
    return "".join(result)

print(pierwsza_litera("Don't repeat yourself"))
print(pierwsza_litera("Read the fine manual"))
print(pierwsza_litera("All terrain armoured transport"))

#zad 2

names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]

def name_sorter(names):
    male = []
    female = []
    slownik = {}
    for n in names:
        if n.endswith("a"):
            female.append(n)
        else:
            male.append(n)
    male.sort()
    female.sort()
    slownik['male'] = male
    slownik['female'] = female
    return slownik

print(name_sorter(names))

#zad3

zdanie = 'Kobyła ma mały bok'

def palindrome(zdanie):
    zdanie = zdanie.lower()
    zdanie = zdanie.split(" ")
    a = "".join(zdanie)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False

print(palindrome(zdanie))

#zad 4

def div(a,b):
    lista = []
    for i in range(a,b+1):
        if (i % 2 == 0) and (i % 3 != 0):
            lista.append(i)
    return lista

print(div(0,20))

#zad 5

def roll (a, b =6, c = 0):
    import random
    suma_rzutow = 0
    if b not in (3,4,6,8,10,12,100) :
        info = 'no such dice'
        return print(info)
    else:

        for i in range(a):
            rzut = random.randint(1,b)
            suma_rzutow += rzut
            print('rzut',i+1,'= :',rzut)
    wynik = (suma_rzutow + c)
    return wynik


print(roll(2,6,-5))
