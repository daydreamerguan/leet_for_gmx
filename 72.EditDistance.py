class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_word1 = len(word1)
        len_word2 = len(word2)
        dp_list = []
        for i in xrange(0, len_word1 + 1):
            dp_list.append([ 0 for j in xrange(0, len_word2 + 1)])
        for i in xrange(0, len_word1 + 1):
            for j in xrange(0, len_word2 + 1):
                if i == j == 0:
                    continue
                if i == 0 or j == 0:
                    dp_list[i][j] = abs(i - j)
                    continue
                index1 = i - 1
                index2 = j - 1
                if word1[index1] == word2[index2]:
                    dp_list[i][j] = dp_list[i - 1][j - 1]
                else:
                    dp_list[i][j] = min(dp_list[i - 1][j - 1], dp_list[i][j - 1], dp_list[i - 1][j]) + 1
        return dp_list[len_word1][len_word2]

if __name__ == '__main__':
    print Solution().minDistance("horse", "ros")
    print Solution().minDistance("intention", "execution")
