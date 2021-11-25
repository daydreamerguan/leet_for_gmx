# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result_list = []
        self.midVisit(root, result_list)
        for i in xrange(0, len(result_list) - 1):
            if result_list[i] >= result_list[i + 1]:
                return False
        return True

    def midVisit(self, root, result_list):
        if not root:
            return
        self.midVisit(root.left, result_list)
        result_list.append(root.val)
        self.midVisit(root.right, result_list)