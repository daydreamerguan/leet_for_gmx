# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        val = root.val
        pval = p.val
        qval = q.val
        if pval == val or qval == val:
            return root

        if pval < val and qval < val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif  pval > val and qval > val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

if __name__ == '__main__':
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node6.left = node2
    node6.right = node8
    node2.left = node0
    node2.right = node4
    node4.left = node3
    node4.right = node5
    node8.left = node7
    node8.right = node9
    print(Solution().lowestCommonAncestor(node6, 2, 4).val)
    print(Solution().lowestCommonAncestor(node6, 2, 8).val)