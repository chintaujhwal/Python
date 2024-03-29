class A:
    def process(self):
        print("Process in A")


class B(A):
    pass


class C:
    def process(self):
        print("Process in C")


class D(B, C):
    pass


obj = D()
obj.process()


print(D.__mro__)  # D --> B --> A --> C --> object

#  A
#  |
#  B               C
#  |               |
#   ---------------
#          |
#          D

