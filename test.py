cake_01 = {'taste': 'vanilia',
           'glaze': 'chocolade',
           'text': 'Happy Brithday',
           'weight': 0.7}

cake_02 = {'taste': 'tee',
           'glaze': 'lemon',
           'text': 'Happy Python Coding',
           'weight': 1.3}


def show_cake_info(a_cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        a_cake['taste'], a_cake['glaze'], a_cake['text'], a_cake['weight']))


cakes = [cake_01, cake_02]

for a_cake in cakes:
    show_cake_info(a_cake)


class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')

bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)

print("Today in our offer:")
for c in bakery_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(
        c.name, c.kind, c.taste, c.additives, c.filling))


class Cake:

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:    {}".format(self.kind))
        print("Taste:   {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')

bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)

cake02.set_filling('vanilla cream')
cake03.add_additives(['cocoa powder', 'coconuts'])

print("Today in our offer:")
for c in bakery_offer:
    c.show_info()