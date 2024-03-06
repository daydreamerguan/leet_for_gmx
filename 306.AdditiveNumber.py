class Solution(object):
    def checkAdditive(self, num_str, first_end, second_end):
        first_str = num_str[0:first_end]
        second_str = num_str[first_end: second_end]

        next_change = 0
        left_str = num_str[second_end:]
        while left_str != "":

            if first_str.startswith("0") and len(first_str) > 1:
                return False
            if second_str.startswith("0") and len(second_str) > 1:
                return False
            add_result = int(first_str) + int(second_str)
            print("checkAdditive", first_str, second_str, left_str)
            add_result_str = str(add_result)
            
            if not left_str.startswith(add_result_str):
                return False
            if next_change == 0:
                first_str = add_result_str
            else:
                second_str = add_result_str
            next_change = (next_change + 1) % 2
            left_str = left_str[len(add_result_str):]
        return True


    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_len = len(num)
        if num_len < 3:
            return False
        item = []
        for left_index in range(1, num_len - 1):
            for right_index in range(left_index + 1, num_len):
                print(left_index, right_index)
                if self.checkAdditive(num, left_index, right_index):
                    return True
        return False

if __name__ == '__main__':
    obj = Solution()
    # print(obj.isAdditiveNumber("123"))
    # print(obj.isAdditiveNumber("112358"))
    # print(obj.isAdditiveNumber("199100199"))
    # print(obj.isAdditiveNumber("199100199299"))
    # print(obj.isAdditiveNumber("199100199299499"))

        