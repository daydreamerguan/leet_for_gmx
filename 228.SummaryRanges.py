class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        index = 0
        size = len(nums)
        ret_list = []
        if size == 0:
            return []
        while index < size:
            value_left, value_right, index = self.sum_range(nums, index, size)
            if value_left == value_right:
                ret_list.append("{0}".format(value_left))
            else:
                ret_list.append("{0}->{1}".format(value_left, value_right))
        return ret_list

    def sum_range(self, nums, index, size):
        value_left = nums[index]
        value_right = nums[index]
        while index < size:
            if abs(nums[index] - value_right) <= 1:
                value_right = nums[index]
                index += 1
            else:
                break
        return value_left, value_right, index