# https://www.zhihu.com/question/21923021
# kmp @ zhihu
class Solution(object):

    # typical kmp algorithm
    # lazy function
    def inner_function_implemention(self, haystack, needle):
        return haystack.find(needle)

    def build_next_array(self, needle):
        ret_array = [0, ]
        cnt_index = 1
        

    def standard_kmp(self, haystack, needle):
        return

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        use_inner_function = True
        if use_inner_function:
            return self.inner_function_implemention(haystack, needle)


        