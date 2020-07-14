
class A:
    def func(self):
        print('a')

class B(A):
    def func(self):
        super().func()
        print('b')

class C(B):
    def func(self):
        super().func()
        print('c')

class D(B,C):
    def func(self):
        super().func()
        print('d')

D().func()