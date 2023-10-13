class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        ugly_nums = [2, 3, 5]
        for num in ugly_nums:
            while n != 1:
                if n % num != 0:
                    break
                n /= num
        return n == 1