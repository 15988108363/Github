__doc__ = "学生模型"
class StudentModel:
    """学生数据模型"""
    def __init__(self, id=0, name="", age=0, score=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score
    def __str__(self):
        return "编号:%s,姓名:%s,年龄:%d,成绩:%0.2f"%(self.id,self.name,self.age,self.score)
    def __repr__(self):
        return 'StudentModel(%s,%s,%d,%0.2f)'%(self.id,self.name,self.age,self.score)
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @id.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @id.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @id.setter
    def score(self, value):
        self.__score = value