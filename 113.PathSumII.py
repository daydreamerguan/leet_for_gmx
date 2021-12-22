# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ret_lists = []
        self.calPathSum(root, [], ret_lists, targetSum)
        return ret_lists

    def calPathSum(self, root, cnt_list, matched_lists, targetSum):
        if not root:
            return
        cnt_list.append(root.val)
        if (not root.left) and (not root.right):
            if sum(cnt_list) == targetSum:
                matched_lists.append([i for i in cnt_list])
        if root.left:
            self.calPathSum(root.left, cnt_list, matched_lists, targetSum)
        if root.right:
            self.calPathSum(root.right, cnt_list, matched_lists, targetSum)
        cnt_list.pop()
        return