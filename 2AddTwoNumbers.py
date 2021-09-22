# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head_l1 = l1
        head_l2 = l2
        ret_head = ListNode()
        cnt_node = ret_head
        add = 0
        while head_l1 or head_l2:
            v1 = head_l1.val if head_l1 else 0
            v2 = head_l2.val if head_l2 else 0
            val = v1 + v2 + add
            if val >= 10:
                val -= 10
                add = 1
            else:
                add = 0
            new_node = ListNode(val)
            cnt_node.next = new_node
            cnt_node = new_node
            if head_l1:
                head_l1 = head_l1.next
            if head_l2:
                head_l2 = head_l2.next
        if add == 1:
            cnt_node.next = ListNode(1)
        return ret_head.next
