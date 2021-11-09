class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        waiting_num_list = [i + 1 for i in xrange(0, n)]
        result_num_list = []
        cnt_pernum = 1
        for i in xrange(1, n):
            cnt_pernum *= i
        cnt_mul = n - 1
        cnt_global_index = k - 1
        while cnt_mul > 0:
            num_index = cnt_global_index / cnt_pernum
            result_num_list.append(str(waiting_num_list[num_index]))
            del waiting_num_list[num_index]
            cnt_global_index -= (num_index * cnt_pernum)
            cnt_pernum /= cnt_mul
            cnt_mul -= 1
        result_num_list.append(str(waiting_num_list[0]))
        return "".join(result_num_list)

if __name__ == '__main__':
    print Solution().getPermutation(3, 3)
    print Solution().getPermutation(4, 9)
    print Solution().getPermutation(3, 1)

            

