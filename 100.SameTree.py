# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
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
            if not self.isSameTree(p.left, q.left):
                return False
            if not self.isSameTree(p.right, q.right):
                return False

        return True
        