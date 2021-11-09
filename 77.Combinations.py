class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret_list = []
        cnt_ret = []
        self.combine_solver(ret_list, cnt_ret, 0, k, n)
        return ret_list

    def combine_solver(self, ret_list, cnt_ret, start_index, reserve_size, n):
        if reserve_size == 0:
            cnt_result = [x for x in cnt_ret]
            ret_list.append(cnt_result)
            return
        for i in xrange(start_index, n):
            if n - i < reserve_size:
                break
            cnt_ret.append(i + 1)
            self.combine_solver(ret_list, cnt_ret, i + 1, reserve_size - 1, n)
            cnt_ret.pop()

if __name__ == '__main__':
    print Solution().combine(4, 2)
    print Solution().combine(1, 1)
