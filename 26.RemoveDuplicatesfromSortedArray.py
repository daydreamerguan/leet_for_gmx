class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num range from -100 - 100
        cnt_num = -101
        cnt_index = -1
        for index, num in enumerate(nums):
            if num == cnt_num:
                continue
            cnt_num = num
            cnt_index += 1
            nums[cnt_index] = num
        return cnt_index + 1