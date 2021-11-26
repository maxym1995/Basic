class Cake:
    bakery_offer = []
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']

    def __init__(self,name, kind, taste, additives,filling,):
        self.name = name

        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)


    def show_info(self):

        print((self.name).upper())
        print('KIND:',self.kind)
        if self.additives != '':
            print('Additives :',self.additives)
        if self.filling != '':
            print('Filled :',self.filling)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives = additives




cake_01 = Cake('sernik','przekladane','ser','rodzynki','')
cake_02 = Cake('brownie','placek','czekolada','orzechy','polewa_czekoladowa')
cake_03 = Cake('karpatka','przekladane','smietanka','mak','krem')

#
# for cake in self.bakery_offer:
#     print(f'Today in our offer : {cake.name} main taste : {cake.kind}, with additives {cake.additives}, filled with {cake.filling}')

# cake_01.show_info()
# cake_01.set_filling('serek_smietankowy')
# cake_01.show_info()
# cake_01.add_additives(['lukier','posypka','dzem'])
# cake_01.show_info()

cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')
cake_04.show_info()

for bake in Cake.bakery_offer:
    bake.show_info()

cake_05 = 123
print(isinstance(cake_03,(Cake)))
print(isinstance(cake_05,(Cake)))
print(dir(cake_01))
print(vars(Cake))