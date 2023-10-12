class MyQueue(object):

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_push.append(x)


    def move_push_to_pop(self):
        if len(self.stack_pop) == 0:
            push_size = len(self.stack_push)
            for i in xrange(0, push_size):
                self.stack_pop.append(self.stack_push.pop())

    def pop(self):
        """
        :rtype: int
        """
        self.move_push_to_pop()
        return self.stack_pop.pop()



    def peek(self):
        """
        :rtype: int
        """
        self.move_push_to_pop()
        return self.stack_pop[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_pop) + len(self.stack_push) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()