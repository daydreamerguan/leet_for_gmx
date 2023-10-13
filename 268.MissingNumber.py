class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        max_value = max(nums)
        if max_value != size:
            return size
        for index in xrange(0, size):
            cnt_index = index
            while nums[cnt_index] != cnt_index and nums[cnt_index] != max_value:
                temp = nums[cnt_index]
                nums[cnt_index] = nums[temp]
                nums[temp] = temp
        return nums.index(max_value)