class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        return self.do_compute(expression)

    def do_compute(self, s):
        s = s.replace(" ", "")
        value_list = []
        size = len(s)
        s_list = [c for c in s]
        value, index = self.parse_int(s_list, 0, size)
        value_list.append(value)
        operation_list = []
        while index < size:
            operation = s_list[index]
            operation_list.append(operation)
            index += 1
            value, index = self.parse_int(s_list, index, size)
            value_list.append(value)
        dp_list = []
        dp_list1 = [[v,] for v in value_list]
        dp_list.append(dp_list1)
        value_size = len(dp_list1)
        # print("value_size", value_size)
        for next_level_length in range(2, value_size + 1):
            cnt_dp = []
            start_index = 0
            end_index = start_index + next_level_length
            while end_index <= value_size:
                cnt_dp.append(self.merge_compute_result(start_index, end_index, dp_list, operation_list))
                start_index +=1
                end_index +=1
            dp_list.append(cnt_dp)
        return dp_list[-1][0]

    def merge_compute_result(self, start_index, end_index, dp_list, operation_list):
        merge_size = end_index - start_index
        result_list = []
        #print(start_index, end_index)
        for left_size in range(1, merge_size):
            
            left_set = dp_list[left_size - 1][start_index]
            right_size = merge_size - left_size
            right_start_index = start_index + left_size
            # print(dp_list, merge_size, right_start_index)
            right_set = dp_list[right_size - 1][right_start_index]
            operation = operation_list[right_start_index -1]
            self.merge_two_set(left_set, right_set, operation, result_list)
        return result_list

    def merge_two_set(self, list_left, list_right, operation, result_list):
        set_left = set(list_left)
        set_right = set(list_right)
        for left in list_left:
            for right in list_right:
                if operation == "+":
                    result_list.append(left + right)
                elif operation == "-":
                    result_list.append(left - right)
                else:
                    result_list.append(left * right)


    def parse_int(self, s_list, index, size):
        value_list = []
        ord_zero = ord("0")
        ord_nine = ord("9")
        while index < size:
            if ord_zero <= ord(s_list[index]) <= ord_nine:
                value_list.append(s_list[index])
                index += 1
            else:
                break
        return int("".join(value_list), 10), index


if __name__ == '__main__':
    # print(Solution().diffWaysToCompute("2*3-4*5"))
    pass