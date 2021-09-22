class product:

    def __init__(self):
        self.id = 1


p = product()  # "p" is an object of class "product"

p.name = "Nike Air Max"  # Object attributes
p.type = "Shoe"
p.price = 19000

print(p.__dict__)  # {'id': 1, 'name': 'Nike Air Max', 'type': 'Shoe', 'price': 19000}

#  pre-defined methods to manipulate attributes of class or object.

getattr(p, "name")  # Nike Air Max
hasattr(p, "type")  # True
setattr(p, "name", "Nike Jordan")  # p.name : "Nike Air Max" --> "Nike Jordan"
delattr(p, "price")  # removes attribute "price" from object "p"

print(p.__dict__)  # {'id': 1, 'name': 'Nike Jordan', 'type': 'Shoe'}
