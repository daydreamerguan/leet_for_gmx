class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ret_val = 0
        for s in columnTitle:
            ret_val *= 26
            cnt_num = ord(s) - ord("A")
            ret_val += (cnt_num + 1)
        return ret_val