class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in xrange(0, len(numbers)):
            # ignore same num
            if index > 0 and numbers[index] == numbers[index - 1]:
                continue
            search_num = target - numbers[index]
            found_index = self.find_target_index(numbers, 0, len(numbers), index, search_num)
            if found_index != -1:
                return [index + 1, found_index + 1]

    def find_target_index(self, numbers, num_start, num_end, used_index, search_num):
        if num_start >= num_end:
            return -1
        mid_index = int ((num_start + num_end) / 2)
        if numbers[mid_index] > search_num:
            return self.find_target_index(numbers, num_start, mid_index, used_index, search_num)
        elif numbers[mid_index] < search_num:
            return self.find_target_index(numbers, mid_index + 1, num_end, used_index, search_num)
        else:
            # search not used_index
            if mid_index == used_index:
                len_num = len(numbers)
                if mid_index + 1 < len_num and numbers[mid_index + 1] == search_num:
                    return mid_index + 1
            else:
                return mid_index