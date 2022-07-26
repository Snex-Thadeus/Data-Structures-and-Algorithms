# Given the head of a linked list, return the list after sorting it in ascending order.
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
# LeetCode 148
class ListNode(object): #O(n log n) #Merge sort
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        #Split the list in 2 halfs
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next= None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        tail = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next

            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next
