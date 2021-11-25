class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)
        if len_s1 + len_s2 != len_s3:
        	return False
        dp_matrix = []
        for i in xrange(0, len_s1 + 1):
        	dp_matrix.append([False for j in xrange(0, len_s2 + 1)])
        
        for i in xrange(0, len_s1 + 1):
        	for j in xrange(0, len_s2 + 1):
        		if i + j == 0:
        			dp_matrix[i][j] = True
        			continue
        		s3_character = s3[i + j  - 1]
        		s2_character = s2[j - 1] if j > 0 else ""
        		s1_character = s1[i - 1] if i > 0 else ""
        		if s2_character == s3_character:
        			if dp_matrix[i][j -1]:
        				dp_matrix[i][j] = True
        		if s1_character == s3_character:
        			if dp_matrix[i - 1][j]:
        				dp_matrix[i][j] = True
        return dp_matrix[len_s1][len_s2]

if __name__ == '__main__':
	print Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")
	print Solution().isInterleave(s1 = "", s2 = "", s3 = "")
	print Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")
