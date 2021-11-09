class Item(object):
    def __init__(self, single_str, str_index):
        self.value = single_str
        self.str_index = str_index
        self.index = -1

    def cmp(self, other_item):
        return cmp(self.str_index, other_item.str_index)

class Heap(object):
    def __init__(self):
        self.items = []
    def upFlow(self, index):
        if index == 0:
            return
        parent_index = (index - 1) / 2
        if self.items[index].cmp(self.items[parent_index]) < 0:
            self.swap(index, parent_index)
        self.upFlow(parent_index)


    def swap(self, i1, i2):
        tmp = self.items[i1]
        self.items[i1] = self.items[i2]
        self.items[i1].index = i1
        self.items[i2] = tmp
        self.items[i2].index = i2

    def downFlow(self, index):
        cnt_size = len(self.items)
        index1 = index * 2 + 1
        index2 = index * 2 + 2
        if index1 >= cnt_size:
            return
        min_child = index1
        if index2 < cnt_size:
            if self.items[index2].cmp(self.items[index1]) < 0:
                min_child = index2
        if self.items[index].cmp(self.items[min_child]) > 0:
            self.swap(index, min_child)
            self.downFlow(min_child)

    def addItem(self, item):
        size = len(self.items)
        self.items.append(item)
        self.items[size].index = size
        self.upFlow(size)

    def popItem(self):

        size = len(self.items)
        if size == 0:
            return
        self.swap(0, size - 1)
        self.items.pop()
        self.downFlow(0)

    def print_items(self):
        for item in self.items:
            print item.value, item.str_index, item.index





class Solution(object):
    def minWindow(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: str
        """
        template_length = len(t)
        template_dict = {}
        cnt_template_dict = {}
        reserve_template_length = template_length
        max_start = -1
        max_end = -1
        max_length = 0
        for item in t:
            if item not in template_dict:
                template_dict[item] = 0
                cnt_template_dict[item] = 0
            template_dict[item] += 1
            cnt_template_dict[item] += 1
        my_heap = Heap()
        for (index, item) in enumerate(s):
            if item in template_dict:
                new_item = Item(item, index) 
                my_heap.addItem(new_item)
                cnt_template_dict[item] -= 1
                if cnt_template_dict[item] >= 0:
                    reserve_template_length -= 1
                head_s = my_heap.items[0].value
                   # print "cnt heap length", len(my_heap.items), cnt_template_dict, head_s, s
                # my_heap.print_items()
                while cnt_template_dict[head_s] < 0:
                    cnt_template_dict[head_s] += 1
                    my_heap.popItem()
                    head_s = my_heap.items[0].value
                    # print "cnt heap length", len(my_heap.items), cnt_template_dict, head_s, s
                    # my_heap.print_items()
                if reserve_template_length == 0:
                    cnt_start = my_heap.items[0].str_index
                    cnt_end = index + 1
                    cnt_max_length = cnt_end - cnt_start
                    # print s[max_start:max_end]
                    if (cnt_max_length < max_length) or max_length == 0:
                        max_length = cnt_max_length
                        max_start = cnt_start
                        max_end = cnt_end

        if max_length == 0:
            return ""
        return s[max_start:max_end]


if __name__ == '__main__':
    # s = "ADOBECODEBANC", t = "ABC"
    print Solution().minWindow("ADOBECODEBANC", "ABC")
    print Solution().minWindow("a", "a")
    print Solution().minWindow("a", "aa")
        