class WordDictionary(object):
    class TrieNode(object):
        def __init__(self, char):
            self.val = char
            self.subnodes = {}
            self.is_end = False

        def contain(self, char):
            return char in self.subnodes

        def add_node(self, char):
            self.subnodes[char] = WordDictionary.TrieNode(char)

        def get_subnode(self, char):
            assert(self.contain(char))
            return self.subnodes[char]

        def fit_char_list(self, char_list, index, size):
            if index == size:
                if self.is_end:
                    return True
                else:
                    return False
            char = char_list[index]
            if char != ".":
                if char in self.subnodes:
                    return self.subnodes[char].fit_char_list(char_list, index + 1, size)
                else:
                    return False
            else:
                for k, v in self.subnodes.iteritems():
                    if v.fit_char_list(char_list, index + 1, size):
                        return True
                return False


    def __init__(self):
        self.root = WordDictionary.TrieNode(None)

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        if not word:
            return
        cnt_node = self.root
        for char in word:
            if not cnt_node.contain(char):
                cnt_node.add_node(char)
            cnt_node = cnt_node.get_subnode(char)
        cnt_node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        char_list = [char for char in word]
        size = len(char_list)
        return self.root.fit_char_list(char_list, 0, size)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)