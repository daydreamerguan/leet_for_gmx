import collections
class MyStack(object):

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        size = len(self.queue)
        self.queue.append(x)
        cnt_index = 0
        while cnt_index < size:
            self.queue.append(self.queue.popleft())
            cnt_index += 1


    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()


    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()