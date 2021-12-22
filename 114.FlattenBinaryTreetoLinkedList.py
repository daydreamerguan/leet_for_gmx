# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        ret_list = []
        self.getPreOrderList(root, ret_list)
        for idx, node in enumerate(ret_list):
            node.left = None
            if idx != len(ret_list) - 1:
                node.right = ret_list[idx + 1]
            else:
                node.right = None

    def getPreOrderList(self, root, ret_list):
        if not root:
            return
        ret_list.append(root)
        self.getPreOrderList(root.left, ret_list)
        self.getPreOrderList(root.right, ret_list)