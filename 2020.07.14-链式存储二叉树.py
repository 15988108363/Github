# Binary_tree_list =["A",["B",["D",None,None],["E",None,None]],["C",["F",None,None],None]] 顺序表
"""二叉树构建遍历
重点代码
"""
class QueueError(Exception):
    pass

class SQueue:
    def __init__(self):
        self._elems = []
    def is_empty(self):
        return self._elems ==[]
    #入队
    def enqueue(self,elem):
        self._elems.append(elem)
    #出队
    def dequeue(self):
        if not self._elems:
            raise  QueueError("队列为空")
        return self._elems.pop(0)

class TreeNode:
    def __init__(self,date=None,left=None,right=None):
        self.date = date        #数据
        self.left = left        #连接左子树
        self.right = right      #连接右子树
    def print_self(self):
        print("date=%s,left=%s,right=%s"%(self.date,self.left,self.right))
#二叉树类
class Bitree:
    def __init__(self,root=None):
        self.root = root

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    def preorder(self,node):#先序遍历
        if node is None:
            return
        print(node.date,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
    def middleorder(self,node):#中序遍历
        if node is None:
            return
        self.middleorder(node.left)
        print(node.date,end=" ")
        self.middleorder(node.right)
    def postorder(self,node):#后续遍历
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.date, end=" ")
    def levelorder(self,node):
        qu = SQueue()
        qu.enqueue(node)
        while not qu.is_empty():
            node = qu.dequeue()
            print(node.date,end=" ")
            if node.left:
                qu.enqueue(node.left)
            if node.left:
                qu.enqueue(node.right)
if __name__ =="__main__":
    #按照后续遍历增加结点
    b = TreeNode("B")
    f = TreeNode("F")
    g = TreeNode("G")
    d = TreeNode("D",f,g)
    i = TreeNode("I")
    h = TreeNode("H")
    e = TreeNode("E",i,h)
    c = TreeNode("C",d,e)
    a = TreeNode("A",b,c)
    bt = Bitree(a)  # 初始化树对象，传入根节点
    a.print_self()
    print("pre order....")
    bt.preorder(bt.root)
    print("\t")
    print("middle order....")
    bt.middleorder(bt.root)
    print("\t")
    print("post order....")
    bt.postorder(bt.root)
    print("\t")
    print("level order....")
    bt.levelorder(bt.root)