# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# LeetCode 83
# Input: head = [1,1,2]
# Output: [1,2]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        cur = head

        while cur: #0(n)
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next #Deletes the duplicate node

            cur = cur.next

        return head