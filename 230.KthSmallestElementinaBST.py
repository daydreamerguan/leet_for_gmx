# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        visited_item = [0, None]
        self.do_search(root, k, visited_item)
        return visited_item[1]

    def do_search(self, root, k, visited_item):
        assert(root)
        if visited_item[0] >= k:
            return
        if root.left:
            self.do_search(root.left, k, visited_item)
        if visited_item[0] >= k:
            return
        visited_item[0] += 1
        if visited_item[0] >= k:
            visited_item[1] = root.val
            return
        if root.right:
            self.do_search(root.right, k, visited_item)