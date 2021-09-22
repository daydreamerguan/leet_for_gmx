class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result_list = []
        same = True
        index = 0
        length_list = [len(x) for x in strs]
        min_length = min(length_list)
        str_length = len(strs)
        while same and index < min_length:
            for i in xrange(0, str_length):
                if strs[0][index] != strs[i][index]:
                    same = False
                    break
            if same:
                result_list.append(strs[0][index])
                index += 1
        return "".join(result_list)

if __name__ == '__main__':
    print Solution().longestCommonPrefix(["flower","flow","flight"])
    print Solution().longestCommonPrefix(["dog","racecar","car"])