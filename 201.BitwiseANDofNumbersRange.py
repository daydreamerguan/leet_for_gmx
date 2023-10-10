class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        nums = [ 2**i for i in xrange(0, 32)]
        nums.reverse()
        found = False
        ret = 0
        for num in nums:
            left_quotient = int(left / num)
            right_quotient = int(right / num)
            if left_quotient > 0 or right_quotient > 0:
                found = 1
            if not found:
                continue
            if left_quotient == right_quotient:
                if left_quotient > 0:
                    ret += num
                    left -= num
                    right -= num
            else:
                break
        return ret