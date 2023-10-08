class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        len_s = len(s)
        ones_set = set()
        multi_set = set()
        for index in xrange(0, len_s - 9):
            substr = s[index: index + 10]
            if substr not in ones_set:
                ones_set.add(substr)
            else:
                multi_set.add(substr)
        return list(multi_set)