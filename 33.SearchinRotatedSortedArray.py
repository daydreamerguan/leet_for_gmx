class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        offset = self.getStartOffset(nums)
        len_nums = len(nums)
        return self.binary_search_with_offset(nums, len_nums, 0, len_nums, offset, target)
    
    def getStartOffset(self, nums):
        len_nums = len(nums)
        offset = 0
        for index in xrange(0, len_nums):
            next_index = (index + 1) % len_nums
            if nums[index] > nums[next_index]:
                offset = next_index
                break
        return offset

    def getRealIndexWithOffset(self, index, offset, len_nums):
        return (index + offset) % len_nums 

    def binary_search_with_offset(self, nums, len_nums, left, right, offset, target):
        # [left right)
        real_left = self.getRealIndexWithOffset(left, offset, len_nums)
        real_right = self.getRealIndexWithOffset(right, offset, len_nums)
        if right - left <= 1:
            return real_left if nums[real_left] == target else -1
        elif right - left < 1:
            return -1
        mid = (right + left) / 2
        real_mid = self.getRealIndexWithOffset(mid, offset, len_nums)
        cmp_result = cmp(target, nums[real_mid])
        if cmp_result == 0:
            return real_mid
        elif cmp_result < 0:
            return self.binary_search_with_offset(nums, len_nums, left, mid, offset, target)
        else:
            return self.binary_search_with_offset(nums, len_nums, mid + 1, right, offset, target)


if __name__ == '__main__':
    print Solution().search([4,5,6,7,0,1,2], 0)
    print Solution().search([4,5,6,7,0,1,2], 3)
    print Solution().search([1], 1)
    print Solution().search([1], 0)