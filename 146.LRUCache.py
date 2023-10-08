class LRUCache(object):

    class LRUNode(object):
        def __init__(self, key, val, prev_node=None, next_node=None):
            self.val = val
            self.key = key
            self.prev_node = prev_node
            self.next_node = next_node

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.last = None
        self.cnt_num = 0
        self.value_dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.value_dict:
            return -1
        node = self.value_dict[key]
        value = node.val
        self.put(key, value)
        return value
    
    def remove_key(self, key):
        if key not in self.value_dict:
            return
        self.cnt_num -= 1
        node = self.value_dict[key]
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.head = node.next_node

        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.last = node.prev_node

        del self.value_dict[key]

    def remove_last(self):
        if not self.last:
            return
        self.remove_key(self.last.key)


    def put(self, key, value):

        self.remove_key(key)

        new_node = LRUCache.LRUNode(key, value)
        new_node.next_node = self.head
        if self.head:
            self.head.prev_node = new_node
        else:
            self.last = new_node
        self.head = new_node
        self.value_dict[key] = new_node
        self.cnt_num += 1
        if self.cnt_num > self.capacity:
            self.remove_last() 

        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)