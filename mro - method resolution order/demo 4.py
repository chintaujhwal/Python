class A:
    def process(self):
        print("Process in A")


class B:
    def process(self):
        print("Process in B")


class C(A, B):
    def process(self):
        print("Process in C")


class D(C, B):
    pass


obj = D()
obj.process()

print(D.__mro__)  # D --> C --> A --> B --> object

#    A               B
#    |               |
#     ---------------|
#            |       |
#            C       |
#            |       |
#             -------
#                |
#                D
