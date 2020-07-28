class Skill:
    def __init__(self,code,name,cooling_time,atk,mana_cost):
        self.code = code
        self.name = name
        self.cooling_time = cooling_time
        self.atk = atk
        self.mana_cost = mana_cost
    def __str__(self):
        return "%d---%s---%d---%d---%d"%(self.code,self.name,self.cooling_time,self.atk,self.mana_cost)
    def __repr__(self):
        return "self.code,self.name,self.cooling_time,self.atk,self.mana_cost"
    @staticmethod
    def first(target,func_condition):
        for item in target:
            if func_condition(item):
                yield item
#——————————————————————————————————————————————————————————————————————————————————
def get_skill(target):
    for item in target:
        if item.code >= 102:
            yield (item.code,item.name,item.cooling_time,item.atk,item.mana_cost)
def get_skill02(target):
    for item in target:
        if item.code >= 102:
            yield item
#-------------------------------------------------------
list02 = []
list03 = []
skill_list = [Skill(100,"太上无极",30,100,40),
              Skill(101,"无边魔域",50,90,50),
              Skill(102,"爆炎术",20,180,50),
              Skill(103,"睡虎三刀",40,190,60),
              Skill(104,"虚空刺",50,130,70),
              ]
iter01 = get_skill(skill_list)
for item in iter01:
    list02.append(item)
print(list02)
iter02 = get_skill(skill_list)
for item in iter02:
    list03.append(item)
print(list03)
s01 = Skill(100,"太上无极",30,100,40)
print(s01)
#====================改进版-生成器=========================
iter01 = get_skill(skill_list)
list04 = (item for item in iter01)#节约内存
print(list04)
for i in list04:
    print(i)
#======================================================
print("="*40)
item = Skill.first(skill_list,lambda item:item.code>101)
for i in item:
    print(i)