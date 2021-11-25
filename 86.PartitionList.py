# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        ret_head = None
        cnt_prefix = None
        ret_tail = None
        tail_subfix = None
        cnt_node = head
        while cnt_node:
            new_node = ListNode(cnt_node.val, None)
            if new_node.val < x:
                if not ret_head:
                    ret_head = new_node
                if cnt_prefix:
                    cnt_prefix.next = new_node
                cnt_prefix = new_node
            else:
                if not ret_tail:
                    ret_tail = new_node
                if tail_subfix:
                    tail_subfix.next = new_node
                tail_subfix = new_node
            cnt_node = cnt_node.next
        if cnt_prefix:
            cnt_prefix.next = ret_tail
        if ret_head:
            return ret_head
        else:
            return ret_tail