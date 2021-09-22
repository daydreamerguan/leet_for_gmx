class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        ret_len = 0
        size = len(s)
        cnt_character_dict = {}
        for x in xrange(0, size):
            character = s[x]
            if character not in cnt_character_dict:
                cnt_character_dict[character] = x
                
            else:
                delete_index = cnt_character_dict[character]
                for delete_index in xrange(start, delete_index + 1):
                    del cnt_character_dict[s[delete_index]]
                cnt_character_dict[character] = x
                start = delete_index + 1
            if len(cnt_character_dict) > ret_len:
                ret_len = len(cnt_character_dict)
        return ret_len


            