# -*- coding: UTF-8 -*- 
#bucket sort + pigeon
import math
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 
        max_val = nums[0]
        min_val = nums[0]
        bucket_size = 
        max_bucket = []
        min_bucket = []
        len_num = len(nums)
        for i in range(0, len_num):
            max_bucket.append(None)
            min_bucket.append(None)
        bucket_size = int(math.ceil(((float(max_val - min_val)) / (len_num  - 1) ))