class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        final_ret = []
        for i in xrange(0, size + 1):
            cnt_ret_list = []
            cnt_ret = []
            self.combine_solver(cnt_ret_list, cnt_ret, 0, i, size)
            for ret in cnt_ret_list:
                if not ret:
                    final_ret.append(ret)
                else:
                    new_ret = [nums[item] for item in ret]
                    final_ret.append(new_ret)
        return final_ret

    def combine_solver(self, ret_list, cnt_ret, start_index, reserve_size, n):
        if reserve_size == 0:
            cnt_result = [x for x in cnt_ret]
            ret_list.append(cnt_result)
            return
        for i in xrange(start_index, n):
            if n - i < reserve_size:
                break
            cnt_ret.append(i)
            self.combine_solver(ret_list, cnt_ret, i + 1, reserve_size - 1, n)
            cnt_ret.pop()

if __name__ == '__main__':
    print Solution().subsets([1,2,3])
    print Solution().subsets([0])