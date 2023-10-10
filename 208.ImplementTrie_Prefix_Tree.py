class Trie(object):
    class TrieNode(object):
        def __init__(self, char):
            self.val = char
            self.subnodes = {}
            self.is_end = False

        def contain(self, char):
            return char in self.subnodes

        def add_node(self, char):
            self.subnodes[char] = Trie.TrieNode(char)

        def get_subnode(self, char):
            assert(self.contain(char))
            return self.subnodes[char]

    def __init__(self):
        self.root = Trie.TrieNode(None)

    def insert(self, word):
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
        if not word:
            return False
        cnt_node = self.root
        for char in word:
            if not cnt_node.contain(char):
                return False
            cnt_node = cnt_node.get_subnode(char)
        return cnt_node.is_end


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return True
        cnt_node = self.root
        for char in prefix:
            if not cnt_node.contain(char):
                return False
            cnt_node = cnt_node.get_subnode(char)
        return cnt_node is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)