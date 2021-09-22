class NumItem(object):
    """docstring for NumItem"""
    def __init__(self, num, index):
        self.num = num
        self.index = index

def comp_num(a, b):
    return cmp(a.num, b.num);

class Solution(object):


    def search_left(self, item_list, i, left, right, target):
    	# print "search_left", item_list, i, left, right, target
        if left >= right:
            return -1
        mid_index = int(left + right) / 2
        cnt_sum = item_list[i].num +  item_list[mid_index].num
        if cnt_sum == target:
            return mid_index
        elif cnt_sum > target:
            return self.search_left(item_list, i, left, mid_index, target)
        else:
            return self.search_left(item_list, i, mid_index + 1, right, target)

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        item_list = []
        for idx, num in enumerate(nums):
            item_list.append(NumItem(num, idx))
        item_list.sort(cmp=comp_num)
        size = len(item_list)
        for idx in xrange(0, size- 1):
            ret = self.search_left(item_list, idx, idx + 1, size, target)
            if ret >= 0:
                return [item_list[idx].index, item_list[ret].index]


if __name__ == '__main__':
    print Solution().twoSum([3,3], 6)