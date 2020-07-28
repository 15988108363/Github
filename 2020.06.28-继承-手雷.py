
class Grendes:
    def __init__(self,atk,atk_scope):
        self.atk =atk
        self.atk_scope = atk_scope

class explosion_target:
    def __init__(self):
        print("我要爆炸了")

class person(explosion_target):
    def player(self):
        super().__init__()
        print("炸到我了")

i01 = Grendes(12,34)
e01 = explosion_target
p01 = person()
p01.player()
