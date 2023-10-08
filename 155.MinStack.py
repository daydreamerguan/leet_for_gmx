class MinStack(object):

    def __init__(self):
        self.min_heap = []
        self.stack = []
        self.heap_stack_map = {}
        self.stack_heap_map = {}
        self.size = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        self.stack.append(val)
        self.min_heap.append(val)
        self.heap_stack_map[self.size] = self.size
        self.stack_heap_map[self.size] = self.size
        self.size += 1
        self.upflow(self.size - 1)
        
    def upflow(self, heap_index):
        if heap_index == 0:
            return
        upper_index = (heap_index - 1) / 2
        if self.min_heap[heap_index] < self.min_heap[upper_index]:
            self.exchange(heap_index, upper_index)
            self.upflow(upper_index)

    def exchange(self, index1, index2):
        stack_pos1 = self.heap_stack_map[index1]
        stack_pos2 = self.heap_stack_map[index2]
        temp = self.min_heap[index1]
        self.min_heap[index1] = self.min_heap[index2]
        self.min_heap[index2] = temp
        self.heap_stack_map[index1] = stack_pos2
        self.stack_heap_map[stack_pos2] = index1
        self.heap_stack_map[index2] = stack_pos1
        self.stack_heap_map[stack_pos1] = index2

    def downflow(self, heap_index):
        left_index = heap_index * 2 + 1
        right_index = heap_index * 2 + 2
        child_index = None
        if left_index >= self.size:
            return
        if right_index >= self.size:
            child_index = left_index
        else:
            if(self.min_heap[left_index] < self.min_heap[right_index]):
                child_index = left_index
            else:
                child_index = right_index
        if child_index:
            if self.min_heap[heap_index] > self.min_heap[child_index]:
                self.exchange(heap_index, child_index)
                self.downflow(child_index)


    def pop(self):
        """
        :rtype: None
        """
        if self.size > 0:
            ret_value = self.stack[self.size - 1]
            heap_pos = self.stack_heap_map[self.size - 1]
            self.exchange(heap_pos, self.size - 1)
            self.stack.pop()
            self.min_heap.pop()
            assert(self.stack_heap_map[self.size - 1] == self.size - 1)
            assert(self.heap_stack_map[self.size - 1] == self.size - 1)
            del self.stack_heap_map[self.size - 1]
            del self.heap_stack_map[self.size - 1]
            self.size -= 1
            self.downflow(heap_pos)
        

    def top(self):
        if(self.size > 0):
            return self.stack[self.size - 1]
        """
        :rtype: int
        """
        

    def getMin(self):
        if(self.size > 0):
            return self.min_heap[0]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()