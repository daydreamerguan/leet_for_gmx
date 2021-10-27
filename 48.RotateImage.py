class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_dict = {}
        visited_strs = set()
        for cnt_str in strs:
            visited_strs.add(cnt_str)
            str_list = [x for x in cnt_str]
            if not str_list:
                str_list = ["",]
            str_list.sort()
            first_str = "".join(str_list)
            if first_str not in result_dict:
                result_dict[first_str] = []
            result_dict[first_str].append(cnt_str)
        result = []
        for k, v in result_dict.iteritems():
            result.append(v)
        return result
