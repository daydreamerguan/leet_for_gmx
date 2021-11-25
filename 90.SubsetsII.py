class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
        num_items = nums_dict.items()
        nums_size = len(num_items)
        result_list = []
        self.getSubset(0, result_list, num_items, nums_size, [])
        return result_list

    def getSubset(self, index, result_list, num_items, nums_size, item_counts):
        if index == nums_size:
            cnt_result = []
            for cnt_index, count in enumerate(item_counts):
                for i in xrange(0, count):
                    cnt_result.append(num_items[cnt_index][0])
            result_list.append(cnt_result)
            return
        cnt_counts = num_items[index][1]
        for i in xrange(0, cnt_counts + 1):
            item_counts.append(i)
            self.getSubset(index + 1, result_list, num_items, nums_size, item_counts)
            item_counts.pop()

if __name__ == '__main__':
    print Solution().subsetsWithDup([1,2,2])
    print Solution().subsetsWithDup([0])