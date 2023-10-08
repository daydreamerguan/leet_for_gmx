class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.do_rotate(nums, k, 0, len(nums))
        # print(nums)

    def swap_k_num(self, nums, from_start, end_start, k):
        for i in range(0, k):
            temp = nums[from_start + i]
            nums[from_start + i] = nums[end_start + i]
            nums[end_start + i] = temp

    def do_rotate(self, nums, k, index_start, index_end):
        size = index_end - index_start
        if size <= 0:
            return
        if k >= size:
            k = k % size
        if k == 0:
            return
        cnt_start = index_start + k
        next_k = k - (size % k)
        # print (k, size, next_k)
        while cnt_start < index_end:
            swap_size = k
            if cnt_start + k > index_end:
                swap_size = index_end - cnt_start
            # print(swap_size, cnt_start, index_end)
            self.swap_k_num(nums, index_start, cnt_start, swap_size)
            cnt_start += swap_size
        if next_k != k:
            self.do_rotate(nums, next_k, index_start, index_start + k)
        return


if __name__ == '__main__':
    Solution().rotate([1,2,3,4,5,6,7], 3)
    Solution().rotate([-1,-100,3,99], 2)
    Solution().rotate([1,2,3,4,5,6,7], 4)
    Solution().rotate([1,2,3,4,5,6,7], 5)
    Solution().rotate([1,2,3,4,5,6,7], 6)