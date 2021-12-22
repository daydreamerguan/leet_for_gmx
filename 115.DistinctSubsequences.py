class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp_list = []
        s_len = len(s)
        t_len = len(t)
        for i in xrange(0, s_len + 1):
            dp_list.append([0 for temp in xrange(0, t_len + 1)])

        for i in xrange(0, s_len + 1):
            for j in xrange(0, t_len + 1):
                if i == 0 and j == 0:
                    dp_list[i][j] = 1
                    continue
                if j > i:
                    dp_list[i][j] = 0
                s_i = ""
                t_j = ""
                if i > 0:
                    s_i = s[i - 1]
                if j > 0:
                    t_j = t[j - 1]
                if s_i == t_j:
                    dp_list[i][j] = dp_list[i - 1][j - 1] + dp_list[i - 1][j]
                else:
                    dp_list[i][j] = dp_list[i - 1][j]

        return dp_list[s_len][t_len]

