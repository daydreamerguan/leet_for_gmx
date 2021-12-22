# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        path_sum_list = self.calPathSum(root)
        return targetSum in set(path_sum_list)
        
    def calPathSum(self, root):
        if not root:
            return []
        ret_list = []
        if not root.left:
            sub_list = self.calPathSum(root.right)
            ret_list = [i + root.val for i in sub_list]
        elif not root.right:
            sub_list = self.calPathSum(root.left)
            ret_list =  [i + root.val for i in sub_list]
        else:
            sub_list = []
            sub_list.extend(self.calPathSum(root.right))
            sub_list.extend(self.calPathSum(root.left))
            ret_list =  [i + root.val for i in sub_list]
        if not ret_list:
        	ret_list = [root.val]
        return ret_list