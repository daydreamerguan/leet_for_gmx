class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_int_list1 = []
        num_int_list2 = []
        for num in num1:
            num_int_list1.append(int(num))
        for num in num2:
            num_int_list2.append(int(num))
        result_list_reversed = []
        len_num1 = len(num1)
        len_num2 = len(num2)
        index1 = len_num1 - 1
        while index1 >= 0:
            index2 = len_num2 - 1
            cnt_num1 = num_int_list1[index1]
            while index2 >= 0:
                cnt_num2 = num_int_list2[index2]
                result_index = len_num1 - index1 + len_num2 - index2 - 2
                while len(result_list_reversed) < result_index + 1:
                    result_list_reversed.append(0)
                multiply_result = cnt_num1 * cnt_num2
                next_result = multiply_result / 10
                cnt_result = multiply_result % 10
                new_result = cnt_result + result_list_reversed[result_index]
                if new_result >= 10:
                    new_result %= 10
                    next_result += 1
                result_list_reversed[result_index] = new_result
                index_next = 2
                while next_result > 0:
                    if len(result_list_reversed)  < result_index + index_next:
                        result_list_reversed.append(0)
                    new_next_result = result_list_reversed[result_index + index_next - 1] + next_result
                    new_result = new_next_result % 10
                    next_result = new_next_result / 10
                    result_list_reversed[result_index + index_next - 1] = new_result
                    index_next += 1
                index2 -= 1
            index1 -= 1
        result_list_reversed.reverse()
        final_result = []
        start_with_zero = True
        for item in result_list_reversed:
            if start_with_zero and item == 0:
                continue
            start_with_zero = False
            final_result.append(item)
        if not final_result:
            final_result = [0,]
        return "".join([str(i) for i in final_result])

if __name__ == '__main__':
    Solution().multiply("123", "456")