# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.handle(nums, 0, len(nums))

    def handle(self, nums, left, right):
        if right - left <= 0:
            return None

        mid_index = (right + left) / 2
        ret_node = TreeNode(nums[mid_index])
        ret_node.left = self.handle(nums, left, mid_index)
        ret_node.right = self.handle(nums, mid_index + 1, right)
        return ret_node
        