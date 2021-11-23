# cake_01_taste = 'vanilia'
# cake_01_glaze = 'chocolade'
# cake_01_text = 'Happy Brithday'
# cake_01_weight = 0.7
#
# cake_02_taste = 'tee'
# cake_02_glaze = 'lemon'
# cake_02_text = 'Happy Python Coding'
# cake_02_weight = 1.3
#
#
# def show_cake_info(taste, glaze, text, weight):
#     print('{} cake with {} glaze with text "{}" of {} kg'.format(
#         taste, glaze, text, weight))
#
#
# show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
# show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)
#
# #Zadanie 1 - uproszczenie bez klasy
#
# cake_01 = {
# 'taste' : 'vanilia',
# 'glaze' : 'chocolade',
# 'text' : 'Happy Brithday',
# 'weight' : 0.7}
#
# cake_02 = {
# 'taste' : 'tee',
# 'glaze' : 'lemon',
# 'text' : 'Happy Python Coding',
# 'weight' : 1.3
# }
#
#
# def show_cake_info(a_cake):
#     print('{} cake with {} glaze with text "{}" of {} kg'.format(
#         a_cake['taste'], a_cake['glaze'], a_cake['text'], a_cake['weight']))
#
#
# cakes = [cake_01, cake_02]
#
# for a_cake in cakes:
#     show_cake_info(a_cake)
#
# #Zadanie 2

import pickle

class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free,text):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text =='':
            self.__text = text
        else:
            self.__text = ''
            print('Text can be set only for cake ({})'.format(name))


    #zadanie 3
    def show_info(self):
        print((self.name).upper())
        print('Kind: ',self.taste)
        if len(self.additives) > 0 :
            print("Additives: ",self.additives)
        if len(self.filling) > 0 :
            print('Filled: ',self.filling)
        print('Gluten free :',self.__gluten_free)
        print('Text :',self.__text)
        print('*'*20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self, text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    def save_to_file(self,path):
        with open(path,'wb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

cake_01 = Cake('Karpatka', 'tort','smietanka',[],'krem','','wesloych_urodzin')
cake_02 = Cake('Makowiec','cake','mak','orzechy','rodzynki',False,'Happy_18')
cake_03 = Cake('Brownie','placek','czekolada','platki_czekolady','powidla',False,'najleszego_w_imieniny')



cake_01.show_info()
# cake_02.show_info()
cake_01.set_filling('karmel')
cake_01.show_info()
# cake_01.add_additives('lizak')

cake_01.add_additives(['cukier_puder','kruszonka'])
cake_01.show_info()
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa',True,'')
cake_04.show_info()
print(isinstance(cake_01,Cake))
print(vars(cake_01), dir(cake_01))
cake_05 = Cake('Serniczek','biszkopt','ser','mak','rodzynki',True,'')
print(cake_05)
print(dir(cake_03))
cake_05._Cake__gluten_free = False
cake_05.show_info()
# print(bakery_offer)
for c in Cake.bakery_offer:
    c.show_info()

