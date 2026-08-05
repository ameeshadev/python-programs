# constructor overriding
class A:
    def __init__(self, value):
        self.value = value

    def m1(self):
        print(10)

class B(A):
    def m1(self):
        print(20)

class C(B):
    def m1(self):
        print(30)

obj = C()
obj.m1()
