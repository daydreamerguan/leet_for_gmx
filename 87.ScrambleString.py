class Solution(object):



    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return self.isScrambleWithDict((s1, s2), 0, len(s1), 0, len(s2), {})

    def is_result_exist(self, start_s1, end_s1, start_s2, end_s2, result_dict):
        if start_s1 not in result_dict:
            return False
        if end_s1 not in result_dict[start_s1]:
            return False
        if start_s2 not in result_dict[start_s1][end_s1]:
            return False
        if end_s2 not in result_dict[start_s1][end_s1][start_s2]:
            return False
        return True

    def put_result(self, start_s1, end_s1, start_s2, end_s2, result_dict, result):
        if start_s1 not in result_dict:
            result_dict[start_s1] = {}
        if end_s1 not in result_dict[start_s1]:
            result_dict[start_s1][end_s1] = {}
        if start_s2 not in result_dict[start_s1][end_s1]:
            result_dict[start_s1][end_s1][start_s2] = {}
        result_dict[start_s1][end_s1][start_s2][end_s2] = result

    def get_result(self, start_s1, end_s1, start_s2, end_s2, result_dict):
        return result_dict[start_s1][end_s1][start_s2][end_s2]

    def isScrambleWithDict(self, s1_s2_tuple, start_s1, end_s1, start_s2, end_s2, result_dict):
        range1 = end_s1 - start_s1
        range2 = end_s2 - start_s2
        if range1 != range2:
            print 'Error range', start_s1, end_s1, start_s2, end_s2
            assert False
            return False
        if range1 == 1:
            return s1_s2_tuple[0][start_s1] == s1_s2_tuple[1][start_s2]

        if self.is_result_exist(start_s1, end_s1, start_s2, end_s2, result_dict):
            return self.get_result(start_s1, end_s1, start_s2, end_s2, result_dict)
        final_result = False
        for i in xrange(1, range1):
            # print start_s1, end_s1, start_s2, end_s2, i
            prefix_start_s1 = start_s1
            prefix_end_s1 = start_s1 + i
            subfix_start_s1 = start_s1 + i
            subfix_end_s1 = end_s1

            prefix_start_s2 = start_s2
            prefix_end_s2 = start_s2 + i
            subfix_start_s2 = start_s2 + i
            subfix_end_s2 = end_s2

            rev_prefix_start_s2 = end_s2 - i
            rev_prefix_end_s2 = end_s2
            rev_subfix_start_s2 = start_s2
            rev_subfix_end_s2 = end_s2 - i
            # prefix_result = self.isScrambleWithDict(s1_s2_tuple, prefix_start_s1, prefix_end_s1, prefix_start_s2, prefix_end_s2, result_dict)
            # subfix_result = self.isScrambleWithDict(s1_s2_tuple, subfix_start_s1, subfix_end_s1, subfix_start_s2, subfix_end_s2, result_dict)
            # cnt_result = prefix_result and subfix_result
            cnt_result = self.isScrambleWithDict(s1_s2_tuple, prefix_start_s1, prefix_end_s1, prefix_start_s2, prefix_end_s2, result_dict) and self.isScrambleWithDict(s1_s2_tuple, subfix_start_s1, subfix_end_s1, subfix_start_s2, subfix_end_s2, result_dict)
            if not cnt_result:
                cnt_result = self.isScrambleWithDict(s1_s2_tuple, prefix_start_s1, prefix_end_s1, rev_prefix_start_s2, rev_prefix_end_s2, result_dict) and self.isScrambleWithDict(s1_s2_tuple, subfix_start_s1, subfix_end_s1, rev_subfix_start_s2, rev_subfix_end_s2, result_dict)

            if cnt_result:
                final_result = cnt_result
                break
        self.put_result(start_s1, end_s1, start_s2, end_s2, result_dict, final_result)
        return final_result

if __name__ == '__main__':
    print Solution().isScramble("abcde","caebd")
    print Solution().isScramble("ab","ab")
    print Solution().isScramble("ba","ab")
    print Solution().isScramble("b","b")
    print Solution().isScramble("great","rgeat")
    print Solution().isScramble("abcdbdac","bdacabcd")
    print Solution().isScramble("abcdba","baabcd")


"abcdbdacbdac"
"bdacabcdbdac"

