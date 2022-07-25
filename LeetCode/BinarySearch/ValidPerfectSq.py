#Given a positive integer num, write a function which returns True if num is a perfect square else False.

class Solution(object):
    def isPerfectSquare(self, num):
        # #O(sqrt (n))
        # for i in range(1, num+1):
        #     if i * i == num:
        #         return True
        #     if i * i > num:
        #         return False
            #O(log N)
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            if m * m > num:
                r = m -1
            elif m * m < num:
                l = m + 1
            else :
                return True

        return False