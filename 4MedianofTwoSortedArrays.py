
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size_num1 = len(nums1)
        size_num2 = len(nums2)
       '''
        mid_left = (size_num1 + size_num2 - 1) / 2
        mid_right = (size_num1 + size_num2) / 2
        return (self.find_kth(nums1, 0, size_num1, nums2, 0, size_num2, mid_left) + self.find_kth(nums1, 0, size_num1, nums2, 0, size_num2, mid_right)) * 0.5
        '''
        # 右开区间, 这个是哨兵
        mid_left = (size_num1 + size_num2 + 1) / 2
        mid_right = (size_num1 + size_num2 + 2) / 2
        return (self.find_kth_copy(nums1, 0, size_num1, nums2, 0, size_num2, mid_left) + self.find_kth_copy(nums1, 0, size_num1, nums2, 0, size_num2, mid_right)) * 0.5
        

    def find_kth_copy(self, nums1, left_nums1, nums1_size, nums2, left_nums2, nums2_size, k):
        if left_nums1 >= nums1_size:
            return nums2[left_nums2 + k  - 1]
        if left_nums2 >= nums2_size:
            return nums1[left_nums1 + k - 1]

        if k == 1:
            return min(nums1[left_nums1], nums2[left_nums2])

        import sys
        mid_val1 = sys.maxint
        mid_val2 = sys.maxint
        # 哨兵 / 2
        mid_k = k / 2 - 1
        if left_nums1 + mid_k < nums1_size:
            mid_val1 = nums1[left_nums1 + mid_k]
        if left_nums2 + mid_k < nums2_size:
            mid_val2 = nums2[left_nums2 + mid_k]

        if mid_val1 < mid_val2:
            return self.find_kth_copy(nums1, left_nums1 + mid_k + 1, nums1_size, nums2, left_nums2, nums2_size, k - mid_k - 1)
        else:
            return self.find_kth_copy(nums1, left_nums1, nums1_size, nums2, left_nums2 + mid_k + 1,  nums2_size, k - mid_k - 1)
