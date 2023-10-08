class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = ""
        if(numerator * denominator < 0):
            flag = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer_part = str(numerator / denominator)

        mod_part = numerator % denominator

        integer_part_dict = {}
        cnt_index = 0
        decimal_parts = []
        if mod_part == 0:
            return flag + integer_part
        while mod_part not in integer_part_dict and mod_part != 0:
            integer_part_dict[mod_part] = cnt_index
            cnt_index += 1
            mod_part *= 10
            decimal_parts.append(str(mod_part / denominator))
            mod_part = mod_part % denominator
        # not repeat
        repeat_start = -1
        if mod_part == 0:
            return flag + integer_part + "." + "".join(decimal_parts)
        else:
            repeat_start = integer_part_dict[mod_part]
            not_repeat_part = "".join(decimal_parts[:repeat_start])
            repeat_part = "".join(decimal_parts[repeat_start:])
            return flag + integer_part + "." + not_repeat_part + "(" + repeat_part + ")"
