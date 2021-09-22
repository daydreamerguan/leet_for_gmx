class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        left = 0
        right = len(str_x) - 1
        while left < right and str_x[left] == str_x[right]:
            left += 1
            right -= 1
        return right <= left