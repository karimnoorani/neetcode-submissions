class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.start = None
        self.rear = None
        self.currLength = 0
        self.maxSize = k

    def enQueue(self, value: int) -> bool:
        node = ListNode(value)
        if not self.rear:
            self.start = node
            self.rear = node
            self.currLength += 1
            return True
        
        if self.currLength < self.maxSize:
            self.rear.next = node
            self.rear = node
            self.currLength += 1
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        if self.currLength == 0:
            return False
        elif self.currLength == 1:
            self.start = None
            self.rear = None
            self.currLength -= 1
            return True
        else:
            self.start = self.start.next
            self.currLength -= 1
            return True

    def Front(self) -> int:
        return self.start.val if self.start else -1

    def Rear(self) -> int:
        return self.rear.val if self.rear else -1

    def isEmpty(self) -> bool:
        return self.currLength == 0

    def isFull(self) -> bool:
        return self.currLength == self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()