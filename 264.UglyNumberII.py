class Heap(object):
    def __init__(self):
        self.items = []

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
        self.items.append(item)
        self.upFlow(size)

    def popItem(self):
        l = len(self.items)
        if l == 0:
            return self.items.pop()
        else:
            self.swap(0, l -1)
            ret = self.items.pop()
            self.downFlow(0)
            return ret

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited_set = set()
        min_heap = Heap()
        min_heap.addItem(1)
        index = 0
        ugly_nums = [2, 3, 5]
        while True:
            num = min_heap.popItem()
            visited_set.add(num)
            index += 1
            if index == n:
                return num
            for mul in ugly_nums:
                new_num = num * mul
                if new_num not in visited_set:
                    visited_set.add(new_num)
                    min_heap.addItem(new_num)


