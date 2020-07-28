class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class Linklist:
    def __init__(self):
        self._head = None
    def init_list(self,date):
        self._head =Node(None)
        p = self._head
        for i in date:
            p.next =Node(i)
            p = p.next
    def print_link01(self):
        try:
            while True:
                print(self._head.val,end=" ")
                self._head = self._head.next
        except:
            print("\t")

    def print_link02(self):
        p =self._head.next
        while p:
            print(p.val,end=" ")
            p= p.next

    def print_link03(self):
        while self._head:
            print(self._head.val, end=" ")
            self._head = self._head.next

if __name__ == "__main__":
     lst01 = Linklist()
     list01 =[1,2,3,4,5,6]
     lst01.init_list(list01)
     lst01.print_link01()
     print("=" * 40)

     lst02 = Linklist()
     list02 = [1, 2, 3, 4, 5, 6]
     lst02.init_list(list02)
     lst02.print_link02()
     print("\t")
     print("=" * 40)

     lst03 = Linklist()
     list03 = [1, 2, 3, 4, None, 6]
     lst03.init_list(list03)
     lst03.print_link03()
