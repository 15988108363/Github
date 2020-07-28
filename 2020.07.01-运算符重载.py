class Vector:
    """向量"""
    def __init__(self,x):
        self.x = x
    def __str__(self):#输出给人看的格式
        return "横向量：%d"%(self.x)
    def __repr__(self):#打印，复制对象
        return "Vector(%d)"%(self.x)
    def __add__(self, other):
        return Vector(self.x +other)
    def __mul__(self, other):
        return Vector(self.x *other)
    def __pow__(self, power, modulo=None):
        return Vector(pow(self.x,power,2))
    def __iadd__(self, other):
        self.x += other
        return self#返回自身，调用Vector
    def __le__(self, other):
        return self.x <= other

v01 = Vector(12)
v02 = v01 +3
print(v02)
v03 = v02*5
print(v03)
v04 = pow(v03,2,2)
print(v04)
v01 += 1
print(v01)
v01.x += v03.x
print(v01)
print(v01 <= 12)