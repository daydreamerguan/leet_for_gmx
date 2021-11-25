class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        result_count = [0]
        valid_set = set()
        for i in xrange(1, 27):
            valid_set.add(str(i))
        if s_len == 0:
            return 0
        result_dict = {}
        return self.dfsDecoding(s, 0, s_len, valid_set, result_dict)


    def dfsDecoding(self, s, index, s_len, valid_set, result_dict):
        if index >= s_len:
            return 1
        result = 0
        if index in result_dict:
            return result_dict[index]
        for i in xrange(1, 3):
            next_index = index + i
            if next_index > s_len:
                continue
            sub_s = s[index:next_index]
            if sub_s not in valid_set:
                continue
            result += self.dfsDecoding(s, next_index, s_len, valid_set, result_dict)
        result_dict[index] = result
        return result

if __name__ == '__main__':
    print Solution().numDecodings("12")
    print Solution().numDecodings("226")
    print Solution().numDecodings("0")
    print Solution().numDecodings("06")
    print Solution().numDecodings("111111111111111111111111111111111111111111111")

