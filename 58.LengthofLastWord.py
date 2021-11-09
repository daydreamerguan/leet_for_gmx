class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt_index = len(s) - 1
        last_len = 0
        while cnt_index >= 0 and s[cnt_index] == " ":
            cnt_index -= 1
        while cnt_index >= 0:
            if s[cnt_index]!= " ":
                last_len += 1
                cnt_index -= 1
            else:
                break
        return last_len 
