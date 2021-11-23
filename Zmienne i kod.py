# def Display_Options(n):
#     for i in range(len(options)):
#         print(i+1,' - ',options[i])
#     choice = input("Select above option or press exit:")
#     return choice
#
# choice = 'x'
# options = ['load data','export data','analyze & predict']
#
# while choice :
#     choice = Display_Options(options)
#     if choice:
#         try:
#             choice_num = int(choice) - 1
#             if choice_num >= 0 and choice_num < len(options):
#                 print("you have selected {} - {}".format(choice_num + 1, options[choice_num]))
#             else:
#                 print("choose a value from a list or press enter")
#         except:
#             print("You need to enter a number")
#     else:
#         print('----- END -----')
#

#ZAD2


path = r'C:\Users\maxym\Desktop\cwiczenie\zadanko.txt'

def sprawdzenie(sciezka):
    with open(sciezka,'r') as file:
        content = file.read()
        word_count = len(content.split())
    return word_count

print(sprawdzenie(path))

price = 123
bonus = 23
bonus_granted = True

# if bonus_granted:
#     price -= bonus
#
# print(price)

price = (price-bonus) if bonus_granted else price
print(price)

rating = 5
#
# if rating == 5:
#     print('very good')
# elif rating == 4:
#     print('good')
# else:
#     print('weak')

rating = 'very good' if rating == 5 else 'good' if rating == 4 else 'weak'
print(rating)

#zad 3

colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def wykres(kolory,n):
    return kolory[:n]
colors2 = []

for c in range(len(colors)):
    print(wykres(colors,c))

napis = '''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.
'''

napis = napis.split()
print(napis)
napis = napis[1:12]
napis = " ".join(napis)
print(napis)

definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '

print(definition[definition.index('(') + 1:definition.index(')')])

#ENNUMERATE I ZIP

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p,l in zip(projects,leaders):
    print(f'The leader of {p} is {l}')

for i,(d,p,l,) in enumerate(zip(dates,projects,leaders)):
    print(f'{i} - The leader of {p} started {d} is {l}')

#ITERACJA PO SLOWNIKU

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
values = []
for i in range(len(banknotes_coins)):
    values.append(0)
# print(values)

dict_denominations = dict(zip(banknotes_coins,values))
print(dict_denominations)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for v in sorted(dict_denominations.keys()):
    print('Denominate',v,'-amount :',dict_denominations[v])