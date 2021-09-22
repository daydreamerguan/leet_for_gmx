# -*- coding: UTF-8 -*-
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        parentthesis = [["()"], ]
        for i in xrange(2, 9):
            self.generateNextParenthesis(parentthesis, i)
        return parentthesis[n - 1]
    

    def generateNextParenthesis(self, prev_data, n):
        ret_list = []
        ret_set = set()
        for x in prev_data[-1]:
            new_data = "{}{}{}".format("(", x, ")")
            if new_data not in ret_set:
                ret_set.add(new_data)
                ret_list.append(new_data)
        for i in xrange(0, n - 1):
            left_list = prev_data[i]
            right_list = prev_data[n - 1 - i - 1]
            for x in left_list:
                for y in right_list:
                    new_data = "{}{}".format(x, y)
                    if new_data not in ret_set:
                        ret_set.add(new_data)
                        ret_list.append(new_data)
        prev_data.append(ret_list)

if __name__ == '__main__':
    Solution().generateParenthesis(8)