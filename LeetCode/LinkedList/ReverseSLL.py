# Given the head of a singly linked list, reverse the list, and return the reversed list.
#Leetcode 206

class Solution(object):
    def reverseList(self, head):
        #Recursive
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head #Reverse
        head.next = None
        return newHead

        # prev, curr = None, head
        #
        # #Iterative way O(n) O(1)
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        return prev
