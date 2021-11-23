def validate_pesel(pesel):

    if type(pesel) != int:
        return False

    pesel = str(pesel)
    if len(pesel) != 11:
        return False

    list_pesel = []
    for i in range(10):
        a = pesel[i]
        # print(a)
        a = int(a)
        list_pesel.append(a)
    # print(list_pesel)
    wagi = [1,3,7,9,1,3,7,9,1,3]

    suma = 0
    for l in range(10):
        iloczyn = wagi[l]*list_pesel[l]
        suma += iloczyn
    # print(suma)
    iloraz = suma % 10
    print(iloraz)
    roznica = 10 - iloraz
    # print(roznica)
    if roznica == int(pesel[10]):
        return True
    else:
        return False
print(validate_pesel(99999999999))




lista = []





