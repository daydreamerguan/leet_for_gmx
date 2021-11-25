# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result_list = []
        cnt_level_nodes = []
        if not root:
            return result_list
        cnt_level_nodes.append(root)
        while cnt_level_nodes:
            next_level_nodes = []
            cnt_level_result = []
            for node in cnt_level_nodes:
                cnt_level_result.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            cnt_level_nodes = next_level_nodes
            result_list.append(cnt_level_result)
        return result_list
        