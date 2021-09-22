class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        cnt_s = s
        index = 0
        result_int = 0
        while cnt_s:
            if not cnt_s.startswith(roman_list[index]):
                index += 1
            else:
                result_int += num_list[index]
                cnt_s = cnt_s[len(roman_list[index]):]
        return result_int

if __name__ == '__main__':
    print Solution().romanToInt("LVIII")
    print Solution().romanToInt("MCMXCIV")


