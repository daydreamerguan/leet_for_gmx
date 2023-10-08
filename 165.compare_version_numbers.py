class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v_list1 = self.get_version_list(version1)
        v_list2 = self.get_version_list(version2)
        return self.compare_version_list(v_list1, v_list2)

    def compare_version_list(self, list1, list2):
        len1 = len(list1)
        len2 = len(list2)
        max_len = max(len1, len2)
        for i in xrange(0, max_len):
            v1 = 0
            v2 = 0
            if i < len1:
                v1 = list1[i]
            if i < len2:
                v2 = list2[i]
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

    def get_version_list(self, ver_str):
        v_str_list = ver_str.split(".")
        v_int_list = []
        for v_str in v_str_list:
            v_int_list.append(self.get_version_of_string(v_str))
        return v_int_list

    def get_version_of_string(self, in_str):
        index = 0
        str_len = len(in_str)
        while index < str_len and in_str[index] == "0":
            index += 1
        if index >= str_len:
            return 0
        return int(in_str[index:])