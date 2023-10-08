# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # node state 0 1 2, 
        self.root_list = []
        self.add_left_tree(root)

    def add_left_tree(self, root):
        self.root_list.append(root)
        while(self.root_list[-1].left):
            self.root_list.append(self.root_list[-1].left)

    def next(self):
        """
        :rtype: int
        """
        next_node = self.root_list.pop()
        if next_node.right:
            self.add_left_tree(next_node.right)
        return next_node.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.root_list) != 0


        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()