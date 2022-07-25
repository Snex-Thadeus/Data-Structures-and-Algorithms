#LeetCode 875 #O(log max(p)*p)
import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r #Maxi in our piles

        while l <= r:
            k = (l + r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1 #Try t look for smaller k in the left
            else:
                l = k + 1 #The rate was too small

        return res