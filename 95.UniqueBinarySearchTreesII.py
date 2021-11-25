# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result_dict = {}
        return self.generateBSTInRange(1, n + 1, result_dict)

    def copy_tree(self, root):
        if not root:
            return None
        ret_node = TreeNode(root.val)
        ret_node.left = self.copy_tree(root.left)
        ret_node.right = self.copy_tree(root.right)
        return ret_node


    def generateBSTInRange(self, left, right, result_dict):
        ret_list = []
        if left >= right:
            ret_list.append(None)
            return ret_list

        if (left, right) in result_dict:
            cnt_result = result_dict[(left, right)]
            for node in cnt_result:
                ret_list.append(self.copy_tree(node))
            return ret_list

        for spliter in xrange(left, right):
            left_list = self.generateBSTInRange(left, spliter, result_dict)
            right_list = self.generateBSTInRange(spliter + 1, right, result_dict)
            for left_node in left_list:
                for right_node in right_list:
                    new_node = TreeNode(spliter)
                    new_node.left = self.copy_tree(left_node)
                    new_node.right = self.copy_tree(right_node)
                    ret_list.append(new_node)
        result_dict[(left, right)] = ret_list
        return ret_list
