class ImpactEffect:
    """影响效果，隔离技能释放器 与具体的影响效果"""
    def impact(self):
        raise NotImplementError()#强制子类必须有父类此方法，否则报错

class LowerDefense(ImpactEffect):
    """降低伤害"""
    def __init__(self,distaance,ratio):#降低防御力，比例距离
        self.distance = distaance
        self.ratio = ratio
    def impact(self):
        print("降低%d米内，目标%0.2f防御力"%(self.distance,self.ratio))

class LowerSpeed(ImpactEffect):
    """降低速度"""
    def __init__(self,distaance,ratio,time):#降低速度，比例距离
        self.distance = distaance
        self.ratio = ratio
        self.time = time
    def impact(self):
        print("降低%d米内，%d秒内目标%.2f速度"%(self.distance,self.time,self.ratio))

class Damage(ImpactEffect):
    """伤害生命"""
    def __init__(self,value):#降低伤害
        self.value = value
    def impact(self):
        print("伤害%d值生命"%(self.value))

class SkillDeployer:
    """技能释放器"""
    def __init__(self,name):
        #配置释放器，储存当前技能具有的所有的影响效果的对象
        self.name = name
        self.__list_impact = self.__config_deployer()
    def __config_deployer(self):
        """配置释放器
        return
        """
        #*.定义配置
        #1.读取相应的影响效果
        #2.创建影响效果对象
        dict_skill_config = {
        "韦陀杵":["LowerDefense(12,75)","Damage(100)"],
        "降龙十八掌":["LowerSpeed(3,24,3)", "Damage(80)"],
        }
        list_impact_name = dict_skill_config[self.name]#根据将（技能名）获取值（影响效果列表）
        #list_impact = []
        #for item in list_impact_name:
        #   list_impact.append(eval(item))     eval镜像对象创建影响对象，并加入到列表中
        #list_impact = [eval(item) for item in list_impact_name]
        return [eval(item) for item in list_impact_name]#列表推导式
    def generate_skill(self):
        """生成技能
        return
        """
        print(self.name+"释放了")
        #执行所有影响效果
        for item in self.__list_impact:
            #编码期间，认为调用的是影响效果（父类ImpactEffect)
            #运行期间，由于创建的是子类对象（伤害生命Damage...），所以执行的是子类
            item.impact()#调用各类impact
#_________________________测试程序__________________________________________
#创建技能对象
wei_tuo_chu = SkillDeployer("韦陀杵")
wei_tuo_chu.generate_skill()#释放对象
xiang_long = SkillDeployer("降龙十八掌")
xiang_long.generate_skill()