MAX_VALUE_STR = str(2**31 - 1)
MIN_VALUE_STR = str((-2)**31)
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = self.trim_leading_white_space(s)
        if len(s) == 0:
            return 0
        sign, leading_index = self.detetmine_sign(s)
        s = s[leading_index:]
        s= self.read_digits(s)
        if len(s) == 0:
            s = "0"

        return max(min(int(s) *sign, 2**31 - 1), (-2)**31)

    def read_digits(self, s):
        index = 0
        len_s = len(s)
        digit_list = []
        while index < len_s and s[index] == "0":
            index += 1

        while index < len_s and s[index] in "0123456789":
            digit_list.append(s[index])
            index += 1
        return "".join(digit_list)


    def detetmine_sign(self, s):
        len_s = len(s)
        if len_s == 0:
            return 1, 0
        if s[0] == "-":
            return -1, 1

        elif s[0] == "+":
            return 1, 1
        return 1, 0
    
    def trim_leading_white_space(self, s):
        index = 0
        len_s = len(s)
        while (index < len_s and s[index] == " "):
            index += 1
        return s[index:]

    def BiggerThanMax(self, s):
        if len(s) < len(MAX_VALUE_STR):
            return False
        return cmp(s, MAX_VALUE_STR) > 0

    def LessThanMin(self, s):
        if len(s) < len(MIN_VALUE_STR):
            return False
        return cmp(s, MIN_VALUE_STR) > 0

if __name__ == '__main__':
    print Solution().myAtoi("   -42")