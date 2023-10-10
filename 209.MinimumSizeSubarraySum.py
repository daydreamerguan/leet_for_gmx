class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sums_list = []
        sums_list.append(0)
        target_len = 0
        for index, num in enumerate(nums):
            sums_list.append(sums_list[index] + num)
        if sums_list[-1] < target:
            return 0
        sum_len = len(sums_list)
        for index, cnt_sum in enumerate(sums_list):
            fit_index = self.find_left_most_fit_index(sums_list, cnt_sum, index + 1, sum_len, target)
            if fit_index != -1:
                if target_len == 0:
                    target_len = fit_index - index
                    # print(target_len, fit_index, index, "1")
                else:
                    target_len = min(fit_index - index, target_len)
                    # print(target_len, fit_index, index, "2")
            else:
                break
        return target_len
    def find_left_most_fit_index(self, sums_list, cnt_sum, left, right, target):
        if left == right:
            return -1
        if right - left == 1:
            if sums_list[left] - cnt_sum >= target:
                return left
            else:
                return -1
        mid_index = int((left + right) / 2)
        new_sum = sums_list[mid_index] - cnt_sum
        if new_sum >= target:
            left_test = self.find_left_most_fit_index(sums_list, cnt_sum, left, mid_index, target)
            if left_test != -1: 
                return left_test
            else:
                return mid_index
        else:
            return self.find_left_most_fit_index(sums_list, cnt_sum, mid_index + 1, right, target)

if __name__ == '__main__':
    Solution().minSubArrayLen(7, [2,3,1,2,4,3])