import random
colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []

for c in colors:
    for f in figures:
        new_value = c + f
        allCards.append(new_value)
print(allCards)
player1 = []
player2 = []
random.shuffle(allCards)
max = len(allCards)
print(allCards)
i = 0
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print(player1)
print(player2)
print("2 sposob rozdania kart")
player1 = []
player2 = []
player1.append(allCards[:12])
player2.append(allCards[12:])
print(player1,player2)