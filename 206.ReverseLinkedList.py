# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        parent = None
        cnt_node = head
        if cnt_node is None:
            return None
        while cnt_node.next != None:
            next_node = cnt_node.next
            cnt_node.next = parent
            parent = cnt_node
            cnt_node = next_node
        cnt_node.next = parent
        return cnt_node