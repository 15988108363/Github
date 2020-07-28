class Weapon:#武器类
    def __init__(self):
        print("我是一种武器")
    def Date(self,kind,atk):
        self.kind = kind
        self.atk =atk
        print("%s的攻击力有了"%self.kind)
    def Action(self,price,attack):
        self.price = price
        self.attack = attack
        print("%s的价格是：%s" % (self.kind,self.price))
        print("%s要攻击你了"%self.kind)#调用实力变量self。kind

class Gun(Weapon):
    """子类构造函数，不调用父类"""
    def __init__(self):#覆写父类方法
        pass
    def Date(self,atk,atk_speed):
        super().Date("手枪",atk)
        self.atk_speed = atk_speed
        self.powder = self.atk * self.atk_speed
        print("每秒攻击力:%d"%self.powder)

class Grenade(Weapon):#无覆写父类方法，会出现父类__init__
    """子类不构造函数，自动调用父类"""
    def Date(self,atk,atk_scope):
        super().Date("手雷",atk)
        self.atk_scope= atk_scope
        print("攻击范围：%d"%self.atk_scope)

w01 = Weapon()
w01.Date("武器",123)
w01.Action(244,21)

g01 =Gun()
g01.Date(1221,12)
g01.Action(2121,122)

G01 = Grenade()
G01.Date(1221,32)
G01.Action(1221,21)