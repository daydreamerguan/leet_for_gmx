class GraphNode(object):
    def __init__(self, word):
        self.word = word
        self.linked_word_set = set()
        self.target_distance = 1000

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        if beginWord not in wordList:
            word_set.add(beginWord)
        if endWord not in word_set:
            return []
        ret_list = []
        word_length = len(beginWord)
        word_graphnode_dict = {}
        for word in word_set:
            word_graphnode_dict[word] = GraphNode(word)

        for split_index in xrange(0, word_length):
            same_word_dict = {}
            for cnt_word in word_set:
                shift_word = cnt_word[0:split_index] + cnt_word[split_index + 1:]
                # print "shift_word", shift_word
                if shift_word not in same_word_dict:
                    same_word_dict[shift_word] = []
                same_word_dict[shift_word].append(cnt_word)

            for k, v in same_word_dict.iteritems():
                for word in v:
                    word_node = word_graphnode_dict[word]
                    for another_word in v:
                        if word == another_word:
                            continue
                        another_node = word_graphnode_dict[another_word]
                        word_node.linked_word_set.add(another_word)
                        another_node.linked_word_set.add(word)


        
        visited_words = set()
        cnt_word_list = [endWord,]
        visited_words.add(endWord)
        cnt_distance = 0
        while cnt_word_list:
            next_word_list = []
            for visiting_word in cnt_word_list:
                visiting_node = word_graphnode_dict[visiting_word]
                visiting_node.target_distance = cnt_distance
                for next_word in visiting_node.linked_word_set:
                    if next_word not in visited_words:
                        visited_words.add(next_word)
                        # print "visting word", visiting_word, "adding word", next_word
                        next_word_list.append(next_word)
            cnt_word_list = next_word_list
            cnt_distance += 1

        # for k, v in word_graphnode_dict.iteritems():
            # print "word", k, "distance is", v.target_distance, "link to"
            # for link in v.linked_word_set:
            #     print "======", link
        if beginWord not in visited_words:
            return []
        self.findLadderList(beginWord, word_graphnode_dict, [], ret_list)
        return ret_list

    def findLadderList(self, word, word_graphnode_dict, cnt_list, ret_list):
        cnt_node = word_graphnode_dict[word]
        cnt_list.append(word)
        cnt_distance = cnt_node.target_distance
        # print "visiting word"
        if cnt_node.target_distance == 0:
            ret_list.append([x for x in cnt_list])
        else:
            for next_word in cnt_node.linked_word_set:
                next_node = word_graphnode_dict[next_word]
                if next_node.target_distance != cnt_distance - 1:
                    continue
                self.findLadderList(next_word, word_graphnode_dict, cnt_list, ret_list)
        cnt_list.pop()

if __name__ == '__main__':
    print Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])


        