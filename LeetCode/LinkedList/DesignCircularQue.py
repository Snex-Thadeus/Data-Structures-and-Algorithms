# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations
# are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle.
# It is also called "Ring Buffer".
# LeetCode 622

class ListNode:
    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue(object):

    def __init__(self, k):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value):
        if self.isFull(): return False
        cur = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = cur #Left of cur
        self.right.prev = cur
        self.space -= 1
        return True

    def deQueue(self):
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self):
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self):
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self):
        return self.left.next == self.right

    def isFull(self):
        return self.space == 0