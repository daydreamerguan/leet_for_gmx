class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result_list = []
        index_a = len(a) - 1
        index_b = len(b) - 1
        add = 0
        while index_a >= 0 or index_b >= 0:
        	a_value = 0 if index_a < 0 or a[index_a] != "1" else 1
        	b_value = 0 if index_b < 0 or b[index_b] != "1" else 1
        	result = a_value + b_value + add
        	add = result / 2
        	result_list.append(result % 2)
        	index_a -= 1
        	index_b -= 1
       	if add > 0:
       		result_list.append(1)
       	result_list.reverse()
       	str_result_list = [str(i) for i in result_list]
       	return "".join(str_result_list)