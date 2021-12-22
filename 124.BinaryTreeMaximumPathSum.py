# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        final_max = [-1001]
        self.maxPathSumWithRecord(root, final_max)
        return final_max[0]
       
    def maxPathSumWithRecord(self, root, record_list):
        if not root:
            return -1001

        left_max = self.maxPathSumWithRecord(root.left, record_list)
        right_max = self.maxPathSumWithRecord(root.right, record_list)

        local_max = root.val
        if left_max > 0:
            local_max += left_max
        if right_max > 0:
            local_max += right_max
        record_list[0] = max(local_max, left_max, right_max, record_list[0])
        sub_max = max(left_max, right_max)
        ret_max = root.val
        if sub_max > 0:
            ret_max += sub_max
        return ret_max