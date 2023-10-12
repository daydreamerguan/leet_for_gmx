# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        parent = None
        cnt_node = node
        while cnt_node.next:
            next_node = cnt_node.next
            cnt_node.val = cnt_node.next.val
            cnt_node.next = next_node.next
            cnt_node = next_node