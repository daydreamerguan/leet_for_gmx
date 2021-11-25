# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret_list = []
        self.inorderTraversalWithResult(root, ret_list)
        return ret_list

    def inorderTraversalWithResult(self, root, ret_list):
        if not root:
            return
        self.inorderTraversalWithResult(root.left, ret_list)
        ret_list.append(root.val)
        self.inorderTraversalWithResult(root.right, ret_list)