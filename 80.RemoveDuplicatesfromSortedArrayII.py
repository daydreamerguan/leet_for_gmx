class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_num = - 10 ** 5
        cnt_repica = 0
        cnt_index = 0
        for index, num in enumerate(nums):
            if num != cnt_num:
                cnt_num = num
                cnt_repica = 1
                nums[cnt_index] = cnt_num
                cnt_index += 1
            else:
                if cnt_repica < 2:
                    nums[cnt_index] = cnt_num
                    cnt_repica += 1
                    cnt_index += 1
        return cnt_index