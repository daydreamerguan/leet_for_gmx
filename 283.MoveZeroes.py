class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        index = 0
        non_zero_index = 0
        while index < size:
            while(nums[index] != 0):
                index += 1
                if index >= size:
                    break
            if non_zero_index <= index:
                non_zero_index = index + 1
            while non_zero_index < size and nums[non_zero_index] == 0:
                non_zero_index += 1

            if non_zero_index >= size:
                break
            self.swap(nums, index, non_zero_index)
            index += 1
            non_zero_index += 1

    def swap(self, nums, i , j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
