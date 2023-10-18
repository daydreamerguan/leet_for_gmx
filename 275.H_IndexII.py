class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size = len(citations)
        if citations[-1]  == 0:
            return 0
        return self.do_find(citations, 0, size, size)

    def do_find(self, citations, left, right, size):
        if left == right:
            return 0
        index = int((left + right) / 2)
        greater_num = size - index
        cnt_cite = citations[index]
        b_is_greater = cnt_cite >= greater_num
        if index == left:
            return greater_num if b_is_greater else 0
        if b_is_greater:
            return max(self.do_find(citations, left, index, size), greater_num)
        else:
            return self.do_find(citations, index + 1, right, size)
