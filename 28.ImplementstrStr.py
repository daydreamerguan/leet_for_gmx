# https://www.zhihu.com/question/21923021
# kmp @ zhihu
class Solution(object):

    # typical kmp algorithm
    # lazy function
    def inner_function_implemention(self, haystack, needle):
        return haystack.find(needle)

    def build_next_array(self, needle):
        len_needle = len(needle)
        ret_array = [-1] * (len_needle + 1) 
        cnt_index = 1
        index = 0
        pattern_index = -1
        while index < len_needle:
            if pattern_index == -1 or needle[index] == needle[pattern_index]:
                index += 1
                pattern_index += 1
                ret_array[index] = pattern_index
            else:
                pattern_index = ret_array[pattern_index]
        return ret_array
        

    def standard_kmp(self, haystack, needle):
        next_list  = self.build_next_array(needle)
        len_str = len(haystack)
        len_needle = len(needle)
        str_index = 0
        pattern_index = 0
        while str_index < len_str and pattern_index < len_needle:
            if pattern_index == -1 or haystack[str_index] == needle[pattern_index]:
                str_index += 1
                pattern_index += 1
            else:
                pattern_index = next_list[pattern_index]

        if pattern_index == len_needle: # j走到了末尾，说明匹配到了
            return str_index - pattern_index
        else:
            return -1

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        use_inner_function = False
        if use_inner_function:
            return self.inner_function_implemention(haystack, needle)
        return self.standard_kmp(haystack, needle)


        