class Solution(object):
    def intToRoman(self, num):
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


        """
        :type num: int
        :rtype: str
        """
        result_list = []
        cnt_num = num
        index = 0
        while cnt_num != 0:
            if cnt_num < num_list[index]:
                index += 1
            else:
                cnt_num -= num_list[index]
                result_list.append(roman_list[index])
        return "".join(result_list)

if __name__ == '__main__':
    print Solution().intToRoman(58)
    print Solution().intToRoman(1994)
    print Solution().intToRoman(3999)

                                                                                                                