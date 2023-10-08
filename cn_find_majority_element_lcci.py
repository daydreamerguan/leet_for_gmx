
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore vote
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            else:
                if candidate != num:
                    count -= 1
                else:
                    count += 1
        # reset
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) / 2:
            return candidate
        else:
            return -1