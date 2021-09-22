MAX_VALUE_STR = str(2**31 - 1)
MIN_VALUE_STR = str((-2)**31)
print MAX_VALUE_STR, MIN_VALUE_STR
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        abs_str_x = str(abs(x))
        if x < 0:
            str_x = "-" + abs_str_x[::-1]
            if self.LessThanMin(str_x):
                return 0
            else:
                return int(str_x)
        else:
            str_x = str_x[::-1]
            if self.BiggerThanMax(str_x):
                return 0
            else:
                return int(str_x)

    def BiggerThanMax(self, s):
        if len(s) < len(MAX_VALUE_STR):
            return False
        return cmp(s, MAX_VALUE_STR) > 0

    def LessThanMin(self, s):
        if len(s) < len(MIN_VALUE_STR):
            return False
        return cmp(s, MIN_VALUE_STR) > 0