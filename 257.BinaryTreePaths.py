# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        cnt_path = []
        self.do_search(root, cnt_path, result)
        return result
    
    def do_search(self, root, cnt_path, result):
        if not root:
            return
        cnt_path.append(str(root.val))
        if root.left is None and root.right is None:
            result.append("->".join(cnt_path))
        if root.left:
            self.do_search(root.left, cnt_path, result)
        if root.right:
            self.do_search(root.right, cnt_path, result)
        cnt_path.pop()
