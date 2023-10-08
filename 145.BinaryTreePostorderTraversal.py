# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret_list = self.postorderTraversal(root.left)
        ret_list.extend(self.postorderTraversal(root.right))
        ret_list.append(root.val)
        return ret_list
        