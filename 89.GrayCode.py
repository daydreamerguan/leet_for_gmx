class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        gray_code_list = [[0, 1], ]
        for i in xrange(1, n):
            new_list = [j for j in gray_code_list[i - 1]]
            # print new_list
            last_len = len(gray_code_list[i - 1])
            cnt_add = 2 ** i
            for j in xrange(0, last_len):
                new_list.append(cnt_add + gray_code_list[i - 1][last_len - 1 - j])
            gray_code_list.append(new_list)

        return gray_code_list[n - 1]

if __name__ == '__main__':
    print Solution().grayCode(3)