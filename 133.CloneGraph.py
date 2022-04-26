"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        ret_dict = {}
        return self.cloneGraphWithDict(node, ret_dict)
        #  ret_dict[node.val]
        
    def cloneGraphWithDict(self, node, visited_dict):
        new_node = Node(node.val)
        visited_dict[node.val] = new_node
        for neighbor in node.neighbors:
            if neighbor.val in visited_dict:
                new_node.neighbors.append(visited_dict[neighbor.val])
            else:
                new_node.neighbors.append(self.cloneGraphWithDict(neighbor, visited_dict))
        return new_node
