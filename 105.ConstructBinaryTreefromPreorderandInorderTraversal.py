# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder_dict = {}
        inorder_dict = {}
        for index, num in enumerate(preorder):
            preorder_dict[num] = index

        for index, num in enumerate(inorder):
            inorder_dict[num] = index

        list_len = len(preorder)
        assert len(preorder) == len(inorder)
        return self.buildTreeWithRange(preorder, inorder, 0, list_len, 0, list_len, preorder_dict, inorder_dict)
        
    def buildTreeWithRange(self, preorder, inorder, preorder_left, preorder_right, inorder_left, inorder_right, preorder_dict, inorder_dict):
        size = preorder_right - preorder_left
        if size <= 0:
            return None
        assert size == inorder_right - inorder_left
        cnt_node_val = preorder[preorder_left]
        ret_node = TreeNode(cnt_node_val)
        inorder_index = inorder_dict[cnt_node_val]
        left_size = inorder_index - inorder_left
        right_size = inorder_right - inorder_index - 1

        pre_left_child_start = preorder_left + 1
        pre_left_child_end = pre_left_child_start + left_size

        inorder_left_child_start = inorder_left
        inorder_left_child_end = inorder_left + left_size
        ret_node.left = self.buildTreeWithRange(preorder, inorder, pre_left_child_start, pre_left_child_end,  inorder_left_child_start, inorder_left_child_end, preorder_dict, inorder_dict)

        pre_right_child_start = pre_left_child_end
        pre_right_child_end = preorder_right

        inorder_right_child_start = inorder_index + 1
        inorder_right_child_end = inorder_right
        ret_node.right = self.buildTreeWithRange(preorder, inorder, pre_right_child_start, pre_right_child_end, inorder_right_child_start, inorder_right_child_end, preorder_dict, inorder_dict)
        return ret_node

