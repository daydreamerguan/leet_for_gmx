# -*- coding: UTF-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        merged_array_list = []
        for inner_list in lists:
        	while inner_list != None:
        		merged_array_list.append(inner_list)
        		inner_list = inner_list.next
        def list_item_cmp(a, b):
        	return cmp(a.val, b.val)
        merged_array_list.sort(cmp = list_item_cmp)
        list_len = len(merged_array_list)
        for index in xrange(0, list_len - 1):
        	merged_array_list[index].next = merged_array_list[index + 1]
        if list_len == 0:
            return None
        merged_array_list[-1].next = None
       	return merged_array_list[0]