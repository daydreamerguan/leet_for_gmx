# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret_list = []
        candidate_list = [root,]
        while len(candidate_list) != 0:
            next_candidates = []
            added = False
            for candidate in candidate_list:
                if candidate:
                    if not added:
                        ret_list.append(candidate.val)
                        added = True
                    next_candidates.append(candidate.right)
                    next_candidates.append(candidate.left)
            candidate_list = next_candidates
        return ret_list
