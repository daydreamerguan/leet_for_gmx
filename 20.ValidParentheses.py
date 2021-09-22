# -*- coding: UTF-8 -*-
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        push_stack_character_dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        pop_stack_character_dict = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        waiting_match_list = []
        match_index = -1
        for x in s:

            if x in push_stack_character_dict:
                waiting_match_list.append(x)
                match_index += 1

            else:
                if match_index == -1:
                    return False
                match_index -= 1
                match_left = waiting_match_list.pop()
                if pop_stack_character_dict[x] != match_left:
                    return False

        return match_index == -1

if __name__ == '__main__':
    print Solution().isValid("()")
    print Solution().isValid("()[]{}")
    print Solution().isValid("(]")
    print Solution().isValid("([)]")
    print Solution().isValid("{[]}")
