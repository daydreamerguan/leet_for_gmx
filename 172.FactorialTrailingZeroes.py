class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        two_five_count_list = []
        two_five_count_list.append([0, 0])
        final_count = [0, 0]
        for i in xrange(2, n + 1):
            result = [0, 0]
            if i / 2 >= 1 and i % 2 == 0:
                index = i / 2 - 1
                result[0] = two_five_count_list[index][0] + 1
            if i / 5 >= 1 and i % 5 == 0:
                index = i / 5 - 1
                result[1] = two_five_count_list[index][1] + 1
            two_five_count_list.append(result)
            final_count[0] += result[0]
            final_count[1] += result[1]
        return  min(final_count)