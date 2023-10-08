class Solution(object):

    def compare(self, a, b):
        str_ab = str(a) + str(b)
        str_ba = str(b) + str(a)
        return cmp(str_ab, str_ba)

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        nums.sort(cmp=self.compare)
        nums.reverse()
        if(nums[0] == 0):
            nums = [0,]
        nums_str = [str(a) for a in nums]
        return "".join(nums_str)