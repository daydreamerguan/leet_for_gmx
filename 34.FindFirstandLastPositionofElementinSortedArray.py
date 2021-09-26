class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.search_left(nums, len(nums), 0, len(nums), target)
        right = self.search_right(nums, len(nums), 0, len(nums), target)
        return [left, right]

    def cmp_left(self, target, index, nums):
        if nums[index] == target:
            if index == 0:
                return 0
            elif nums[index - 1] < target:
                return 0
            else:
                return 1
        elif nums[index] < target:
            return -1
        return 1

    def search_left(self, nums, len_nums, left, right, target):
        if right - left == 1:
            return left if nums[left] == target else -1
        elif right - left < 1:
            return -1
        mid = (right + left) / 2
        cmp_result = self.cmp_left(target, mid, nums)
        if cmp_result == 0:
            return  mid
        elif cmp_result == 1:
            return self.search_left(nums, len_nums, left, mid, target)
        else:
            return self.search_left(nums, len_nums, mid + 1, right, target)

    def cmp_right(self, target, index, nums, len_nums):
        if nums[index] == target:
            if index == len_nums - 1:
                return 0
            elif nums[index + 1] > target:
                return 0
            else:
                return -1
        elif nums[index] < target:
            return -1
        return 1

    def search_right(self, nums, len_nums, left, right, target):
        if right - left == 1:
            return left if nums[left] == target else -1
        elif right - left < 1:
            return -1
        mid = (right + left) / 2
        cmp_result = self.cmp_right(target, mid, nums, len_nums)
        if cmp_result == 0:
            return  mid
        elif cmp_result == 1:
            return self.search_right(nums, len_nums, left, mid, target)
        else:
            return self.search_right(nums, len_nums, mid + 1, right, target)

if __name__ == '__main__':
    print Solution().searchRange([5,7,7,8,8,10], 8)
    print Solution().searchRange([5,7,7,8,8,10], 6)
    print Solution().searchRange([], 6)

