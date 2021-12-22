class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        nums = list(nums_set)
        nums.sort()
        if not nums:
            return 0
        cnt_index = 1
        max_con = 1
        cnt_con = 1
        nums_len =len(nums)
        while cnt_index < nums_len:
            if nums[cnt_index] - nums[cnt_index - 1] == 1:
                cnt_con += 1
                if cnt_con > max_con:
                    max_con = cnt_con
            else:
                cnt_con = 1
            cnt_index += 1
        return max_con