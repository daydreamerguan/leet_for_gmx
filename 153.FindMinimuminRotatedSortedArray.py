class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findMinLogn(nums)
        nums_length = len(nums)
        for i in xrange(0, nums_length):
            if nums[(i + 1) % nums_length] < nums[i]:
                return nums[(i + 1) % nums_length]
        return nums[0]

    def findMinLogn(self, nums):
        return self.findMinLognWithRotate(0, len(nums), nums)

    def findMinLognWithRotate(self, left, right, nums):
        if right - left == 1:
            return nums[left]
       
        mid = (right + left) / 2
        # print ("find range", left, right, mid)
        if nums[mid] < nums[left]:
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            return self.findMinLognWithRotate(left, mid, nums)
        elif nums[mid] > nums[right - 1]:
            return self.findMinLognWithRotate(mid, right, nums)
        else:
            return nums[left]
