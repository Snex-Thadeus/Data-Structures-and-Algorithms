# Given the head of a singly linked list, return true if it is a palindrome.
# LeetCode 234

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        fast = head
        slow = head

        #Find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #Reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        #Chech palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

        #Array Solution
        # nums = []
        #
        # while head:
        #     nums.append(head.val)
        #     head = head.next
        #
        # l, r = 0, len(nums)-1
        # while l <= r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l += 1
        #     r -= 1
        #
        # return True