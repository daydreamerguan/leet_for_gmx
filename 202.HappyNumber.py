class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt_num = n
        visited_nums = set()
        while cnt_num != 1:
            cnt_num = self.get_min_equivalent_n(cnt_num)
            if cnt_num in visited_nums:
                return False
            visited_nums.add(cnt_num)
            cnt_num = self.get_next_n(cnt_num)
        return True

    def get_next_n(self, n):
        ret_list = []
        cnt_num = n
        while cnt_num > 0:
            mod_num = cnt_num % 10
            ret_list.append(mod_num)
            cnt_num -= mod_num
            cnt_num /= 10
        ret_num = 0
        for num in ret_list:
            ret_num += (num ** 2)
        return ret_num

    def get_min_equivalent_n(self, n):
        ret_list = []
        cnt_num = n
        while cnt_num > 0:
            mod_num = cnt_num % 10
            ret_list.append(mod_num)
            cnt_num -= mod_num
            cnt_num /= 10
        ret_list.sort()
        ret_num = 0
        for num in ret_list:
            ret_num *= 10
            ret_num += num
        return ret_num

