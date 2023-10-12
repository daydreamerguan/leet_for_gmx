class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        sum_list = []
        size = len(s)
        s_list = [c for c in s]
        add_state = True
        cnt_value, index = self.parse_int(s_list, 0, size)
        while index < size:
            operation = s_list[index]
            index += 1
            next_value, index = self.parse_int(s_list, index, size)
            if operation in ("+", "-"):
                add_value = cnt_value if add_state else -cnt_value
                sum_list.append(add_value)
                add_state = operation == "+"
                cnt_value = next_value
            else:
                if operation == "*":
                    cnt_value = cnt_value * next_value
                else:
                    cnt_value = int(cnt_value / next_value)
        add_value = cnt_value if add_state else -cnt_value
        sum_list.append(add_value)
        return sum(sum_list)



    def parse_int(self, s_list, index, size):
        value_list = []
        if s_list[index] == "-":
            value_list.append(s_list[index])
            index +=1
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
    print(Solution().calculate("3+2*2"))