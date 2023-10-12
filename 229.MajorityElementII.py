class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.three_num_moore_vote(nums)


    def three_num_moore_vote(self, nums):
        size = len(nums)
        val1 = None
        val2 = None
        vote1 = 0
        vote2 = 0
        ret_list = []
        for v in nums:
            if vote1 > 0 and v == val1:
                vote1 += 1
            elif vote2 > 0 and v == val2:
                vote2 += 1
            elif vote1 == 0:
                val1 = v
                vote1 += 1
            elif vote2 == 0:
                val2 = v
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1
        if val1 is not None:
            count_val1 = nums.count(val1)
            if count_val1 * 3 > size:
                ret_list.append(val1)
        if val2 is not None and val1 != val2:
            count_val2 = nums.count(val2)
            if count_val2 * 3 > size:
                ret_list.append(val2)
        return ret_list