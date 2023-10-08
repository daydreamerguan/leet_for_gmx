class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.MaxProductWithRange(nums, 0, len(nums))
    
    def GetMaxProductWithNegtive(self, nums, left, right):
        if right - left == 1:
            return nums[left]
        product = 1
        for i in xrange(left, right):
            product *= nums[left]
        if product > 0:
            return product
        else:
            left_most_product = 1
            cnt_index = left
            while left_most_product > 0 and cnt_index < right:
                left_most_product *= nums[cnt_index]
                cnt_index += 1
            right_most_product = 1
            cnt_index = right - 1
            while right_most_product > 0 and cnt_index >= left:
                right_most_product *= nums[cnt_index]
                cnt_index -= 1
            max_neg_product = max(left_most_product, right_most_product)
            print ("max_neg_product", max_neg_product)
            return product / max_neg_product 



    def MaxProductWithRange(self, nums, left, right):
        if left >= right:
            return 0
        if right - left == 1:
            return nums[left]
        zero_div = -1
        for i in xrange(left, right):
            if nums[i] == 0:
                zero_div = i
                break
        if zero_div != -1:
            return max(0, self.GetMaxProductWithNegtive(nums, left, zero_div), self.MaxProductWithRange(nums, zero_div + 1, right))
        else:
            return self.GetMaxProductWithNegtive(nums, left, right)