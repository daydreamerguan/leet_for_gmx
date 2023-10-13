class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ret_map = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c not in ret_map:
                ret_map[c] = 0
            ret_map[c] += 1
        for c in t:
            if c in ret_map:
                ret_map[c] -= 1
                if ret_map[c] == 0:
                    del ret_map[c]
        return len(ret_map) == 0
