class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update_x(self, new_x):  # to update X
        self.x = new_x

    def update_y(self, new_y):  # to update Y
        self.y = new_y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return self.x + other.x and self.y + other.y  # point(self.x + other and self.y + other)


p1 = point(10, 20)
p2 = point(0, 0)

print("P1 :", p1.x, p1.y)
print("P2 :", p2.x, p2.y)

p2.update_x(10)
p2.update_y(20)

print("P1 = P2 :", p1 == p2)  # p1.__eq__(p2)
print("P1 + P2 :", p1.x + p2.x, p1.y + p2.y)
