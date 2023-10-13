class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        cnt_num = num
        while cnt_num >= 10:
            result_list = []
            while cnt_num > 0:
                mod = cnt_num % 10
                result_list.append(mod)
                cnt_num -= mod
                cnt_num /= 10
            cnt_num = sum(result_list)

        return cnt_num