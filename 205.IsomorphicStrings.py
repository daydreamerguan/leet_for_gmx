class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        s_mapping_list = self.get_mapping_list(s)
        t_mapping_list = self.get_mapping_list(t)
        for i in xrange(0, len_s):
            if s_mapping_list[i] != t_mapping_list[i]:
                return False
        return True

    def get_mapping_list(self, s):
        ret_list = []
        s_i_map = {}
        index = 0
        for char in s:
            if char not in s_i_map:
                s_i_map[char] = index
                index += 1
            ret_list.append(s_i_map[char])
        return ret_list