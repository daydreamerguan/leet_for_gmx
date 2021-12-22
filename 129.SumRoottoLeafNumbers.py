# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ret_list = []
        self.sumNumbersForList(root, [], ret_list)
        return sum(ret_list)

    def calcListNums(self, num_list):
        mul = 1
        ret = 0
        for i in xrange(len(num_list) - 1, -1, -1):
            ret += num_list[i] * mul
            mul * = 10
        return ret

    def sumNumbersForList(self, root, cnt_list, ret_list):
        if not root:
            return
        cnt_list.append(root.val)
        if not (root.left or root.right):
            ret_list.append(self.calcListNums(cnt_list))
        else:
            if root.left:
                self.sumNumbersForList(root.left, cnt_list, ret_list)
            if root.right:
                self.sumNumbersForList(root.right, cnt_list, ret_list)
        cnt_list.pop()