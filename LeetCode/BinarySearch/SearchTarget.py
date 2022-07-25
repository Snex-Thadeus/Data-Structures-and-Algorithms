# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1. #704 Leetcode

class Solution(object):
    def search(self, nums, target):
        # target = 0
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            m = (lo + hi) // 2  # m = lo +((hi - lo) // 2)
            mid = nums[m]
            if mid == target:
                return m
            elif mid < target:
                lo = m + 1
            else:
                hi = m - 1

        return -1