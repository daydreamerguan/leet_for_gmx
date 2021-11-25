# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cnt_reversed = True
        result_list = []
        cnt_level_nodes = []
        if not root:
            return result_list
        cnt_level_nodes.append(root)
        while cnt_level_nodes:
            next_level_nodes = []
            cnt_level_result = []
            while cnt_level_nodes:
                node = cnt_level_nodes.pop()
                cnt_level_result.append(node.val)
                if cnt_reversed:
                    if node.left:
                        next_level_nodes.append(node.left)
                    if node.right:
                        next_level_nodes.append(node.right)
                else:
                    if node.right:
                        next_level_nodes.append(node.right)
                    if node.left:
                        next_level_nodes.append(node.left)
            cnt_level_nodes = next_level_nodes
            result_list.append(cnt_level_result)
            cnt_reversed = not cnt_reversed
        return result_list