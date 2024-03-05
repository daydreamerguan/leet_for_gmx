def find_cache_index(left, right):
    index = 0
    length = right - left + 1
    while (length > 2**(index + 1)):
        index += 1
    # print("find_cache_index", left, right, index, 2**(index + 1))
    return index


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [num for num in nums]
        self.sum_cache_list = []
        cnt_len = 1
        # print("nums", nums)
        while cnt_len <= len(self.nums):

            cnt_value = 0
            cnt_index = 0
            cnt_cache_list = []
            while cnt_index < cnt_len:
                cnt_value += self.nums[cnt_index]
                cnt_index += 1
            cnt_cache_list.append(cnt_value)
            while cnt_index < len(self.nums):
                cnt_value += self.nums[cnt_index]
                cnt_value -= self.nums[cnt_index - cnt_len]
                cnt_cache_list.append(cnt_value)
                cnt_index += 1
            print(cnt_cache_list)
            self.sum_cache_list.append(cnt_cache_list)
            cnt_len *= 2


    def sumRange(self, left, right):
        if(right < left):
            return 0
        if(right == left):
            return self.nums[left]
        index = find_cache_index(left, right)
        left_add = self.sum_cache_list[index][left]
        next_left = left + 2**index
        return left_add + self.sumRange(next_left, right)
        """
        :type left: int
        :type right: int
        :rtype: int
        """



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
if __name__ == '__main__':
    s = NumArray([-2,0,3,-5,2,-1])
    print(s.sumRange(0,2))
    print(s.sumRange(2,5))
    print(s.sumRange(0,5))