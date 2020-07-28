class Employee:
    pass

#class EmployeeIterator:
#    """迭代器 """
#    def __init__(self,target):
#       self.target = target
#       self.index = 0
#
#   def __next__(self):
#        if self.index > len(self.target)-1:
#            raise StopIteration()
#        item = self.target[self.index]
#        self.index +=1
#        return item

class EmployeeManager:
    def __init__(self,employees):
        self.all_employee = employees
    def __iter__(self):
        for item in self.all_employee:
            yield item
            print("qwqw")
manager =EmployeeManager([Employee(),Employee(),Employee()])
for item in manager:
    print(item)