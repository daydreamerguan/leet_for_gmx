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
        word_index_dict = {}
        index_word_dict = {}
        for i, word in enumerate(wordDict):
            word_index_dict[word] = i
            index_word_dict[i] = word
        for word in wordDict:
            len_word = len(word)
            if len_word > max_word_len:
                max_word_len = len_word
            if len_word < min_word_len:
                min_word_len = len_word
        dp_list = [{} for i in xrange(0, s_len + 1)]
        dp_list[0][0] = ""
        for i in xrange(1, s_len + 1):
            for j in xrange(min_word_len, max_word_len + 1):
                start_pos = i - j
                if start_pos < 0:
                    break
                if not dp_list[start_pos]:
                    continue
                sub_str = s[start_pos: i]
                if sub_str in wordSet:
                    dp_list[i][start_pos]= word_index_dict[sub_str]
        retword_list = []
        self.backtrack_getword_list(dp_list, s_len, retword_list, [], index_word_dict)
        return retword_list
        # backtrack

    def backtrack_getword_list(self, dp_list, index, retword_list, cnt_word_list, index_word_dict):
        if index == 0:
            word_index_list = reversed(cnt_word_list)
            cnt_word_list = [index_word_dict[i] for i in word_index_list]
            retword_list.append(" ".join(cnt_word_list))
            return
        backtrack_dict = dp_list[index]
        for next_pos, word_index in backtrack_dict.iteritems():
            cnt_word_list.append(word_index)
            self.backtrack_getword_list(dp_list, next_pos, retword_list, cnt_word_list, index_word_dict)
            cnt_word_list.pop()



if __name__ == '__main__':
    print Solution().wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])