class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        left_num = n

        while left_num >= 2:
            if left_num % 2 != 0:
                return False
            left_num /= 2
        return left_num == 1