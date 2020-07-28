"""
    迭代器
"""
class Skill:
    pass

class SkillIterator:
    def __init__(self,target,index=0):
        self.target = target
        self.index = 0
class SkillManager:
    def __init__(self,skills):
        self.skills = skills
    def __iter__(self):
        #创建迭代器对象 传递 需要迭代的对象
        """执行过程，1.调用__iter__()方法不执行，
        2.调用__next__()方法执行时，到yield语句暂时离开
        3.再次调用__next__()方法不执行，从上次离开的代码开始执行，到yield暂时离开
        4.待执行完方法体，抛出StopIteration异常
        """
        print("准备返回第一个元素")
        yield self.skills[1]
        print("准备返回第二个元素")
        yield self.skills[2]
        print("准备返回第三个元素")
        yield self.skills[3]

#======================客户端=============================
manager = SkillManager([Skill(),Skill(),Skill()])
#for item in manager.skills:
#for item in manager:#获取manager对象中聚合类型（列表）成员
#   print(item)
iterator = SkillManager("oui").__iter__()
while True:
    try:
        iterator = iterator.__next__()
        print(item)
    except StopIteration as e:
        print(e)
        break
