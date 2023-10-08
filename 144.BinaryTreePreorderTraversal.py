# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret_list = [root.val,]
        ret_list.extend(self.preorderTraversal(root.left))
        ret_list.extend(self.preorderTraversal(root.right))
        return ret_list