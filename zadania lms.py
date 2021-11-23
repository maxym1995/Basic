#Random average
import random
def random_average(n):
    values = []
    for a in range(n):
        num = random.randint(1,100)
        values.append(num)
    print(values)
    sum = 0
    for value in values:
        sum += value
    print(sum)
    average = sum/len(values)
    print(average)
    return average

# random_average(5)

#Div

def div():

    a = input('Please give me 1st number')
    b = input('Please give me 2nd number')
    try:
        dival = int(a)/int(b)
        print(dival)
    except ValueError and ZeroDivisionError:
        print('Incorect values entered')


#silnia


def silnia(n):
    a = 1
    for i in range(n):
        a *= i+1

    return a

print(silnia(5))



