class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        state_info_list = [[0, 0]]
        for index, num in enumerate(nums):
            cnt_profit = []
            cnt_profit.append(max(state_info_list[index]))
            cnt_profit.append(state_info_list[index][0] + nums[index])
            state_info_list.append(cnt_profit)
        return max(state_info_list[-1])
