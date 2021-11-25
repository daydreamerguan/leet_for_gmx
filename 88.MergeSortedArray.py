class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        cnt_index = m + n - 1
        cnt_m = m - 1
        cnt_n = n -1
        while cnt_index >= 0:
            num_ref = None
            num_index = -1
            if cnt_m < 0:
                num_ref = nums2
                num_index = cnt_n 
                cnt_n -= 1
            elif cnt_n < 0:
                num_ref = nums1
                num_index = cnt_m
                cnt_m -= 1
            if not num_ref:
                if nums1[cnt_m] > nums2[cnt_n]:
                    num_ref = nums1
                    num_index = cnt_m
                    cnt_m -= 1
                else:
                    num_ref = nums2
                    num_index = cnt_n 
                    cnt_n -= 1
            nums1[cnt_index] = num_ref[num_index]
            cnt_index -= 1

