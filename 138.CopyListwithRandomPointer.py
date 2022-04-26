"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        original_array = []
        node = head
        index = 0
        index_node_dict = {}
        node_index_dict = {}
        ret_array = []
        while node:
            ret_array.append(Node(node.val))
            if index > 0:
                ret_array[index - 1].next = ret_array[index]
            original_array.append(node)
            index_node_dict[index] = node
            node_index_dict[node] = index
            node = node.next
            index += 1

        for index, node in enumerate(original_array):
            new_node = ret_array[index]
            if node.random is not None:
                random_index = node_index_dict[node.random]
                # print random_index
                new_node.random = ret_array[random_index]

        return ret_array[0]
        


    