# -*- coding: UTF-8 -*- 
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        copy_nums = nums
        copy_nums.sort()
        nums_map = {}

        # init nums -> position map, because we wont use same position number twice.

        for index, num in enumerate(copy_nums):
            if num not in nums_map:
                nums_map[num] = set()
            nums_map[num].add(index)
        negetive_and_zero_map = {}
        positive_map = {}
        tuple_set = set()
        num_size = len(copy_nums)
        triples_list = []
        for x in xrange(0, num_size - 1):
            for y in xrange(x + 1, num_size):
                cnt_tuple = (copy_nums[x], copy_nums[y])
                if cnt_tuple  in tuple_set:
                    continue
                nums_map[copy_nums[x]].remove(x)
                nums_map[copy_nums[y]].remove(y)
                if (copy_nums[x] <= 0 and copy_nums[y] <= 0) or (copy_nums[x] > 0 and copy_nums[y] > 0):
                    # 相当于两种情况, 分别是先选好的两个数字 小于等于0 或者是 都大于0的情况
                    cnt_sum = copy_nums[x] + copy_nums[y]
                    if -cnt_sum in nums_map and len(nums_map[-cnt_sum]) != 0:
                        tuple_set.add(cnt_tuple)
                        triples_list.append([copy_nums[x], copy_nums[y], -cnt_sum])
                nums_map[copy_nums[x]].add(x)
                nums_map[copy_nums[y]].add(y)

        return triples_list

if __name__ == '__main__':
    print Solution().threeSum([-1,0,1,2,-1,-4])
    print Solution().threeSum([0,])