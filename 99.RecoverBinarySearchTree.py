# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        result_list = []
        self.midVisitWithChildState(root, result_list, None, False)
        swap_prev_node = None
        swap_sub_node = None
        for i in xrange(0, len(result_list) - 1):
            pre_node = result_list[i]
            sub_node = result_list[i + 1]
            if pre_node.val >= sub_node.val:
                swap_prev_node = pre_node
                break
        for i in xrange(len(result_list) - 1, 0, -1):
            sub_node = result_list[i]
            pre_node = result_list[i - 1]
            if pre_node.val >= sub_node.val:
                swap_sub_node = sub_node
                break
        tmp_val = swap_prev_node.val
        swap_prev_node.val = swap_sub_node.val
        swap_sub_node.val = tmp_val

    def midVisitWithChildState(self, root, result_list, parent, left):
        if not root:
            return
        self.midVisitWithChildState(root.left, result_list, root, True)
        result_list.append(root)
        self.midVisitWithChildState(root.right, result_list, root, False) 
