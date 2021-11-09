class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_0 =  0
        nums_1 = 0
        for num in nums:
            if num == 0:
                nums_0 += 1
            elif num == 1:
                nums_1 += 1

        for i in xrange(0, nums_0):
            nums[i] = 0

        for i in xrange(0, nums_1):
            nums[i + nums_0] = 1

        nums_2 = len(nums) - nums_0 - nums_1
        nums_01 = nums_0 + nums_1

        for i in xrange(0, nums_2):
            nums[i + nums_01] = 2

