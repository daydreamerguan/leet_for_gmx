class Solution(object):

    def swap_num(self, nums, cnt_num, index):
        temp = nums[cnt_num - 1]
        nums[cnt_num - 1] = nums[index]
        nums[index] = temp
        return temp

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        for index in xrange(0, len_nums):
            cnt_num = nums[index]
            while len_nums >= cnt_num >= 1 and cnt_num != index + 1 and nums[cnt_num - 1] != cnt_num:
                cnt_num = self.swap_num(nums, cnt_num, index)

        for index in xrange(0, len_nums):
            if nums[index] != index + 1:
                return index + 1
        return len_nums + 1