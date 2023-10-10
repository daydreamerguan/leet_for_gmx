# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = self.find_new_head(head, val)
        cnt_node = new_head
        parent = None
        while cnt_node:
            if cnt_node.val != val:
                parent = cnt_node
                cnt_node = parent.next
                continue
            cnt_node = self.find_new_head(cnt_node, val)
            if parent:
                parent.next = cnt_node
        return new_head

    def find_new_head(self, head, val):
        while head:
            if head.val != val:
                return head
            head = head.next
        return None