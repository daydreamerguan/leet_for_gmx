class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_pos(nums, target, 0, len(nums))
    
    def search_pos(self, nums, target, left, right):
        if right - left == 1:
            if nums[left] >= target:
                return left
            else:
                return right
        elif right - left < 1:
            return left

        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.search_pos(nums, target, mid + 1, right)
        else:
            return self.search_pos(nums, target, left, mid)
