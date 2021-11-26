class Cake:
    def __init__(self,name, kind, taste, additives,filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling



cake_01 = Cake('sernik','przekladane','ser','rodzynki','')
cake_02 = Cake('brownie','placek','czekolada','orzechy','polewa_czekoladowa')
cake_03 = Cake('karpatka','przekladane','smietanka','mak','krem')

bakery_offer = []
bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)
print(bakery_offer)

for cake in bakery_offer:
    print(f'Today in our offer : {cake.name} main taste : {cake.kind}, with additives {cake.additives}, filled with {cake.filling}')
