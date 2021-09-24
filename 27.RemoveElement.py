class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 0 <= nums[i] <= 50
        cnt_index = -1
        for index, num in enumerate(nums):
            if num == val:
                continue
            cnt_index += 1
            nums[cnt_index] = num
        return cnt_index + 1