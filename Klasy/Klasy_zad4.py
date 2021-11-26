class Cake:
    bakery_offer = []
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']

    def __init__(self,name, kind, taste, additives,filling,gluten_free):
        self.name = name

        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free

    def show_info(self):

        print((self.name).upper())
        print('KIND:',self.kind)
        if self.additives != '':
            print('Additives :',self.additives)
        if self.filling != '':
            print('Filled :',self.filling)
        print('Gluten Free :',self.__gluten_free)
    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives = additives


cake_01 = Cake('sernik','przekladane','ser','rodzynki','',True)
cake_01.__gluten_free = False # to doda nowy obiekt klasy
cake_01._Cake__gluten_free = False  # to pozwala modyfikowac ukryty obiekt klasy
cake_02 = Cake('brownie','placek','czekolada','orzechy','polewa_czekoladowa',True)
cake_03 = Cake('karpatka','przekladane','smietanka','mak','krem',False)


# cake_01.show_info()
# cake_01.set_filling('serek_smietankowy')
# cake_01.show_info()
# cake_01.add_additives(['lukier','posypka','dzem'])
# cake_01.show_info()

# cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa',True)
# cake_04.show_info()

for bake in Cake.bakery_offer:
    bake.show_info()

print(dir(Cake))
print(vars(cake_01))

