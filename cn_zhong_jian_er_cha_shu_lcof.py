# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        start = 0
        end = len(preorder)
        # preorder first is root
        # find root in inorder, so we can get left tree and right tree
        # then recursion to leave node
        return self.buildTreeWithRange(preorder, inorder, start, end, start, end)

    def buildTreeWithRange(self, preorder, inorder, pre_start, pre_end, inorder_start, inorder_end):
        if pre_end - pre_start < 1:
            return None

        ret_node = TreeNode(preorder[pre_start])
        left_tree_length = 0
        inorder_divide = -1
        for i in xrange(inorder_start, inorder_end):
            
            if inorder[i] == preorder[pre_start]:
                inorder_divide = i
                break
            left_tree_length += 1
        ret_node.left = self.buildTreeWithRange(preorder, inorder, pre_start + 1, pre_start + 1 + left_tree_length, inorder_start, inorder_divide)
        ret_node.right = self.buildTreeWithRange(preorder, inorder, pre_start + 1 + left_tree_length, pre_end, inorder_divide + 1, inorder_end)
        return ret_node
