# -*- coding: UTF-8 -*-
class Solution(object):


    def addTripleKey(self, tripple_array, result_dict):
        cnt_dict = result_dict
        for x in tripple_array:
            if x not in cnt_dict:
                cnt_dict[x] = {}
            cnt_dict = cnt_dict[x]

    def hasTripleKey(self, tripple_array, result_dict):
        cnt_dict = result_dict
        for x in tripple_array:
            if x not in cnt_dict:
                return False
            cnt_dict = cnt_dict[x]
        return True

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_length = len(nums)
        nums_sorted = []
        nums_index_dict = {}
        for index, x in enumerate(nums):
            nums_sorted.append(x)
        nums_sorted.sort()
        for index, x in enumerate(nums_sorted):
            if x not in nums_index_dict:
                nums_index_dict[x] = set()
            nums_index_dict[x].add(index)
        if nums_length < 4:
            return []

        tripple_dict = {}
        result_list = []
        for x in xrange(0, nums_length - 2):
            for y in xrange(x + 1, nums_length - 1):
                for z in xrange(y + 1, nums_length):
                    num1 = nums_sorted[x]
                    num2 = nums_sorted[y]
                    num3 = nums_sorted[z]
                    if self.hasTripleKey([num1, num2, num3], tripple_dict):
                        continue
                    nums_remain = target - num1 - num2 - num3
                    if nums_remain < num3 or nums_remain < num1 or nums_remain < num2:
                        continue
                    if nums_remain not in nums_index_dict:
                        continue
                    self.addTripleKey([num1, num2, num3], tripple_dict)
                    nums_index_dict[num1].remove(x)
                    nums_index_dict[num2].remove(y)
                    nums_index_dict[num3].remove(z)

                    if len(nums_index_dict[nums_remain]) != 0:
                        result_list.append([num1, num2, num3, nums_remain])

                    nums_index_dict[num1].add(x)
                    nums_index_dict[num2].add(y)
                    nums_index_dict[num3].add(z)

        return result_list

if __name__ == '__main__':
    print Solution().fourSum([1,0,-1,0,-2,2], 0)
    print Solution().fourSum([2,2,2,2,2], 8)
