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
if __name__ == "__main__":
    s01 = SQueue()
    print(s01.is_empty())
    s01.enqueue(12)
    s01.enqueue(13)
    s01.enqueue(14)
    s01.enqueue(15)
    print(s01.is_empty())
