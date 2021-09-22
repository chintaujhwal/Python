class A:
    def process(self):
        print('Process in A')
        #  print(type(self))


class B:
    def process(self):
        print('Process in B')
        #  print(type(self))


class C(A, B):
    def process(self):
        A.process(self)  # to call both process's
        B.process(self)


obj = C()
obj.process()

print(C.__mro__)  # C --> A --> B --> object

#  A               B
#  |               |
#   ---------------
#          |
#          C
