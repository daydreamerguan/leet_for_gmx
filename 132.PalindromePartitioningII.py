class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        if len_s == 0:
            return 0
        dp_list = []
        is_palindrome_list = []
        for i in xrange(0, len_s):
            dp_list.append(i)
            is_palindrome_list.append([False for j in xrange(0, len_s)])

        for  i in xrange(0, len_s):
            for j in xrange(0, i + 1):
                if s[i] == s[j] and (i - j < 2 or is_palindrome_list[j + 1][i - 1]):
                    is_palindrome_list[j][i] = True
                    if j == 0:
                        dp_list[i] = 0
                    else:
                        dp_list[i] = min(dp_list[i], dp_list[j - 1] + 1)
        return dp_list[-1]