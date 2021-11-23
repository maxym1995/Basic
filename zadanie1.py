import random

rows = random.randint(5,15)
columns = random.randint(5,15)
print(rows)
print(columns)

x = 0
while x < rows:
    stars = ''
    for c in range(rows):
    stars += '*'
    x += 1
print(stars)