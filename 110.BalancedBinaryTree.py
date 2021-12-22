# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, balanced = self.CheckBalence(root)
        return balanced

    def CheckBalence(self, root):
        if not root:
            return 0, True
        left_height, left_balanced = self.CheckBalence(root.left)
        right_height, right_balanced = self.CheckBalence(root.right)
        height = max(left_height, right_height) + 1
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return height, balanced
