class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add = 1
        for index in xrange(len(digits) - 1, -1, -1):
            result = digits[index] + add
            add = result / 10
            digits[index] = result % 10
        if add:
            return [1] + digits
        else:
            return digits