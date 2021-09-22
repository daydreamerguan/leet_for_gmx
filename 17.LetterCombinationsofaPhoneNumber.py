number_digits_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution(object):

    def letterOperation(self, digits, index, result_set, cnt_result, digits_length):
        if index >= digits_length:
            return
        for x in number_digits_map[digits[index]]:
            result = cnt_result + x
            if index == digits_length - 1:
                if result not in result_set:
                    result_set.add(result)
            else:
                self.letterOperation(digits, index + 1, result_set, result, digits_length)


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result_set = set()
        self.letterOperation(digits, 0, result_set, "", len(digits))
        result_list = list(result_set)
        result_list.sort()
        return result_list

if __name__ == '__main__':
    print Solution().letterCombinations("23")
    print Solution().letterCombinations("")
    print Solution().letterCombinations("2")
