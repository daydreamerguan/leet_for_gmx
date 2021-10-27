class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_max = max(nums)
        if num_max < 0:
            return num_max
        max_count = 0
        cnt_count = 0
        for num in nums:
            if cnt_count + num < 0:
                cnt_count = 0
                continue
            cnt_count += num
            if max_count < cnt_count:
                max_count = cnt_count
        return max_count

if __name__ == '__main__':
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print Solution().maxSubArray([5,4,-1,7,8])
    print Solution().maxSubArray([1])