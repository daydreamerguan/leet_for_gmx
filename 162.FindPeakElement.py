class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = len(nums) - 1

        left = 0
        while right != left:
            mid = (left + right) / 2
            if nums[mid] > nums[mid + 1]:
                right = mid 
            else:
                left = mid + 1
            print left, right
        return left

if __name__ == '__main__':
    print Solution().findPeakElement([1,2,1,3,5,6,4])