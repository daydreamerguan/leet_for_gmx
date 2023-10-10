class Heap(object):
    def __init__(self, size_limit):
        self.items = []
        self.size_limit = size_limit

    def upFlow(self, index):
        if index == 0:
            return
        parent_index = (index - 1) / 2
        if self.items[index] < self.items[parent_index]:
            self.swap(index, parent_index)
        self.upFlow(parent_index)

    def swap(self, i1, i2):
        tmp = self.items[i1]
        self.items[i1] = self.items[i2]
        self.items[i2] = tmp

    def downFlow(self, index):
        cnt_size = len(self.items)
        index1 = index * 2 + 1
        index2 = index * 2 + 2
        if index1 >= cnt_size:
            return
        min_child = index1
        if index2 < cnt_size:
            if self.items[index2] < self.items[index1]:
                min_child = index2
        if self.items[index] > self.items[min_child]:
            self.swap(index, min_child)
            self.downFlow(min_child)

    def addItem(self, item):

        size = len(self.items)
        if size < self.size_limit:
            self.items.append(item)
            self.upFlow(size)
        else:
            if item <= self.items[0]:
                return
            self.items[0] = item
            self.downFlow(0)


class Solution(object):


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_max_heap = Heap(k)
        for num in nums:
            k_max_heap.addItem(num)
        return k_max_heap.items[0]