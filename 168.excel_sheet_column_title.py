class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        left_num = columnNumber
        result_list = []
        while True:
            left_num -= 1
            mod_num = left_num % 26
            div_num = int(left_num / 26)
            left_num = div_num
            result_list.append(mod_num)
            if left_num <= 0:
                break
        result_list.reverse()
        str_list = []
        for num in result_list:
            str_list.append(chr(ord("A") + num))
        return "".join(str_list)
