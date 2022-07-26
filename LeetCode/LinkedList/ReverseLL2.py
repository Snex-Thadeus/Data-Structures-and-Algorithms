# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# LeetCode 92

class ListNode(object): #O(N) M O(1)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)

        # reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left-1):
            leftPrev, cur = cur, cur.next

        #Now cur="left", leftPrev="node before left"
        #reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        #Updating the pointers
        leftPrev.next.next = cur #cur is node after "right"
        leftPrev.next = prev #prev is "right"
        return dummy.next
