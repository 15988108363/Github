#创建结点类
class Node(object):
    def __init__(self,val,next=None):
        self.val = val #有用数据
        self.next = next
#链表的操作
class Linklist(object):
    def __init__(self):
        self.head =None
    def init_list(self,date):
        self.head = Node(None)
        p =self.head
        for i in date:
            p.next = Node(i)#链表的开头
            p =p.next#可移动变量
    def show(self):
        p = self.head.next
        while p!= None:
            print(p.val,end=" ")
            p =p.next
        print(p)
    def get_length(self):
        n =0
        p = self.head
        while p.next is not None:
            n +=1
            p =p.next
        return n
    def append(self,item):
        p=self.head
        while p.next is not None:
            p =p.next
        p.next =Node(item)

    def clear(self):
        self.head.next=None
    def get_item(self,index):
        p = self.head.next
        i = 0
        while i <= index and p is not None:
            i +=1
            p = p.next
        if p is None:
           raise IndexError("list index is out of range")
        else:
            return  p.val
    def insert_item(self,index,item):
        if index < 0 or index >self.get_length():
           raise IndexError("list index is out of range")
        p = self.head
        i =0
        while i <index:
           p= p.next
           i +=1
        node = Node(item)
        node.next = p.next
        p.next =node
    def delete(self,item):
        p = self.head
        while p.next is not None:
            if p.next.val == item:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError("x is not in list")

if __name__ == "__main__":
    link =Linklist()
    l = [1,2,3,4,5]
    link.init_list(l)
    link.show()
    print(link.get_length())
    link.append(6)
    link.show()
    print(link.get_length())
    link.insert_item(1,2)
    link.show()