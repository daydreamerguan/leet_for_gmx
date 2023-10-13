class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_num = 0
        for num in nums:
            xor_num = xor_num ^ num
        # appear twice xor is zero, then xor_num = a xor b

        lsb_num = xor_num & -xor_num
        ret0 = 0 
        ret1 = 0
        for num in nums:
            if lsb_num & num != 0:
                ret0 = ret0 ^ num
            else:
                ret1 = ret1 ^ num
        return [ret0, ret1]