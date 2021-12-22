"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        cnt_level_list = [root,]
        while cnt_level_list:
            list_len = len(cnt_level_list)
            next_level_list = []
            for index, node in enumerate(cnt_level_list):
                if not node:
                    continue
                node.next = cnt_level_list[index + 1] if index != list_len - 1 else None
                next_level_list.append(node.left)
                next_level_list.append(node.right)
            cnt_level_list = next_level_list
        return root