# -*- coding: UTF-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret_head = None
        cnt_node = None
        while (l1 is not None) or (l2 is not None):
            next_node = None
            if l2 is None or ((l1 is not None) and l1.val <= l2.val):
                next_node = ListNode(l1.val)
                l1 = l1.next
            else:
                next_node = ListNode(l2.val)
                l2 = l2.next
            # print "create node", next_node.val
            if ret_head is None:
                ret_head = next_node
                cnt_node = ret_head
            else:
                cnt_node.next = next_node
                cnt_node = next_node
        return ret_head

if __name__ == '__main__':
    l11 = ListNode(1, None)
    l12 = ListNode(2, None)
    l11.next = l12
    l13 = ListNode(4, None)
    l12.next = l13
    l21 = ListNode(1, None)
    l22 = ListNode(3, None)
    l21.next = l22
    l23 = ListNode(4, None)
    l22.next = l23
    Solution().mergeTwoLists(l11, l21)