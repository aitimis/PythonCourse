shop1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20}
shop2 = {'mere': 11, 'pere': 15, 'prune': 6}
shop3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}
need_to_buy = {'mere': 2, 'pere': 3, 'prune': 6}
available_shops= {'profi': shop1  , 'kauf':shop2 , 'lidl':shop3}
class BestBuy():
    shops=dict()
    def __init__(self):
        pass
    def add_shop(self,shop,shop_name):
        self.shops.update({shop_name:shop})
    def best_buy(self, cart: dict):
        total = {}
        smallest_cost = None
        _best_buy = ''
        for product, quanty in cart.items():
            # print(product, quanty)
            for shop_name, shop_products in self.shops.items():
                #print(shop_name, shop_products)
                price = shop_products.get(product)
                # print(product, quanty, price)
                cost = quanty * price
                # print(shop_name, product, cost)
                saved_cost = total.get(shop_name, 0)
                new_saved_cost = saved_cost + cost
                total[shop_name] = new_saved_cost
        for shop_name,total_cost in total.items():
            if smallest_cost is None  or smallest_cost > total_cost  :
                smallest_cost=total_cost
                _best_buy = shop_name
        print(smallest_cost , _best_buy)

best_buy=BestBuy()
best_buy.add_shop(shop2,'lidl')
best_buy.best_buy(cart=need_to_buy)
best_buy.add_shop(shop1,'profi')
best_buy.best_buy(cart=need_to_buy)
print(best_buy.shops)
print(__name__)