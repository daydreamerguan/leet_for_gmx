# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        postorder_dict = {}
        inorder_dict = {}
        for index, num in enumerate(postorder):
            postorder_dict[num] = index

        for index, num in enumerate(inorder):
            inorder_dict[num] = index

        list_len = len(postorder)
        assert len(inorder) == len(postorder)
        return self.buildTreeWithRange(postorder, inorder, 0, list_len, 0, list_len, postorder_dict, inorder_dict)
        
    def buildTreeWithRange(self, postorder, inorder, postorder_left, postorder_right, inorder_left, inorder_right, postorder_dict, inorder_dict):
        size = postorder_right - postorder_left
        if size <= 0:
            return None
        assert size == inorder_right - inorder_left
        cnt_node_val = postorder[postorder_right - 1]
        ret_node = TreeNode(cnt_node_val)
        inorder_index = inorder_dict[cnt_node_val]
        left_size = inorder_index - inorder_left
        right_size = inorder_right - inorder_index - 1

        post_left_child_start = postorder_left
        post_left_child_end = post_left_child_start + left_size

        inorder_left_child_start = inorder_left
        inorder_left_child_end = inorder_left + left_size
        ret_node.left = self.buildTreeWithRange(postorder, inorder, post_left_child_start, post_left_child_end,  inorder_left_child_start, inorder_left_child_end, postorder_dict, inorder_dict)

        post_right_child_start = post_left_child_end
        post_right_child_end = postorder_right - 1

        inorder_right_child_start = inorder_index + 1
        inorder_right_child_end = inorder_right
        ret_node.right = self.buildTreeWithRange(postorder, inorder, post_right_child_start, post_right_child_end, inorder_right_child_start, inorder_right_child_end, postorder_dict, inorder_dict)
        return ret_node

