class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_start_production = [1,]
        for num in nums:
            left_start_production.append(left_start_production[-1] * num)

        nums.reverse()
        right_start_production = [1,]

        for num in nums:
            right_start_production.append(right_start_production[-1] * num)
        # print(left_start_production)
        # print(right_start_production)
        size = len(nums)
        result = []
        for index, num in enumerate(nums):
            result.append(left_start_production[index] * right_start_production[size - index - 1])
        return result

if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))