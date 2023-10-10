# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.do_count_nodes(root, None, None)
    
    def do_count_nodes(self, node, counted_left_height, counted_right_height):
        if not node:
            return 0
        if counted_left_height is None:
            counted_left_height = self.get_node_left_most_height(node)
        else:
            counted_left_height -= 1
        if counted_right_height is None:
            counted_right_height = self.get_node_right_nost_height(node)
        else:
            counted_right_height -= 1
        if counted_left_height == counted_right_height:
            return 2 ** counted_left_height - 1
        else:
            left_nodes = self.do_count_nodes(node.left, counted_left_height, None)
            right_nodes = self.do_count_nodes(node.right, None, counted_right_height)
            return 1 + left_nodes + right_nodes


    def get_node_left_most_height(self, node):
        ret = 0
        while node:
            ret += 1
            node = node.left                
        return ret

    def get_node_right_nost_height(self, node):
        ret = 0
        while node:
            ret += 1
            node = node.right                
        return ret
