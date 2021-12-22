class Solution(object):


    def IsPalindrome(self, s):
        s_len = len(s)
        left = 0
        right = s_len - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        s_len = len(s)
        palindrome_list = []
        for i in xrange(0, s_len):
            cnt_list = []
            for j in xrange(i, s_len):
                sub_s = s[i:j + 1]
                if self.IsPalindrome(sub_s):
                    cnt_list.append(j + 1)
            palindrome_list.append(cnt_list)

        ret_list = []
        self.getAllPartition(s, palindrome_list, ret_list, 0, [], s_len)
        return ret_list

    def getAllPartition(self, s, palindrome_list, ret_list, index, cnt_list, s_len):
        if not palindrome_list:
            return
        if index >= s_len:
            ret_list.append([p for p in cnt_list])
            return
        cnt_palindrome_list = palindrome_list[index]
        for end_index in cnt_palindrome_list:
            cnt_list.append(s[index:end_index])
            self.getAllPartition(s, palindrome_list, ret_list, end_index, cnt_list, s_len)
            cnt_list.pop()
