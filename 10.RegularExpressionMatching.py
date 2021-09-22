class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        matching_dp_list = []
        for x in xrange(0, len(s) + 1):
            cnt_list = []
            for y in xrange(0, len(p) + 1):
                cnt_list.append(False)
            matching_dp_list.append(cnt_list)
        for x in xrange(0, len(s ) + 1):
            for y in xrange(0, len(p) + 1):
                if y == 0 and x == 0:
                    matching_dp_list[x][y] = True
                else:
                    matching_dp_list[x][y] = self.match(s, p, x, y, matching_dp_list)
        # for i in matching_dp_list:
        #    print i
        return matching_dp_list[len(s)][len(p)]

    def match_dot(self, cnt_s, cnt_p, x, y, matching_dp_list):
        if len(cnt_s) == 0:
            return False
        return matching_dp_list[x - 1][y - 1]

    def match_asterisk(self, cnt_s, cnt_p, x, y, matching_dp_list, s, p):
        if cnt_s == "":
            return matching_dp_list[x][y - 2]
        result = matching_dp_list[x][y - 2] or (matching_dp_list[x - 1][y] and (p[y - 2] == s[x - 1] or p[y - 2] == "."))
        return result
        '''
        result = matching_dp_list[x][y - 2] or matching_dp_list[x][y - 1]
        if cnt_s != "":
            result = result or (matching_dp_list[x - 1][y] and (p[y - 2] == s[x - 1] or p[y - 2] == "."))
        
        '''

    def match_normal(self, cnt_s, cnt_p, x, y, matching_dp_list):
        return cnt_s == cnt_p and matching_dp_list[x - 1][y -1]

    def match(self, s, p, x, y, matching_dp_list):
        cnt_s = ""
        if x > 0:
            cnt_s = s[x - 1]
        cnt_p = p[y - 1] if y > 0 else ""
        if cnt_p == ".":
            # print x, y, "match_dot"
            return self.match_dot(cnt_s, cnt_p, x, y, matching_dp_list)
        elif cnt_p == "*":
            # print x, y, "match_asterisk"
            return self.match_asterisk(cnt_s, cnt_p, x, y, matching_dp_list, s, p)
        else:
            # print x, y, "match_normal"
            return self.match_normal(cnt_s, cnt_p, x, y, matching_dp_list)

if __name__ == '__main__':
    # "aaba", "ab*a*c*a"

    print Solution().isMatch("aaa", "a")

