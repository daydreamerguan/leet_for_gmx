class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_list = [i for i in range(0, n + 1)]
        square_num = 2
        while square_num ** 2 <= n:
            add_num = square_num ** 2
            index = add_num
            for index in xrange(add_num, n + 1):
                num_list[index] = min(num_list[index], num_list[index - add_num] + 1)
            square_num += 1
        return num_list[n]