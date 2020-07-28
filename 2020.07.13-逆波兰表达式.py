class Node(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class StackError(Exception):
    pass
class Lstack:
    def __init__(self):
        self._top = None #标记栈顶位置
    def is_empty(self):
        return self._top is None
    def push(self,elem):
        # node = Node(elem)
        # node.next = self._top
        # self._top =node
        self._top = Node(elem,self._top)
    def pop(self):
        if self._top is None:
            raise StackError("empty")
        p = self._top
        self._top = p.next
        return p.val
    def top(self):
        if self._top is None:
            raise StackError("empty")
        return self._top.val
str01 = str(input("简单逆波兰表达式："))
print(str01)
lst = Lstack()
left = 0
list01 = []
for right in range(0,len(str01)):
    if str01[right] == " ":
        print(str01[left:right])
        list.append(str01[left:right])
        left = right+1
        right +=1
for i in list01:
    if i != "+" or "-":
        lst.push(i)