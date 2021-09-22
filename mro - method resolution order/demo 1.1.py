class A:
    def process(self):
        print('Process in A')
        #  print(type(self))


class B:
    def process(self):
        print('Process in B')
        #  print(type(self))


class C(A, B):
    pass


obj = C()
obj.process()

print(C.__mro__)  # C --> A --> B --> object

#  A               B
#  |               |
#   ---------------
#          |
#          C
