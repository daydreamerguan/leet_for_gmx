class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
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
        if left >= right:
            return 1

        if (left, right) in result_dict:
            cnt_result = result_dict[(left, right)]
            return cnt_result
        size = 0
        for spliter in xrange(left, right):
            left_count = self.generateBSTInRange(left, spliter, result_dict)
            right_count = self.generateBSTInRange(spliter + 1, right, result_dict)
            size += left_count * right_count
        result_dict[(left, right)] = size
        return size