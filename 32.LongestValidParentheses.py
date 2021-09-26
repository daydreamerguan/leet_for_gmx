# -*- coding: UTF-8 -*-

class Solution(object):


    def push_new_range_to_range_list(self, rangelist, new_range):
        if len(rangelist) == 0:
            rangelist.append(new_range)
            return
        last_range = rangelist[-1]
        if last_range[1] + 1 == new_range[0]:
            rangelist.pop()
            self.push_new_range_to_range_list(rangelist, [last_range[0], new_range[1]])
        elif last_range[0] - 1 == new_range[0] and last_range[1] + 1 == new_range[1]:
            rangelist.pop()
            self.push_new_range_to_range_list(rangelist, new_range)
        else:
            rangelist.append(new_range)
            return

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        stack_array = []
        valid_sub_range_list = []
        for index, x in enumerate(s):
            if x == "(":
                stack_array.append(["(", index])
            else:
                if len(stack_array) > 0:
                    if stack_array[-1][0] == "(":
                        last_item = stack_array.pop()
                        self.push_new_range_to_range_list(valid_sub_range_list, [last_item[1], index])
                else:
                    # add 
                    stack_array.append([")", index])

        max_len_start = -1 
        max_len_end = -1
        for cnt_range in valid_sub_range_list:
            new_len = cnt_range[1] - cnt_range[0] + 1
            if new_len > max_length:
                max_length = new_len
                max_len_start = cnt_range[0]
                max_len_end = cnt_range[1]
        return max_length

if __name__ == '__main__':
    print Solution().longestValidParentheses("(()")
    print Solution().longestValidParentheses(")()())")
    print Solution().longestValidParentheses("")