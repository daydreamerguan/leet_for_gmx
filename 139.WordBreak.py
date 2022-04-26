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
        sub_s_dp_list = []
        for i in xrange(0, s_len):
            sub_s_dp_list.append([False for j in xrange(0, s_len + 1)])
        for i in xrange(0, s_len):
            for j in xrange(i + min_word_len, min(s_len, i + max_word_len) + 1):
                sub_str = s[i:j]
                print sub_str
                if sub_str in wordSet:
                    sub_s_dp_list[i][j] = True
        dp_list = [False for i in xrange(0, s_len + 1)]
        dp_list[0] = True
        for i in xrange(1, s_len + 1):
            if not dp_list[i - 1]:
                continue
            start_pos = i - 1
            for j in xrange(min_word_len, max_word_len + 1):
                if start_pos + j > s_len:
                    break
                print "test", start_pos, start_pos + j 
                if sub_s_dp_list[i][start_pos + j]:
                    dp_list[start_pos + j] = True
        print dp_list
        return dp_list[s_len]

if __name__ == '__main__':
    print Solution().wordBreak("applepenapple", ["apple","pen"])


