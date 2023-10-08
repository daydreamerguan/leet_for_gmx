class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findMinLogn(nums)

    def findMinLogn(self, nums):
        return self.findMinLognWithRotate(0, len(nums), nums)

    def findMinLognWithRotate(self, left, right, nums):
        if right - left == 1:
            return nums[left]
       
        mid = (right + left) / 2


        if nums[mid] < nums[left]:
            return min(nums[mid], self.findMinLognWithRotate(left, mid, nums))
        elif nums[mid] > nums[right - 1]:
            return self.findMinLognWithRotate(mid, right, nums)
        else:
            return min(self.findMinLognWithRotate(left, mid, nums), self.findMinLognWithRotate(mid, right, nums))
