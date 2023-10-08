class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt_index = 0
        while cnt_index < len_s and s[cnt_index] == " ":
            cnt_index += 1
        cnt_start = cnt_index
        len_s = len(s)
        word_list = []
        while cnt_index < len_s:
            if s[cnt_index] != " ":
                cnt_index += 1
                continue
            else:
                word_list.append(s[cnt_start: cnt_index])
                while cnt_index < len_s and s[cnt_index] == " ":
                    cnt_index += 1
                cnt_start = cnt_index
        if cnt_start < cnt_index:
            # last one
            word_list.append(s[cnt_start:])
        word_list.reverse()
        return " ".join(word_list)

