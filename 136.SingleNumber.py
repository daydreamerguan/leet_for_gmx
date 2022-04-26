class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_half = 3 * (10 ** 4)
        nums_count = 3 * (10 ** 4) * 2 + 1
        nums_count_list = [0 for i in xrange(0, nums_count)]
        for num in nums:
            nums_count_list[num + num_half] += 1

        for index, num in enumerate(nums_count_list):
            if num == 1:
                return index - num_half
