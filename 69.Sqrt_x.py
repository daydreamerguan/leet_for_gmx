class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        cnt_sqrt = 0
        cnt_square = 0
        while x - cnt_square >= (cnt_sqrt * 2 + 1):
            cnt_square += (cnt_sqrt * 2 + 1)
            cnt_sqrt += 1
        return cnt_sqrt
        