# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
#LeetCode 35

class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return l