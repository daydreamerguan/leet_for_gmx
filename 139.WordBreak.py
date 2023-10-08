class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        s_len = len(s)
        max_word_len = 0
        min_word_len = 300
        wordSet = set(wordDict)
        for word in wordDict:
            len_word = len(word)
            if len_word > max_word_len:
                max_word_len = len_word
            if len_word < min_word_len:
                min_word_len = len_word
        dp_list = [False for i in xrange(0, s_len + 1)]
        dp_list[0] = True
        for i in xrange(1, s_len + 1):
            for j in xrange(min_word_len, max_word_len + 1):
                start_pos = i - j
                if start_pos < 0:
                    break
                if not dp_list[start_pos]:
                    continue
                sub_str = s[start_pos: i]
                if sub_str in wordSet:
                    dp_list[i] = True
                    continue
        # print dp_list
        return dp_list[s_len]