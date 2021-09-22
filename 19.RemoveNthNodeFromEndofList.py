# -*- coding: UTF-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        stack_list = []
        cnt_head = head
        while cnt_head != None:
            stack_list.append(cnt_head)
            cnt_head = cnt_head.next

        list_length = len(stack_list)
        # remove the head
        if n == list_length:
            ret_node = head.next
            head.next = None
            return ret_node
        # remove the others
        else:
            delete_index = list_length - n
            cnt_node = stack_list[delete_index]
            stack_list[delete_index - 1].next = cnt_node.next
            cnt_node.next = None
            return head
