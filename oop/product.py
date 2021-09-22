class product:
    tax = 0.12  # Static Variable

    @staticmethod
    def update_tax(new_rate):  # Static Method
        product.tax = new_rate

    def __init__(self, name, price, qoh):
        self.name = name
        self.price = price
        self.qoh = qoh

    def purchase(self, qty):
        self.qoh += qty

    def sell(self, qty):
        self.qoh -= qty

    @property
    def net(self):
        return self.price + self.price * product.tax


p1 = product("S20 Ultra", 1399, 10)
p2 = product("S20+", 1199, 20)
p3 = product("S20", 999, 25)

p1.purchase(10)  # --> quantity of p1 + 10
p1.sell(5)       # --> quantity of p1 - 5
print(p1.net)    # --> price of p1 + TAX
