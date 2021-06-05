my_list = [1, 2, 3]

for i in my_list:
    print(i)

iterator = my_list.__iter__()
print(type(iterator))


class Shop:
    def __init__(self, products: list):
        self.products = products
    def __iter__(self):
        return ShopIterator()

class ShopIterator:
    products = ['apples', 'milk']
    def __init__(self, products: list):
        self.products = products
    def __iter__(self):
        return self
    def __next__(self):
        if not self.products:
            raise StopIteration
        return self.products.pop()

shop = Shop(['books'])
print('From constructor:', shop.products)
shop_iter = shop.__iter__()
print('First element:', shop_iter.__next__())
print('Second element:', shop_iter.__next__())
print('Third element:', shop_iter.__next__())