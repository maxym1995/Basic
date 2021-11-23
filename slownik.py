slownik = {
    'Google' : 1480,
    'Email' : 300,
    'Trafic' : 440,
    'TV_Spot' : 700}

print(slownik['Email'])

slownik_updated = {
    "Trafic" : 520,
    "News" : 600
}

slownik.update(slownik_updated)
print(slownik.keys())
print(slownik.values())
del slownik['Email']
print(slownik)
slownik['Nowka'] = 14
print(slownik)

# colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# figures = [
#     {'Figure': 'Ace', 'Power': 14},
#     {'Figure': 'King', 'Power': 13},
#     {'Figure': 'Queen', 'Power': 12},
#     {'Figure': 'Jack', 'Power': 11},
#     {'Figure': '10', 'Power': 10},
#     {'Figure': '9', 'Power': 9}]
#
# for f in figures:
#     aCard = f.copy()
#     print(aCard)
#     # aCard['Color'] = c
#     # allCards.append(aCard)
