# LeetCode 19
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next #Shift right by one
            n -= 1

        while right: #End of the list
            left = left.next
            right = right.next

        #Delete the node
        left.next = left.next.next
        return dummy.next