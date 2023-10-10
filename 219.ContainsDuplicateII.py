class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_index_map = {}
        for index, num in enumerate(nums):
            if num not in nums_index_map:
               nums_index_map[num] = index
            else:
                if abs(nums_index_map[num] - index) <= k:
                    return True
                else:
                    nums_index_map[num] = index
        return False
