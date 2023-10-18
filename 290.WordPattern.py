class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word_list = s.split(" ")
        pattern_mapping = {}
        word_mappping = {}
        if len(pattern) != len(word_list):
            return False
        for index, word in enumerate(word_list):
            character = pattern[index]
            if word in pattern_mapping:
                if pattern_mapping[word] != character :
                    return False
            if character in word_mappping:
                if word_mappping[character] != word:
                    return False
            pattern_mapping[word] = character
            word_mappping[character] = word
        return True