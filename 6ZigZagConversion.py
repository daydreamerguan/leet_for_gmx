class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arraylist = []
        for index in xrange(0, numRows):
        	arraylist.append([])

        col = 0
        direction = 0
        index = 0
        len_s = len(s)
        while index < len_s:
        	arraylist[col].append(s[index])
        	#print "col", col, "append", s[index]
        	if direction == 0:
        		if col + 1 >= numRows:
        			col -= 1
        			direction = 1
        		else:
        			col += 1
        	else:
        		if col - 1 < 0:
        			col += 1
        			direction = 0
        		else:
        			col -= 1
        	index += 1
        result_list = []
        for array in arraylist:
        	result_list.append("".join(array))

        return "".join(result_list)

if __name__ == '__main__':
	print Solution().convert("PAYPALISHIRING", 4)