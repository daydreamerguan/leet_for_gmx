class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace("e", "E")
        s_list = s.split("E")
        if len(s_list) > 2:
            return False
        if len(s_list) == 1:
            return self.IsDecimalOrInteger(s_list[0])
        if not s_list[0]:
            return False
        else:
            return self.IsDecimalOrInteger(s_list[0]) and self.IsSignInteger(s_list[1])

    def IsDecimalOrInteger(self, s):
        if s.startswith("+") or s.startswith("-"):
            return self.IsDecimal(s[1:])
        else:
            return self.IsDecimal(s)

    def IsSignInteger(self, s):
        if s.startswith("+") or s.startswith("-"):
            return self.IsInteger(s[1:])
        else:
            return self.IsInteger(s)

    def IsDecimal(self, s):
        if not s:
            return False
        if s.find(".") == -1:
            return self.IsInteger(s)
        s_list = s.split(".")
        if len(s_list) > 2:
            return False
        if len(s_list) == 1:
            return self.IsInteger(s_list[0])
        if not s_list[0]:
            return self.IsInteger(s_list[1])
        else:
            result = self.IsInteger(s_list[0]) 
            if s_list[1]:
                return  result and self.IsInteger(s_list[1]) 
            return result

    def IsInteger(self, s):
        if not s:
            return False
        for i in s:
            if ord(i) < ord("0") or ord(i) > ord("9"):
                return False
        return True

if __name__ == '__main__':
    valid_list = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    invalid_list = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    for item in valid_list:
        print Solution().isNumber(item)
    for item in invalid_list:
        print Solution().isNumber(item)



