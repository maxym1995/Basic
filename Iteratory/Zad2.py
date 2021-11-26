import time


class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __getitem__(self, item):
        if item > len(self.products) * len(self.promotions) * len(self.customers):
            raise StopIteration
        else:
            pos_products = item / (len(self.promotions) * len(self.customers))
            item = item % (len(self.promotions)* len(self.customers))
            pos_promotions = item / len(self.customers)
            item = item % len(self.customers)
            pos_customers = item
            return f'{self.products[int(pos_products)]}, {self.promotions[int(pos_promotions)]}, {self.customers[int(pos_customers)]}'


products = ["Product {}".format(i) for i in range(1, 500)]
promotions = ["Promotion {}".format(i) for i in range(1, 50)]
customers = ['Customer {}'.format(i) for i in range(1, 500)]

combinations = Combinations(products, promotions, customers)

m = iter(combinations)
print(next(m))
print(next(m))

for c in combinations:
    pass

time.sleep(10)