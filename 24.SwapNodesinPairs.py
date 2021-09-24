# -*- coding: UTF-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def swapTwo(self, node_prev, node_first, node_second):
        if node_second is None:
            return node_first
        if node_prev:
            node_prev.next = node_second
        node_first.next = node_second.next
        node_second.next = node_first
        return node_second

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cnt_node = head
        node_prev = None
        ret_head = None
        while cnt_node is not None:
            ret_node = self.swapTwo(node_prev, cnt_node, cnt_node.next)
            # get the ret head
            if ret_head is None:
                ret_head = ret_node 
            # after swap prev -> [cnt -> next] -> next.next : prev -> next -> cnt -> next.next ...
            node_prev = cnt_node
            cnt_node = cnt_node.next
        return ret_head

        