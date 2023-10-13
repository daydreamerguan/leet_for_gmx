class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        size = len(citations)
        if size == 0:
            return 0
        cnt_cite = 0
        for i, cite in enumerate(citations):
            if cite > i:
                cnt_cite += 1
                continue
            else:
                break
        return cnt_cite