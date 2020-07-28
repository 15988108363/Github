class QueueError(Exception):
    pass
class Node(object):#创建结点
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class LQueue:
    def __init__(self):
        self.front = self.rear = Node(None)
    def is_empty(self):
        return self.front ==self.rear
    def enqueue(self,elem):
        self.rear.next =Node(elem)
        self.rear = self.rear.next
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("队列为空")
        self.front = self.front.next
        return self.front.val
    def clear(self):
        self.front = self.rear
if __name__ =="__main__":
    lq = LQueue()
    print((lq.is_empty()))