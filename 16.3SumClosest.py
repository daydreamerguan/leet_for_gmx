# -*- coding: UTF-8 -*- 
class Solution(object):


    def findClosetIndex(self, nums, target_num, left, right):
        if right - left == 1:
            return left
        mid = (right + left) / 2
        if nums[mid] == target_num:
            return mid
        elif nums[mid] > target_num:
            return self.findClosetIndex(nums, target_num, left, mid)
        else:
            return self.findClosetIndex(nums, target_num, mid, right)

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        copy_nums = nums
        nums.sort()
        num_size = len(nums)
        closest_diff = 10000000
        closest_num = 100000000
        for x in xrange(0, num_size - 1):
            for y in xrange(x + 1, num_size):
                num_x = nums[x]
                num_y = nums[y]
                request_num = target - num_x -num_y
                target_index = self.findClosetIndex(nums, request_num, 0, num_size)
                for index in xrange(target_index - 3, target_index + 4):
                    if index < 0 or index >= num_size:
                        continue
                    if index == x or index == y:
                        continue
                    cnt_num = num_x  + num_y + nums[index]
                    cnt_diff = abs(cnt_num - target)
                    if cnt_diff < closest_diff:
                        closest_num =  cnt_num
                        closest_diff = cnt_diff


        return closest_num

if __name__ == '__main__':
    print Solution().threeSumCloset([-1,2,1,-4], 1)
    print Solution().threeSumCloset([0,0,0], 1)