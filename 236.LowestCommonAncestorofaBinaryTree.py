# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        result_list = [False, False, None]
        self.do_search(root, p, q, result_list)
        return result_list[2]


    def do_search(self, root, p, q, result_list):
        parent_pq = result_list[0] or result_list[1]
        p_val = p.val
        q_val = q.val
        val = root.val
        if p_val == val:
            result_list[0] = True
        elif q_val == val:
            result_list[1] = True

        if result_list[0] and result_list[1]:
            return
        if root.left:
            self.do_search(root.left, p, q, result_list)
            if result_list[0] and result_list[1] and (not parent_pq) and result_list[2] is None:
                result_list[2] = root
                return
        if root.right:
            self.do_search(root.right, p, q, result_list)
            if result_list[0] and result_list[1] and (not parent_pq) and result_list[2] is None:
                result_list[2] = root
                return
