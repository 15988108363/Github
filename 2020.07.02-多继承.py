class A:
    def m(self):
        print("a--m")
class B(A):
    def m(self):
        print("b--m")
class C(A):
    def m(self):
        super().m()
        print("c--m")
#===============================================
class D(B,C):#由左至右
    def m(self):
        super().m()#从左到右依次调用用
        print("d--m")
class E(C,B):#由左至右
    def m(self):
        super().m()
        print("d--m")
class F(C,B):
    def m(self):
        super().m()
        B.m(self)
        print("f--m")
#===============================================
d01 =D()
d01.m()
print(D.mro())
print("="*10)

e01 = E()
e01.m()
print("="*10)

f01 = F()
f01.m()