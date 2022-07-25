#Leetcode 374

class Solution(object):
    def guessNumber(self, n):
        guess = 'inbuilt func'
        l, r = 1, n

        while True:
            m = (l + r) // 2
            res = guess(m)

            if res > 0:
                l = m + 1
            elif res < 0:
                r = m - 1
            else:
                return m