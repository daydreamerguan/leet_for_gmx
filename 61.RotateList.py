# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        result_list = []
        cnt_node = head
        if k == 0:
            return head
        while cnt_node:
            result_list.append(cnt_node)
            cnt_node = cnt_node.next
        if not result_list:
            return head
        size = len(result_list)
        start_index = (size - (k % size)) % size
        head = result_list[start_index]
        for i in xrange(0, size):
            cnt_index = (i + start_index) % size
            next_index = (i + start_index + 1) % size
            if next_index == start_index:
                result_list[cnt_index].next = None
            else:
                result_list[cnt_index].next = result_list[next_index]
        return head


        