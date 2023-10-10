class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_rob_nums = nums[2:-1]
        first_unrob_nums = nums[1:]
        return max(self.do_rob(first_unrob_nums), self.do_rob(first_rob_nums) + nums[0]) 

    def do_rob(self, nums):
        state_info_list = [[0, 0]]
        for index, num in enumerate(nums):
            cnt_profit = []
            cnt_profit.append(max(state_info_list[index]))
            cnt_profit.append(state_info_list[index][0] + nums[index])
            state_info_list.append(cnt_profit)
        return max(state_info_list[-1])