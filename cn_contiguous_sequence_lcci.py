class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_num = -999999999999999999999999999999

        # if not num >= 0 return the max num
        first_not_neg_index = -1
        for index, num in enumerate(nums):
            if num >= 0:
                first_not_neg_index = index
                break
        if first_not_neg_index == -1:
            return max(nums)

        cnt_sum = 0
        max_sum = 0
        # if previous sum > 0,  and it to cnt num, compare to max sum
        for i in xrange(first_not_neg_index, len(nums)):
            if cnt_sum + nums[i] < 0:
                cnt_sum = 0
                continue
            cnt_sum += nums[i]
            if max_sum < cnt_sum:
                max_sum = cnt_sum
        return max_sum