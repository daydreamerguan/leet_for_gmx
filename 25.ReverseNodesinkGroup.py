# -*- coding: UTF-8 -*-
#Definition for singly-linked list.
# class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution(object):

    def swap_array_range(self, node_array, left, right):
        cnt_left = left
        cnt_right = right
        while cnt_left < cnt_right:
            temp = node_array[cnt_left]
            node_array[cnt_left] = node_array[cnt_right]
            node_array[cnt_right] = temp
            cnt_left += 1
            cnt_right -= 1




    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node_array = []
        cnt_node = head
        while cnt_node:
            node_array.append(cnt_node)
            cnt_node = cnt_node.next
        cnt_start = 0
        cnt_end = k - 1
        while cnt_end < len(node_array):
            self.swap_array_range(node_array, cnt_start, cnt_end)
            cnt_start += k
            cnt_end += k
        for i in xrange(0, len(node_array) - 1):
            node_array[i].next = node_array[i + 1]
        if len(node_array) > 0:
            node_array[-1].next = None
        else:
            return None
        return node_array[0]

if __name__ == '__main__':
    l4 = ListNode(4, None)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    ret_head = Solution().reverseKGroup(l1, 4)
    while ret_head:
        print ret_head.val
        ret_head = ret_head.next