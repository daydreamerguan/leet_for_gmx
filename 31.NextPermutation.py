# -*- coding: UTF-8 -*-
class Solution(object):

    def reverse_nums(self, nums, num_size):
        left = 0
        right = num_size - 1
        while left <= right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

    def popup_sort_range(self, nums, left, right):
        
        for x in xrange(left, right - 1):
            for y in xrange(x + 1, right):
                if nums[x] > nums[y]:
                    temp = nums[x]
                    nums[x] = nums[y]
                    nums[y] = temp

    def swap_with_min_bigger_than_num(self, nums, nums_size, start_index, cnt_num):
        swap_index = -1
        for x in xrange(start_index, nums_size):
            if nums[x] > cnt_num:
                if swap_index == -1 or nums[x] < nums[swap_index]:
                    swap_index = x
        temp = nums[start_index - 1]
        nums[start_index - 1] = nums[swap_index]
        nums[swap_index] = temp


    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_size = len(nums)
        found_not_inverse_pair = False

        not_reverse_num = nums_size - 2
        while not_reverse_num >= 0:
            if(nums[not_reverse_num] < nums[not_reverse_num + 1]):
                found_not_inverse_pair = True
                break
            not_reverse_num -= 1

        if not found_not_inverse_pair:
            self.reverse_nums(nums, nums_size)
        else:
            self.swap_with_min_bigger_than_num(nums, nums_size, not_reverse_num + 1,  nums[not_reverse_num])
            self.popup_sort_range(nums, not_reverse_num + 1, nums_size)


