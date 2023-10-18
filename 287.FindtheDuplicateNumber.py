class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow_index = nums[0]
        fast_index = nums[slow_index]
        # print("1 slow", slow_index, "fast", fast_index)
        while(slow_index != fast_index):
            slow_index = nums[slow_index]
            fast_index = nums[nums[fast_index]]
            # print("2 slow", slow_index, "fast", fast_index)
        slow_index = 0
        while(slow_index != fast_index):
            slow_index = nums[slow_index]
            fast_index = nums[fast_index]
            # print("3 slow", slow_index, "fast", fast_index)
        return slow_index

if __name__ == '__main__':
    print(Solution().findDuplicate([1,3,4,2,2]))
    print(Solution().findDuplicate([5,1,3,4,2,2]))
    print(Solution().findDuplicate([6,5,1,3,4,2,2]))
    print(Solution().findDuplicate([6,2,1,3,4,2,5]))
    print(Solution().findDuplicate([6,2,1,4,3,2,5]))