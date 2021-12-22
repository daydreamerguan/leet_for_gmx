class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.generate(rowIndex + 1)[-1]
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri_list = [[1]]
        for i in xrange(1, numRows):
            last_len = len(tri_list[i -1])
            cnt_list = []
            for j in xrange(0, last_len + 1):
                left_add = tri_list[i - 1][j - 1] if j - 1 >= 0 else 0
                right_add = tri_list[i - 1][j] if j < last_len else 0
                cnt_list.append(left_add + right_add)
            tri_list.append(cnt_list)
        return tri_list