# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# LeetCode 24
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object): #M O(1) T=O(N)
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            #save pointers
            nxtPair = curr.next.next
            second = curr.next

            #reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            #update ptrs
            prev = curr
            curr = nxtPair

        return dummy.next