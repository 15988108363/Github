class Node(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
"""
    弹栈：p = top 
    top = top.next
    return p.val
    入栈：node =Node()
    node.next =top 
    top = node
"""
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
if __name__=="__main__":
    st = Lstack()
    print(st.is_empty())
    st.push(12)
    st.push(13)
    st.push(14)
    st.push(15)
    print(st.top())
    print(st._top.val)
    while not st.is_empty():
        print(st.pop())
