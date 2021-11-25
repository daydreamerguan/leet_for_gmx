# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSameTreeSymmetric(root.left, root.right)

    def isSameTreeSymmetric(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_none = p is None
        q_none = q is None
        if p_none ^ q_none:
            return False
        if p:
            if p.val != q.val:
                return False
            if not self.isSameTreeSymmetric(p.left, q.right):
                return False
            if not self.isSameTreeSymmetric(p.right, q.left):
                return False

        return True