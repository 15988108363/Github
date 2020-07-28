__doc__ ="业务逻辑层"

class StudentManagerController:
    def __init__(self, ):
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu

    def generate_id(self): # **kwargs
        # 生成编号
        if len(self.__list_stu) > 0:
            id = self.__list_stu[-1].id + 1
        else:
            id = 1
        return id
        #return self.__list_stu[-1].id +1 if len(self.__list_stu)> 0 id=self.__list_stu[-1].id +1 else id=1
    def order_by_score(self):
        new_list = self.__list_stu[:]
        for r in range(len(new_list)-1):
            for c in range(r+1, len(new_list)-1):
                if new_list[r].score > new_list[c].score:
                    new_list[r],new_list[c] = new_list[c],new_list[r]
        return new_list

    def remove_student(self,id):
        """删除学生"""
        for stu in self.list_stu:
            if stu.id == id:
                self.list_stu.remove(stu)
                return True
        return False
